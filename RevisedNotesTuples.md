# RevisedNotesTuples

--- 

## Metadata

- **Day :** Tuesday
- **Date :** 2025-09-09
- **Time :** 14:54
- **Tags :** #python #Revised #tuples 
- **References :** [[RevisedNotes]], [[FunctionsTuples]], [[ImportantQuestionsTuples1]]
- **Branch of :** Python > RevisedNotes > RevisedNotesTuples
- **Author :**  dx

---

# Notes

---

# Tuples 

---

## len():

* it will give the length of tuple , no error if empty give zero , TypeError if non iterable passed 
---
## tuple.count(x) 

* Type Error if more that 1 arg
* it check with ==
* it goes from left to right 
* it can also be used with list str
* linear time complexity O(n) , space o(1) costs extra memory 
* it a tuple contains (False,0) it will consider False and 0 differently
* common use to check the duplicates 
* doo not use count() when there is multiple calling of it with multiple values calling `.count()` repeatedly for many different values is O(n) each time → O(n·k). Use `collections.Counter` (one pass) instead:

```python
from collections import Counter freq = Counter(my_tuple)
```

* do not use when a condition instead sum as 
*  **Complex predicate counting**: if you want to count items satisfying a condition (not equality), use a generator + `sum`:
    
    ```python
    
    # count even numbers sum(1 for x in my_tuple if x % 2 == 0)
    ```
    
- **Large tuples + many repeated queries**: build a frequency map once, then query in O(1).
---
## tuple.index(item , start , stop)

* to find the first occurrence of the element in specified range by default it will checks the full tuple left to right
* based on ==
* the stop value is exclusive and the start value is inclusive
* return 0 based index 
* ValueError if not found
* TypeError at least one arg required

* ## Complexity
- Time: **O(n)** in the worst case  
- Space: **O(1)** (constant extra memory)

* use try except
```python
try:
    idx = t.index(x)
except ValueError:
    idx = -1  # or handle missing value
```    
* With `slice` and `len()` to find relative positions:

```python
i = t.index(x, start, stop)
print(len(t[:i]))  # elements before first occurrence
```

## Complexities
```java
## **Complexity O(n) time, O(1) space**

This is shorthand from **Big-O notation** used in computer science to describe how an algorithm scales.

---

### **O(n) time**

- **Meaning:** The algorithm may need to look at every element in the tuple (or list/string).
    
- `n` = number of elements.
    
- So, in the **worst case**, the runtime grows **linearly** with the size of the input.
    

**Example:**

`t = (1, 2, 3, 4, 5) t.index(5)   # might scan all 5 elements before finding match`

If the tuple has 1 million items and the value is at the end, `.index()` will compare up to 1 million times.

---

### **O(1) space**

- **Meaning:** The algorithm does not use extra memory that grows with the input size.
    
- It just needs a few fixed variables (like an index counter, comparison temp).
    
- Memory use stays **constant**, regardless of tuple size.
    

**Example:**

`t = (1, 2, 3, 4, 5) idx = t.index(4)`

The method just loops with a pointer — it doesn’t build a copy of the tuple or allocate extra arrays.

---

### **Summary**

- **O(n) time:** runtime increases proportionally to tuple size.
    
- **O(1) space:** memory usage stays the same (constant), no matter the tuple size.
    

---

👉 So when you see **“Complexity O(n) time, O(1) space”** for `.count()` or `.index()`, it means:

- **They are linear searches.**
    
- Fast for small tuples, but expensive for very large ones if used repeatedly.
```

---
## Tuple Packing and Unpackings

### Collect remaining items in a list
```python
a, *b = (1, 2, 3, 4)
print(a)  # 1
print(b)  # [2, 3, 4]
```

### Star can be in middle
```python
first, *middle, last = (10, 20, 30, 40, 50)
print(first, middle, last)  # 10 [20, 30, 40] 50

```

### Nested unpacking
```python
data = ("Bob", (28, "Developer"))
name, (age, job) = data
print(name, age, job)  # Bob 28 Developer

```

### Errors
*  valueerror
```python
t = (1, 2, 3)
a, b = t  
# ValueError: too many values to unpack

```
* not actually making the tuple 
```python
x = (5)   
print(type(x))  # <class 'int'>, not tuple

```
* multiple unpacking
```python
a, *b, *c = (1, 2, 3)  
# SyntaxError: two starred expressions in assignment

```

### USES
* swapping variables
```python
a, b = 1, 2
a, b = b, a
print(a, b)   # 2 1

```
* unpacking in return from a function 
```python
def get_point():
    return (3, 4)

x, y = get_point()
print(x, y)   # 3 4

```

* iterating the pairs  
```python
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
for num, letter in pairs:
    print(num, letter)

```
* ignoring the values with _
```python
person = ("Alice", 25, "Engineer")
name, _, job = person
print(name, job)   # Alice Engineer

```

*  Extended unpacking with ranges

```python
*begin, last = range(5) print(begin, last)   # [0, 1, 2, 3] 4
```

* #### Performance & Complexity

- Packing = O(1) (just grouping references).
    
- Unpacking = O(n) (assigns `n` variables, one by one).
    
- Starred unpacking builds a **list**, so it costs O(k) memory where `k` = number of collected item
---
## tuple()

* to generate a new tuple with a iterable
* if nothing passed it will create a empty tuple
* it a int or non iterable passed it will give TypeError
* if a str is passeda as arg it will make a tuple of each element
* if a dict is passed it will create a tuple of its keys only
* we can also create it from generator obj
* generator or iterator obj exaustation as 
```python
g = (i for i in range(3))
print(tuple(g))  # (0, 1, 2)
print(tuple(g))  # ()   (already consumed)

```
##### Complexity

- **Creating from empty**: O(1).
- **Creating from iterable**: O(n) time and space, where `n = len(iterable)`.
    - Iterates once over the iterable.
    - Copies references into a fixed tuple object


---
## min(t) / max(t)
### Syntax

```python
min(iterable, *, key=None, default)  
min(arg1, arg2, *args, key=None)

max(iterable, *, key=None, default)  
max(arg1, arg2, *args, key=None)

```
* it will give min/ max from the iterable 
* for strings it compares with lexicographic comparison (dictionary order)

* it can take multiple arg so we can also use it as 
```python
min(2,3,4,56,4)
```
* in dict compares the keys
* can be pared with key=len , key=lambda x : x[1]
* we can also define default as to ignore error of empty iterable 
* Type Error if not iterable 
* Value Error if empty 
* Type Error if iterable of different datatype

* ## Complexity

- **Time complexity**: O(n), must check every element.
    
- **Space complexity**: O(1), just tracks current min/max
* using key as arg
```python
students = [{"name": "A", "marks": 90}, {"name": "B", "marks": 75}]
topper = max(students, key=lambda s: s["marks"])
print(topper)  # {'name': 'A', 'marks': 90}

```

*  safety handel errors
```python
scores = []
lowest = min(scores, default="N/A")
print(lowest)  # "N/A"
```
* when it is comparing multiple stringd then it uses the lexicographic order otherwise it use Unicode method as 
```python
print(min("apple"))  # 'a'
print(max("apple"))  # 'p' (ASCII/Unicode order)
```

## sum(iterable , start=0) 

* it will give the sum of all the items in iterable
* the start arg optional will be added before the sum of iterable is calculated 
* supports , decimal , float and all other that adddition allows(+)
* give 0 no error if iterable is empty
* doesnt work with non numeric datatypes
* if the iterable is empty and assigned the start value then it will give the output as start value
* Type Error if different datatypes
* 
* ## Complexity

- **Time complexity**: O(n) → sums each element once.
    
- **Space complexity**: O(1) → accumulates running total, no extra list created.

* example 
```python
a = [1, 2]
b = [3, 4]
total = sum(a + b)  # 10
# Or sum with start
total = sum(a, start=sum(b))  # 10
```



### sorted(tuple) ,  
it gives list 

### reversed(tuple) , any( ) , all( ), filter() , map() 
they give iterator object 

above one works same as lists