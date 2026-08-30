
# DUNDER METHODS

---

## Are They Predefined

Yes and no. Let me be precise.

The **names** are predefined -- Python's data model defines what each `__name__` means and when Python calls it. The **implementations** can be your own.

```
Python defines:   __add__ means "called when + is used"
You define:       what __add__ actually does for your class
Python calls:     your implementation when + is used
```

---

## Every Class Already Has Dunders From object

Because everything inherits from `object`, and `object` defines default implementations of many dunders, your class already has them before you write anything:

```python
class Dog:
    pass

d = Dog()

# these all work WITHOUT you defining anything:
print(d.__class__)      # <class 'Dog'>
print(d.__repr__())     # <__main__.Dog object at 0x...>
print(d.__str__())      # <__main__.Dog object at 0x...>
print(d.__hash__())     # some integer
print(d.__eq__(d))      # True (identity comparison)

# object provides default implementations for all of these
```

The default implementations are minimal -- `__repr__` just shows class name and memory address, `__eq__` just compares identity (same as `is`). You override them to make your class behave meaningfully.

---

## Overriding -- Replacing Default Behavior

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __repr__(self):
        # called by repr(d) and as fallback for str(d)
        return f"Dog(name={self.name!r}, breed={self.breed!r})"

    def __str__(self):
        # called by str(d) and print(d)
        return f"{self.name} the {self.breed}"

    def __eq__(self, other):
        # called by d1 == d2
        if not isinstance(other, Dog):
            return NotImplemented
        return self.name == other.name and self.breed == other.breed

    def __hash__(self):
        # called when used as dict key or in set
        # must define if you define __eq__
        return hash((self.name, self.breed))


d1 = Dog("rex", "labrador")
d2 = Dog("rex", "labrador")
d3 = Dog("max", "poodle")

print(repr(d1))     # Dog(name='rex', breed='labrador')
print(str(d1))      # rex the labrador
print(d1 == d2)     # True  -- uses our __eq__
print(d1 == d3)     # False
print(d1 is d2)     # False -- different objects
dogs = {d1, d2, d3} # uses __hash__ and __eq__
print(len(dogs))    # 2 -- d1 and d2 are equal so set deduplicates
```

---

## Defining Custom Dunders -- Make Your Class Behave Like Built-ins

This is the real power. You can make your class support any Python operation:

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # + operator
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # - operator
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    # * operator (scalar multiplication)
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    # * operator when scalar is on LEFT: 3 * v
    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    # len()
    def __len__(self):
        return 2

    # v[0], v[1]
    def __getitem__(self, index):
        if index == 0: return self.x
        if index == 1: return self.y
        raise IndexError("Vector index out of range")

    # bool(v) -- is vector non-zero
    def __bool__(self):
        return self.x != 0 or self.y != 0

    # abs(v) -- magnitude
    def __abs__(self):
        return (self.x**2 + self.y**2) ** 0.5

    # str(v) and print(v)
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    # repr(v)
    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"

    # for i in v
    def __iter__(self):
        yield self.x
        yield self.y

    # v == other
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1 + v2)      # Vector(4, 6)    -- __add__
print(v1 - v2)      # Vector(-2, -2)  -- __sub__
print(v1 * 3)       # Vector(3, 6)    -- __mul__
print(3 * v1)       # Vector(3, 6)    -- __rmul__
print(len(v1))      # 2               -- __len__
print(v1[0])        # 1               -- __getitem__
print(bool(v1))     # True            -- __bool__
print(abs(v2))      # 5.0             -- __abs__
print(str(v1))      # Vector(1, 2)    -- __str__
for coord in v1:    # 1 then 2        -- __iter__
    print(coord)
print(v1 == v2)     # False           -- __eq__
```

This is exactly what numpy does for its arrays in C. Same dunder methods, implemented in C instead of Python.

---

## Context Manager Dunders

```python
class DatabaseConnection:
    def __init__(self, url):
        self.url = url
        self.connection = None

    def __enter__(self):
        # called when entering 'with' block
        self.connection = connect(self.url)
        return self.connection     # this is what 'as' binds to

    def __exit__(self, exc_type, exc_val, exc_tb):
        # called when leaving 'with' block
        # even if an exception occurred
        self.connection.close()
        return False   # False means: do not suppress exceptions


with DatabaseConnection("db://localhost") as conn:
    conn.execute("SELECT * FROM users")
# __exit__ called automatically here
# connection always closed even if exception raised
```

---

## Callable Dunders

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        # makes the OBJECT callable like a function
        return x * self.factor


double = Multiplier(2)
triple = Multiplier(3)

print(double(5))    # 10  -- calling the object
print(triple(5))    # 15

# this is how ML model inference works:
# model = NeuralNetwork()
# output = model(input_data)   -- calls model.__call__(input_data)
# PyTorch's nn.Module defines __call__ to run forward()
```

---

## Comparison Dunders 

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __eq__(self, other):   # ==
        return self.celsius == other.celsius

    def __ne__(self, other):   # !=
        return self.celsius != other.celsius

    def __lt__(self, other):   # 
        return self.celsius < other.celsius

    def __le__(self, other):   # <=
        return self.celsius <= other.celsius

    def __gt__(self, other):   # >
        return self.celsius > other.celsius

    def __ge__(self, other):   # >=
        return self.celsius >= other.celsius


t1 = Temperature(100)
t2 = Temperature(50)

print(t1 > t2)      # True
print(t1 == t2)     # False
print(sorted([t1, t2]))   # works because __lt__ defined
```

Shortcut: `@functools.total_ordering` -- define `__eq__` and one of `__lt__/__le__/__gt__/__ge__` and Python fills in the rest automatically.

---

## Container Dunders

```python
class Bag:
    def __init__(self):
        self.items = []

    def __len__(self):
        # len(bag)
        return len(self.items)

    def __getitem__(self, index):
        # bag[0], bag[1:3]
        return self.items[index]

    def __setitem__(self, index, value):
        # bag[0] = "apple"
        self.items[index] = value

    def __delitem__(self, index):
        # del bag[0]
        del self.items[index]

    def __contains__(self, item):
        # "apple" in bag
        return item in self.items

    def __iter__(self):
        # for item in bag
        return iter(self.items)


bag = Bag()
bag.items = ["apple", "banana", "cherry"]

print(len(bag))              # 3      -- __len__
print(bag[0])                # apple  -- __getitem__
print(bag[1:3])              # ['banana', 'cherry'] -- __getitem__ slice
bag[0] = "mango"             # __setitem__
del bag[2]                   # __delitem__
print("mango" in bag)        # True   -- __contains__
for item in bag:             # __iter__
    print(item)
```

---

## Attribute Access Dunders

```python
class SmartObject:

    def __getattr__(self, name):
        # called ONLY when normal attribute lookup fails
        # useful for dynamic attributes
        print(f"attribute {name} not found, returning default")
        return None

    def __getattribute__(self, name):
        # called for EVERY attribute access
        # even existing ones
        # dangerous to override -- easy to cause infinite recursion
        print(f"accessing {name}")
        return super().__getattribute__(name)

    def __setattr__(self, name, value):
        # called on EVERY attribute assignment
        print(f"setting {name} = {value}")
        super().__setattr__(name, value)

    def __delattr__(self, name):
        # called on del obj.attr
        print(f"deleting {name}")
        super().__delattr__(name)
```

---

## Numeric Dunders -- Full Set

```python
__add__      # +
__sub__      # -
__mul__      # *
__truediv__  # /
__floordiv__ # //
__mod__      # %
__pow__      # **
__neg__      # -x  (unary minus)
__pos__      # +x  (unary plus)
__abs__      # abs(x)
__round__    # round(x)
__floor__    # math.floor(x)
__ceil__     # math.ceil(x)
__int__      # int(x)
__float__    # float(x)
__complex__  # complex(x)
__bool__     # bool(x)

# reflected versions -- called when left operand returns NotImplemented
__radd__     # other + self
__rsub__     # other - self
__rmul__     # other * self

# in-place versions -- called for += -= *= etc
__iadd__     # +=
__isub__     # -=
__imul__     # *=
```

---

## The Full Dunder Reference

```
LIFECYCLE
__new__          object creation (before __init__)
__init__         object initialization
__del__          object destruction (when refcount hits 0)

REPRESENTATION
__repr__         repr(obj), fallback for str()
__str__          str(obj), print(obj)
__format__       format(obj), f-strings
__bytes__        bytes(obj)

COMPARISON
__eq__           ==
__ne__           !=
__lt__           
__le__           <=
__gt__           >
__ge__           >=
__hash__         hash(obj), dict keys, set membership

NUMERIC
__add__  __radd__  __iadd__     +  +=
__sub__  __rsub__  __isub__     -  -=
__mul__  __rmul__  __imul__     *  *=
__truediv__                     /
__floordiv__                    //
__mod__                         %
__pow__                         **
__neg__  __pos__  __abs__       unary - + abs()
__int__  __float__  __bool__    type conversions

CONTAINER
__len__          len(obj)
__getitem__      obj[key]
__setitem__      obj[key] = value
__delitem__      del obj[key]
__contains__     item in obj
__iter__         for item in obj
__next__         next(obj)
__reversed__     reversed(obj)

ATTRIBUTE ACCESS
__getattr__      obj.name  (only when not found normally)
__getattribute__ obj.name  (every access)
__setattr__      obj.name = value
__delattr__      del obj.name

CALLABLE
__call__         obj(args)

CONTEXT MANAGER
__enter__        with obj as x
__exit__         leaving with block

ASYNC
__await__        await obj
__aiter__        async for
__anext__        async for next value
__aenter__       async with
__aexit__        leaving async with

DESCRIPTORS
__get__          accessing through class
__set__          setting through class
__delete__       deleting through class
```

---

>  these are like overloading the operators but not advised to make the custom dunders

---

```
Dunder methods = Python's operator overloading mechanism
__add__        = overloading +
__mul__        = overloading *
__eq__         = overloading ==
__len__        = overloading len()
__call__       = overloading ()
```

Identical concept to C++ operator overloading:

```cpp
// C++ operator overloading
class Vector {
    Vector operator+(const Vector& other) {
        return Vector(x + other.x, y + other.y);
    }
    
    bool operator==(const Vector& other) {
        return x == other.x && y == other.y;
    }
};
```


```python
# Python exact same concept
class Vector:
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
```

Same idea. Different syntax. Same purpose.

---

## WHY NOT CREATE CUSTOM DUNDERS

The warning is specifically about **inventing new dunder names that do not exist in Python's data model**. Not about using existing ones.

```python
# FINE -- using existing defined dunders
class Dog:
    def __init__(self): pass     # exists in data model
    def __str__(self): pass      # exists in data model
    def __eq__(self, other): pass # exists in data model

# DANGEROUS -- inventing new ones
class Dog:
    def __bark__(self): pass     # does NOT exist in data model
    def __fetch__(self): pass    # does NOT exist in data model
```

Three reasons not to invent new dunders:

### Reason 1 -- Future Collision

Python adds new dunder methods with new versions. If you invent `__bark__` today and Python adds `__bark__` in version 3.15 with completely different meaning, your code silently breaks.

python

```python
# you in 2024
class Dog:
    def __bark__(self):
        return "woof"

# Python 3.15 hypothetically adds __bark__ to mean something else
# your Dog class now accidentally implements that behavior
# no error, silent wrong behavior
```

### Reason 2 -- False Signal

Dunders signal to every Python programmer "this integrates with Python's built-in protocol". Seeing `__bark__` makes them look for what Python feature it hooks into. Finding nothing is confusing.

### Reason 3 -- No Benefit

You gain nothing from the double underscores on a custom method. Just use a regular name:

python

```python
# instead of this
def __bark__(self): return "woof"

# just do this
def bark(self): return "woof"
```

---

## THE PRECISE RULE

```
USE existing dunders      -> always fine, this IS operator overloading
OVERRIDE existing dunders -> always fine, this IS the intended mechanism
INVENT new __name__       -> never do this, use regular method names
```

python

```python
# GREEN -- using and overriding existing dunders
class Matrix:
    def __add__(self, other): ...    # overloading +
    def __mul__(self, other): ...    # overloading *
    def __getitem__(self, idx): ...  # overloading []
    def __len__(self): ...           # overloading len()
    def __repr__(self): ...          # overloading repr()

# RED -- inventing new dunders
class Matrix:
    def __invert_matrix__(self): ... # just call it invert()
    def __normalize__(self): ...     # just call it normalize()
```

---

## THE C++ PARALLEL IS EXACT

```
C++                          Python
---                          ------
operator+                    __add__
operator-                    __sub__
operator*                    __mul__
operator/                    __truediv__
operator==                   __eq__
operator<                    __lt__
operator[]                   __getitem__
operator()                   __call__
operator<<  (stream out)     __str__ / __repr__
constructor                  __init__
destructor                   __del__
```

- The only difference is Python's operator overloading also covers built-in functions like `len()`, `abs()`, `int()`, `bool()` which C++ does not have direct equivalents for in the same way. Python's data model is broader than C++ operator overloading but the core concept is identical.
