# Topics 

- `type()`
- type as a MetaClass


_______

# PyTypeObject -- type()

This is the most important struct. Every `ob_type` pointer points to one of these. It is the class itself as a C struct:

```c
// Simplified -- actual struct has 50+ fields
typedef struct _typeobject {
    PyObject_VAR_HEAD           // it is itself a Python object

    const char  *tp_name;       // "int", "str", "list" etc
    Py_ssize_t   tp_basicsize;  // size of instances in bytes
    Py_ssize_t   tp_itemsize;   // for variable size objects

    // function pointers -- the methods
    destructor   tp_dealloc;    // called when refcount hits 0
    reprfunc     tp_repr;       // __repr__
    PyNumberMethods   *tp_as_number;    // __add__, __mul__ etc
    PySequenceMethods *tp_as_sequence;  // __len__, __getitem__ etc
    PyMappingMethods  *tp_as_mapping;   // for dicts
    hashfunc     tp_hash;       // __hash__
    ternaryfunc  tp_call;       // __call__
    richcmpfunc  tp_richcompare;// __eq__, __lt__ etc

    // class hierarchy
    PyObject    *tp_bases;      // tuple of base classes
    PyObject    *tp_mro;        // method resolution order

    // ... 40+ more fields
} PyTypeObject;
```

When you call `x + y` in Python:

```
1. get x->ob_type           -> points to PyLong_Type
2. get PyLong_Type->tp_as_number  -> number methods table
3. get tp_as_number->nb_add -> function pointer to int addition
4. call that function with x and y
```

- Every operation on every object is a function pointer lookup in the type struct. This is how Python implements operator overloading -- `__add__`, `__mul__` etc are just entries in this struct.
- The `type()` has two functions to create classes and get the type of the object
- `type` is a MetaClass the class Which  create classes

- Every PyObject has `ob_type`. That field answers the question "what am I?":
```python
x = 10
# ob_type of x's PyObject points to --> int

s = "hello"  
# ob_type of s's PyObject points to --> str
```

- `ob_type` points to a **class object**. That class object is what `type()` returns:

```python
print(type(10))        # <class 'int'>
print(type("hello"))   # <class 'str'>
print(type(3.14))      # <class 'float'>
print(type([1,2,3]))   # <class 'list'>
```

- `type(x)` literally just reads `x`'s `ob_type` field and returns what it points to. That is all it does at the basic level.

## Type Functions

`type` in Python does TWO completely different things depending on how you call it:

```
type(one argument)    ->  returns the type of that object
type(three arguments) ->  CREATES a new class
```

### Checking type:

```python
type(10)           # returns int
type("hello")      # returns str
type([1,2,3])      # returns list
```

### Creating a class:

```python
# normally you write a class like this:
class Dog:
    def bark(self):
        return "woof"

# but internally Python does THIS:
Dog = type("Dog", (object,), {"bark": lambda self: "woof"})

# these two are IDENTICAL
# type() with 3 args creates a class
```

The three arguments are:

```
type(name,         bases,          dict)
     "Dog"         (object,)       {"bark": function}
     |              |               |
     class name     parent classes  methods and attributes
```

## Type is a MetaClass

A ==metaclass is the class of a class==. Sounds circular. 

```
Normal object:    instance of a class
                  Dog() is an instance of Dog

Class:            instance of a metaclass
                  Dog is an instance of type
```

```python
class Dog:
    pass

rex = Dog()

print(type(rex))   # <class 'Dog'>    rex is instance of Dog
print(type(Dog))   # <class 'type'>   Dog is instance of type
print(type(type))  # <class 'type'>   type is instance of ITSELF
```

Visually:

```
type() creates --> Dog class
Dog  creates  --> rex object

rex   --[instance of]--> Dog
Dog   --[instance of]--> type
type  --[instance of]--> type (itself)
```

---

### The Circular Relationship

```python
print(isinstance(type, object))    # True
print(isinstance(object, type))    # True
print(issubclass(type, object))    # True
print(issubclass(object, type))    # False
```

Break it down:

```
isinstance(type, object)   -> True
meaning: type is an INSTANCE of object
meaning: type is an object (everything is)
meaning: type's ob_type chain eventually reaches object

isinstance(object, type)   -> True
meaning: object is an INSTANCE of type
meaning: the object class was CREATED by type
meaning: object's ob_type points to type

issubclass(type, object)   -> True
meaning: type INHERITS from object
meaning: type is a child class of object

issubclass(object, type)   -> False
meaning: object does NOT inherit from type
meaning: object is not a child of type
         but it IS an instance of type (different thing)
```

The difference between **instance of** and **subclass of**:

```
subclass  = inheritance = IS-A relationship in the class hierarchy
instance  = an object created from that class

Dog subclass Animal   -> Dog IS-A Animal, inherits its behavior
rex instance Dog      -> rex is a specific Dog object
```

So:

```
type is a subclass of object   -> type inherits from object
object is an instance of type  -> object was created by type

They reference each other but in different ways.
Subclass = hierarchy. Instance = creation.
```

In C this is bootstrapped by hand -- both PyType_Type and PyBaseObject_Type are statically allocated and their fields manually cross-linked when CPython starts. The chicken-and-egg problem is solved by just hardcoding the initial state.


____________
## Properties & Realtionship 

- the `type()` checks who created the class ? internally it checks the `ob_type` of the class or object

```python
x = 5
print(type(x)) # <class 'int'>
```

- The type here checks who created the object x it was created by class int
- How a class creates a calss ? Butt internally the class created itself actually is a Object 
### The Custom Classes

- If we make like 

```python
class Dog:
    pass
```
- The class Dog internally ==Object is created by type which is a metaclass== ie that creates class 

```
           type
             ↑
     creates classes
             ↑
           Dog
             ↑
     creates objects
             ↑
             d
```

- ==d is a instance of Dog==
- ==Dog is a class created by type (internally the Dog itself is a object)==
- ==type is a metaclass which created classes==
- ==`type -> Dog -> dog_instance`==
- ==d is instance of Dog==
- ==Dog is instance of type==
- ==type is instance of type==

```
class Dog:    pass
```

Python is ACTUALLY doing something conceptually similar to:

```
Dog = type("Dog", (), {})
```

So:

- ==`type` creates the class object==
- ==the resulting class object is `Dog`==

Meaning:

```
Dog is an OBJECT
```

and its type is:

```
type(Dog)# <class 'type'>

Custom classes are objects of type

type  ---> creates ---> Dog class object
Dog   ---> creates ---> d instance object
```

### int,str,list & other

- ==They are ALSO class objects.==
- ==Every thing is a instance of type== 
- ==type is want creares them==
- ==but type and other classes itself is a inherited by object root class==
- ==The type also creates object class==
- ==They everything even the type enherits from object and the custom made classes also==

==so object is a class from whic type inheriets and evry one heroits that is the inheriting part but in runtime thhe type is the on e who create everything in form of instance the object , itself , type instance itself etc==

```python
print(type(int))
print(type(str))
print(type(list))
```

Output:
```
<class 'type'>
<class 'type'>
<class 'type'>
```

Meaning:
```
int is object of type
str is object of type
list is object of type
```

#### Creation & Inherientence

1. type -> Dog -> d
2. object -> Dog -> d

______

```
                    inheritance
                        ▲
                        │
                      object
                        ▲
                        │
                      type
                    /  |  \
             creates class objects
                /     |      \
              int    str    MyClass
               │      │       │
            instances instances instances
               │      │       │
              42    "hello"    x
```


## Final 

### What actually is a type ? 

- So In python everything is a object 
- The each object's class defination is inherited from the root `object` class
- The `int`,`str`,`list`,`type` and custom made all are inherited from the `object` class
- This is inherientence part but creation part handeled by the type
- `type` created the `object` object it also creates `int`,`str`,`list`,`type` itself also and custom classes which basically is object internally 
- The further custom classes objects are created by that custom class ie Object for the python internally
- It has two jobs the type it tells the `ob_type` ie the object points to which class
- Second is it creates objects (internally) ie custom classes by `Dog = type("Dog", (), {})`
- So when we define a class python internally calls the above function to create custom class ie object for python intrnally
- and that custom class object is created byt the custom class
- All the classes are created by `type` which is a running object created by class `type` which is inherited form the `object` root class
- So in defination `type` is a metaclass but when program runs `type` metaclss creates itself object and further `type` creates other class objects ...
- A Python class is a real runtime object created by the metaclass type, and that class object then acts as a blueprint/factory for creating normal instance objects.
- type does NOT create all objects directly, Classes create normal instances, `type` creates CLASS objects.
- type is itself an instance of type `type(type) == type` {Ok}

### Summary

In Python, almost everything is an object, including classes themselves. The root base class of the inheritance system is `object`, meaning nearly all classes such as `int`, `str`, `list`, custom classes, and even `type` ultimately inherit from `object` and receive foundational behavior like attribute handling, identity, and default representations from it. However, inheritance and creation are two different systems: inheritance describes what behavior a class gets, while creation describes who constructs an object. Normal classes act as blueprints that create instance objects, for example `Dog()` creates a `Dog` instance, but classes themselves are also objects that must be created by something else. That creator is usually the built-in metaclass `type`. When Python sees a class definition like `class Dog: pass`, it internally constructs the class object using `type`, conceptually similar to `Dog = type("Dog", (), {})`. Therefore, `Dog` is an instance of `type`, just as `d = Dog()` makes `d` an instance of `Dog`. The same applies to built-in classes: `int`, `str`, and `list` are all class objects created by `type`. This creates a hierarchy such as `type -> Dog -> d` or `type -> int -> 5`, where `type` creates classes and classes create normal objects. A metaclass is simply a class whose instances are classes, meaning it controls how classes are constructed. Python’s default metaclass is `type`, but custom metaclasses can modify or validate classes during their creation. The system becomes self-referential because `type` itself inherits from `object`, while `object` is also an instance of `type`, forming Python’s internal bootstrap loop. So the complete mental model is: `object` is the root parent class providing shared behavior, `type` is the default metaclass that constructs class objects, classes construct instance objects, and all of these are themselves objects inside Python’s unified object system.