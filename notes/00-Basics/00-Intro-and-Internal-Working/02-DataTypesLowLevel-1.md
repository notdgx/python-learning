
# Topics 

- Pyhton datatypes at low level 
- PyObject
- How they handeled 

________

# Cpp vs Py

- In C++ there are two fundamentally different categories:

```cpp
// PRIMITIVE TYPES -- raw memory, no overhead
int    x = 10;        // exactly 4 bytes, raw binary
float  f = 3.14;      // exactly 4 bytes, IEEE 754 binary
char   c = 'A';       // exactly 1 byte, ASCII value 65
bool   b = true;      // 1 byte, 0 or 1
double d = 3.14159;   // exactly 8 bytes

// OBJECT TYPES -- structs with overhead
std::string s = "hello";   // object, has methods, heap allocated
std::vector<int> v;        // object, has methods, heap allocated
```

- ==Primitives in C++ are not objects.== They have no methods. They have no type information attached to them. They are raw bits in memory. When you write `int x = 10`, the ==CPU stores the binary representation of 10 in 4 bytes. That is it. No wrapper. No metadata. Just bits.==

```
C++ memory for int x = 10:
+--+--+--+--+
|00|00|00|0A|   <- 4 raw bytes, value 10 in hex
+--+--+--+--+
   4 bytes total. nothing else.
```

- This is the hard truth. Every single value in Python -- integers, floats, booleans, strings, everything -- is a full object. ==A PyObject struct on the heap.==
- In C++ `10` is a literal with no methods. In ==Python `10` is an instance of the `int` class== and has methods. The dot notation works on everything. 

```python
x = 10
y = 3.14
z = True
s = "hello"

# ALL of these are objects
# ALL of them are on the heap
# ALL of them have type information
# ALL of them have reference counts
# ALL of them have methods

print(type(10))         # <class 'int'>
print(type(3.14))       # <class 'float'>
print(type(True))       # <class 'bool'>
print(type("hello"))    # <class 'str'>
```

```python
print(isinstance(10, int))        # True
print(isinstance(3.14, float))    # True
print(isinstance(True, bool))     # True
print(isinstance("hi", str))      # True

# int itself is a class
print(type(int))                  # <class 'type'>
print(type(float))                # <class 'type'>

# you can even call them as constructors
x = int(10)       # same as x = 10
y = float(3.14)   # same as y = 3.14
z = str(42)       # "42"


print(int.__bases__)    # (<class 'object'>,)
print(float.__bases__)  # (<class 'object'>,)
print(bool.__bases__)   # (<class 'int'>,)  <- bool inherits from int!

```

# Datatypes

- Python does NOT have primitive vs object like C++. The real distinction is immutable vs mutable.
- ==This is dynamic typing.== The type lives on the OBJECT, not the variable name.
- When the same variable name is changed to a different datatype then the key variable name jsut starting points to a ==different PyObject== in heap if the previous ref count = 0 then memory is freed
- Every time a immputable datatype is reassigned it start point to a new object and previous PyObject is freed if ref_Count = 0 
- However Python caches -5 to 255 in memory at starting of interpreater they are never freed for optimization and speed and reusability
- In C++:  type is a property of the VARIABLE (compile time decision)
- In Python: type is a property of the OBJECT (runtime, stored in ob_type)
- The variable `x` is just a name. A label. It can point at any PyObject regardless of type. The PyObject itself carries its type in `ob_type`.
- C++: ==primitives are raw bits,== type belongs to the variable, 
     decided at compile time, zero overhead.
- Python: NO primitives exist, everything is a PyObject on the heap, type belongs to the object via ob_type, checked at runtime, variable is just name that can point at any object of any type. The flexibility costs memory and speed but gains expressiveness and safety.
- Python datatypes are literally C structs.


## PyObject

When you write `x = 10` in Python, CPython creates this C struct in memory:
```c
// this is what actually exists in memory
struct PyLongObject {
    PyObject_HEAD        // <-- we will destroy this completely
    digit ob_digit[1];
};
```

- ==`PyObject_HEAD` is just a macro it contains the cahraterstics of the data== and the digit contains the actual data in arrat depending on need and size
### PyObject_HEAD 

>Just a Macro

- The macro exists purely for convenience and consistency. Instead of manually writing `PyObject ob_base` in every single struct, you just write `PyObject_HEAD` and the macro expands it. Every Python type struct starts with this, guaranteeing every object has `ob_refcnt` and `ob_type` at the same memory offset.

Now here is the answer to your question. `PyObject_HEAD` is not a struct. It is not a function. It is a **C macro**:
```c
// Include/object.h -- actual CPython source
#define PyObject_HEAD   PyObject ob_base;
```

That is it. One line. It expands to a single field `ob_base` of type `PyObject`.

```c
struct PyFloatObject {
    PyObject_HEAD
    double ob_fval;
};
```

The C preprocessor expands it to:

```c
struct PyFloatObject {
    PyObject ob_base;    // <-- PyObject_HEAD became this
    double ob_fval;
};
```

Which means the full memory layout is:

```c
struct PyFloatObject {
    // ob_base (PyObject) contains:
    Py_ssize_t    ob_refcnt;    // 8 bytes
    PyTypeObject *ob_type;      // 8 bytes
    // then the actual float data:
    double        ob_fval;      // 8 bytes
};
// Total: 24 bytes
```

### Common Fields of All DataTypes

#### ==ob_refcnt==

```
Simple meaning: how many things are pointing at this object right now
```
```python
x = 10        # ob_refcnt = 1  (x points to it)
y = x         # ob_refcnt = 2  (x and y both point to it)
del x         # ob_refcnt = 1  (only y points now)
del y         # ob_refcnt = 0  -> IMMEDIATELY FREED from memory
```

- When this hits zero, Python says =="nobody needs this anymore" and frees the memory.== That is the entire garbage collection mechanism for most cases. Just a counter.

---

#### ob_type

```
Simple meaning: what TYPE is this object -- int? str? list? your custom class?
```
```python
x = 10
# ob_type points to the int class
# this is how Python knows x is an int at runtime
# this is how x.bit_length() works -- look up bit_length in ob_type
# this is how x + y works -- look up __add__ in ob_type
```

- Every single operation Python does on an object starts here. It checks ob_type first. Always. ==Without ob_type there is no dynamic typing.== It is the backbone of everything.

_______

## Types

### Immutable 

```python
x = 10
x = 20      # this does NOT change the PyObject(10)
            # it creates a NEW PyObject(20)
            # x name now points to the new one
            # PyObject(10) still exists until refcount = 0
```

```
Before:  x --> [PyObject: 10]
After:   x --> [PyObject: 20]
               [PyObject: 10]  <- still in memory briefly
                                  freed when refcount hits 0
```

Strings are immutable:
```python
s = "hello"
s[0] = "H"     # TypeError: 'str' object does not support item assignment
```

You cannot change a string in place. You create a new one:
```python
s = "hello"
s = "H" + s[1:]   # new string object created
```

### Mutable 

```python
lst = [1, 2, 3]
lst.append(4)      # modifies the SAME PyObject
                   # no new list created
                   # all names pointing to this list see the change

a = lst
b = lst
lst.append(5)
print(a)   # [1, 2, 3, 4, 5]  -- a sees it
print(b)   # [1, 2, 3, 4, 5]  -- b sees it
           # because a, b, lst all point to the SAME PyObject
```

```
IMMUTABLE (cannot change in place)
-----------------------------------
int          whole numbers, arbitrary precision
float        64-bit double precision
complex      2 + 3j  complex numbers
bool         True / False (subclass of int)
str          unicode text, immutable sequence
tuple        immutable sequence of objects
frozenset    immutable set
bytes        immutable sequence of raw bytes

MUTABLE (can change in place)
------------------------------
list         ordered mutable sequence
dict         key-value hashmap
set          unordered unique values
bytearray    mutable bytes
```

_________
_______

## Python int -- PyLongObject

- ==It is immutable datatype==
- It is a class `int` inherited formm the class `object` which is also root class od everything
- It can grows very very to large numbers as it is a Pyobject in whihc the digits are stored as array of digits 
- For small numbers it is one digit. For ==huge numbers it allocates more digit slots.== This is called ==**arbitrary precision arithmetic** or **bignum**==. The cost is that big integer math is slower than C++ fixed-width integer math.
- It is large in size as the digit of number grows large
- 1 chunk or 1 array slot carries 30bit 

```c
// actual CPython source -- Objects/longobject.h
struct PyLongObject {
    PyObject_VAR_HEAD          // refcount + type pointer + size
    digit ob_digit[1];         // the actual number stored here
};
```

```
Memory layout of x = 10:
+------------------+
| ob_refcnt = 1    |  8 bytes -- reference count
+------------------+
| ob_type = &PyLong_Type | 8 bytes -- pointer to int class
+------------------+
| ob_size = 1      |  8 bytes -- number of digits
+------------------+
| ob_digit = 10    |  4 bytes -- actual value
+------------------+
Total: ~28 bytes minimum

vs C++: int x = 10 = 4 bytes
Python uses 7x more memory for the same integer
```

_____
______
### HEAD 

```c
// Include/cpython/longintrepr.h
struct PyLongObject {
    PyObject_VAR_HEAD      // refcnt + ob_type + ob_size
    digit ob_digit[1];     // array of digits (grows for big numbers)
};
```

Expanded fully:

```c
struct PyLongObject {
    Py_ssize_t    ob_refcnt;    // 8 bytes -- reference count
    PyTypeObject *ob_type;      // 8 bytes -- points to PyLong_Type
    Py_ssize_t    ob_size;      // 8 bytes -- number of digits
    digit         ob_digit[1];  // 4 bytes -- the actual number
};
// Total: 28 bytes for a small integer
```

- `ob_size` tells you ==how many digit slots== are used. For `x = 10`, ob_size is 1. For a massive number like `2**1000`, ob_size is much larger and more digit slots are allocated right after the struct in memory.

Memory layout visualized:

---
```
Address  Content
+0       ob_refcnt  = 1          (how many names ie keys point here)
+8       ob_type    = 0x...      (pointer to int class object)
+16      ob_size    = 1          (one digit)
+24      ob_digit   = 10         (the actual value)
```
_________
### Cpp vs Py Size Limit

C++ int is 32 bits. Maximum value: 2,147,483,647. Overflow silently wraps around

```cpp
int x = 2147483647;
x = x + 1;
printf("%d\n", x);   // -2147483648  <- silent overflow!
```

Python int has NO maximum. It grows as needed:

```python
x = 2 ** 1000    # a number with 300+ digits
print(x)         # prints the whole thing, no overflow

x = 99999999999999999999999999999999 * 99999999999999999999999999999999
print(x)         # works perfectly
```

> CPython pre-creates PyObjects for integers -5 to 256 at startup. These are never freed and never recreated:

```python
a = 100
b = 100
print(a is b)    # True -- SAME PyObject, cached

a = 1000
b = 1000
print(a is b)    # False -- different PyObjects, outside cache range
```

- `is` checks identity -- same object in memory. `==` checks equality -- same value.

```python
a = 1000
b = 1000
print(a == b)    # True  -- same value
print(a is b)    # False -- different objects
```

- For -5 to 256: Python reuses existing PyObjects. No new allocation. This saves massive amounts of memory and allocation overhead since small integers are used constantly.

### ob_size

```
Simple meaning: how many digit slots does this number need
```

```python
x = 10              # ob_size = 1  (fits in one slot)
x = 2 ** 100        # ob_size = 4  (needs four slots, big number)
```

- Python integers have no size limit. They grow. ob_size tracks how many internal slots are currently being used to store the number.
- Each 30 bit
- Each internal digit slot = 4 bytes = 32 bits of storage
                            │
                            └── only 30 bits used for integer data
                            

```
PyLongObject

┌──────────────────────────────┐
│ Object header                │
│ ob_refcnt → 8 bytes          │
│ ob_type   → 8 bytes          │
│ metadata                      │
├──────────────────────────────┤
│ digit[0] → 4 bytes / 30 bits │
│ digit[1] → 4 bytes / 30 bits │
│ digit[2] → 4 bytes / 30 bits │
└──────────────────────────────┘
```


---

### ob_digit[]

```
Simple meaning: the actual number stored here, split into chunks
```

```python
x = 10     # ob_digit[0] = 10   (the number itself)
```

- For small numbers this is just the number directly. For huge numbers it is split across multiple slots like digits of a very large number. You never see this directly. Python handles the math across all the 
- 
- slots automatically.

```
number =
digit[0] × 2⁰
+
digit[1] × 2³⁰

= 0 × 1
+ 1 × 1073741824

= 1073741824
```



![[Pasted image 20260826140647.png]]

![[Pasted image 20260826140736.png]]


### Diff


```
Feature              C++                      Python
-------              ---                      ------
Primitives           yes (int,float,char)     NO -- everything is object
Type location        on the variable          on the object (ob_type)
Type checking        compile time             runtime
Type change          impossible               just rebind the name
int size             32 bits, fixed           arbitrary precision
int memory           4 bytes                  28+ bytes
float memory         8 bytes                  24 bytes
overflow             silent wrap              impossible (grows)
bool                 separate type            subclass of int
string               char array / std::string immutable object
mutability concept   not primary distinction  PRIMARY distinction
methods on int       no                       yes
inheritance          optional                 everything inherits object
integer cache        no                       -5 to 256 pre-cached
type conversion      often implicit           mostly explicit
```

________

## Python float -- PyFloatObject

- It is same as CPP it uses the sstandard IEEE 554
- Floating Point repersentation
- 8 bytes Full precision float

```c
struct PyFloatObject {
    PyObject_HEAD         // refcount + type pointer
    double ob_fval;       // the actual float value (8 bytes)
};
```

```
Memory: ~24 bytes
vs C++ double: 8 bytes
```

### HEAD
```c
// Include/floatobject.h
typedef struct {
    PyObject_HEAD        // refcnt + ob_type
    double ob_fval;      // the actual float value
} PyFloatObject;
```

Expanded:

```c
typedef struct {
    Py_ssize_t    ob_refcnt;    // 8 bytes
    PyTypeObject *ob_type;      // 8 bytes  points to PyFloat_Type
    double        ob_fval;      // 8 bytes  the actual number
} PyFloatObject;
// Total: 24 bytes
```
### ob_fval

```
Simple meaning: the actual decimal number stored here
```
```python
x = 3.14    # ob_fval = 3.14  (stored as 64-bit double, same as C double)
```

- Straightforward. Just the number. Float has no size issue because it is always exactly 64 bits. No growth needed.

___
_______


## Python bool -- subclass of int

- Bool is ==literally a subclass of int.== True is 1, False is 0:

```python
print(True == 1)     # True
print(False == 0)    # True
print(True + True)   # 2  -- because bool IS an int
print(True * 5)      # 5
```

- This is not a quirk. It is the type system working correctly. bool inherits from int so all int operations work on bools.
- `True` and `False` are not created every time you use them. ==They are **single global instances**== that exist for the entire lifetime of the Python process. `ob_type` points to `PyBool_Type` which itself has `PyLong_Type` as its base.
- ==Bool is a subclass of int.== There is no separate bool struct:

```c
// booleans are just PyLongObject with value 0 or 1
// Py_True and Py_False are global PyLongObject instances
// created once at CPython startup, never freed

static PyLongObject _Py_TrueStruct = {
    PyObject_VAR_HEAD_INIT(&PyBool_Type, 1)
    { 1 }     // ob_digit[0] = 1
};

static PyLongObject _Py_FalseStruct = {
    PyObject_VAR_HEAD_INIT(&PyBool_Type, 0)
    { 0 }     // ob_digit[0] = 0
};

#define Py_True  ((PyObject *) &_Py_TrueStruct)
#define Py_False ((PyObject *) &_Py_FalseStruct)
```


________
____

## Python str -- PyUnicodeObject

Strings are more complex ==because they handle unicode:==
```c
// Simplified from Include/cpython/unicodeobject.h
typedef struct {
    PyObject_HEAD            // refcnt + ob_type
    Py_ssize_t length;       // number of characters
    Py_hash_t  hash;         // cached hash value (-1 if not computed)
    struct {
        unsigned int interned:2;    // is this string interned?
        unsigned int kind:3;        // 1=latin1, 2=UCS2, 4=UCS4
        unsigned int compact:1;     // is data right after this struct?
        unsigned int ascii:1;       // is it pure ASCII?
    } state;
    wchar_t *wstr;           // pointer to character data
} PyASCIIObject;
```

Strings store their character data differently based on content:

```
Pure ASCII text    ->  1 byte per character  (latin-1 encoding)
Text with accents  ->  2 bytes per character (UCS-2)
Full unicode       ->  4 bytes per character (UCS-4)
```

Python picks the most compact representation automatically.


### length

```
Simple meaning: how many characters are in this string
```
```python
s = "hello"    # length = 5
s = "hi"       # length = 2
```

Stored so Python never has to count characters every time. Just look up length directly.

---

### hash

```
Simple meaning: a number fingerprint of this string, cached so it is not recalculated every time
```
```python
s = "hello"
d = {s: 42}    # Python computes hash of "hello" to find its dict slot
               # stores it in hash field so next time no recalculation
```

==Hashing is used every time a string is used as a dictionary key==. Caching it saves time. Starts as -1 meaning not calculated yet. Calculated once, stored forever.

---

### kind

```
Simple meaning: how many bytes per character -- depends on what characters are in the string
```

```
kind = 1    ->  1 byte per character   (pure english/ASCII text)
kind = 2    ->  2 bytes per character  (includes accented chars, arabic, etc)
kind = 4    ->  4 bytes per character  (full unicode, emojis, rare scripts)
```

```python
s = "hello"      # kind=1, pure ASCII, 1 byte each, compact
s = "héllo"      # kind=2, has accent, 2 bytes each
s = "hello 😀"   # kind=4, has emoji, 4 bytes each
```

Python picks the smallest representation that can hold all the characters. ==Saves memory automatically.==

---

### ==interned==

```
Simple meaning: is this string shared globally so only one copy exists in memory
```

python

```python
a = "hello"
b = "hello"
# Python may intern this -- both a and b point to the SAME object
# instead of two separate "hello" objects
# saves memory for common strings
print(a is b)    # often True for simple strings
```

Python does this automatically for short strings that look like identifiers. You can force it with `sys.intern()`.

________
_____________

## Addition 


When Python does any operation, it checks `ob_type` at runtime:

```python
x = 10
y = 20
z = x + y

# what Python actually does:
# 1. get ob_type of x  -> int
# 2. find __add__ in int's method table
# 3. call int.__add__(x, y)
# 4. int.__add__ checks y is also int
# 5. does the addition
# 6. returns new int PyObject
```

If types are incompatible:

```python
x = 10
y = "hello"
z = x + y
# 1. get ob_type of x -> int
# 2. find __add__ in int's method table
# 3. call int.__add__(x, y)
# 4. int.__add__ checks y -- it is a str, not int
# 5. returns NotImplemented
# 6. Python then tries str.__radd__(y, x)
# 7. str.__radd__ also returns NotImplemented
# 8. Python raises TypeError
```


# TypeConversion

## TYPE CONVERSION -- EXPLICIT vs IMPLICIT

Python does very little implicit conversion unlike C++:

cpp

```cpp
// C++ implicit conversion
int x = 10;
double y = x;    // automatically converts, no error
```

python

```python
# Python explicit conversion required
x = 10
y = x / 3        # gives 3.3333 (float) -- division always returns float
y = x // 3       # gives 3 (int) -- floor division

# mixing types usually requires explicit cast
x = 10
s = "value is " + str(x)    # must explicitly convert int to str
                              # "value is " + 10 would TypeError
```

The few implicit conversions Python does:

python

```python
# int -> float in math operations
x = 10      # int
y = 3.14    # float
z = x + y   # Python promotes int to float automatically
print(type(z))   # float

# bool -> int (because bool IS int)
print(True + 5)  # 6 -- no conversion needed, bool IS int
```