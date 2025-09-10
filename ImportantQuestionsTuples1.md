# ImportantQuestionsTuples1

--- 

## Metadata

- **Day :** Wednesday
- **Date :** 2025-09-10
- **Time :** 14:26
- **Tags :** #python #Revised #importantquestions1 #tuples   
- **References :** [[ImportantQuestions1]], [[FunctionsTuples]], [[RevisedNotesTuples]]
- **Branch of :** Python > ImportantQuestions1 > ImportantQuestionsTuples1
- **Author :**  dx

---

# Notes

* we can use `max(tuple , default=None)` it will give None when the tuple is empty
* to acces a middle element of a list 

```python
t=(2,4,6,7,8,4,3)
return t[len(t)//+1]
```

* we can also make a tuple with range , 7 exclusive

```python
tuple(range(1,7)) # create a tuple as (1,2,3,4,5,6)
```

* to check if all the itemsin a tuple is of specified datatype or not

```python
all ( isinstance(x , int) for i in tuple1 )
```

* there is no tuple compression instead we use generator object with tuple() to directly convert a tuple , nmost pythonic and fast way
```python
tuple(x for x in tuple if x%2==0)
```

* to join tuples of  strings 
```python
"".join(x for x in tuple)
```

* to swap last and first charachter , we have to make sure while concating two or more tuples that e=we should use (t[0],) with comman otherwise it will recognise it as element and use its datatype it can cause error

```python
def swap_ends():
    t = (1, 2, 3, 4, 5)
    return (t[-1],) + t[1:-1] + (t[0],)
```

* we can use index to find first occurance index but if not found it will raise an error to play safely use 

```python 
return t.index(i) if i in t else "not present"
```

* enamurate( ) it gives enamurate object as ( index , value ) .... and we can also define start index value it will go even beyond index limit
* to find alll the index of value
``
```python
All Indices

def all_indices():
    t = (1, 2, 3, 2, 4, 2)
    return [i for i, x in enumerate(t) if x == 2]
```

* to get unique elementss present in tuple , preserving order ,most pythonic and efficient way 

```python
Unique Elements

def unique_elements():
    t = (1, 2, 2, 3, 3, 3, 4)
    return tuple(dict.fromkeys(t))
```

*  to use to store the coordinates

```python
def tuple_as_keys():
    coords = [(0, 0), (1, 1), (2, 2)]
    return {coord: f'point{i}' if i else 'origin' for i, coord in enumerate(coords)}
```

* we can unpack a tuple with a star as
```python
t = (1,2,3,4,5)
first , *rest = t 

## it will store first as 1 and rest as tuple of [2,3,4,5] listttttt
```

* best way t count most occuring element 
```python
# Most Frequent Element

def most_frequent():
    t = (1, 2, 3, 2, 2, 4, 5)
    return max(set(t), key=t.count)
```

* zip always give the inner elements as in form of tuple
* flattened nested tuples can be any number

```python
def que55(t=((1, 2), (3, 4), (5, 6))):
    t2=tuple()
    for i in t:
        if isinstance(i,tuple):
            t2=t2+que55(i)
        else:
            t2=t2+(i,)
    return t2

# print(que55())
```

* to get a tuple of duplicate elements

```python
 Duplicate Detection

def find_duplicates():
    t = (1, 2, 3, 2, 4, 3, 5)
    seen = set()
    duplicates = set()
    for x in t:
        if x in seen:
            duplicates.add(x)
        seen.add(x)
    return tuple(duplicates)
```

* make a tuple with pairing consective pairs 

```python
    t = (1, 2, 3, 4, 5, 6)
    pairs = list(zip(t[::2], t[1::2]))
    return pairs
```

* to get the interscection of two with preserving order 
```python
def tuple_intersection_ordered(t1, t2):
    s2 = set(t2)  # O(m)
    return tuple(x for x in t1 if x in s2)

```


* to get second largest , we cant just use t[1] because duplicates can be present so 

```python
ef second_largest():
    t = (5, 2, 8, 1, 9, 3)
    sorted_t = sorted(set(t), reverse=True)
    return sorted_t[1]
```

* as tuple is immutable but if we want to replace somethng we can just make a new tuple
```python
def replace_elements():

    t = (1, 2, 3, 2, 4)
    old, new = 2, 9
    return tuple(new if x == old else x for x in t)
```

*   cummatative sum canculation 

```python
 Cumulative Sums

def cumulative_sums():
    t = (1, 2, 3, 4, 5)
    result = []
    cumsum = 0
    for x in t:
        cumsum += x
        result.append(cumsum)
    return tuple(result)
```

* to check is tuple is sorted or not 

```python
Sorted Check

def is_sorted():
    t = (1, 2, 3, 4, 5)
    return t == tuple(sorted(t))
```

* left rotation

```python
Left Rotation

def rotate_left():

    t = (1, 2, 3, 4, 5
    n = 2
    return t[n:] + t[:n]
```

* to get the missing number
```python
Missing Number

def find_missing():
    t = (1, 2, 4, 5, 6)
    full_set = set(range(min(t), max(t) + 1))
    return list(full_set - set(t))[0]
```



* is unique all elements 

```python
 Uniqueness Check

def all_unique():
    t = (1, 2, 3, 4, 5)
    return len(t) == len(set(t))
```

* multiple tules merge

```python
def que75(t=[(1, 2), (3, 4), (5, 6)]):
    t2=tuple()
    for i in t:
        if isinstance(i,tuple):
            t2+=que75(i)
        else:
            t2+=(i,)
    return t2
```

* consective difference   **Output**: (5, -3, 8, 5)

```python
. Consecutive Differences

def consecutive_differences():
    t = (10, 15, 12, 20, 25)
    return tuple(t[i+1] - t[i] for i in range(len(t)-1))
```


* longest string

```python
 Longest String

def longest_string():
    t = ('cat', 'elephant', 'dog', 'butterfly')
    return max(t, key=len)
```

* sliding window zip

```python
def que80():
    t = (1, 2, 3, 4, 5)
    return list((zip(t,t[1:])))
# print(que80())
```


* nested unpacking of a tuple

```python
 Nested Unpacking
 
def nested_unpacking():
    t = ((1, 2), (3, (4, 5)))
    (a, b), (c, (d, e)) = t
    return a, b, c, d, e
```

* to get columns in matrix
```python
  

# 87. Matrix Operations

def matrix_column():
    matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    col_index = 1
    return tuple(row[col_index] for row in matrix)
    
    
    if column number given then
    
    return tuple(row[col_num - 1] for row in matrix)
```



* **input**: tuples = [(2, 1), (1, 3), (1, 2)] **Output**: Sort by sum: [(1, 2), (2, 1), (1, 3)

```python
 Custom Tuple Comparison

def custom_sort():
    tuples = [(2, 1), (1, 3), (1, 2)]
    return sorted(tuples, key=lambda x: sum(x))
```


---
