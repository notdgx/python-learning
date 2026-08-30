# RevisedNotesDicts

--- 

## Metadata

- **Day :** Thursday
- **Date :** 2025-09-11
- **Time :** 12:25
- **Tags :** #python #dicts #Revised   
- **References :** [[RevisedNotes]], [[FunctionDicts]] , [[ImportantQuestionsDicts1]]
- **Branch of :** Python > Revisednotes > RevisedNotesDicts
- **Author :**  dx

---

# Notes

---

## **len() :** gives the length of iterable
## **dict.clear() :**
* it will delete every thing in the dict but still dictionary will remain even though it is empty 
* output none 
* modifies original dict in place
* TypeError if any arg is passed 
* affect all the references , not same as reassigning

```python
a = {"k": 1}
b = a
a.clear()
print(b)  # {}

**Not the same as reassigning**

d = {"a": 1}
e = d
d = {}        # only d changes, e stays {"a": 1}`

```

* if multiple threads share a dictionary, calling `.clear()` while others iterate may cause runtime errors (`RuntimeError: dictionary changed size during iteration`).

## dict.copy ()

* it creates a shallow copy of the dictionary 
* TypeError if any arg is passed
* returns a new copy of dictionary
* it creates a new onject it does not point to same object if the onj is not cached for small dicts
* Attribute error if not dictionary or copyable
* If the values are **mutable objects** (like lists or dicts), they are **shared** between original and copy.
* this is only case of nested dict , lists as they are mutable the are nested in a dict but actually they are a datatype pointing a something if we do this they are also changed
#### Why mutable values behave this way in `dict.copy()`

###### 1. Mutables vs immutables in Python

- **Immutable types** (`int`, `float`, `str`, `tuple`):
    - Once created, they can’t be changed in place.
    - If you assign or copy them, you just copy the value (or technically, the reference, but since they can’t change, it doesn’t matter).
- **Mutable types** (`list`, `dict`, `set`, custom objects):
    - They **can be modified in place**
    - Copying a reference means two variables can now mutate the same object.

```python
nested = {"a": [1, 2]}
c = nested.copy()

c["a"].append(3)
print(nested)   # {'a': [1, 2, 3]}
print(c)        # {'a': [1, 2, 3]}


for  a tuue copy use

import copy
deep = copy.deepcopy(nested)
```


## dict.fromkeys(iterable , key=None)

* it is used to create key value pair from a iterable of keys , 
* by defauly it defile all the keys in iterable with value None
* we can change it though
* and if the iterable has duplicate values it will ignore it and only take the non duplicate values only 
* it a str is passed it will make its each char as a key
* returns a new dict
* TypeError if non iteranle
* if itrerable or key is something mutable sequence like list or dict it will share the same object 
```python
d = dict.fromkeys(["a", "b"], [])
d["a"].append(1)
print(d)  
# {'a': [1], 'b': [1]}  <-- both changed!
```

* can be used as
```python
d = dict.fromkeys(range(5), 0)
print(d)  
# {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
```


## dict.get(key , default=None)

* give the value as per key or default value
* by default if key is not found then the default which is None is returned 
* we can set our own default 
* TypeError if different number of arg
* safer than d[key] as it will return key error
* best and fastest way to count freuency 
```python
s = "banana"
freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1
print(freq)  # {'b': 1, 'a': 3, 'n': 2}
```

* # What does “unhashable key” mean?

##### 1. How dict keys work
- A **dict** in Python is a **hash table**.
- Keys must be **hashable** so Python can:
    - Compute a **hash value** (an integer) for the key.
    - Use that hash to decide **where to store / find** the key’s value quickly.
If a key has no fixed hash, Python can’t put it in the dict.


## dict.items()


* it will return a object containing sequence of tuple of key,value pair as dict_items([('a', 1), ('b', 2), ('c', 3)])
* accesses able as
* it return dict_items object

```python
for k, v in d.items():
print(k, v)
```

* ```python
  squared = {k: v**2 for k, v in d.items() if v % 2 == 0}

  ```

* no error if empty
* error if any arg passed


## dict.keys()

* it returns dict_keys object 
* which can be further wrapped in list(), tuple()
* TypeError is any arg passed
* No error if empty it will return empty dict_key object
* Convert to **list**, **tuple**, or **set** if you need indexing or set operations:
```python
list(d.keys())    # ['a', 'b', 'c', 'd']
tuple(d.keys())   # ('a', 'b', 'c', 'd')
set(d.keys())     # {'a', 'b', 'c', 'd'}
```


## dict.pop(key , default)

* KeyError if not found or default is not found
* remove the specifed key value pair and return the value of it
* Type Error if no arg passed
* if dict is empty it will give KeyError if default provided then default 

## dict.popitem( )

* it takes no arg 
* TypeError if arg passed
* Removes and returns a **key-value pair** as a **tuple** `(key, value)`.
* remove the last intersection 
* return it as tuple
* KeyError if empty dict 
```python
d = {"a": 1, "b": 2, "c": 3}
item = d.popitem()
print(item)  # ('c', 3)  # Python 3.7+: removes last inserted item
print(d)     # {'a': 1, 'b': 2}
```

## dict.setdefault(key, default=None)

* returns the key if not present then if default provided it will add a key value pair as that
 - If **key exists**, returns its value **without changing it**.
- If **key does not exist**, adds it with the **default value** and returns it.
- best use counting frequency making 
```python
s = "banana"
count = {}
for ch in s:
    count.setdefault(ch, 0)
    count[ch] += 1
print(count)
# {'b': 1, 'a': 3, 'n': 2}
```
* **Does not overwrite existing values**


## dict.update(other_dict)
Syntaxes : 
dict.update([other])
dict.update(**kwargs)

* output none 
* modifies the original dict
* TypeError if invalid input format - non iterable
* Updates the dictionary with key-value pairs from another dictionary or iterable of pairs if  the other dict has same key then it will update the key of old dict as other dict new key value pair
```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

d1.update(d2)
print(d1)
# {'a': 1, 'b': 3, 'c': 4}
```
- Keys in `d2` overwrite keys in `d1`.
- Keys not present in `d1` are **added**.
```python
d = {"a": 1}
pairs = [("b", 2), ("c", 3)]
d.update(pairs)
print(d)
# {'a': 1, 'b': 2, 'c': 3}

UPDATING

d = {"a": 1}
d.update(b=2, c=3)
print(d)
# {'a': 1, 'b': 2, 'c': 3}


Enmpty dict behaviour

d = {}
d.update({"x": 100})
print(d)
# {'x': 100}

d.update([])
print(d)
# {}  # no change
 

```

## dict.values()

* it gives dict_value object
* TypeError if arg passed
```python
d = {"a": 1, "b": 2, "c": 3}
print(d.values())
# dict_values([1, 2, 3])

for v in d.values():
    print(v)
# 1
# 2
# 3


CAN BE FURTHER WRAPPED

vals_list = list(d.values())
vals_tuple = tuple(d.values())
vals_set = set(d.values())

**Not a list** — you cannot index directly:

d.values()[0]  # TypeError

```

---
