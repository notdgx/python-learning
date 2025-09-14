# ImportantQuestionsLists1

--- 

## Metadata

- **Day :** Sunday
- **Date :** 2025-09-14
- **Time :** 13:45
- **Tags :** #python #lists #importantquestions1   
 - **References :** [[ImportantQuestions1]], [[RevisedNotesLists1]] ,[[RevisedNotesLists2]], [[FunctionsLists]]
- **Branch of :** python > ImportantQuestions1 > ImportantQuestionsLists1
- **Author :**  dx
- **Not Done :** 86,88,91-100

---

# Notes

---




# Python List Utilities

  

## Error Prevention and Safe Operations

  

- **Removing elements** can raise `ValueError` if the element is not found. Use:

  

  ```python

  if a in lst:
      lst.remove(a)

  ```

  

- **Popping elements** can raise `IndexError` if the list is empty or the index is out of range. Always guard:

  

  ```python

  if 0 <= index < len(lst):
      lst.pop(index)
  return lst

  ```

  

- `pop()` accepts negative indices (e.g., `lst.pop(-1)` removes the last element).

  

## Basic Checks and Validations

  

- **Element presence:**

  ```python

  a in lst

  ```

  

- **Empty list check:**

  ```python

  "Empty" if not lst else "Not Empty"

  ```

  

- **Safe `min`/`max`:**

  ```python

  min(lst) if lst else None

  ```

  

- **List comprehension:**

  ```python

  [item for item in lst if <condition>]

  ```

  

- **Safe indexing:**

  ```python

  def get_first_last(lst):
      """Extract first and last elements."""
      if len(lst) >= 2:
          return [lst[0], lst[-1]]
      elif len(lst) == 1:
          return [lst[0], lst[0]]
      return []

  ```

  

- **Uniform type check:**

  ```python

  all(isinstance(x, int) for x in lst)

  ```

  

## Finding Second Largest

  

```python

"""Find second largest number."""
unique_sorted = sorted(set(lst), reverse=True)
return unique_sorted[1] if len(unique_sorted) >= 2 else None

```

  

## List Rotation

  

```python

def rotate_left(lst, positions):
    """Rotate list left by positions."""
    if not lst:
        return lst
    positions %= len(lst)
    return lst[positions:] + lst[:positions]

```

  

- For right rotation: use `positions = len(lst) - n`.

- Example: `[1,2,3,4,5]` left by 2 → `[3,4,5,1,2]`.

  

## Chunking Lists

  

```python

def chunk_list(lst, chunk_size):
    """Split list into chunks of specified size."""
    return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]

```

  

## Enumerate and Dictionary Grouping

  

```python

a = ['apple', 'banana', 'cherry', 'apricot']
b = {}
for i in range(len(a)):
    g = []
    for j in a:
        if a[i][0].lower() == j[0].lower():
            g.append(j)
    b[a[i][0]] = g
print(b)

```

# Python List Utilities

  

---

  

## Find All Indices

  

```python

def find_all_indices(lst, target):
    """Find all indices where target appears."""
    return [i for i, x in enumerate(lst) if x == target]

```

  

---

  

## Replace at Multiple Indices

  

```python

def replace_at_indices(lst, indices, new_value):
    """Replace elements at specified indices."""
    result = lst.copy()
    for index in indices:
        if 0 <= index < len(result):
            result[index] = new_value
    return result

```

  

---

  

## Palindrome Check

  

```python

"""Check if list is a palindrome."""
return lst == lst[::-1]

```

  

---

  

## Transpose 2D List

  

```python

def transpose_matrix(matrix):
    """Transpose 2D list."""
    return list(zip(*matrix))

```

  

```text

# Example:
# [[1, 2, 3],
# [4, 5, 6]]

# →

# [[1, 4],
#  [2, 5],
#  [3, 6]]

```

  

---

  

## Sorted and Merging

  

```python

# Using sorted
a = [1,2,3]
b = [4,5,6]
# 1st
print(sorted(a+b))
# 2nd
a.extend(b)
a.sort()
print(a)

```

  

**Fastest merge:**

  

```python

def merge_sorted_lists(lst1, lst2):
    """Merge two sorted lists into one sorted list."""
    result = []
    i = j = 0

  
    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            result.append(lst1[i])
            i += 1
        else:
            result.append(lst2[j])
            j += 1

  

    result.extend(lst1[i:])
    result.extend(lst2[j:])
    return result

```

  

---

  

## Running Sum

  

```python

def running_sum(lst):
    """Calculate running sum."""
    result = []
    total = 0
    for num in lst:
        total += num
        result.append(total)
    return result

```

  

---

  

## Running Maximum

  

```python

def running_maximum(lst):

    """Calculate running maximum."""
    if not lst:
        return []
    result = [lst[0]]
    current_max = lst[0]
  

    for num in lst[1:]:
        current_max = max(current_max, num)
        result.append(current_max)
    return result

```

  

---

  

## Element Frequency

  

```python

def element_frequency(lst):
    """Count frequency of each element."""
    freq = {}
    for element in lst:
        freq[element] = freq.get(element, 0) + 1
    return freq

```

  

_Slower alternative:_  

```python

print(dict((i, lst.count(i)) for i in lst))

```

  

---

  

## Moving Average

  

```python

def moving_average(lst, window_size):
    """Calculate moving average."""
    if len(lst) < window_size:
        return []



    result = []
    for i in range(len(lst) - window_size + 1):
        window = lst[i:i + window_size]
        avg = sum(window) / window_size
        result.append(avg)
    return result

```

  

---

  

## Interleave Elements

  

```python

a = [1,3,5]
b = [2,4,6]
c = []
for i, j in zip(a, b):
    c.extend([i, j])
print(c)

```

  

```python

def interleave_lists(lst1, lst2):
    """Interleave elements of two lists."""
    result = []
    min_len = min(len(lst1), len(lst2))

  

    for i in range(min_len):
        result.append(lst1[i])
        result.append(lst2[i])

  

    result.extend(lst1[min_len:])
    result.extend(lst2[min_len:])

    return result

```

  

---

  

## Partition Even and Odd

  

```python

def partition_even_odd(lst):
    """Partition list into even and odd numbers."""
    even = [x for x in lst if x % 2 == 0]
    odd = [x for x in lst if x % 2 != 0]
    return even, odd

```

  

---

  

## Find Missing Number

  

```python

def find_missing_number(lst, n):

    """Find missing number in range 1 to n."""
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(lst)
    return expected_sum - actual_sum

```

  

---

  

## Binary Search

  

```python

a = [1,3,5,7,9,11]
n = 7
low, high = 0, len(a)-1
is_asc = a[low] < a[high]
while low <= high:
    mid = (low + high) // 2
    if a[mid] == n:
        print(mid)
        break

    if is_asc:
        if a[mid] < n:
            low = mid + 1
        else:
            high = mid - 1

    else:
        if a[mid] > n:
            low = mid + 1
        else:
            high = mid - 1

```

  

---

  

## Longest Increasing Subsequence

  

```python

def lis_length(lst):

    """Find length of longest increasing subsequence."""

    if not lst:
        return 0
    dp = [1] * len(lst)
    for i in range(1, len(lst)):
        for j in range(i):
            if lst[j] < lst[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

```

  

---

  

## Sliding Window Maximum

  

```python

def sliding_window_maximum(lst, window_size):

    """Find maximum in each sliding window."""
    if len(lst) < window_size:
        return []

  

    result = []
    for i in range(len(lst) - window_size + 1):
        window = lst[i:i + window_size]
        result.append(max(window))
    return result

```

  

---

  

## Compare Lists Elementwise

  

```python

print([x == y for x, y in zip(a, b)])

```

  

---

  

## Permutation Check

  

```python

"""Check if one list is permutation of another."""
return sorted(lst1) == sorted(lst2)

```

  

---

  

## Deep Flatten

  

```python

def deep_flatten(lst):
    """Recursively flatten deeply nested list."""
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(deep_flatten(item))
        else:
            result.append(item)
    return result

```

  

---

  

## Remove Duplicates (Preserve Order)

  

```python

def remove_duplicates_preserve_order(lst):

    """Remove duplicates while preserving order."""

    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

```

  

---

  

## Cartesian Product

  

```python

"""Generate cartesian product of two lists."""

return [(x, y) for x in lst1 for y in lst2]

```

  

---

  

## Cartesian Excluding Self-Pairs

  

```python

# all pairs excluding (i,i)

c = [(i, j) for i in a for j in a if i != j]

```

  

---

  

## Combinations

  

```python

c = [(a[i], a[j]) for i in range(len(a)) for j in range(i+1, len(a))]

```

  

---

  

## Memory-Efficient Duplicate Finding

  

```python

def find_duplicates_memory_efficient(lst):

    """Memory-efficient duplicate finding."""

    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

```