# Topics 

- Object Class
- Heirarcy

_____

# Tree

```
object  (PyBaseObject_Type in C)
|
+-- int  (PyLong_Type)
|     |
|     +-- bool  (PyBool_Type)
|                True, False are instances
|
+-- float  (PyFloat_Type)
|
+-- complex  (PyComplex_Type)
|            2+3j  type
|
+-- str  (PyUnicode_Type)
|
+-- bytes  (PyBytes_Type)
|          b"hello"
|
+-- bytearray  (PyByteArray_Type)
|              mutable version of bytes
|
+-- memoryview  (PyMemoryView_Type)
|               zero-copy view into buffer
|
+-- NoneType  (PyNone_Type)
|             None is the only instance
|
+-- NotImplementedType
|   NotImplemented is the only instance
|
+-- ellipsis  (PyEllipsis_Type)
|             ... is the only instance
|
+-- type  (PyType_Type)
|         THIS IS THE METACLASS
|         the class of all classes
|         including itself
|
+-- super  (PySuper_Type)
|          used for super() calls
|
+-- BaseException
|     |
|     +-- Exception
|     |     |
|     |     +-- ArithmeticError
|     |     |     |
|     |     |     +-- FloatingPointError
|     |     |     +-- OverflowError
|     |     |     +-- ZeroDivisionError
|     |     |
|     |     +-- LookupError
|     |     |     |
|     |     |     +-- IndexError
|     |     |     +-- KeyError
|     |     |
|     |     +-- AttributeError
|     |     +-- ImportError
|     |     |     |
|     |     |     +-- ModuleNotFoundError
|     |     |
|     |     +-- NameError
|     |     |     |
|     |     |     +-- UnboundLocalError
|     |     |
|     |     +-- TypeError
|     |     +-- ValueError
|     |     |     |
|     |     |     +-- UnicodeError
|     |     |           |
|     |     |           +-- UnicodeDecodeError
|     |     |           +-- UnicodeEncodeError
|     |     |           +-- UnicodeTranslateError
|     |     |
|     |     +-- OSError
|     |     |     |
|     |     |     +-- FileNotFoundError
|     |     |     +-- PermissionError
|     |     |     +-- TimeoutError
|     |     |     +-- ConnectionError
|     |     |           |
|     |     |           +-- BrokenPipeError
|     |     |           +-- ConnectionRefusedError
|     |     |
|     |     +-- RuntimeError
|     |     |     |
|     |     |     +-- RecursionError
|     |     |     +-- NotImplementedError
|     |     |
|     |     +-- StopIteration
|     |     +-- StopAsyncIteration
|     |     +-- MemoryError
|     |     +-- BufferError
|     |
|     +-- Warning
|     |     |
|     |     +-- DeprecationWarning
|     |     +-- RuntimeWarning
|     |     +-- SyntaxWarning
|     |     +-- UserWarning
|     |     +-- FutureWarning
|     |     +-- ResourceWarning
|     |
|     +-- SystemExit
|     +-- KeyboardInterrupt
|     +-- GeneratorExit
|
+-- Sequences (Abstract -- collections.abc)
|     |
|     +-- list  (PyList_Type)
|     |     |
|     |     +-- (no built-in children
|     |          but you can subclass)
|     |
|     +-- tuple  (PyTuple_Type)
|     |
|     +-- range  (PyRange_Type)
|     |
|     +-- str    (already shown above)
|     |
|     +-- bytes  (already shown above)
|
+-- Mappings
|     |
|     +-- dict  (PyDict_Type)
|
+-- Sets
|     |
|     +-- set  (PySet_Type)
|     |
|     +-- frozenset  (PyFrozenSet_Type)
|
+-- Callables / Functions
|     |
|     +-- function  (PyFunction_Type)
|     |             def foo(): ...
|     |
|     +-- method  (PyMethod_Type)
|     |           bound method on a class
|     |
|     +-- builtin_function_or_method
|     |   print, len, range etc
|     |
|     +-- classmethod  (PyClassMethod_Type)
|     +-- staticmethod (PyStaticMethod_Type)
|     +-- lambda       (same as function internally)
|
+-- Iterators
|     |
|     +-- list_iterator
|     +-- tuple_iterator
|     +-- str_iterator
|     +-- dict_keyiterator
|     +-- dict_valueiterator
|     +-- dict_itemiterator
|     +-- set_iterator
|     +-- range_iterator
|     +-- generator  (PyGen_Type)
|     +-- coroutine  (PyCoroType)
|     +-- async_generator
|
+-- Code and Frames
|     |
|     +-- code    (PyCode_Type)
|     |           compiled bytecode object
|     |
|     +-- frame   (PyFrame_Type)
|                 execution frame
|
+-- Modules
|     |
|     +-- module  (PyModule_Type)
|                 every import is an instance
|
+-- I/O
      |
      +-- TextIOWrapper
      +-- BufferedReader
      +-- BufferedWriter
      +-- FileIO
```


## The Absolute root

Everything in Python inherits from one thing:

```
object
```

That is the root. Every class, every type, every built-in, every class you ever write -- all of them have `object` at the top of their chain.

```python
print(int.__bases__)       # (<class 'object'>,)
print(str.__bases__)       # (<class 'object'>,)
print(list.__bases__)      # (<class 'object'>,)
print(bool.__bases__)      # (<class 'int'>,)  -- int, not object directly
```

- Everything like functions, datatypes, builtins 
- it inheriets to `type` 
- the `type` creates all classes it is called metaclass

```python
print(type(object))    # <class 'type'>
print(type(type))      # <class 'type'>
print(isinstance(type, object))    # True
print(isinstance(object, type))    # True
```

They are defined in terms of each other:

```
object  is an instance of  type
type    is an instance of  type    (itself)
type    is a subclass of   object
object  is NOT a subclass of type
```

Visually:

```
                    +-----------+
                    |           |
        isinstance  |           v
object <=========== type ======> type
  ^                  |    isinstance
  |   subclass       |    (itself)
  +------------------+
```

- In C this circular relationship is bootstrapped manually when CPython starts. `PyType_Type` and `PyBaseObject_Type` are statically defined and their fields are manually cross-linked at interpreter startup. It is a chicken-and-egg problem solved by hardcoding the initial state.

```python
# walk the full MRO (Method Resolution Order) of any class
print(bool.__mro__)
# (<class 'bool'>, <class 'int'>, <class 'object'>)

print(IndexError.__mro__)
# (<class 'IndexError'>, <class 'LookupError'>,
#  <class 'Exception'>, <class 'BaseException'>, <class 'object'>)

# see all subclasses of a class
print(int.__subclasses__())
# [<class 'bool'>, <enum 'IntEnum'>, ...]

print(BaseException.__subclasses__())
# [<class 'Exception'>, <class 'GeneratorExit'>,
#  <class 'SystemExit'>, <class 'KeyboardInterrupt'>]
```


```
bool      subclass of int       -> True/False are 1/0
int       subclass of object    -> everything is object
type      subclass of object    -> even the metaclass
type      instance of type      -> type creates itself
object    instance of type      -> object was created by type
NoneType  only has one instance -> None
ellipsis  only has one instance -> ...
function  is an object          -> functions are first class
module    is an object          -> imports are objects
frame     is an object          -> execution state is inspectable
code      is an object          -> bytecode is inspectable
```