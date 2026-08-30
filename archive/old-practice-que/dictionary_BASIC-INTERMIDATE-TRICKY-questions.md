# 100 Python Dictionary Coding Questions

This collection contains 100 unique Python dictionary questions split across three difficulty levels, designed for interview preparation, competitive programming, and skill development.

## Basic Level (Questions 1-40)
*Focus: Creating/accessing dictionaries, using keys(), values(), items(), adding/removing keys, basic iteration*

### 1. Create an empty dictionary and print it.
**Input:** N/A
**Output:** `{}`

### 2. Create a dictionary with keys 'name', 'age', 'city' and values 'Alice', 25, 'Boston'.
**Input:** N/A
**Output:** `{'name': 'Alice', 'age': 25, 'city': 'Boston'}`

### 3. Access the value of key 'name' from dictionary {'name': 'Bob', 'age': 30}.
**Input:** `{'name': 'Bob', 'age': 30}`
**Output:** `'Bob'`

### 4. Add a new key-value pair 'country': 'USA' to dictionary {'name': 'Carol', 'age': 28}.
**Input:** `{'name': 'Carol', 'age': 28}`
**Output:** `{'name': 'Carol', 'age': 28, 'country': 'USA'}`

### 5. Remove the key 'age' from dictionary {'name': 'David', 'age': 35, 'city': 'NYC'}.
**Input:** `{'name': 'David', 'age': 35, 'city': 'NYC'}`
**Output:** `{'name': 'David', 'city': 'NYC'}`

### 6. Get all keys from dictionary {'a': 1, 'b': 2, 'c': 3} and convert to list.
**Input:** `{'a': 1, 'b': 2, 'c': 3}`
**Output:** `['a', 'b', 'c']`

### 7. Get all values from dictionary {'x': 10, 'y': 20, 'z': 30} and convert to list.
**Input:** `{'x': 10, 'y': 20, 'z': 30}`
**Output:** `[10, 20, 30]`

### 8. Get all key-value pairs from dictionary {'p': 5, 'q': 6} as a list of tuples.
**Input:** `{'p': 5, 'q': 6}`
**Output:** `[('p', 5), ('q', 6)]`

### 9. Check if key 'name' exists in dictionary {'name': 'Eve', 'age': 22}.
**Input:** `{'name': 'Eve', 'age': 22}`
**Output:** `True`

### 10. Use get() method to safely access key 'salary' from {'name': 'Frank'} with default 0.
**Input:** `{'name': 'Frank'}`
**Output:** `0`

### 11. Update dictionary {'a': 1, 'b': 2} with another dictionary {'c': 3, 'd': 4}.
**Input:** `{'a': 1, 'b': 2}, {'c': 3, 'd': 4}`
**Output:** `{'a': 1, 'b': 2, 'c': 3, 'd': 4}`

### 12. Clear all elements from dictionary {'x': 100, 'y': 200}.
**Input:** `{'x': 100, 'y': 200}`
**Output:** `{}`

### 13. Create a copy of dictionary {'name': 'Grace', 'score': 95}.
**Input:** `{'name': 'Grace', 'score': 95}`
**Output:** `{'name': 'Grace', 'score': 95}`

### 14. Use pop() to remove and return value of key 'age' from {'name': 'Helen', 'age': 29}.
**Input:** `{'name': 'Helen', 'age': 29}`
**Output:** `29`

### 15. Use popitem() to remove and return the last key-value pair from {'a': 1, 'b': 2, 'c': 3}.
**Input:** `{'a': 1, 'b': 2, 'c': 3}`
**Output:** `('c', 3)`

### 16. Use setdefault() to get value of key 'phone' from {'name': 'Ivan'} with default 'N/A'.
**Input:** `{'name': 'Ivan'}`
**Output:** `'N/A'`

### 17. Create dictionary from two lists: keys=['a', 'b', 'c'] and values=[1, 2, 3].
**Input:** `keys=['a', 'b', 'c'], values=[1, 2, 3]`
**Output:** `{'a': 1, 'b': 2, 'c': 3}`

### 18. Find the length of dictionary {'math': 90, 'science': 85, 'english': 88}.
**Input:** `{'math': 90, 'science': 85, 'english': 88}`
**Output:** `3`

### 19. Iterate through dictionary {'red': 1, 'blue': 2} and print each key.
**Input:** `{'red': 1, 'blue': 2}`
**Output:** `red\nblue`

### 20. Iterate through dictionary {'cat': 'meow', 'dog': 'bark'} and print each value.
**Input:** `{'cat': 'meow', 'dog': 'bark'}`
**Output:** `meow\nbark`

### 21. Iterate through dictionary {'apple': 5, 'banana': 3} and print key-value pairs.
**Input:** `{'apple': 5, 'banana': 3}`
**Output:** `apple 5\nbanana 3`

### 22. Check if dictionary {'name': 'John'} is empty.
**Input:** `{'name': 'John'}`
**Output:** `False`

### 23. Convert dictionary {'x': 1, 'y': 2} to a list of tuples.
**Input:** `{'x': 1, 'y': 2}`
**Output:** `[('x', 1), ('y', 2)]`

### 24. Convert list of tuples [('a', 1), ('b', 2)] to a dictionary.
**Input:** `[('a', 1), ('b', 2)]`
**Output:** `{'a': 1, 'b': 2}`

### 25. Create dictionary using fromkeys() method with keys ['p', 'q', 'r'] and default value 0.
**Input:** `['p', 'q', 'r']`
**Output:** `{'p': 0, 'q': 0, 'r': 0}`

### 26. Replace value of key 'score' in {'name': 'Kate', 'score': 75} with 85.
**Input:** `{'name': 'Kate', 'score': 75}`
**Output:** `{'name': 'Kate', 'score': 85}`

### 27. Check if value 100 exists in dictionary {'a': 50, 'b': 100, 'c': 75}.
**Input:** `{'a': 50, 'b': 100, 'c': 75}`
**Output:** `True`

### 28. Get the maximum value from dictionary {'x': 10, 'y': 25, 'z': 15}.
**Input:** `{'x': 10, 'y': 25, 'z': 15}`
**Output:** `25`

### 29. Get the minimum value from dictionary {'p': 8, 'q': 3, 'r': 12}.
**Input:** `{'p': 8, 'q': 3, 'r': 12}`
**Output:** `3`

### 30. Count total number of key-value pairs in {'a': 1, 'b': 2, 'c': 3, 'd': 4}.
**Input:** `{'a': 1, 'b': 2, 'c': 3, 'd': 4}`
**Output:** `4`

### 31. Create dictionary with integer keys {1: 'one', 2: 'two', 3: 'three'}.
**Input:** N/A
**Output:** `{1: 'one', 2: 'two', 3: 'three'}`

### 32. Access multiple values from dictionary {'name': 'Leo', 'age': 24, 'city': 'LA'} using keys 'name' and 'city'.
**Input:** `{'name': 'Leo', 'age': 24, 'city': 'LA'}`
**Output:** `['Leo', 'LA']`

### 33. Check if key 'phone' is NOT in dictionary {'name': 'Max', 'email': 'max@email.com'}.
**Input:** `{'name': 'Max', 'email': 'max@email.com'}`
**Output:** `True`

### 34. Get sum of all values in dictionary {'a': 10, 'b': 20, 'c': 30}.
**Input:** `{'a': 10, 'b': 20, 'c': 30}`
**Output:** `60`

### 35. Create a dictionary with tuple keys {(1, 2): 'coordinates', (3, 4): 'point'}.
**Input:** N/A
**Output:** `{(1, 2): 'coordinates', (3, 4): 'point'}`

### 36. Remove key 'temp' from dictionary {'name': 'Nina', 'temp': 'delete'} using del keyword.
**Input:** `{'name': 'Nina', 'temp': 'delete'}`
**Output:** `{'name': 'Nina'}`

### 37. Check if two dictionaries {'a': 1, 'b': 2} and {'b': 2, 'a': 1} are equal.
**Input:** `{'a': 1, 'b': 2}, {'b': 2, 'a': 1}`
**Output:** `True`

### 38. Create dictionary from string 'hello' where keys are characters and values are their positions.
**Input:** `'hello'`
**Output:** `{'h': 0, 'e': 1, 'l': 3, 'o': 4}`

### 39. Convert dictionary keys {'name': 'Oscar', 'age': 31} to uppercase.
**Input:** `{'name': 'Oscar', 'age': 31}`
**Output:** `{'NAME': 'Oscar', 'AGE': 31}`

### 40. Get first key-value pair from dictionary {'first': 1, 'second': 2, 'third': 3}.
**Input:** `{'first': 1, 'second': 2, 'third': 3}`
**Output:** `('first', 1)`

## Intermediate Level (Questions 41-80)
*Focus: Nested dictionaries, dictionary comprehension, frequency counters, merging dictionaries, sorting by key/value*

### 41. Create nested dictionary {'person': {'name': 'Alice', 'details': {'age': 25, 'city': 'Boston'}}}.
**Input:** N/A
**Output:** `{'person': {'name': 'Alice', 'details': {'age': 25, 'city': 'Boston'}}}`

### 42. Access 'age' from nested dictionary {'student': {'info': {'name': 'Bob', 'age': 20}}}.
**Input:** `{'student': {'info': {'name': 'Bob', 'age': 20}}}`
**Output:** `20`

### 43. Use dictionary comprehension to create {x: x**2 for x in range(1, 6)}.
**Input:** `range(1, 6)`
**Output:** `{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}`

### 44. Count frequency of each character in string 'hello world' using dictionary.
**Input:** `'hello world'`
**Output:** `{'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}`

### 45. Merge two dictionaries {'a': 1, 'b': 2} and {'c': 3, 'd': 4} using ** operator.
**Input:** `{'a': 1, 'b': 2}, {'c': 3, 'd': 4}`
**Output:** `{'a': 1, 'b': 2, 'c': 3, 'd': 4}`

### 46. Sort dictionary {'b': 2, 'a': 1, 'c': 3} by keys.
**Input:** `{'b': 2, 'a': 1, 'c': 3}`
**Output:** `{'a': 1, 'b': 2, 'c': 3}`

### 47. Sort dictionary {'alice': 85, 'bob': 90, 'charlie': 75} by values.
**Input:** `{'alice': 85, 'bob': 90, 'charlie': 75}`
**Output:** `{'charlie': 75, 'alice': 85, 'bob': 90}`

### 48. Find key with maximum value in dictionary {'x': 10, 'y': 25, 'z': 15}.
**Input:** `{'x': 10, 'y': 25, 'z': 15}`
**Output:** `'y'`

### 49. Find key with minimum value in dictionary {'p': 8, 'q': 3, 'r': 12}.
**Input:** `{'p': 8, 'q': 3, 'r': 12}`
**Output:** `'q'`

### 50. Group words by their first letter: ['apple', 'banana', 'cherry', 'apricot'].
**Input:** `['apple', 'banana', 'cherry', 'apricot']`
**Output:** `{'a': ['apple', 'apricot'], 'b': ['banana'], 'c': ['cherry']}`

### 51. Invert dictionary {'a': 1, 'b': 2, 'c': 3} so values become keys.
**Input:** `{'a': 1, 'b': 2, 'c': 3}`
**Output:** `{1: 'a', 2: 'b', 3: 'c'}`

### 52. Filter dictionary {'a': 10, 'b': 5, 'c': 15, 'd': 8} to keep only values > 7.
**Input:** `{'a': 10, 'b': 5, 'c': 15, 'd': 8}`
**Output:** `{'a': 10, 'c': 15, 'd': 8}`

### 53. Create dictionary of word lengths from list ['cat', 'elephant', 'dog'].
**Input:** `['cat', 'elephant', 'dog']`
**Output:** `{'cat': 3, 'elephant': 8, 'dog': 3}`

### 54. Combine dictionaries {'a': [1, 2]} and {'a': [3, 4], 'b': [5]} by extending lists.
**Input:** `{'a': [1, 2]}, {'a': [3, 4], 'b': [5]}`
**Output:** `{'a': [1, 2, 3, 4], 'b': [5]}`

### 55. Get all keys from nested dictionary {'outer': {'inner1': 1, 'inner2': 2}}.
**Input:** `{'outer': {'inner1': 1, 'inner2': 2}}`
**Output:** `['outer', 'inner1', 'inner2']`

### 56. Count vowels and consonants in 'programming' using dictionary.
**Input:** `'programming'`
**Output:** `{'vowels': 3, 'consonants': 8}`

### 57. Create grade statistics: calculate average from {'alice': 85, 'bob': 92, 'charlie': 78}.
**Input:** `{'alice': 85, 'bob': 92, 'charlie': 78}`
**Output:** `85.0`

### 58. Remove all keys with None values from {'a': 1, 'b': None, 'c': 3, 'd': None}.
**Input:** `{'a': 1, 'b': None, 'c': 3, 'd': None}`
**Output:** `{'a': 1, 'c': 3}`

### 59. Create dictionary comprehension for even numbers: {x: 'even' for x in range(10) if x % 2 == 0}.
**Input:** `range(10)`
**Output:** `{0: 'even', 2: 'even', 4: 'even', 6: 'even', 8: 'even'}`

### 60. Transform dictionary values {'a': 'hello', 'b': 'world'} to uppercase.
**Input:** `{'a': 'hello', 'b': 'world'}`
**Output:** `{'a': 'HELLO', 'b': 'WORLD'}`

### 61. Find common keys between {'a': 1, 'b': 2, 'c': 3} and {'b': 4, 'c': 5, 'd': 6}.
**Input:** `{'a': 1, 'b': 2, 'c': 3}, {'b': 4, 'c': 5, 'd': 6}`
**Output:** `['b', 'c']`

### 62. Create frequency counter for list [1, 2, 2, 3, 3, 3] using dictionary comprehension.
**Input:** `[1, 2, 2, 3, 3, 3]`
**Output:** `{1: 1, 2: 2, 3: 3}`

### 63. Merge multiple dictionaries [{'a': 1}, {'b': 2}, {'c': 3}] into one.
**Input:** `[{'a': 1}, {'b': 2}, {'c': 3}]`
**Output:** `{'a': 1, 'b': 2, 'c': 3}`

### 64. Extract subset of dictionary {'name': 'John', 'age': 30, 'city': 'NYC'} with keys ['name', 'city'].
**Input:** `{'name': 'John', 'age': 30, 'city': 'NYC'}, ['name', 'city']`
**Output:** `{'name': 'John', 'city': 'NYC'}`

### 65. Create nested dictionary from flat dict {'a.b': 1, 'a.c': 2, 'b.d': 3}.
**Input:** `{'a.b': 1, 'a.c': 2, 'b.d': 3}`
**Output:** `{'a': {'b': 1, 'c': 2}, 'b': {'d': 3}}`

### 66. Calculate sum of values for each key in list of dicts [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}].
**Input:** `[{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]`
**Output:** `{'a': 4, 'b': 6}`

### 67. Sort dictionary by values in descending order: {'x': 10, 'y': 30, 'z': 20}.
**Input:** `{'x': 10, 'y': 30, 'z': 20}`
**Output:** `{'y': 30, 'z': 20, 'x': 10}`

### 68. Create dictionary from zip of two lists with duplicate removal: [1, 2, 2, 3], ['a', 'b', 'c', 'd'].
**Input:** `[1, 2, 2, 3], ['a', 'b', 'c', 'd']`
**Output:** `{1: 'a', 2: 'c', 3: 'd'}`

### 69. Find all keys in dictionary {'a': 10, 'b': 5, 'c': 15} where value is greater than 7.
**Input:** `{'a': 10, 'b': 5, 'c': 15}`
**Output:** `['a', 'c']`

### 70. Update nested dictionary: add 'phone': '123-456' to {'person': {'name': 'Alice', 'age': 25}}.
**Input:** `{'person': {'name': 'Alice', 'age': 25}}`
**Output:** `{'person': {'name': 'Alice', 'age': 25, 'phone': '123-456'}}`

### 71. Count unique words in text 'the cat and the dog' using dictionary.
**Input:** `'the cat and the dog'`
**Output:** `{'the': 2, 'cat': 1, 'and': 1, 'dog': 1}`

### 72. Create multiplication table dict: {i: {j: i*j for j in range(1, 4)} for i in range(1, 4)}.
**Input:** `range(1, 4)`
**Output:** `{1: {1: 1, 2: 2, 3: 3}, 2: {1: 2, 2: 4, 3: 6}, 3: {1: 3, 2: 6, 3: 9}}`

### 73. Swap keys and values in dictionary {'name': 'John', 'age': '30'} handling duplicates.
**Input:** `{'name': 'John', 'age': '30'}`
**Output:** `{'John': 'name', '30': 'age'}`

### 74. Group students by grade: [{'name': 'A', 'grade': 'B'}, {'name': 'C', 'grade': 'A'}, {'name': 'D', 'grade': 'B'}].
**Input:** `[{'name': 'A', 'grade': 'B'}, {'name': 'C', 'grade': 'A'}, {'name': 'D', 'grade': 'B'}]`
**Output:** `{'B': ['A', 'D'], 'A': ['C']}`

### 75. Find intersection of dictionary values: {'a': [1, 2, 3], 'b': [2, 3, 4]}.
**Input:** `{'a': [1, 2, 3], 'b': [2, 3, 4]}`
**Output:** `[2, 3]`

### 76. Create running sum dictionary from list [1, 2, 3, 4, 5].
**Input:** `[1, 2, 3, 4, 5]`
**Output:** `{1: 1, 2: 3, 3: 6, 4: 10, 5: 15}`

### 77. Validate dictionary structure: check if all keys in {'name': str, 'age': int} have correct types.
**Input:** `{'name': 'John', 'age': 25}, {'name': str, 'age': int}`
**Output:** `True`

### 78. Create pivot table: convert [{'name': 'A', 'subject': 'math', 'score': 90}] to {'A': {'math': 90}}.
**Input:** `[{'name': 'A', 'subject': 'math', 'score': 90}]`
**Output:** `{'A': {'math': 90}}`

### 79. Calculate percentage distribution from {'apples': 20, 'oranges': 30, 'bananas': 50}.
**Input:** `{'apples': 20, 'oranges': 30, 'bananas': 50}`
**Output:** `{'apples': 20.0, 'oranges': 30.0, 'bananas': 50.0}`

### 80. Find most frequent element in list ['a', 'b', 'a', 'c', 'a'] using dictionary.
**Input:** `['a', 'b', 'a', 'c', 'a']`
**Output:** `'a'`

## Advanced/Tricky Level (Questions 81-100)
*Focus: Conditional transformations, complex key access, defaultdict, Counter, manipulating dicts with tuples/lists, flattening nested dicts, reverse lookups*

### 81. Use defaultdict to group words by length: ['cat', 'elephant', 'dog', 'bird'].
**Input:** `['cat', 'elephant', 'dog', 'bird']`
**Output:** `defaultdict(<class 'list'>, {3: ['cat', 'dog'], 8: ['elephant'], 4: ['bird']})`

### 82. Use Counter to find 3 most common elements in [1, 2, 2, 3, 3, 3, 4, 4, 4, 4].
**Input:** `[1, 2, 2, 3, 3, 3, 4, 4, 4, 4]`
**Output:** `[(4, 4), (3, 3), (2, 2)]`

### 83. Flatten nested dictionary {'a': {'b': {'c': 1, 'd': 2}}, 'e': 3} with dot notation keys.
**Input:** `{'a': {'b': {'c': 1, 'd': 2}}, 'e': 3}`
**Output:** `{'a.b.c': 1, 'a.b.d': 2, 'e': 3}`

### 84. Create reverse lookup dict: given {'a': [1, 2], 'b': [2, 3]}, return {1: ['a'], 2: ['a', 'b'], 3: ['b']}.
**Input:** `{'a': [1, 2], 'b': [2, 3]}`
**Output:** `{1: ['a'], 2: ['a', 'b'], 3: ['b']}`

### 85. Implement dictionary with tuple keys for 2D coordinates: {(0,0): 'origin', (1,1): 'diagonal'}.
**Input:** N/A
**Output:** `{(0, 0): 'origin', (1, 1): 'diagonal'}`

### 86. Deep merge two nested dictionaries handling conflicts by summing numeric values.
**Input:** `{'a': {'x': 1, 'y': 2}}, {'a': {'x': 3, 'z': 4}}`
**Output:** `{'a': {'x': 4, 'y': 2, 'z': 4}}`

### 87. Transform nested list [['a', 1], ['b', 2], ['a', 3]] into dict with list values {'a': [1, 3], 'b': [2]}.
**Input:** `[['a', 1], ['b', 2], ['a', 3]]`
**Output:** `{'a': [1, 3], 'b': [2]}`

### 88. Create conditional dict comprehension: {k: v for k, v in {'a': 1, 'b': 2, 'c': 3}.items() if k != 'b' and v > 1}.
**Input:** `{'a': 1, 'b': 2, 'c': 3}`
**Output:** `{'c': 3}`

### 89. Implement sliding window frequency counter for string 'abcabc' with window size 3.
**Input:** `'abcabc', window_size=3`
**Output:** `{'abc': 2, 'bca': 1, 'cab': 1}`

### 90. Use defaultdict(Counter) to count character frequencies per word in ['hello', 'world'].
**Input:** `['hello', 'world']`
**Output:** `defaultdict(<class 'collections.Counter'>, {'hello': Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1}), 'world': Counter({'r': 1, 'w': 1, 'o': 1, 'l': 1, 'd': 1})})`

### 91. Sort dictionary by multiple criteria: first by value desc, then by key asc for {'b': 2, 'a': 2, 'c': 1}.
**Input:** `{'b': 2, 'a': 2, 'c': 1}`
**Output:** `{'a': 2, 'b': 2, 'c': 1}`

### 92. Create dictionary of sets for many-to-many relationships: map students to courses.
**Input:** `[('Alice', 'Math'), ('Bob', 'Math'), ('Alice', 'Science')]`
**Output:** `{'Alice': {'Math', 'Science'}, 'Bob': {'Math'}}`

### 93. Implement LRU cache using OrderedDict with capacity 3, track access order.
**Input:** `operations: ['get(1)', 'put(1,a)', 'put(2,b)', 'get(1)', 'put(3,c)', 'put(4,d)']`
**Output:** `OrderedDict([(1, 'a'), (3, 'c'), (4, 'd')])`

### 94. Parse and group nested JSON-like structure by extracting all 'id' fields recursively.
**Input:** `{'users': [{'id': 1, 'profile': {'id': 2}}, {'id': 3}]}`
**Output:** `[1, 2, 3]`

### 95. Create frequency distribution with percentiles from data [1, 2, 2, 3, 3, 3, 4, 4, 4, 4].
**Input:** `[1, 2, 2, 3, 3, 3, 4, 4, 4, 4]`
**Output:** `{1: {'count': 1, 'percentage': 10.0}, 2: {'count': 2, 'percentage': 20.0}, 3: {'count': 3, 'percentage': 30.0}, 4: {'count': 4, 'percentage': 40.0}}`

### 96. Implement dictionary that automatically converts string keys to lowercase on insertion.
**Input:** `CustomDict({'Name': 'John', 'AGE': 30})`
**Output:** `{'name': 'John', 'age': 30}`

### 97. Create word co-occurrence matrix from sentence 'the cat sat on the mat' with window size 2.
**Input:** `'the cat sat on the mat', window=2`
**Output:** `{'the': {'cat': 1, 'mat': 1}, 'cat': {'the': 1, 'sat': 1}, 'sat': {'cat': 1, 'on': 1}, 'on': {'sat': 1, 'the': 1, 'mat': 1}, 'mat': {'on': 1, 'the': 1}}`

### 98. Merge list of dicts with conflict resolution: sum numbers, concatenate strings with separator.
**Input:** `[{'a': 1, 'b': 'x'}, {'a': 2, 'b': 'y', 'c': 3}]`
**Output:** `{'a': 3, 'b': 'x|y', 'c': 3}`

### 99. Transform hierarchical data to flat structure with path-based keys and reverse operation.
**Input:** `{'a': {'b': {'c': 1}}}`
**Output:** `{'a/b/c': 1}`

### 100. Create dictionary-based state machine with transitions: states=['A','B','C'], transitions={'A':['B'],'B':['C'],'C':['A']}.
**Input:** `states=['A','B','C'], transitions={'A':['B'],'B':['C'],'C':['A']}`
**Output:** `{'current': 'A', 'transitions': {'A': ['B'], 'B': ['C'], 'C': ['A']}, 'history': []}`

---

**Author:** AI Assistant  
**Created:** For Python learners preparing for interviews, competitive programming, and skill development  
**Focus:** Dictionary operations, data manipulation, and algorithmic thinking

**Instructions:**
- Each question focuses primarily on dictionary usage
- Built-in modules like `collections.defaultdict`, `collections.Counter` are allowed
- Solutions should be clean, efficient, and well-commented
- Questions progress from basic dictionary operations to complex data transformations