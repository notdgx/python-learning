# `NoneType`


- `NoneType` -- the type of the `None` object.

- `None` is not a keyword in the way C's `NULL` is a macro. It is an actual Python object sitting on the heap, a singleton instance of the class `NoneType`.

```python
>>> type(None)
<class 'NoneType'>
>>> id(None)
140234567891234   # fixed address, never changes
```

**At the C level**, CPython defines it as:

```c
PyObject _Py_NoneStruct = {
    _PyObject_EXTRA_INIT
    1,           /* ob_refcnt -- starts at 1, never hits 0 */
    &_PyNone_Type
};

#define Py_None (&_Py_NoneStruct)
```

- It is a statically allocated `PyObject` -- not heap allocated, not refcount collected. Lives in the BSS/data segment of the CPython binary itself, same as integer cache objects for -5 to 256.

- `_PyNone_Type` is a `PyTypeObject` where almost every function pointer slot is either a stub that raises `TypeError` or returns a sentinel. You cannot do arithmetic on it, cannot iterate it, cannot call it.

- **The singleton guarantee** is hard -- CPython never creates a second `NoneType` instance. `Py_None` is a C macro pointing to that one static struct. Every `None` reference in every Python program in the process points to that same address.

**Practical consequence you care about:**

```python
x is None   # CORRECT -- identity check, one pointer comparison
x == None   # WRONG  -- calls __eq__, can be overridden, slower
```

- `is None` compiles to `IS_OP` bytecode, one pointer compare against `Py_None`. `== None` goes through full `COMPARE_OP` dispatch, calls `__eq__`, which can be user-defined.

**Why `NoneType` cannot be instantiated:**

```python
>>> NoneType = type(None)
>>> NoneType()
TypeError: cannot create 'NoneType' instances
```

- The `tp_new` slot in `_PyNone_Type` is set to a function that always raises `TypeError`. The class exists, you can get a reference to it, but instantiation is blocked at the C level.

- **Refcount curiosity** -- `None`'s refcount is enormous in any running program because every function that returns nothing implicitly returns `None`, every `RETURN_VALUE` opcode bumps it. But since it is statically allocated, hitting zero is impossible by design -- CPython never deallocates it regardless.

- One line summary: `None` is a statically allocated singleton `PyObject` of type `NoneType`, lives in CPython's data segment, refcount is irrelevant to its lifetime, `is None` is the correct check because it is a single pointer comparison.

## Summary 

- SO it is a single pyobject 
- There cant be duplicate of it and it is always present in python interpreater running 
- It is like the integer cached value -5 to 255 And True and False alwasy in memory
- Its refcount can never be zero and it isnever freed 
- Cant make 2 or more of it always one None is present if multiple hings need the None just their reference is pointed to it and refcount is increased by 1 
- `None`, `True`, `False`, and the small integer cache all live in the **DATA SEGMENT** of the CPython process binary.
- It cant be created , called , iterated it will give typee error 
- The Heap storage is not because we dont want never these to be refcount zero 

# Storage of None/True/False

CPython process binary.

```
Process Memory Layout
---------------------
+------------------+
|   Stack          |  <-- C function call frames, local vars, grows down
+------------------+
|      |           |
|      v           |
|                  |
|      ^           |
|      |           |
+------------------+
|   Heap           |  <-- malloc/pymalloc, your regular PyObjects live here
+------------------+
|   BSS Segment    |  <-- uninitialized global/static C vars (zeroed at load)
+------------------+
|   Data Segment   |  <-- initialized global/static C vars  <-- THESE LIVE HERE
+------------------+
|   Text Segment   |  <-- executable code (opcodes, C functions)
+------------------+
```

- They are **global static C variables** declared at file scope in CPython's source. The OS loader puts them in the data segment when the process starts. They exist for the entire lifetime of the process, no malloc, no free, no pymalloc involved at all.
- `True` and `False` are instances of `PyBool_Type`, which is a **subtype of `PyLongObject`**. Meaning `True` is literally stored as a `PyLongObject` with `ob_digit[0] = 1` and `False` with `ob_digit[0] = 0` (or `ob_size = 0` for false). That is why `True + True == 2` works -- bool inherits int's `tp_as_number` arithmetic slots. Same static allocation, same data segment, same singleton guarantee, same blocked `tp_new`.

# Properties of True/False/None

## Storage

Object          | Storage       | How
----------------|---------------|----------------------------------
None            | Data segment  | PyObject _Py_NoneStruct  (global var)
True            | Data segment  | PyLongObject _Py_TrueStruct (global var)
False           | Data segment  | PyLongObject _Py_FalseStruct (global var)
-5 to 256       | Data segment  | static PyLongObject small_ints[262] (static array)

## Singleton

```
None
  --> tp_new slot raises TypeError
  --> physically impossible to construct a second one from Python

True / False
  --> bool.__new__ intercepts and always returns existing singleton
  --> bool(1) does NOT create a new object, returns _Py_TrueStruct pointer

Cached ints -5..256
  --> int creation goes through _PyLong_FromSTR / PyLong_FromLong etc.
  --> every path checks: is value in [-5, 256]?
  --> if yes: return &small_ints[value + NSMALLNEGINTS]  (pointer into static array)
  --> never allocates a new PyLongObject for these values
```


## refcount

This one is **version dependent** and is where the real internals get interesting.

**Pre CPython 3.12:**

Not mechanically enforced. It never hit zero in practice because the interpreter's own internal tables always held a reference. But if you somehow forced refcount to zero, `_Py_Dealloc` would call `tp_dealloc`, which calls `PyObject_Free`, which calls `free()` on a data segment address -- undefined behavior, likely a crash or heap corruption. No safety net.

**CPython 3.12+ -- PEP 683 Immortal Objects:**

Hard mechanical enforcement added. A sentinel refcount value is assigned:

```c
// In 3.12+
#define _Py_IMMORTAL_REFCNT  UINT_MAX  // 4294967295 on 64-bit

// Py_DECREF now checks:
#define Py_DECREF(op)                           \
    do {                                        \
        if (_Py_IsImmortal(op)) break;          \  // <-- if immortal, skip entirely
        if (--((PyObject*)(op))->ob_refcnt == 0)\
            _Py_Dealloc(op);                    \
    } while(0)
```

None, True, False, and small integers are initialized with `ob_refcnt = _Py_IMMORTAL_REFCNT`. `Py_DECREF` sees the sentinel and does nothing. Refcount cannot be decremented at all, mechanically impossible, not just "won't happen in practice."


## Summary 


```
Property              | None | True/False | small_ints[-5..256]
----------------------|------|------------|--------------------
Data segment          |  YES |    YES     |        YES
Singleton             |  YES |    YES     |        YES
Singleton mechanism   | tp_new blocked | __new__ returns existing | creation path returns cached ptr
Refcount never 0      |  YES |    YES     |        YES
Mechanism pre-3.12    | always referenced | always referenced | always referenced
Mechanism 3.12+       | immortal sentinel | immortal sentinel | immortal sentinel
Can be iterated       |  NO  |    NO      |        NO
Can be called         |  NO  |    NO      |        NO
```



# Others like True/False/None 

## Empty tuple,byte,string,frozenset objects

```
// Empty tuple -- Objects/tupleobject.c
static PyTupleObject *free_list[...]
// _PyTuple_EMPTY is a static singleton

// Empty string -- Objects/unicodeobject.c
// unicode_empty is a static PyUnicodeObject

// Empty bytes -- Objects/bytesobject.c
// bytes_empty is a static PyBytesObject

// Empty frozenset -- Objects/setobject.c
// frozenset() with no args returns same singleton
```
## Single ASCCI char (0-127)

- CPython interns all 256 latin-1 characters at startup as static `PyUnicodeObject` instances. Same mechanism as integer cache -- creation path checks if it is a single char in range, returns cached pointer.

## every type object

Every built-in type is a statically allocated `PyTypeObject` global variable in CPython source:

```c
// In CPython source -- all static globals
PyTypeObject PyLong_Type = { ... };
PyTypeObject PyFloat_Type = { ... };
PyTypeObject PyUnicode_Type = { ... };
PyTypeObject PyList_Type = { ... };
PyTypeObject PyDict_Type = { ... };
PyTypeObject PyTuple_Type = { ... };
PyTypeObject PyBool_Type = { ... };
PyTypeObject PyType_Type = { ... };   // type itself
PyTypeObject PyBaseObject_Type = { ... };  // object itself
```

## **Ellipsis object `...`**

```c
// Objects/object.c
PyObject _Py_EllipsisObject = {
    _PyObject_EXTRA_INIT 1, &PyEllipsis_Type
};
```

Singleton, data segment, same as None. Used heavily in numpy for slice indexing.

```python
>>> ... is ...
True
>>> type(...)
<class 'ellipsis'>
```


## **NotImplemented**

```c
// Objects/object.c
PyObject _Py_NotImplementedStruct = {
    _PyObject_EXTRA_INIT 1, &_PyNotImplemented_Type
};
```

Returned from dunder methods like `__eq__` when the comparison is not supported for that type. Tells Python to try the reflected operation on the other operand.
```python
>>> NotImplemented is NotImplemented
True
>>> type(NotImplemented)
<class 'NotImplementedType'>
```

---

## ** Small bytes objects (0-255 single byte)**

Similar to single-char string cache. CPython caches all 256 single-byte `PyBytesObject` instances.

```python
>>> a = bytes([65])
>>> b = bytes([65])
>>> a is b
True
```


__________

## All

```
Statically allocated / immortal objects in CPython
---------------------------------------------------
None                        1 singleton
True / False                2 singletons
Small integers -5..256      262 objects in static array
Empty tuple ()              1 singleton
Empty string ""             1 singleton
Empty bytes b""             1 singleton
Empty frozenset             1 singleton
Single-char strings 0-127   128 objects in static array
Single-byte bytes 0-255     256 objects in static array
Ellipsis ...                1 singleton
NotImplemented              1 singleton
Built-in type objects       ~50+ static PyTypeObject globals
```