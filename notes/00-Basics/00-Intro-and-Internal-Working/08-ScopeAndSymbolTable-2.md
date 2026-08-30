---
date: 2026-08-30
time: "19:34:11+05:30"
---
# Cpp vs Py Addresss 


```
C++                              Python
--------------------------------|--------------------------------
int x = 10;                     | x = 10
                                |
compiler assigns x              | compiler assigns x
address 0x404000                | key "x" in globals dict
                                |
machine code:                   | bytecode:
mov eax, [0x404000]             | LOAD_GLOBAL "x"
                                |   -> PyDict_GetItem(globals, "x")
                                |   -> hash "x", find bucket, return value
                                |
address hardcoded in bytes      | name string used at runtime
zero indirection                | one hash lookup
name "x" completely gone        | name "x" still exists in bytecode
```

## Queries 

- Python doenst have scope resolution operator like the Cpp
- But the scope is resolved at compiled time to bytecode by the symbol table, corrsct opcode selection
- The cpp resolve them at compiled time to addresses and freezes them while python use symbol table to resolve  correct opcode and the values are fetched accordingly like the local address array ot global dict
### global

- `global` keyword is help at bytecode compilation to explicitly tell to emit global
```python
x = 10

def foo():
    global x       # tell compiler: x is GLOBAL in this function
    x = 20         # emit STORE_GLOBAL, not STORE_FAST
```
### nonlocal

- `nonlocal` is a keyword which tells the compiler to see in the outher scope not global 
```python
def outer():
    x = 10
    def inner():
        nonlocal x    # tell compiler: x is from enclosing scope
        x = 20        # emit STORE_DEREF, writes into the cell
```

- Python has **no function overloading**. 
```python
def foo(x):
    print("first")

def foo(x, y):      # this does not overload
    print("second") # this REPLACES the first foo in the dict
```

```
module.__dict__["foo"] = first_foo_object    # after first def
module.__dict__["foo"] = second_foo_object   # after second def -- first is gone
```

- The name `"foo"` is a key in the globals dict. Second `def` just overwrites the value at that key. First function object's refcount drops to 0 if nothing else holds it. Freed.
### overloading

- Python has not overloading like the cpp if done like that it shadows it the key will get the last object instead it is achieved by the duck typing 
- If it works it works like 

```python
def foo(x, y=None):
    if y is None:
        # handle one argument case
    else:
        # handle two argument case
```
### shadowing

- Shadowing = inner scope name hides outer scope name with the same name.

```cpp
int x = 10;
void foo() {
    int x = 20;  // shadows global x, compiler knows both exist at different addresses
    // global x still exists, inner x hides it locally
}
// global x is 10 still
```

```python
x = 10           # global

def foo():
    x = 20       # local x, shadows global x
    print(x)     # prints 20, LOAD_FAST, sees local x

print(x)         # prints 10, global x untouched
```
- Both languages allow it. C++ compiler tracks both at different addresses. Python compiler emits `LOAD_FAST` inside `foo` so it never touches global x.
- Shadowing Builtins -- Legal In Python, Dangerous , The LEGB search order means globals shadow builtins. You just put a key in the globals dict that matches a builtin name. Python has no protection against this.

```python
list = [1, 2, 3]    # "list" key now in module.__dict__
                     # shadows builtins.__dict__["list"]

x = list("abc")     # LOAD_GLOBAL finds "list" in globals first
                     # gets [1,2,3] not the list type
                     # TypeError: 'list' object is not callable
```
### overwriting

- Overwriting is Rebinding In Python
- This is not overwriting memory. It is **rebinding** -- changing which PyObject the name points to. The old object is untouched. 
```python
x = 10
x = 20     # not modifying the integer 10
           # creating new PyLongObject(20)
           # pointing "x" key in dict to the new object
           # PyLongObject(10) refcount drops, may be freed
```
```cpp
int x = 10;
x = 20;    // actually writes 20 into the same memory address
           // the int at that address is modified in place
```

- C++     : variable IS memory location, assignment modifies it
- Python  : variable IS a name (dict key), assignment changes what it points to
- The Each function gets its own scope stucture called as `PyCodeObject` at compilation of bytecode think it of as the pyton code functions blueprint form source sode like waht it has locals etc, but at runtime when the fucntions in called the instance are made called `PyFrameObject` from these Code objects each havning its seperate data it is like so that if a ficntion is called mutiple times each will get its own instance of `PyFrameObject` and manage it 

- Does Each Function Get Its Own Scope Structure -> **At compile time -- PyCodeObject per function:**
- Each function definition produces its own `PyCodeObject`. This is the static blueprint -- created once, shared across all calls.

```
PyCodeObject for outer {
    co_varnames = ("x",)       -- locals of outer
    co_cellvars = ("x",)       -- x is captured by inner, lives in cell
    co_code     = [...]
}

PyCodeObject for inner {
    co_varnames = ("y",)       -- locals of inner
    co_freevars = ("x",)       -- x comes from outer
    co_code     = [...]
}
```
**At runtime -- PyFrameObject per call:**
```
call outer() -->  PyFrameObject {
                      f_code       -> PyCodeObject(outer)
                      f_globals    -> module.__dict__
                      f_localsplus -> [CellObject(x)]
                  }

call inner() -->  PyFrameObject {
                      f_code       -> PyCodeObject(inner)
                      f_globals    -> module.__dict__
                      f_back       -> outer's frame
                      f_localsplus -> [CellObject ref]   <- points to outer's cell
                  }
```

- Call outer() 3 times -- 3 separate PyFrameObjects, all using the same PyCodeObject. Each call gets its own `f_localsplus` array -- its own private locals. The PyCodeObject is shared, read-only. The PyFrameObject is per-call, mutable.

```
PyCodeObject  -- blueprint, created once per function definition
PyFrameObject -- instance, created once per function call
```

- It behave like clas and object in cpp 
### PyCellObject

- The inner and outer is resolved using a single `PyCellObject` reference it stores referencces tto PyObjects tht can be commonly modifable form the other PyFrameObjects enclosed the outer 

```python
def outer():
    x = 10
    def inner():
        print(x)
    inner()
```

**At compile time**, the compiler detects `x` is used in `inner` but defined in `outer`. It marks:

- `outer` : `x` is a **cell variable** -- must live in a `PyCellObject`, not directly in `f_localsplus`
- `inner` : `x` is a **free variable** -- comes from an enclosing cell

- Both frames share one `PyCellObject`. This is why if outer modifies `x` after creating inner, inner sees the change. They are literally sharing the same cell.
- **This is the `E` in LEGB** -- enclosing scope. It is not a dict search. It is a direct pointer to a shared cell object.
- **At runtime when outer() is called:**

```
1. PyFrameObject for outer created
2. f_localsplus[0] = PyCellObject { ob_ref = NULL }
   (a cell is allocated for x, starts empty)

3. outer executes: x = 10
   STORE_DEREF 0
   -> PyCellObject { ob_ref = PyLongObject(10) }
   (x's value lives inside the cell, not directly in the array slot)

4. inner function object is created
   PyFunctionObject {
       func_code    -> PyCodeObject(inner)
       func_closure -> tuple( PyCellObject* )  <- same cell outer uses
   }
   (inner gets a pointer to the SAME cell object outer has)

5. inner() is called
   PyFrameObject for inner created
   f_localsplus contains the cell references from func_closure

6. inner executes: print(x)
   LOAD_DEREF 0
   -> follow f_localsplus[0] -> PyCellObject -> ob_ref -> PyLongObject(10)
   -> push 10 onto eval stack
```

```
outer frame:
  f_localsplus[0] -> PyCellObject
                          |
                          ob_ref -> PyLongObject(10)
                          ^
inner frame:              |
  f_localsplus[0] ---------  (same PyCellObject)
```


________
- When a function returns, its `PyFrameObject` is destroyed. The `f_localsplus` array is gone. All local variables that were stored there -- gone. Refcounts drop, objects potentially freed.
- Thus it needed to be stored some where there the cellobject comes into play 
```python
def outer():
    x = 10
    def inner():
        print(x)    # inner needs x AFTER outer returns
    return inner

fn = outer()        # outer's frame is destroyed here
fn()                # inner runs HERE -- where is x?
```

- `outer` returned. Its frame is gone. But `inner` still needs `x`. If `x` was stored directly in `outer`'s `f_localsplus` array, it would be gone. `fn()` would be reading freed memory. Undefined behavior -- C/C++ style crash.
- Python solves this with cell objects. A cell is a **heap-allocated box** that holds one `PyObject` pointer. It lives independently of any frame. Both the outer frame and the inner function hold a pointer to the same box. When the outer frame dies, the box survives because `inner` still holds a reference to it.
- A cell object is a heap-allocated C struct containing a single `PyObject*` pointer called `ob_ref`. It exists because local variables normally live in a frame's `f_localsplus` array which gets destroyed when the function returns. When the compiler detects that a nested function references an outer function's variable, it marks that variable as a cell variable. At runtime the outer function stores the variable inside a `PyCellObject` on the heap instead of directly in the array. The inner function receives a pointer to that same cell in its `func_closure` tuple. Both point to identical cell. When the outer frame is destroyed, the cell survives because the inner function still holds a reference. When the inner function reads the variable via `LOAD_DEREF`, it follows the pointer to the cell and reads `ob_ref`. Because both share one cell, any modification to the variable by either function is immediately visible to the other. The cell lives exactly as long as something holds a reference to it -- normal refcounting, nothing special.


## Full Summary 


C++ resolves scope entirely at compile time. The compiler sees a variable name, checks its declaration, assigns it a memory address or stack offset, and bakes that address directly into the machine code. By the time the binary exists, names are completely gone -- only addresses remain. The CPU never knows what `x` was called. Scope in C++ is a compile time concept that dissolves into addresses.

Python cannot do this because it is dynamically typed. The compiler does not know what type a variable will be at runtime, so it cannot assign fixed memory addresses. Instead Python keeps names alive and uses actual dictionary objects as namespaces at runtime. Every scope in Python is a real dictionary living on the heap.

When CPython compiles your source code, it first runs the lexer which breaks the raw text into tokens, then the parser which builds an AST representing the grammatical structure. At this point a separate pass called the symbol table builder walks the entire AST before emitting a single bytecode instruction. It scans every name in every scope and classifies each one -- is this name assigned inside a function? Mark it LOCAL. Is it referenced but never assigned? Mark it GLOBAL or FREE. Does a nested function reference it? Mark it as a CELL variable. The symbol table also assigns integer indices to every local variable. This entire structure is temporary -- it is a C data structure that lives only during compilation.

The bytecode compiler then makes a second pass over the AST, and this time it consults the symbol table to decide which opcode to emit for each name access. If the symbol table says a name is local, it emits `LOAD_FAST` which accesses a raw C array by index. If the symbol table says global, it emits `LOAD_GLOBAL` which does a dictionary lookup. If the name belongs to an enclosing function's scope, it emits `LOAD_DEREF` which follows a pointer to a shared cell object. Once every opcode is emitted the symbol table has served its purpose. Nothing holds a reference to it anymore. Its refcount drops to zero and CPython frees it. The scope decision is now frozen inside the opcodes themselves.

The output of compilation is a `PyCodeObject` -- a C struct on the heap containing the bytecode, the constant values, the name strings needed for runtime lookups, and metadata like how many local variables exist. This is written to a `.pyc` file in `__pycache__`. Next time the source is unchanged, CPython loads the `.pyc` directly, skipping the entire compilation pipeline. The `PyCodeObject` is a read-only blueprint, created once per function definition and shared across all calls.

When a function is actually called at runtime, CPython creates a `PyFrameObject` -- a separate C struct also on the heap. This is the live execution context for that specific call. It contains a pointer back to the `PyCodeObject` for the bytecode, a pointer to the module's globals dictionary, a `f_localsplus` array which is a raw C array of `PyObject` pointers for local variables, and `f_back` pointing to the calling frame. Every call to the same function creates a new `PyFrameObject` with its own fresh `f_localsplus`. The `PyCodeObject` is shared. The `PyFrameObject` is per-call. Exactly like a class versus an instance.

At this point the PVM's main evaluation loop in `ceval.c` takes over. It reads opcodes one by one from the bytecode and executes a corresponding C code block for each. `LOAD_FAST` hits `f_localsplus[i]` directly -- no dictionary, pure array index, O(1), fastest possible access. `LOAD_GLOBAL` calls `PyDict_GetItem` on the globals dictionary first, then on the builtins dictionary if not found there. `LOAD_DEREF` follows a pointer to a `PyCellObject` and reads its `ob_ref` field.

The cell object is the mechanism behind closures. When the compiler detects that a nested function references a variable from an enclosing function, it marks that variable as a cell variable in the outer function. At runtime the outer function does not store that variable directly in `f_localsplus` -- instead it stores a `PyCellObject` there, and the value lives inside the cell's `ob_ref`. When the inner function object is created, it receives a `func_closure` tuple containing a pointer to that same `PyCellObject`. Both the outer frame and the inner frame now point to the identical cell. When either one reads or writes the variable, they are both operating on the same `ob_ref`. This is why closures see the current value of variables, not a copy at the time of creation.

LEGB -- Local, Enclosing, Global, Builtin -- is not a runtime search that happens on every lookup. It is the compile time classification that determines which opcode gets emitted. The opcode is the resolution. `LOAD_FAST` means L was chosen. `LOAD_DEREF` means E was chosen. `LOAD_GLOBAL` covers both G and B because it searches globals first then builtins sequentially. The compiler made the L/E/G/B decision at compile time using the symbol table. The runtime just executes the pre-decided instruction. The only place actual sequential searching happens is inside `LOAD_GLOBAL` which checks globals then builtins in order -- and if both miss, raises `NameError`.

Scope is controlled through four mechanisms. First, position -- where you write an assignment decides the scope automatically, module level goes to the globals dict, inside a function goes to the locals array. Second, the `global` keyword which tells the compiler to emit `STORE_GLOBAL` instead of `STORE_FAST` so the assignment writes into the module dictionary. Third, the `nonlocal` keyword which tells the compiler to emit `STORE_DEREF` so the assignment writes through the shared cell into the enclosing function's variable. Fourth, explicit dot access like `module.x` or `builtins.list` which bypasses LEGB entirely and directly accesses a specific namespace dictionary -- Python's equivalent of C++'s `::` operator.

Python allows shadowing at every level. A local name shadows a global with the same name because `LOAD_FAST` never reaches `LOAD_GLOBAL`. A global name shadows a builtin because `LOAD_GLOBAL` finds the key in the globals dict before checking builtins. Shadowing builtins is legal and Python will not warn you -- if you write `list = 42` at module level, the string `"list"` now exists as a key in `module.__dict__`, and every subsequent `LOAD_GLOBAL "list"` finds your integer there before ever reaching `builtins.__dict__`. The real builtin is untouched, just unreachable via normal lookup. You can still get it explicitly via `builtins.list`.

The entire system reduces to this: Python needs names at runtime because its variables are dictionary keys pointing to heap-allocated `PyObject` instances. The symbol table is a temporary compile time tool that decides which dictionary each name belongs to. That decision gets encoded as an opcode. The opcode routes the runtime lookup to the correct data structure -- a raw array for locals, a hash table for globals and builtins, a cell pointer for closures. Speed varies accordingly -- locals are raw array access, globals and builtins cost a hash lookup. The frame object ties it all together, holding the array, the pointer to the globals dict, the closure cells, and the execution state for one live function call.