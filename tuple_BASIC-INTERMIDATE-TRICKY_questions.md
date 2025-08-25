# 100 Python Tuple Coding Questions

## Distribution:
- **40% Basic Questions (1-40)**: Creating tuples, indexing, slicing, immutability, unpacking
- **40% Intermediate Questions (41-80)**: count(), index(), tuples in loops, zip, enumerate, sorting 
- **20% Advanced Questions (81-100)**: Nested access, complex unpacking, dictionary keys, advanced patterns

---

## BASIC QUESTIONS (1-40)

### 1. Create Tuple Length
**Problem**: Create a tuple with elements 1, 2, 3, 4, 5 and return its length.
**Input**: No input required
**Output**: 5

### 2. Access Third Element  
**Problem**: Access the third element of tuple (10, 20, 30, 40, 50).
**Input**: tuple = (10, 20, 30, 40, 50)
**Output**: 30

### 3. Single Element Tuple
**Problem**: Create a tuple with a single element 42.
**Input**: element = 42
**Output**: (42,)

### 4. Element Existence Check
**Problem**: Check if element 25 exists in tuple (15, 25, 35, 45).
**Input**: tuple = (15, 25, 35, 45), element = 25
**Output**: True

### 5. Tuple Concatenation
**Problem**: Concatenate two tuples (1, 2) and (3, 4) into one.
**Input**: tuple1 = (1, 2), tuple2 = (3, 4)
**Output**: (1, 2, 3, 4)

### 6. Tuple Repetition
**Problem**: Repeat tuple ('a', 'b') three times.
**Input**: tuple = ('a', 'b'), times = 3
**Output**: ('a', 'b', 'a', 'b', 'a', 'b')

### 7. Basic Slicing
**Problem**: Slice tuple (1, 2, 3, 4, 5, 6) to get elements from index 2 to 4.
**Input**: tuple = (1, 2, 3, 4, 5, 6)
**Output**: (3, 4, 5)

### 8. Negative Indexing
**Problem**: Get the last element of tuple using negative indexing.
**Input**: tuple = ('apple', 'banana', 'cherry')
**Output**: 'cherry'

### 9. List to Tuple Conversion
**Problem**: Convert list [1, 2, 3] to a tuple.
**Input**: list = [1, 2, 3]
**Output**: (1, 2, 3)

### 10. Basic Unpacking
**Problem**: Unpack tuple (100, 200, 300) into three variables a, b, c.
**Input**: tuple = (100, 200, 300)
**Output**: a=100, b=200, c=300

### 11. Empty Tuple Creation
**Problem**: Create an empty tuple.
**Input**: No input required
**Output**: ()

### 12. Maximum Element
**Problem**: Find the maximum element in tuple (45, 12, 78, 23, 56).
**Input**: tuple = (45, 12, 78, 23, 56)
**Output**: 78

### 13. Minimum Element
**Problem**: Find the minimum element in tuple (45, 12, 78, 23, 56).
**Input**: tuple = (45, 12, 78, 23, 56)
**Output**: 12

### 14. Sum Calculation
**Problem**: Calculate the sum of all elements in tuple (1, 2, 3, 4, 5).
**Input**: tuple = (1, 2, 3, 4, 5)
**Output**: 15

### 15. Tuple to List Conversion
**Problem**: Convert tuple (1, 2, 3) to a list.
**Input**: tuple = (1, 2, 3)
**Output**: [1, 2, 3]

### 16. First Two Elements
**Problem**: Get first two elements of tuple (10, 20, 30, 40) using slicing.
**Input**: tuple = (10, 20, 30, 40)
**Output**: (10, 20)

### 17. Every Second Element
**Problem**: Get every second element from tuple (1, 2, 3, 4, 5, 6).
**Input**: tuple = (1, 2, 3, 4, 5, 6)
**Output**: (1, 3, 5)

### 18. Reverse Tuple
**Problem**: Reverse tuple (1, 2, 3, 4, 5) using slicing.
**Input**: tuple = (1, 2, 3, 4, 5)
**Output**: (5, 4, 3, 2, 1)

### 19. Tuple Equality
**Problem**: Check if tuple (1, 2, 3) is equal to tuple (1, 2, 3).
**Input**: tuple1 = (1, 2, 3), tuple2 = (1, 2, 3)
**Output**: True

### 20. Mixed Data Types
**Problem**: Create a tuple containing mixed data types: int, string, float.
**Input**: int=10, string='hello', float=3.14
**Output**: (10, 'hello', 3.14)

### 21. Second-to-Last Element
**Problem**: Get the second-to-last element using negative indexing.
**Input**: tuple = (10, 20, 30, 40, 50)
**Output**: 40

### 22. String to Tuple
**Problem**: Create tuple from string 'python'.
**Input**: string = 'python'
**Output**: ('p', 'y', 't', 'h', 'o', 'n')

### 23. Empty Tuple Check
**Problem**: Check if a tuple is empty.
**Input**: tuple = ()
**Output**: True

### 24. Lexicographic Comparison
**Problem**: Compare two tuples (1, 2) and (1, 3) lexicographically.
**Input**: tuple1 = (1, 2), tuple2 = (1, 3)
**Output**: tuple1 < tuple2 is True

### 25. Duplicate Elements
**Problem**: Create a tuple with duplicate elements (1, 2, 2, 3, 3, 3).
**Input**: No input required
**Output**: (1, 2, 2, 3, 3, 3)

### 26. Middle Element Access
**Problem**: Access middle element of tuple (1, 2, 3, 4, 5).
**Input**: tuple = (1, 2, 3, 4, 5)
**Output**: 3

### 27. Nested Tuple Length
**Problem**: Get length of nested tuple ((1, 2), (3, 4)).
**Input**: tuple = ((1, 2), (3, 4))
**Output**: 2

### 28. Range to Tuple
**Problem**: Create tuple with range of numbers from 1 to 5.
**Input**: range(1, 6)
**Output**: (1, 2, 3, 4, 5)

### 29. All Except First
**Problem**: Get all elements except the first one using slicing.
**Input**: tuple = (10, 20, 30, 40, 50)
**Output**: (20, 30, 40, 50)

### 30. All Except Last
**Problem**: Get all elements except the last one using slicing.
**Input**: tuple = (10, 20, 30, 40, 50)
**Output**: (10, 20, 30, 40)

### 31. Product of Elements
**Problem**: Multiply all elements in tuple (2, 3, 4) together.
**Input**: tuple = (2, 3, 4)
**Output**: 24

### 32. Type Checking
**Problem**: Find if tuple (1, 2, 3) contains only integers.
**Input**: tuple = (1, 2, 3)
**Output**: True

### 33. Squares Tuple
**Problem**: Create a tuple of squares from 1 to 4.
**Input**: numbers = [1, 2, 3, 4]
**Output**: (1, 4, 9, 16)

### 34. Even Indices
**Problem**: Get elements at even indices from tuple (10, 20, 30, 40, 50).
**Input**: tuple = (10, 20, 30, 40, 50)
**Output**: (10, 30, 50)

### 35. String Join
**Problem**: Join elements of tuple ('a', 'b', 'c') into a string.
**Input**: tuple = ('a', 'b', 'c')
**Output**: 'abc'

### 36. None Value Check
**Problem**: Check if tuple contains any None values.
**Input**: tuple = (1, None, 3)
**Output**: True

### 37. Boolean Tuple
**Problem**: Create a tuple of boolean values.
**Input**: values = [True, False, True]
**Output**: (True, False, True)

### 38. Element Type
**Problem**: Get the type of the first element in tuple (1, 'hello', 3.14).
**Input**: tuple = (1, 'hello', 3.14)
**Output**: <class 'int'>

### 39. Character Tuple
**Problem**: Create a tuple where each element is a character from 'ABC'.
**Input**: string = 'ABC'
**Output**: ('A', 'B', 'C')

### 40. Conceptual Swap
**Problem**: Swap first and last elements conceptually by creating new tuple.
**Input**: tuple = (1, 2, 3, 4, 5)
**Output**: (5, 2, 3, 4, 1)

---

## INTERMEDIATE QUESTIONS (41-80)

### 41. Count Method
**Problem**: Count occurrences of element 3 in tuple (1, 2, 3, 3, 3, 4).
**Input**: tuple = (1, 2, 3, 3, 3, 4)
**Output**: 3

### 42. Index Method
**Problem**: Find the index of first occurrence of 'apple' in tuple.
**Input**: tuple = ('banana', 'apple', 'cherry', 'apple')
**Output**: 1

### 43. Zip Combination
**Problem**: Use zip to combine two tuples element-wise.
**Input**: tuple1 = (1, 2, 3), tuple2 = ('a', 'b', 'c')
**Output**: [(1, 'a'), (2, 'b'), (3, 'c')]

### 44. Enumerate Usage
**Problem**: Use enumerate to get index-value pairs from tuple.
**Input**: tuple = ('x', 'y', 'z')
**Output**: [(0, 'x'), (1, 'y'), (2, 'z')]

### 45. Sort Integers
**Problem**: Sort a tuple of integers in ascending order.
**Input**: tuple = (5, 2, 8, 1, 9)
**Output**: (1, 2, 5, 8, 9)

### 46. Sort Strings
**Problem**: Sort a tuple of strings alphabetically.
**Input**: tuple = ('banana', 'apple', 'cherry')
**Output**: ('apple', 'banana', 'cherry')

### 47. All Indices
**Problem**: Find all indices where element 2 appears in tuple.
**Input**: tuple = (1, 2, 3, 2, 4, 2)
**Output**: [1, 3, 5]

### 48. Unique Elements
**Problem**: Create a tuple containing unique elements from another tuple.
**Input**: tuple = (1, 2, 2, 3, 3, 3, 4)
**Output**: (1, 2, 3, 4)

### 49. Filter Even Numbers
**Problem**: Filter even numbers from tuple (1, 2, 3, 4, 5, 6, 7, 8).
**Input**: tuple = (1, 2, 3, 4, 5, 6, 7, 8)
**Output**: (2, 4, 6, 8)

### 50. Dictionary Keys
**Problem**: Use tuple as dictionary key to store coordinates.
**Input**: coordinates = [(0, 0), (1, 1), (2, 2)]
**Output**: {(0, 0): 'origin', (1, 1): 'point1', (2, 2): 'point2'}

### 51. Tuple Iteration
**Problem**: Iterate through tuple using a for loop and print each element.
**Input**: tuple = ('a', 'b', 'c')
**Output**: a\nb\nc

### 52. Star Unpacking
**Problem**: Use tuple unpacking with * operator to capture remaining elements.
**Input**: tuple = (1, 2, 3, 4, 5)
**Output**: first=1, rest=[2, 3, 4, 5]

### 53. Most Frequent Element
**Problem**: Find the most frequent element in a tuple.
**Input**: tuple = (1, 2, 3, 2, 2, 4, 5)
**Output**: 2

### 54. Zip Lists to Tuples
**Problem**: Create a list of tuples from two separate lists using zip.
**Input**: names = ['Alice', 'Bob'], ages = [25, 30]
**Output**: [('Alice', 25), ('Bob', 30)]

### 55. Flatten Nested Tuples
**Problem**: Flatten a tuple of tuples into a single tuple.
**Input**: tuple = ((1, 2), (3, 4), (5, 6))
**Output**: (1, 2, 3, 4, 5, 6)

### 56. Duplicate Detection
**Problem**: Find elements that appear more than once in a tuple.
**Input**: tuple = (1, 2, 3, 2, 4, 3, 5)
**Output**: (2, 3)

### 57. Generator to Tuple
**Problem**: Use tuple comprehension (generator expression) to create tuple of squares.
**Input**: numbers = [1, 2, 3, 4]
**Output**: (1, 4, 9, 16)

### 58. Consecutive Pairs
**Problem**: Group consecutive elements in pairs using zip.
**Input**: tuple = (1, 2, 3, 4, 5, 6)
**Output**: [(1, 2), (3, 4), (5, 6)]

### 59. Tuple Intersection
**Problem**: Find intersection of two tuples (common elements).
**Input**: tuple1 = (1, 2, 3, 4), tuple2 = (3, 4, 5, 6)
**Output**: (3, 4)

### 60. Dictionary Keys to Tuple
**Problem**: Create tuple from dictionary keys.
**Input**: dict = {'a': 1, 'b': 2, 'c': 3}
**Output**: ('a', 'b', 'c')

### 61. Dictionary Values to Tuple
**Problem**: Create tuple from dictionary values.
**Input**: dict = {'a': 1, 'b': 2, 'c': 3}
**Output**: (1, 2, 3)

### 62. Zip to Dictionary
**Problem**: Use zip to create dictionary from two tuples.
**Input**: keys = ('name', 'age'), values = ('John', 25)
**Output**: {'name': 'John', 'age': 25}

### 63. Average Calculation
**Problem**: Calculate average of numeric elements in tuple.
**Input**: tuple = (10, 20, 30, 40, 50)
**Output**: 30.0

### 64. Second Largest
**Problem**: Find second largest element in tuple.
**Input**: tuple = (5, 2, 8, 1, 9, 3)
**Output**: 8

### 65. Element Replacement
**Problem**: Replace all occurrences of an element by creating new tuple.
**Input**: tuple = (1, 2, 3, 2, 4), old=2, new=9
**Output**: (1, 9, 3, 9, 4)

### 66. Cumulative Sums
**Problem**: Create a tuple of cumulative sums.
**Input**: tuple = (1, 2, 3, 4, 5)
**Output**: (1, 3, 6, 10, 15)

### 67. Sorted Check
**Problem**: Check if tuple is sorted in ascending order.
**Input**: tuple = (1, 2, 3, 4, 5)
**Output**: True

### 68. Left Rotation
**Problem**: Rotate tuple elements to the left by n positions.
**Input**: tuple = (1, 2, 3, 4, 5), n = 2
**Output**: (3, 4, 5, 1, 2)

### 69. Filter with Condition
**Problem**: Find tuple elements that satisfy a condition using filter.
**Input**: tuple = (1, 2, 3, 4, 5, 6), condition: > 3
**Output**: (4, 5, 6)

### 70. String to Integer Conversion
**Problem**: Convert tuple of strings to tuple of integers.
**Input**: tuple = ('1', '2', '3', '4')
**Output**: (1, 2, 3, 4)

### 71. Enumerate with Start
**Problem**: Use enumerate with custom start value.
**Input**: tuple = ('a', 'b', 'c'), start = 1
**Output**: [(1, 'a'), (2, 'b'), (3, 'c')]

### 72. Alternating Elements
**Problem**: Create tuple of alternating elements from two tuples.
**Input**: tuple1 = (1, 3, 5), tuple2 = (2, 4, 6)
**Output**: (1, 2, 3, 4, 5, 6)

### 73. Missing Number
**Problem**: Find missing number in sequence tuple.
**Input**: tuple = (1, 2, 4, 5, 6)
**Output**: 3

### 74. Uniqueness Check
**Problem**: Check if all elements in tuple are unique.
**Input**: tuple = (1, 2, 3, 4, 5)
**Output**: True

### 75. Multiple Tuple Merge
**Problem**: Merge multiple tuples into one.
**Input**: tuples = [(1, 2), (3, 4), (5, 6)]
**Output**: (1, 2, 3, 4, 5, 6)

### 76. Consecutive Differences
**Problem**: Create tuple of differences between consecutive elements.
**Input**: tuple = (10, 15, 12, 20, 25)
**Output**: (5, -3, 8, 5)

### 77. Map Function Application
**Problem**: Use map to apply function to all tuple elements.
**Input**: tuple = (1, 2, 3, 4), function = square
**Output**: (1, 4, 9, 16)

### 78. Longest String
**Problem**: Find longest string in tuple of strings.
**Input**: tuple = ('cat', 'elephant', 'dog', 'butterfly')
**Output**: 'butterfly'

### 79. Tuple Partitioning
**Problem**: Partition tuple into two based on a condition.
**Input**: tuple = (1, 2, 3, 4, 5, 6), condition: even/odd
**Output**: evens=(2, 4, 6), odds=(1, 3, 5)

### 80. Sliding Window
**Problem**: Create sliding window pairs from tuple.
**Input**: tuple = (1, 2, 3, 4, 5)
**Output**: [(1, 2), (2, 3), (3, 4), (4, 5)]

---

## ADVANCED/TRICKY QUESTIONS (81-100)

### 81. Deep Nested Access
**Problem**: Access element in deeply nested tuple structure.
**Input**: tuple = (((1, 2), (3, 4)), ((5, 6), (7, 8)))
**Output**: Access element 6: tuple[1][0][1]

### 82. Nested Unpacking
**Problem**: Implement tuple unpacking with nested structures.
**Input**: tuple = ((1, 2), (3, (4, 5)))
**Output**: (a, b), (c, (d, e)) = tuple

### 83. Complex Dictionary Keys
**Problem**: Use tuple as key in dictionary with complex operations.
**Input**: data = [((1, 2), 'A'), ((2, 3), 'B')]
**Output**: {(1, 2): 'A', (2, 3): 'B'}

### 84. Mutable Contents
**Problem**: Modify list inside tuple (demonstrates mutability of contents).
**Input**: tuple = (1, [2, 3], 4)
**Output**: tuple[1].append(5) → (1, [2, 3, 5], 4)

### 85. Recursive Flattening
**Problem**: Create recursive function to flatten arbitrarily nested tuples.
**Input**: tuple = (1, (2, (3, 4)), 5)
**Output**: (1, 2, 3, 4, 5)

### 86. Function Parameter Unpacking
**Problem**: Use tuple unpacking in function parameters.
**Input**: points = [(1, 2), (3, 4), (5, 6)]
**Output**: def distance(p1, p2): (x1, y1), (x2, y2) = p1, p2

### 87. Matrix Operations
**Problem**: Implement tuple-based matrix operations.
**Input**: matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
**Output**: Get column 1: (2, 5, 8)

### 88. LRU Cache Keys
**Problem**: Create tuple-based LRU cache key system.
**Input**: function calls with args
**Output**: Use (func_name, args_tuple) as cache key

### 89. Custom Tuple Comparison
**Problem**: Implement tuple comparison with custom logic.
**Input**: tuples = [(2, 1), (1, 3), (1, 2)]
**Output**: Sort by sum: [(1, 2), (2, 1), (1, 3)]

### 90. Multiple Assignment Loop
**Problem**: Use tuple for multiple assignment in loop.
**Input**: pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
**Output**: for num, letter in pairs: ...

### 91. State Machine
**Problem**: Implement tuple-based state machine.
**Input**: states and transitions as tuples
**Output**: (current_state, input) → next_state

### 92. Combination Generator
**Problem**: Create generator that yields tuple combinations.
**Input**: tuple = (1, 2, 3)
**Output**: All pairs: (1,2), (1,3), (2,3)

### 93. Args Unpacking
**Problem**: Use tuple unpacking with *args in function.
**Input**: def func(*args): ... with tuple input
**Output**: func(*(1, 2, 3, 4))

### 94. Coordinate Transformations
**Problem**: Implement tuple-based coordinate system transformations.
**Input**: points = [(0, 0), (1, 1), (2, 2)]
**Output**: Rotate 90°: [(0, 0), (-1, 1), (-2, 2)]

### 95. Graph Representation
**Problem**: Create tuple-based graph representation and traversal.
**Input**: edges = [(1, 2), (2, 3), (3, 4)]
**Output**: Adjacent nodes dictionary

### 96. Memoization
**Problem**: Use tuple for memoization in recursive function.
**Input**: fibonacci with tuple-based cache
**Output**: Cache key: (function, n)

### 97. Priority Queue
**Problem**: Implement tuple-based priority queue operations.
**Input**: items = [(3, 'task1'), (1, 'task2'), (2, 'task3')]
**Output**: Sort by priority: (1, 'task2'), (2, 'task3'), (3, 'task1')

### 98. Configuration System
**Problem**: Create tuple-based configuration system.
**Input**: nested configuration tuples
**Output**: Access: config[section][key]

### 99. Exception Unpacking
**Problem**: Use tuple unpacking with exception handling.
**Input**: result, error = operation_that_returns_tuple()
**Output**: if error: handle_error(error)

### 100. Pattern Matching
**Problem**: Implement tuple-based pattern matching logic.
**Input**: patterns = [(type, handler), ...]
**Output**: Match input against patterns and execute handler

---

*These questions progressively build from basic tuple operations to complex, real-world applications suitable for interviews and competitive programming.*