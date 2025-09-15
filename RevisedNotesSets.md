# RevisedNotesSets

--- 

## Metadata

- **Day :** Monday
- **Date :** 2025-09-15
- **Time :** 10:23
- **Tags :** #python #Sets #Revised #  
- **References :** [[RevisedNotes]] , [[FunctionsSets]] , [[ImportantQuestionsSets1]]
- **Branch of :** Python > RevisedNotes > RevisedNotesSets
- **Author :**  dx

---

# Notes

---

## len(set)
* it will give the length of a set
* TypeErrror if non iterable is passed 
* if we assigned a set with duplicates the it will consider it as a single and then return length of a non duplicate vslues

## sorted(set , * , key=None , reverese=True)

* as set is a unordered dstatype so sorted function on a set returns a list of sorted elements of set
* TypeError if not comararble
- **Removes duplicates automatically** (since set already has unique elements).
- Sorting works only if **elements are comparable**.
- sorting by the length of a str
```python
s = {"apple", "kiwi", "banana"}
print(sorted(s, key=len))  # ['kiwi', 'apple', 'banana']
```
* **Sorting large sets** is **O(n log n)** → can be slow for very large datasets.
* 

## min() / max() / sum() / all() / any() 
These work as same as for others

## set.add(element)
* adds a single element to the set
* returns none as modifies the original set
* TypeError is not hashable like list,dict
* cant be chaned as it returns none
* no duplicates allowed if we add a existing element nothing happens but it will be shown as non duplicated
* cant add multiple values at once it will give TypeError if more than one arg
* order is not graunteed


## set.update(iterable1 , iterable2 , .....)

* Returns None
* TypeError if not a iterable or 
* add all elements fom the itertable like a extend function but uunordered 
* we can add values from a list , dict but list must only have hashable values and only keys will be added from dict as they are hashable
* range(1,10) can also be used  as it returns a iterator obj
* multiple iterable values can be added
* it is like  a bulk union but it updates in the set
* update the str charachters
```python
s = {"a"}
s.update("hello")
print(s)  # {'a', 'h', 'e', 'l', 'o'}
```

## set.remove(element)

* it will remove the element from the set
* returns None modifies the original
* KeyError if not present
* TypeError if unhashable passed
```python
#to safley remove element by remove()

x=6
if x in a:
    a.remove(x)
    print(a)
```

## set.discard(element)

* it will remove the element from the set
* it will returns None modifies the original 
* Doesnt raise KeyError if not present **use it more over remove** it gives None
* TypeErro if unhashable as a arg
- Safe removal → **no error if element missing**.
- Works only with **hashable elements**.
- **Safe removal (avoid KeyError)**
```python
s = {1, 2, 3}
s.discard(4)  # safe, no crash
print(s)  # {1, 2, 3}
```


## set.pop()

* it will remove any random value from the set
* return the element removed 
* TypeError if any arg passed
* KeyError id set is empty 
* safe use
```python
return set.pop() if set else "EMPTY"
```


## set.clear()

* emptiess the set
* but doesnot delete it from memory
* returns None
* No Errors
* TypeError if arg is passed
- After `.clear()`, the set is still valid but **empty**
- Works safely even if the set is already empty.
```python
s1 = {1, 2}
s2 = s1
s1.clear()
print(s2)  # set() (both cleared because they point to same object)
```

**Don’t confuse with `del set_obj`**
- `.clear()` → empties the set but keeps the variable alive.
- `del s` → deletes the variable itsel

## set.copy()

* creates a shallow copy of set
* returns a new copy of set
* No errors
* TypeError if any arg is passed
- Creates a **new set object** with the same elements as the original.
- Changes to the **copied set** do **not affect** the original set (and vice versa).
- Since sets can only hold **immutable objects**, shallow copy is sufficient (no deep copy needed).
- Attribute Errors ony work with for which it is defined
```python
lst = [1, 2, 3]
lst.copy()     # ✅ works for lists too
num = 5
num.copy()     # ❌ AttributeError
```

* **Confusion with `=` (assignment)**
```python
s1 = {1, 2, 3}
s2 = s1       # ❌ points to same set (not a copy)
s2 = s1.copy()  # ✅ creates independent copy
```


## set.union(set1,set2,set3,list,tuple,str,dict....)

* Returns a **new set** containing all **unique elements** from all iterables
* TypeError if non iterable
* Returns  a new set
```python
a = {1}
b = {2}
c = {3}
print(a.union(b, c))  # {1, 2, 3}
```
* originals are unchanged doesnt modifies the original
```python
a = {1, 2}
b = {3, 4}
a.union(b)
print(a)  # {1, 2}  (unchanged)
```

* **Works with any iterable, not just sets**
   - But input eements must be **hashable**.
##### Calling `set.union(a, b, c)` vs `a.union(b, c)`

- **`set.union(a, b, c)`**
    - Here `set` is the **class itself**, not an instance.
    - `set.union()` **expects at least one argument to be a set** (or any iterable).
    - Syntax: `set.union(set1, set2, ...)` → `set1` is the first set, then additional iterables.
    - `a = {1, 2} b = {2, 3} c = {3, 4}  print(set.union(a, b, c))  # {1, 2, 3, 4}`
- **`a.union(b, c)`**
    - This is calling `.union()` on a **set instance** `a`.
    - Works the same way: combines `a` with all other iterables.
    `print(a.union(b, c))  # {1, 2, 3, 4}`
    
 **Difference:**
- `set.union()` → class method call, first argument must be a set (or iterable).
- `a.union()` → instance method, cleaner and more common in practice.
###### Dicts
- Yes, dicts are iterables, but iterating over a dict yields **keys** only.

## set.intersection(set1,set2,list,tuple,dict,str, ....)

* Accepts **one or more iterables** (set, list, tuple, string, dict, etc.).
- Returns a **new set** containing elements that are **common to all** iterable
- TypeError if non iterable
- returna a new set
##### Behavior
- Only elements **present in all iterables** are included.
- Works with any **iterable**, but input elements must be **hashable**.
- Can chain multiple iterables:
```python
a = {1, 2}
b = {3, 4}
a.union(b)
print(a)  # {1, 2}  (unchanged)
```

* **Intersection with non-set iterables**
```python
a = {1, 2, 3}
b = [2, 3, 4]
print(a.intersection(b))  # {2, 3}
```

* same story of set.intersection(...) as above using set as class

## set.difference()

* returns the difference 
* returns  a new set 
* the set of elements which are in set but not in set1,set2 ......
* TypeError if not iterable
* returns a new set original unchanged
* ## Using `set.difference(a, b, c)` — class call
- `set` here is the **class**, not a set instance
- Syntax:
`set.difference(set1, set2, set3, ...)`

- **`set1` must be a set instance** (or any iterable)
- Returns a **new set** containing elements in `set1` but not in the others

Example:
```python
a = {1, 2, 3, 4}
b = {3, 4, 5}
c = {4, 5, 6}

print(set.difference(a, b, c))  # {1, 2}
```
Works the same way as `a.difference(b, c)` — the first argument is treated as the set to subtract from.
- **`set.difference()` is a class method** that expects the **first argument to be a set instance** (or at least a set-like object).
- If the first argument is **not a set**, Python will **raise a `TypeError`**


## set.diference_update(set1,set2,list,tuple,str,dict,...)

* modifies the original of first set when used with set as class
* returns none
* non iterable or unhashavle values make a TypError

## set.intersection_update(set1,set2,list,tuple,str,dict,...)

* it will update to set1 or first set when used as a classs
* returns None
* TypeError if non iterable or unhashable vlueds

## set.symmetric_difference_update()
same as for above


## set.symmetric_difference(iterable)

* returns a new set
* give the element that is in either in 1st or 2nd if present in 2nd then it will not add it
* take only one arg
* TypeError if non iterabe or element are unhashable and if more that one arg
* **Important:** Unlike `union` or `intersection`, **you can only pass ONE iterable**. Trying to pass multiple iterables like `(set1, set2, list)` will raise an error.
* Original remains unchanged
- Accepts **one iterable** (set, list, tuple, string, dict, etc.)

## set1.isdisjoint(iterable)

* output is bool
* check if disjoint or not
* TypeError if non iterable or elements unhashable
- Accepts **one iterable** (set, list, tuple, string, dict, etc.)
- Returns a **boolean**:
    - `True` → no common elements
    - `False` → at least one element is common
##### Important Uses 
1. **Check if two sets/lists have no overlap**
`a = {1,2,3} b = [4,5,6] print(a.isdisjoint(b))  # True`
2. **Useful in algorithms**
- Example: verify if a group of elements is **completely independent** from another group.
1. **Quick condition checks** in filtering or validation.


## set1.issubset(iterable)

* returns True or False
* TypeError if non iterable or unhashable element
- Checks whether **all elements of `set1` are present in the iterable**.
- Accepts **one iterable** (set, list, tuple, string, dict, etc.)


## set1.issuperset(iterable)

* return true or false
* TypeError if non iterable or unhashable element
*  Accepts **one iterable** (set, list, tuple, string, dict, etc.)
- Checks whether **all elements of the iterable are present in `set1`**.
 : ⚠️ This is the opposite of `.issubset()`.

---
