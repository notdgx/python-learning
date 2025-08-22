# Python List Coding Questions - 100 Problems

## Basic Level (Questions 1-40)

### 1. Create and Display List
Create a list with the numbers 1, 2, 3, 4, 5 and print it.
**Input:** None
**Output:** [1, 2, 3, 4, 5]

### 2. Access List Elements
Given a list [10, 20, 30, 40, 50], access and print the third element.
**Input:** [10, 20, 30, 40, 50]
**Output:** 30

### 3. List Length
Find the length of the list ['apple', 'banana', 'cherry', 'date'].
**Input:** ['apple', 'banana', 'cherry', 'date']
**Output:** 4

### 4. Append Element
Add the element 'grape' to the end of the list ['apple', 'banana', 'cherry'].
**Input:** ['apple', 'banana', 'cherry']
**Output:** ['apple', 'banana', 'cherry', 'grape']

### 5. Insert Element
Insert 25 at index 2 in the list [10, 20, 30, 40].
**Input:** [10, 20, 30, 40]
**Output:** [10, 20, 25, 30, 40]

### 6. Remove Element by Value
Remove 'banana' from the list ['apple', 'banana', 'cherry', 'banana'].
**Input:** ['apple', 'banana', 'cherry', 'banana']
**Output:** ['apple', 'cherry', 'banana']

### 7. Remove Element by Index
Remove the element at index 1 from [5, 10, 15, 20].
**Input:** [5, 10, 15, 20]
**Output:** [5, 15, 20]

### 8. Check if Element Exists
Check if 'orange' exists in ['apple', 'banana', 'cherry'].
**Input:** ['apple', 'banana', 'cherry']
**Output:** False

### 9. Find Index of Element
Find the index of 'cherry' in ['apple', 'banana', 'cherry', 'date'].
**Input:** ['apple', 'banana', 'cherry', 'date']
**Output:** 2

### 10. Count Occurrences
Count how many times 'apple' appears in ['apple', 'banana', 'apple', 'cherry'].
**Input:** ['apple', 'banana', 'apple', 'cherry']
**Output:** 2

### 11. Basic List Slicing
Extract elements from index 1 to 3 from [0, 1, 2, 3, 4, 5].
**Input:** [0, 1, 2, 3, 4, 5]
**Output:** [1, 2, 3]

### 12. Negative Indexing
Access the last element of [10, 20, 30, 40, 50] using negative indexing.
**Input:** [10, 20, 30, 40, 50]
**Output:** 50

### 13. Replace Element
Replace the element at index 2 with 'NEW' in ['a', 'b', 'c', 'd'].
**Input:** ['a', 'b', 'c', 'd']
**Output:** ['a', 'b', 'NEW', 'd']

### 14. Extend List
Extend [1, 2, 3] with [4, 5, 6].
**Input:** [1, 2, 3], [4, 5, 6]
**Output:** [1, 2, 3, 4, 5, 6]

### 15. Clear List
Clear all elements from [1, 2, 3, 4, 5].
**Input:** [1, 2, 3, 4, 5]
**Output:** []

### 16. Copy List
Create a copy of [1, 2, 3, 4] using the copy() method.
**Input:** [1, 2, 3, 4]
**Output:** [1, 2, 3, 4]

### 17. Concatenate Lists
Concatenate [1, 2] and [3, 4] using the + operator.
**Input:** [1, 2], [3, 4]
**Output:** [1, 2, 3, 4]

### 18. Repeat List
Repeat the list [1, 2] three times.
**Input:** [1, 2]
**Output:** [1, 2, 1, 2, 1, 2]

### 19. Check Empty List
Check if the list [] is empty.
**Input:** []
**Output:** True

### 20. Minimum in List
Find the minimum value in [45, 12, 78, 23, 67].
**Input:** [45, 12, 78, 23, 67]
**Output:** 12

### 21. Maximum in List
Find and return the maximum value in [45, 12, 78, 23, 67].
**Input:** [45, 12, 78, 23, 67]
**Output:** 78

### 22. Sum of List Elements
Calculate the sum of all elements in [1, 2, 3, 4, 5].
**Input:** [1, 2, 3, 4, 5]
**Output:** 15

### 23. List of Squares
Create a list of squares of numbers from 1 to 5.
**Input:** None
**Output:** [1, 4, 9, 16, 25]

### 24. Even Numbers from List
Extract all even numbers from [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
**Input:** [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
**Output:** [2, 4, 6, 8, 10]

### 25. Odd Numbers from List
Extract all odd numbers from [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
**Input:** [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
**Output:** [1, 3, 5, 7, 9]

### 26. List Iteration
Print each element of ['red', 'green', 'blue'] on a new line.
**Input:** ['red', 'green', 'blue']
**Output:** red\ngreen\nblue

### 27. List of Strings Length
Create a list containing the lengths of strings in ['hello', 'world', 'python'].
**Input:** ['hello', 'world', 'python']
**Output:** [5, 5, 6]

### 28. First and Last Elements
Extract the first and last elements from [10, 20, 30, 40, 50].
**Input:** [10, 20, 30, 40, 50]
**Output:** [10, 50]

### 29. Remove Last Element
Remove and return the last element from [1, 2, 3, 4, 5].
**Input:** [1, 2, 3, 4, 5]
**Output:** 5, [1, 2, 3, 4]

### 30. Reverse Slice
Get elements from index 3 to 1 (reverse order) from [0, 1, 2, 3, 4, 5].
**Input:** [0, 1, 2, 3, 4, 5]
**Output:** [3, 2, 1]

### 31. List Contains All
Check if all elements in [2, 4, 6, 8] are even numbers.
**Input:** [2, 4, 6, 8]
**Output:** True

### 32. List Contains Any
Check if any element in [1, 3, 5, 8] is even.
**Input:** [1, 3, 5, 8]
**Output:** True

### 33. Replace Multiple Elements
Replace all occurrences of 'old' with 'new' in ['old', 'car', 'old', 'house'].
**Input:** ['old', 'car', 'old', 'house']
**Output:** ['new', 'car', 'new', 'house']

### 34. List Multiplication Table
Create a list of multiples of 3 up to 15.
**Input:** None
**Output:** [3, 6, 9, 12, 15]

### 35. List Average
Calculate the average of elements in [10, 20, 30, 40, 50].
**Input:** [10, 20, 30, 40, 50]
**Output:** 30.0

### 36. Convert to String List
Convert all numbers in [1, 2, 3, 4, 5] to strings.
**Input:** [1, 2, 3, 4, 5]
**Output:** ['1', '2', '3', '4', '5']

### 37. Convert String to List
Convert the string 'hello' to a list of characters.
**Input:** 'hello'
**Output:** ['h', 'e', 'l', 'l', 'o']

### 38. Join List Elements
Join elements of ['apple', 'banana', 'cherry'] with ', '.
**Input:** ['apple', 'banana', 'cherry']
**Output:** 'apple, banana, cherry'

### 39. Split and Create List
Split the string 'one,two,three,four' by comma and create a list.
**Input:** 'one,two,three,four'
**Output:** ['one', 'two', 'three', 'four']

### 40. List Element Type Check
Check if all elements in  [1, 2, 3, 4, 5]are integers.
**Input:** [1, 2, 3, 4, 5]
**Output:** True

## Intermediate Level (Questions 41-80)

### 41. Sort List Ascending
Sort the list [64, 34, 25, 12, 22, 11, 90] in ascending order.
**Input:** [64, 34, 25, 12, 22, 11, 90]
**Output:** [11, 12, 22, 25, 34, 64, 90]

### 42. Sort List Descending
Sort the list [64, 34, 25, 12, 22, 11, 90] in descending order.
**Input:** [64, 34, 25, 12, 22, 11, 90]
**Output:** [90, 64, 34, 25, 22, 12, 11]

### 43. Reverse List In-Place
Reverse the list [1, 2, 3, 4, 5] in-place.
**Input:** [1, 2, 3, 4, 5]
**Output:** [5, 4, 3, 2, 1]

### 44. List Comprehension - Squares
Use list comprehension to create squares of numbers from 1 to 10.
**Input:** None
**Output:** [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

### 45. List Comprehension with Condition
Use list comprehension to get squares of even numbers from 1 to 10.
**Input:** None
**Output:** [4, 16, 36, 64, 100]

### 46. Nested List Access
Access the element 6 from [[1, 2, 3], [4, 5, 6], [7, 8, 9]].
**Input:** [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
**Output:** 6

### 47. Nested List Modification
Change the element 5 to 50 in [[1, 2, 3], [4, 5, 6], [7, 8, 9]].
**Input:** [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
**Output:** [[1, 2, 3], [4, 50, 6], [7, 8, 9]]

### 48. Remove Duplicates Simple
Remove duplicates from [1, 2, 2, 3, 4, 4, 5] (order doesn't matter).
**Input:** [1, 2, 2, 3, 4, 4, 5]
**Output:** [1, 2, 3, 4, 5]

### 49. Find Second Largest
Find the second largest number in [45, 12, 78, 23, 67, 89, 34].
**Input:** [45, 12, 78, 23, 67, 89, 34]
**Output:** 78

### 50. List Intersection
Find common elements between [1, 2, 3, 4, 5] and [4, 5, 6, 7, 8].
**Input:** [1, 2, 3, 4, 5], [4, 5, 6, 7, 8]
**Output:** [4, 5]

### 51. List Union
Find union of [1, 2, 3, 4] and [3, 4, 5, 6] (unique elements).
**Input:** [1, 2, 3, 4], [3, 4, 5, 6]
**Output:** [1, 2, 3, 4, 5, 6]

### 52. List Difference
Find elements in [1, 2, 3, 4, 5] that are not in [3, 4, 5, 6, 7].
**Input:** [1, 2, 3, 4, 5], [3, 4, 5, 6, 7]
**Output:** [1, 2]

### 53. Rotate List Left
Rotate [1, 2, 3, 4, 5] left by 2 positions.
**Input:** [1, 2, 3, 4, 5], positions=2
**Output:** [3, 4, 5, 1, 2]

### 54. Rotate List Right
Rotate [1, 2, 3, 4, 5] right by 2 positions.
**Input:** [1, 2, 3, 4, 5], positions=2
**Output:** [4, 5, 1, 2, 3]

### 55. Chunk List
Split [1, 2, 3, 4, 5, 6, 7, 8] into chunks of size 3.
**Input:** [1, 2, 3, 4, 5, 6, 7, 8], chunk_size=3
**Output:** [[1, 2, 3], [4, 5, 6], [7, 8]]

### 56. Filter List by Length
Filter words with length > 4 from ['cat', 'elephant', 'dog', 'python', 'ai'].
**Input:** ['cat', 'elephant', 'dog', 'python', 'ai']
**Output:** ['elephant', 'python']

### 57. List Comprehension with Multiple Conditions
Get numbers divisible by both 2 and 3 from range 1 to 20.
**Input:** None
**Output:** [6, 12, 18]

### 58. Enumerate List
Create list of tuples with index and value for ['a', 'b', 'c', 'd'].
**Input:** ['a', 'b', 'c', 'd']
**Output:** [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]

### 59. Zip Two Lists
Combine ['name', 'age', 'city'] and ['John', 25, 'NYC'] into tuples.
**Input:** ['name', 'age', 'city'], ['John', 25, 'NYC']
**Output:** [('name', 'John'), ('age', 25), ('city', 'NYC')]

### 60. List of Dictionaries
Create a list of dictionaries from two lists: keys and values.
**Input:** ['name', 'age'], [['John', 25], ['Jane', 30]]
**Output:** [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}]

### 61. Group Elements by Property
Group words by their first letter: ['apple', 'banana', 'cherry', 'apricot'].
**Input:** ['apple', 'banana', 'cherry', 'apricot']
**Output:** {'a': ['apple', 'apricot'], 'b': ['banana'], 'c': ['cherry']}

### 62. Find All Indices
Find all indices where 'a' appears in ['a', 'b', 'a', 'c', 'a].'
**Input:** ['a', 'b', 'a', 'c', 'a']
**Output:** [0, 2, 4]

### 63. Replace at Multiple Indices
Replace elements at indices [1, 3] with 'X' in ['a', 'b', 'c', 'd', 'e'].
**Input:** ['a', 'b', 'c', 'd', 'e'], indices=[1, 3]
**Output:** ['a', 'X', 'c', 'X', 'e']

### 64. List Palindrome Check
Check if [1, 2, 3, 2, 1] is a palindrome.
**Input:** [1, 2, 3, 2, 1]
**Output:** True

### 65. Transpose 2D List
Transpose the matrix [[1, 2, 3], [4, 5, 6]].
**Input:** [[1, 2, 3], [4, 5, 6]]
**Output:** [[1, 4], [2, 5], [3, 6]]

### 66. Merge Sorted Lists
Merge two sorted lists [1, 3, 5] and [2, 4, 6] into one sorted list.
**Input:** [1, 3, 5], [2, 4, 6]
**Output:** [1, 2, 3, 4, 5, 6]

### 67. Running Sum
Calculate running sum of [1, 2, 3, 4, 5].
**Input:** [1, 2, 3, 4, 5]
**Output:** [1, 3, 6, 10, 15]

### 68. Running Maximum
Calculate running maximum of [3, 1, 4, 1, 5, 9, 2].
**Input:** [3, 1, 4, 1, 5, 9, 2]
**Output:** [3, 3, 4, 4, 5, 9, 9]

### 69. List Elements Frequency
Count frequency of each element in [1, 2, 2, 3, 3, 3, 4].
**Input:** [1, 2, 2, 3, 3, 3, 4]
**Output:** {1: 1, 2: 2, 3: 3, 4: 1}

### 70. Remove Elements by Condition
Remove all elements greater than 5 from [1, 6, 2, 8, 3, 9, 4].
**Input:** [1, 6, 2, 8, 3, 9, 4]
**Output:** [1, 2, 3, 4]

### 71. List Moving Average
Calculate 3-point moving average of [1, 2, 3, 4, 5, 6, 7].
**Input:** [1, 2, 3, 4, 5, 6, 7], window=3
**Output:** [2.0, 3.0, 4.0, 5.0, 6.0]

### 72. Interleave Two Lists
Interleave elements of [1, 3, 5] and [2, 4, 6].
**Input:** [1, 3, 5], [2, 4, 6]
**Output:** [1, 2, 3, 4, 5, 6]

### 73. List Partition
Partition [1, 2, 3, 4, 5, 6] into even and odd numbers.
**Input:** [1, 2, 3, 4, 5, 6]
**Output:** ([2, 4, 6], [1, 3, 5])

### 74. Find Missing Number
Find missing number in [1, 2, 4, 5, 6] (range 1-6).
**Input:** [1, 2, 4, 5, 6]
**Output:** 3

### 75. List Binary Search
Implement binary search to find 7 in sorted list [1, 3, 5, 7, 9, 11].
**Input:** [1, 3, 5, 7, 9, 11], target=7
**Output:** 3

### 76. Longest Increasing Subsequence Length
Find length of longest increasing subsequence in [10, 9, 2, 5, 3, 7, 101, 18].
**Input:** [10, 9, 2, 5, 3, 7, 101, 18]
**Output:** 4

### 77. Remove by Multiple Values
Remove all occurrences of [2, 4] from [1, 2, 3, 4, 5, 2, 4, 6].
**Input:** [1, 2, 3, 4, 5, 2, 4, 6], to_remove=[2, 4]
**Output:** [1, 3, 5, 6]

### 78. List Sliding Window Maximum
Find maximum in each window of size 3 in [1, 3, -1, -3, 5, 3, 6, 7].
**Input:** [1, 3, -1, -3, 5, 3, 6, 7], window=3
**Output:** [3, 3, 5, 5, 6, 7]

### 79. Compare Lists Element-wise
Compare [1, 2, 3, 4] and [1, 3, 3, 5] element by element.
**Input:** [1, 2, 3, 4], [1, 3, 3, 5]
**Output:** [True, False, True, False]

### 80. List Permutation Check
Check if [1, 2, 3] is a permutation of [3, 1, 2].
**Input:** [1, 2, 3], [3, 1, 2]
**Output:** True

## Advanced/Tricky Level (Questions 81-100)

### 81. Flatten Nested List
Flatten [[1, 2], [3, 4, 5], [6]] into a single list.
**Input:** [[1, 2], [3, 4, 5], [6]]
**Output:** [1, 2, 3, 4, 5, 6]

### 82. Deep Flatten Nested List
Flatten [1, [2, 3, [4, 5]], 6] completely.
**Input:** [1, [2, 3, [4, 5]], 6]
**Output:** [1, 2, 3, 4, 5, 6]

### 83. Remove Duplicates Preserve Order
Remove duplicates from [3, 1, 4, 1, 5, 9, 2, 6, 5] keeping first occurrence.
**Input:** [3, 1, 4, 1, 5, 9, 2, 6, 5]
**Output:** [3, 1, 4, 5, 9, 2, 6]

### 84. Cartesian Product of Lists
Generate cartesian product of [1, 2] and ['a', 'b'].
**Input:** [1, 2], ['a', 'b']
**Output:** [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]

### 85. List Combinations
Generate all combinations of length 2 from [1, 2, 3, 4].
**Input:** [1, 2, 3, 4], r=2
**Output:** [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

### 86. List Permutations
Generate all permutations of [1, 2, 3].
**Input:** [1, 2, 3]
**Output:** [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

### 87. Multi-condition Filter
Filter numbers divisible by 2 OR 3 AND greater than 5 from range(1, 21).
**Input:** range(1, 21)
**Output:** [6, 8, 9, 10, 12, 14, 15, 16, 18, 20]

### 88. Nested List Comprehension Matrix
Create 3x3 matrix where each element is i*j using nested list comprehension.
**Input:** None
**Output:** [[0, 0, 0], [0, 1, 2], [0, 2, 4]]

### 89. List Memory Optimization
Create memory-efficient solution for finding duplicates in very large list.
**Input:** [1, 2, 3, 2, 4, 5, 1, 6, 7, 3] (imagine very large)
**Output:** [1, 2, 3]

### 90. Zip Multiple Lists Unequal Length
Zip three lists of different lengths: [1, 2, 3], [4, 5], [6, 7, 8, 9].
**Input:** [1, 2, 3], [4, 5], [6, 7, 8, 9]
**Output:** [(1, 4, 6), (2, 5, 7)]

### 91. List Spiral Order
Create a spiral traversal of 2D list [[1,2,3],[4,5,6],[7,8,9]].
**Input:** [[1,2,3],[4,5,6],[7,8,9]]
**Output:** [1, 2, 3, 6, 9, 8, 7, 4, 5]

### 92. Custom Sort with Multiple Criteria
Sort list of tuples by second element desc, then first element asc: [(1,3), (2,1), (3,3), (1,2)].
**Input:** [(1,3), (2,1), (3,3), (1,2)]
**Output:** [(1,3), (3,3), (1,2), (2,1)]

### 93. List Pattern Matching
Find all sublists of length 3 where middle element is max: [1,5,2,8,3,9,4].
**Input:** [1,5,2,8,3,9,4]
**Output:** [[1,5,2], [3,9,4]]

### 94. Merge Overlapping Intervals
Merge overlapping intervals: [[1,3],[2,6],[8,10],[15,18]].
**Input:** [[1,3],[2,6],[8,10],[15,18]]
**Output:** [[1,6],[8,10],[15,18]]

### 95. List Edit Distance
Calculate minimum edit distance between [1,2,3,4] and [1,3,4,5].
**Input:** [1,2,3,4], [1,3,4,5]
**Output:** 2

### 96. Generate Pascal's Triangle
Generate first 5 rows of Pascal's triangle as nested list.
**Input:** n=5
**Output:** [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]

### 97. List Cycle Detection
Detect if there's a cycle in list references (simulated with indices).
**Input:** [1, 2, 3, 1] (index points create cycle)
**Output:** True

### 98. Maximum Subarray Sum
Find maximum sum of contiguous subarray in [-2,1,-3,4,-1,2,1,-5,4].
**Input:** [-2,1,-3,4,-1,2,1,-5,4]
**Output:** 6

### 99. List Anagram Groups
Group anagrams: ['eat', 'tea', 'tan', 'ate', 'nat', 'bat'].
**Input:** ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
**Output:** [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

### 100. Multi-dimensional List Search
Search for target in row-wise and column-wise sorted 2D list.
**Input:** [[1,4,7,11],[2,5,8,12],[3,6,9,16],[10,13,14,17]], target=5
**Output:** True

---

## Notes:
- Questions progress from basic list operations to advanced algorithms
- Each question includes clear input/output examples
- Edge cases to consider: empty lists, single elements, None values
- Focus on Pythonic solutions and built-in methods where appropriate
- Advanced questions incorporate algorithmic thinking and optimization