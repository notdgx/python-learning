# Topics 

- Scope 
- Scope Resolution 
- Symbol Table 


____________

# LEGB

## C++ vs Py 

- In C/C++, scope is a **compile-time concept**. The compiler resolves which variable a name refers to at compile time. Block scope, function scope, file scope -- all decided before a single instruction runs.
- Python is the **opposite**. Scope resolution is a **runtime lookup** against actual dictionary objects. The "scope" is not a compiler concept -- it is a chain of live dictionaries the PVM searches through at execution time.

```cpp
int x = 10;
void foo() {
    int x = 20;  // compiler KNOWS this is a different x, stack offset decided at compile time
    printf("%d", x);  // offset baked into the binary
}
```

____

## LEGB Search Order

-  It is a **search order** across 4 dictionary-like namespaces:

```
L -- Local     -- the current function's namespace
E -- Enclosing -- any enclosing function's namespace (for closures)
G -- Global    -- the module-level namespace
B -- Builtin   -- builtins module namespace
```

When the PVM executes `LOAD_NAME x`, it does not know where `x` lives. It searches L -> E -> G -> B in order and returns the first match. If nothing found: `NameError`.

### Local Order

- SO the thing is if any the local variabl is created then in the pyhton custom heap stack eval stack contains a raw array of pointers to the PyObject of Local Objects this is the space form ehree it is fetched
- If here it is not found it means it doesnt exist in local scope
- This is fast because no dict lookup needed it is rigth there in local scope


- Every function call creates a **new frame object** on the C heap (not C stack -- remember, CPython's Python frames are heap-allocated `PyFrameObject` structs).
- The critical field: `f_localsplus` -- this is a **raw C array of PyObject pointers**, not a dict. CPython optimizes function locals into a flat array for speed. The compiler assigns each local variable a fixed index into this array at compile time.

```
PyFrameObject {
    PyObject_VAR_HEAD
    PyFrameObject  *f_back        -- pointer to calling frame
    PyCodeObject   *f_code        -- bytecode for this function
    PyObject       *f_globals     -- pointer to module globals dict
    PyObject       *f_locals      -- local namespace (dict or optimized array)
    PyObject      **f_localsplus  -- fast locals array
    int             f_lasti       -- last bytecode index executed
    ...
}
```

```python
def foo():
    x = 10
    y = 20
    return x + y
```

```
dis output:
  LOAD_CONST   10       # push 10 onto eval stack
  STORE_FAST   0 (x)   # pop -> f_localsplus[0]
  LOAD_CONST   20
  STORE_FAST   1 (y)   # pop -> f_localsplus[1]
  LOAD_FAST    0 (x)   # push f_localsplus[0]
  LOAD_FAST    1 (y)   # push f_localsplus[1]
  BINARY_ADD
  RETURN_VALUE
```

`STORE_FAST` / `LOAD_FAST` -- array index access. **O(1), no dict lookup at all.** The compiler already resolved which index each name maps to. This is why function locals are **faster** than globals.


### Global Scope 

- These are the variables in global scope saved as key value pairs
- Their checking requires the dictionary lookup 
- They are slow than the Local FAST
- `f_globals` is a pointer to a real `dict` object -- the module's `__dict__`. This is the same dict you get from `globals()`.
- It has the address of the Global dict but it still needs to lookup 

```python
x = 10

def foo():
    return x   # not in locals -> searches globals dict
```

```
dis output for foo:
  LOAD_GLOBAL  x    # searches f_globals dict for key "x"
  RETURN_VALUE
```

`LOAD_GLOBAL` does an actual **dict hash lookup** -- `PyDict_GetItem(f_globals, "x")`. Slower than `LOAD_FAST`.

The module namespace is literally:

```
module.__dict__ == {
    "__name__": "__main__",
    "__builtins__": <module 'builtins'>,
    "x": <PyLongObject 10>,
    "foo": <PyFunctionObject>,
    ...
}
```


### Built in Scope 

- This is the modeule level or built in level scope 
- It is also dict lookup 
- `f_builtins` -- another dict, the `builtins` module's `__dict__`. Contains `len`, `print`, `range`, `int`, `type`, etc.
- It is a last leveled at order
- Dont use built in scoped names shadows can be dangeroug

```
builtins.__dict__ == {
    "print": <built-in function print>,
    "len":   <built-in function len>,
    "int":   <class 'int'>,
    "type":  <class 'type'>,
    ...
}
```

When you call `len(x)`, CPython:

1. Checks `f_localsplus` -- not there
2. Checks `f_globals` -- not there (unless you shadowed it)
3. Checks `f_builtins` -- found

This is why **shadowing builtins is legal but dangerous**:

```python
list = [1, 2, 3]   # now "list" key in globals dict shadows builtins["list"]
x = list("abc")    # NameError/TypeError -- looks up globals first, finds [1,2,3]
```


________
## Working

- The thing is that at compilation to bytecode one opcode is set in bytecode for execution
- If not found Then follows the LEGB ordern from the where it is specified in opcode 

The compiler decides at **compile time** which opcode to emit:

- Name assigned anywhere in the function body? -> treat as local -> `LOAD_FAST` / `STORE_FAST`
- Name never assigned in function? -> treat as global/builtin -> `LOAD_GLOBAL`

### Local trap

```python
x = 10

def foo():
    print(x)   # <-- UnboundLocalError, not NameError
    x = 20
```

Why? The compiler sees `x = 20` exists in the function body. It classifies `x` as local for the **entire function**. Emits `LOAD_FAST` for `print(x)`. At runtime, `f_localsplus[0]` is `NULL` (not yet assigned). CPython checks for NULL and raises `UnboundLocalError`.

The compiler made the wrong-feeling-but-correct decision: if you assign it anywhere, it's local everywhere in that function.

### The `global` Keyword 
- Forces Opcode Change

```python
x = 10

def foo():
    global x
    x = 20    # STORE_GLOBAL, not STORE_FAST
```

`global x` tells the compiler: emit `LOAD_GLOBAL`/`STORE_GLOBAL` for `x` instead of `LOAD_FAST`/`STORE_FAST`. It directly modifies the module dict.

Without `global`, assignment inside a function always creates a **new local binding** -- it never modifies the global. This is not a "copy" -- it's the compiler routing the store to the local array instead of the global dict.


_________
### The Enclosing Scope 

- Cell Objects

```python
def outer():
    x = 10          # not local to inner, not global
    def inner():
        print(x)    # where does this come from?
    inner()
```

- `x` is in `outer`'s local scope. But `inner` needs it. When `outer` returns, its frame is destroyed. How does `x` survive?

CPython uses **cell objects**.

```
PyObject
  |
  v
PyCellObject {
    PyObject_HEAD
    PyObject *ob_ref    -- pointer to the captured value
}
```

At compile time, the compiler detects that `x` is referenced in a nested function. It marks `x` as a **cell variable** in `outer` and a **free variable** in `inner`.

At runtime:

1. `outer` stores `x` not in `f_localsplus` directly but inside a `PyCellObject`
2. `inner`'s `PyCodeObject` has a `co_freevars` tuple listing names captured from enclosing scopes
3. When `inner` is created (as a `PyFunctionObject`), it gets a `func_closure` -- a tuple of `PyCellObject` pointers
4. `inner` reads `x` via `LOAD_DEREF` -- which dereferences `ob_ref` inside the cell

```
outer frame:
  f_localsplus[0] -> PyCellObject { ob_ref -> PyLongObject(10) }
                                       ^
inner function:                        |
  func_closure[0] -> PyCellObject -----+  (same cell object)
  reads via LOAD_DEREF
```

Both `outer` and `inner` point to the **same cell object**. If `outer` modifies `x` after `inner` is created, `inner` sees the new value because they share the cell.

This is why:

python

```python
def make_adders():
    adders = []
    for i in range(3):
        adders.append(lambda x: x + i)  # all capture same cell
    return adders

f0, f1, f2 = make_adders()
print(f0(0))  # 2, not 0 -- all see final value of i
```

All lambdas share the **same cell object** for `i`. After the loop, `ob_ref` points to `2`. They all read `2`.

---

### `nonlocal` -- Writes Through the Cell
z

```python
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20      # STORE_DEREF -- writes into the cell's ob_ref
    inner()
    print(x)        # 20
```

`nonlocal x` tells the compiler: `x` is a free variable -- emit `STORE_DEREF` which writes into `ob_ref` of the shared cell, not into a new local. Without `nonlocal`, `x = 20` in `inner` would create a new local shadowing the cell.


CURRENT UNDERSTANDINGS

- So the Python need to check the scope of the variable functions etc
- The Cpp when compiled then the scope is already resolved at compile tiem and a full fleged computer binary is made it doesnt know the variable name or anything it just play with the memory address pure machine instructions
- However the symbol table telling abouts the scope and other informations of variables and other functions is made intermidately for compilation but later discarder in binary 
- Symbol table is just a intermediate step  
- Same with python but differently the python the local and global lives in heap memory as PyObject as everything is a PyObject 
- There reference is stores whether it is local or global or outer 
- The intemediate Symbol tree is also made in Python to flag the variable functions etc is glbal or local during bytecode compilation
- But in byte code the it is already decided what a thing is 
- Actual instuction is set to `LOAD_FAST` or `LOAD_GLOBAL` 
- The Python needs variables names 
- For Globals variable names are as key value pairs to lookup in the global values dictionaries 
- The BuiltIn is also a key value dict to look up 
- The Local Variables are stored in a raw address array storing the pointers of local PyObjects in memeory 
- Py Frame also stores the adress to the dict of the global variables 
- The first Priority is To check in the specidfied emitted opcode in bytecoded scope if not found there Order is liek LEGB 
```
L -- Local     -- the current function's namespace
E -- Enclosing -- any enclosing function's namespace (for closures)
G -- Global    -- the module-level namespace
B -- Builtin   -- builtins module namespace
```
- It check from where position specified to below in heirarcy 
- If not fornd there then it raises the `NameError
- The Local fetch is Fast because the adress is stored
- But if the global then forst go to the dict address and then lookup there
- The shadowing naming variables ot other things as python built in can conflict and break program 

QUESTIONS to ask

- doesnt python have any scope respolution like cpp how it is implemented
- and what about the scope keywords 
- is there any conceptt like overloading overshadowing overwriting compare it how it is implementd in cpp and python for functions  
- do each fucntion/scope get like its a seperat table or thing for inner and outer or global scoping
- How is the inner resolved 
- Can we just name the variables like builtin ones even though it is not advised and what is Cell is it related to it 
- Where is external module or import scope checked
- is there any more related question > in [[Python-ScopeAndSymbolTable-2]]