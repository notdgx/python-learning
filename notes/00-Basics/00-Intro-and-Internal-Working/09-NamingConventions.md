# Topic 

- Naming Conventions

___

# Hard Rules

- These are not suggestions. Break them and Python raises a SyntaxError before a single line executes. The symbol table pass we discussed earlier catches these during compilation.

---

### Valids

```python
# VALID starting characters
name        # letters
_name       # underscore
__name      # double underscore
_           # just underscore alone (valid, used as throwaway)
name123     # letters then numbers

# INVALID starting characters
1name       # SyntaxError -- cannot start with digit
-name       # SyntaxError -- cannot start with hyphen
@name       # SyntaxError -- @ is decorator syntax
$name       # SyntaxError -- $ not valid at all in Python
#name       # SyntaxError -- # starts a comment
```


```python
# VALID characters AFTER the first character
name_1      # underscore anywhere
camelCase   # mixed case
name123     # digits after first char fine
__dunder__  # double underscores

# INVALID characters anywhere
my-var      # SyntaxError -- hyphen is subtraction operator
my var      # SyntaxError -- space not allowed
my.var      # this is attribute access not a variable name
my@var      # SyntaxError
```

---

### Unicode Is Valid 
- But Do Not Use It
- Not Conventially Preffered
- Python 3 allows unicode identifiers because the language spec allows any unicode letter:

```python
# technically valid Python 3
café = "coffee"
print(café)       # works

# also valid
π = 3.14159
print(π)          # works

# also valid (please never do this)
变量 = 10
print(变量)        # works
```

Valid but never use non-ASCII identifiers in real code. Causes encoding issues, breaks tooling, confuses every collaborator.

## Keywords

### Hard KeyWords

- These are hardcoded in the lexer. They are not looked up in any symbol table. The lexer recognizes them as special tokens before parsing even begins:

```python
import keyword
print(keyword.kwlist)
```

```
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
```


```python
# all of these are SyntaxError
class = "dog"       # SyntaxError
if = 10             # SyntaxError
return = 5          # SyntaxError
True = 1            # SyntaxError
None = "nothing"    # SyntaxError
```

---

### Soft Keywords

- (Python 3.10+)
- These are keywords only in specific contexts. Valid as variable names elsewhere:

```python
match = 10          # valid -- match is only keyword in match statement
type = "dog"        # valid -- type is only keyword in type alias statement

match command:      # here match IS a keyword
    case "quit":
        quit()
```

________
________

# NAMING CONVENTIONS (PEP 8)

- PEP 8 is Python's official style guide. These are not enforced by the language. Enforced by your team, linters, and professional standards.

---
### Variables and Functions 
>snake_case

```python
# CORRECT
user_name = "alice"
total_count = 0
is_valid = True
max_retry_attempts = 3

def calculate_area(radius):
    return 3.14 * radius ** 2

def get_user_by_id(user_id):
    pass

def is_authenticated(user):
    pass

# WRONG (but valid Python)
userName = "alice"        # camelCase -- used in Java/JS not Python
TotalCount = 0            # PascalCase -- used for classes not variables
MAXRETRYATTEMPTS = 3      # should be snake_case unless it is a constant
```

---

### Constants 

> UPPER_SNAKE_CASE

```python
# module level constants
MAX_CONNECTIONS = 100
PI = 3.14159265358979
DEFAULT_TIMEOUT = 30
BASE_URL = "https://api.example.com"
MAX_RETRIES = 3

# in ML specifically
LEARNING_RATE = 0.001
BATCH_SIZE = 32
NUM_EPOCHS = 100
HIDDEN_DIM = 256
VOCAB_SIZE = 50000
```

- Python does not enforce immutability on these. UPPER_CASE is purely a signal to humans saying "do not change this". The language does not care. You can reassign PI = 99 and Python will not complain. Convention is the only enforcement.

---

### Classes

>PascalCase (UpperCamelCase)

```python
# CORRECT
class UserAccount:
    pass

class HttpRequest:
    pass

class NeuralNetwork:
    pass

class MultiHeadAttention:
    pass

# WRONG
class user_account:     # looks like a function
    pass

class userAccount:      # camelCase -- not Python convention
    pass

class USERACCOUNT:      # all caps -- looks like a constant
    pass
```

---

### Private and Special Names 
>Underscores

This is where Python has a real system with actual behavioral differences, not just convention:
#### Single Leading Underscore -- _name

```python
class BankAccount:
    def __init__(self):
        self.balance = 1000       # public -- use freely
        self._transaction_log = []  # internal -- do not touch from outside

    def _validate_amount(self, amount):   # internal method
        return amount > 0
```

- Convention only. Means "internal implementation detail, not part of public API, may change without notice". Python does not enforce this. You can still access `account._transaction_log` and Python will not stop you. It is a warning sign not a lock.

One real behavioral effect -- module level single underscore names are NOT imported by `from module import *`:

```python
# mymodule.py
public_var = 1
_private_var = 2       # this will NOT be imported
__very_private = 3     # this will NOT be imported

# elsewhere
from mymodule import *
print(public_var)      # works
print(_private_var)    # NameError -- not imported
```

#### Double Leading Underscore -- __name (Name Mangling)

This one has REAL behavioral effect. Python actively rewrites the name:

```python
class Dog:
    def __init__(self):
        self.__secret = "buried bone"    # name mangling applied here

dog = Dog()
print(dog.__secret)          # AttributeError -- name was mangled
print(dog._Dog__secret)      # "buried bone" -- mangled name works
```

Python renames `__secret` to `_Dog__secret` at compile time. This is **name mangling**. The purpose is to avoid accidental override in subclasses:

python
```python
class Animal:
    def __init__(self):
        self.__id = "animal_001"    # becomes _Animal__id

class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.__id = "dog_001"       # becomes _Dog__id -- DIFFERENT attribute
                                    # does not overwrite Animal's __id

d = Dog()
print(d._Animal__id)    # "animal_001"  -- Animal's version safe
print(d._Dog__id)       # "dog_001"     -- Dog's version separate
```

Without name mangling, `self.__id` in Dog would overwrite Animal's `self.__id`. Mangling gives each class its own private namespace.

#### Double Leading AND Trailing Underscore -- **name** (Dunder)


```python
__init__        # constructor
__str__         # string representation
__len__         # len() support
__add__         # + operator
__eq__          # == operator
__repr__        # developer representation
__enter__       # context manager entry
__exit__        # context manager exit
__iter__        # iteration support
__next__        # iterator next value
__call__        # make object callable
__getitem__     # [] access
__setitem__     # [] assignment
__contains__    # in operator
```

Never create your own `__name__` variables. These are reserved for Python's data model. Python will not stop you but you will collide with existing or future Python behavior.

#### Single Underscore Alone -- _


```python
# throwaway variable -- you do not need this value
for _ in range(10):
    print("hello")        # _ used when loop variable not needed

# unpacking throwaway
x, _, z = (1, 2, 3)      # ignoring middle value
first, *_ = [1, 2, 3, 4] # ignoring everything after first

# in REPL -- last result
>>> 5 + 3
8
>>> _
8                          # _ holds last evaluated result in interactive mode
```

---

### Type Hint Conventions (modern Python)


```python
# variables
name: str = "alice"
age: int = 30
scores: list[float] = [9.5, 8.0, 9.1]
config: dict[str, int] = {"timeout": 30}

# functions -- always annotate public functions
def greet(name: str, times: int = 1) -> str:
    return name * times

# when type is unknown or multiple
from typing import Optional, Union, Any

def find_user(user_id: int) -> Optional[str]:  # might return None
    pass

def process(data: Union[str, bytes]) -> None:  # str or bytes
    pass

# modern Python 3.10+ -- cleaner union syntax
def process(data: str | bytes) -> None:        # same as Union
    pass

def find_user(user_id: int) -> str | None:     # same as Optional
    pass
```


## INTERNALLY Variable NAMES

### Names Are Dictionary Keys

Every scope in Python is a dictionary. Variable names are literally string keys in that dictionary:

```python
x = 10
y = "hello"

# at module level this is stored in:
print(globals())
# {..., 'x': 10, 'y': 'hello', ...}
# x and y are STRING KEYS in a real Python dict

def foo():
    a = 1
    b = 2
    print(locals())    # {'a': 1, 'b': 2}
                       # also a dict
```

For module level and class level, names are stored in a `__dict__` dictionary. This is why globals() and locals() return actual dicts -- they ARE the actual storage.

For function locals specifically, CPython optimizes this. Because the symbol table pass already knows all local names at compile time, local variables are stored in a fixed-size array in the frame (f_localsplus) indexed by integers, not a dict. `LOAD_FAST 0` means "load local variable at index 0" -- direct array access, no hash lookup. `locals()` builds a dict from this array on demand.

---

### The Name Binding Operations

Every way a name gets created in Python is called a **binding operation**:

```python
x = 10                  # assignment -- binds x
def foo(): pass         # def -- binds foo to function object
class Dog: pass         # class -- binds Dog to class object
import numpy            # import -- binds numpy to module object
from os import path     # from import -- binds path
for x in range(10):     # for -- binds x each iteration
with open("f") as f:    # with -- binds f
except Exception as e:  # except -- binds e
x: int = 10            # annotated assignment -- binds x
(a, b) = (1, 2)        # unpacking -- binds a and b
[a, *b, c] = [1,2,3,4] # extended unpacking -- binds a, b, c
```

All of these ultimately do the same thing at the PyObject level -- they make a name point to a PyObject. Different syntax, same underlying operation: store a pointer in the scope's dictionary or frame array.

---

### Deletion

```python
x = 10
del x           # removes the binding
                # decrements ob_refcnt of the PyObject
                # if refcount hits 0, PyObject freed
                # the name x no longer exists in scope

print(x)        # NameError -- name 'x' is not defined
```

`del` does not delete the PyObject directly. It removes the name binding and decrements the reference count. The PyObject is only freed if nothing else points to it.

---

### Name Resolution at Bytecode Level

python

```python
x = 10              # module level

def foo():
    print(x)        # which x?

def bar():
    x = 20          # local x
    print(x)
```

The bytecode for `foo`:

```
LOAD_GLOBAL   x    # symbol table said x is global in foo
```

The bytecode for `bar`:

```
LOAD_FAST     x    # symbol table said x is local in bar
```

The decision between `LOAD_GLOBAL` and `LOAD_FAST` is made at compile time by the symbol table pass. By the time bytecode runs, Python already knows which scope each name lives in. This is why:

python

```python
def broken():
    print(x)        # UnboundLocalError not NameError
    x = 10          # symbol table sees this assignment
                    # marks x as LOCAL for entire function
                    # so LOAD_FAST is emitted for print(x)
                    # but x not assigned yet at that point
                    # hence UnboundLocalError
```

This surprises people. The error is UnboundLocalError not NameError because Python decided at compile time that x is local (due to the assignment below), emitted `LOAD_FAST`, but the value has not been assigned yet when `LOAD_FAST` runs.