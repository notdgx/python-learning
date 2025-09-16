# ImportantQuestionsSets1

--- 

## Metadata

- **Day :** Tuesday
- **Date :** 2025-09-16
- **Time :** 17:06
- **Tags :** #python #sets #importantquestions1 #revised
- **References :** [[FunctionsSets]] , [[ImportantQuestions1]] , [[RevisedNotesSets]]
- **Branch of :** Python > 1mportantQuestions1 > ImportantQuestionsSets1
- **Author :**  dx

---

# Notes

---


* better use discard() over the remove() if using use likw
```python
set1.remove(element) if element in set1 else "Not present"
```

* to check a set is empty or not 
```python
# Different ways to check if a set is empty

s1 = set()
s2 = {1, 2}

# 1. Pythonic way (best)
if not s1:
    print("s1 is empty")
else:
    print("s1 is not empty")

#comresssion
a = "EMPTY" if not set else "NOT EMPTY"

# 2. Using len()
if len(s2) == 0:
    print("s2 is empty")
else:
    print("s2 is not empty")

# 3. Compare with empty set
if s1 == set():
    print("s1 is empty (comparison method)")

# 4. Using bool()
if bool(s1) == False:
    print("s1 is empty (bool method)")

# 5. Using exception handling (not recommended, but works)
try:
    first = next(iter(s1))
    print("s1 is not empty, first element =", first)
except StopIteration:
    print("s1 is empty (exception method)")

```

* a empty set is always created with set() not {} this identifies it ass a dict
* `set.clear()` will remove all the elements from a set but the set will be still present as a empty one
* `set.pop()` to remove and return that random element from the set if set empty then KeyError better use it as 
```python
return set1.pop() if set1 else None
```

* set compression
```python
 Create a set of even numbers from 1 to 10
def even_numbers_1_to_10():
    return {x for x in range(1, 11) if x % 2 == 0}
```

* check only +ve element
```python
Check if a set contains only positive numbers
def all_positive(my_set):
    return all(x > 0 for x in my_set if isinstance(x, (int, float)))
```

* check if it comtains duplicates
```python
 Check if a string contains duplicate characters
def has_duplicate_chars(s):
    return len(s) != len(set(s))
```

* Remove all vowels from a set of characters

```python
def remove_vowels(char_set):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    return char_set - vowels
```

*  Create a set of file extensions from filenames
```python
def que28():
    a = ['file1.txt', 'file2.pdf', 'file3.txt', 'file4.jpg']
    return set(("."+i.split(".")[-1] for i in a))
```

* Create a set of prime numbers less than 20
```python
def que30():
    a = range(2, 20)
    primes = set()
    for i in a:
        is_prime = True
        for j in range(2, int(i**0.5) + 1):  # check divisibility up to sqrt(i)
            if i % j == 0:#if a number has a divisor, at least one of them must be ≤ √i.
                is_prime = False
                break
        if is_prime:
            primes.add(i)
    return primes
# print(que30())  # Output: {2, 3, 5, 7, 11, 13, 17, 19}
```

* Create a set of unique lengths from strings

```python
def unique_string_lengths(strings):
    return {len(s) for s in strings}
```

* Check if a set contains any negative numbers

```python
def has_negative_numbers(my_set):
    return any(x < 0 for x in my_set if isinstance(x, (int, float)))
```

*  Create a set from the digits of a number

```python
def digits_to_set(number):
    return set(str(abs(number)))
    
    
    
### `set("-221")`
A set built from a string takes **unique characters** only:
`set("-221") # Output: {'-', '1', '2'}`

👉 Explanation:
- The string is `"-221"`.
- Characters: `'-'`, `'2'`, `'2'`, `'1'`.
- Duplicates removed → `{'-', '1', '2'}`.
```

*  Find maximum and minimum values in a set
```python
def find_min_max(my_set):
    if not my_set:
        return None, None
    numeric_values = [x for x in my_set if isinstance(x, (int, float))]
    if not numeric_values:
        return None, None
    return min(numeric_values), max(numeric_values)
```

* Check if a set contains only alphabetic strings

```python
def all_alphabetic_strings(my_set):
    return all(isinstance(x, str) and x.isalpha() for x in my_set)
```


 * union,intersention
```python
Find the union of two sets

def set_union(set1, set2):
    return set1 | set2  # or set1.union(set2)
    
    
    
Find the intersection of two sets

def set_intersection(set1, set2):
    return set1 & set2  # or set1.intersection(set2)
    
    
    
Find the difference between two sets

def set_difference(set1, set2):
    return set1 - set2  # or set1.difference(set2)
    
    
Find the symmetric difference between two sets

def symmetric_difference(set1, set2):
    return set1 ^ set2  # or set1.symmetric_difference(set2)
    
    
    
Check if one set is a subset of another

def is_subset(set1, set2):
    return set1 <= set2  # or set1.issubset(set2)
    
    
Check if one set is a superset of another

def is_superset(set1, set2):
    return set1 >= set2  # or set1.issuperset(set2)
    
    
    
Check if two sets are disjoint

def are_disjoint(set1, set2):
    return set1.isdisjoint(set2)
    
    
Update a set with the difference of another set

def update_with_difference(set1, set2):
    updated_set = set1.copy()
    updated_set -= set2  # or updated_set.difference_update(set2)
    return updated_set
    
    
    
Update a set with the intersection of another set

def update_with_intersection(set1, set2):
    updated_set = set1.copy()
    updated_set &= set2  # or updated_set.intersection_update(set2)
    return updated_set
    
    
    
Update a set with the union of another set

def update_with_union(set1, set2):
    updated_set = set1.copy()
    updated_set |= set2  # or updated_set.update(set2)
    return updated_set
```

In **set theory** (and in Python’s `set` operations):
- Every set is considered a **subset of itself** → `A.issubset(A)` returns `True`.
- Every set is also a **superset of itself** → `A.issuperset(A)` returns `True`.


* Find common elements across multiple sets
* **Input:** `sets = [{1,2,3}, {2,3,4}, {2,3,5}]` **Sample Output:** `{2, 3}`

  ```python
def intersection_multiple_sets(sets):
    if not sets:
        return set()
    result = sets[0].copy()
    for s in sets[1:]:
        result &= s
    return result
```

* ## Proper Subset & Proper Superset
- **Proper Subset**: A set `A` is a proper subset of `B` if **A is a subset of B AND A ≠ B**.
- **Proper Superset**: A set `A` is a proper superset of `B` if **A is a superset of B AND A ≠ B**.

In Python:
- `A < B` → proper subset
- `A > B` → proper superset
```python
 Check if a set is a proper subset
def is_proper_subset(set1, set2):
    return set1 < set2  # proper subset (strict)
```

* Flatten nested lists and create unique set
```python
def que56(a = [[1, 2], [2, 3], [3, 4, 1]]):
    l=[]
    for i in a :
        if isinstance(i,list ):
            l.extend(que56(i))
        else:
            l.append(i)
    return set(l)
```

* union along multiple sets
```python
Find union of multiple sets

def union_multiple_sets(sets):
    result = set()
    for s in sets:
        result |= s
    return result
    
def que57():
    sets = [{1, 2}, {2, 3}, {3, 4}]
    return set.union(*sets)
```

* Check hierarchical relationship in sets
**Description:** Verify if sets form a subset chain. **Sample Input:** `sets = [{1}, {1, 2}, {1, 2, 3}]` **Sample Output:** `True (each is subset of next)`

```python
def que59():
    sets = [{1}, {1, 2}, {1, 2, 3}]
    return all(s1 < s2 for s1, s2 in zip(sets, sets[1:]))
```

* Find unique elements across all sets
**Description:** Get union of multiple sets. **Sample Input:** `sets = [{1, 2}, {2, 3}, {4, 5}]` **Sample Output:** `{1, 2, 3, 4, 5}`

```python
def que60():
    a =[{1, 2}, {2, 3}, {4, 5}]
    return set.union(*a)
# print(que60())
```

*  Find elements exclusive to first set

```python
def exclusive_to_first(first_set, other_sets):
    combined_others = set()
    for s in other_sets:
        combined_others |= s
    return first_set - combined_others
```

* Check if any set in list is empty

```python
def has_empty_set(sets):
    return any(len(s) == 0 for s in sets)
```

* Find the largest set
```python
def find_largest_set(sets):
    if not sets:
        return None
    return max(sets, key=len)
```

---