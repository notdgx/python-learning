# 100 Python Set Coding Questions

This comprehensive collection contains 100 Python coding questions focused exclusively on set operations and logic, designed for Python learners and portfolio creators.

**Difficulty Distribution:**
- 🟢 **Basic (40%)**: Creating sets, adding/removing elements, deduplication, membership testing
- 🟡 **Intermediate (40%)**: Set methods, union, intersection, difference, conditional logic
- 🔴 **Advanced (20%)**: Set theory puzzles, frozenset, edge cases, complex algorithms

---

## 🟢 BASIC QUESTIONS (1-40)

### 1. Create a set from a list and remove duplicates
**Description:** Convert a list with duplicate elements into a set to remove duplicates.
**Sample Input:** `[1, 2, 2, 3, 4, 4, 5]`
**Sample Output:** `{1, 2, 3, 4, 5}`

### 2. Check if an element exists in a set
**Description:** Use the `in` operator to test membership in a set.
**Sample Input:** `my_set = {1, 2, 3}, element = 2`
**Sample Output:** `True`

### 3. Add a single element to a set
**Description:** Use the `add()` method to insert a new element into a set.
**Sample Input:** `my_set = {1, 2, 3}, element = 4`
**Sample Output:** `{1, 2, 3, 4}`

### 4. Remove an element from a set using remove()
**Description:** Use `remove()` to delete an element (raises KeyError if not found).
**Sample Input:** `my_set = {1, 2, 3}, element = 2`
**Sample Output:** `{1, 3}`

### 5. Remove an element from a set using discard()
**Description:** Use `discard()` to delete an element (no error if missing).
**Sample Input:** `my_set = {1, 2, 3}, element = 5`
**Sample Output:** `{1, 2, 3}`

### 6. Get the length of a set
**Description:** Use `len()` function to count elements in a set.
**Sample Input:** `my_set = {1, 2, 3, 4, 5}`
**Sample Output:** `5`

### 7. Check if a set is empty
**Description:** Determine if a set contains no elements.
**Sample Input:** `my_set = set()`
**Sample Output:** `True`

### 8. Create an empty set
**Description:** Initialize an empty set using the `set()` constructor.
**Sample Input:** `None`
**Sample Output:** `set()`

### 9. Convert a string to a set of characters
**Description:** Transform a string into a set of unique characters.
**Sample Input:** `"hello"`
**Sample Output:** `{'h', 'e', 'l', 'o'}`

### 10. Check if an element is NOT in a set
**Description:** Use the `not in` operator for negative membership testing.
**Sample Input:** `my_set = {1, 2, 3}, element = 5`
**Sample Output:** `True`

### 11. Clear all elements from a set
**Description:** Use the `clear()` method to remove all elements.
**Sample Input:** `my_set = {1, 2, 3}`
**Sample Output:** `set()`

### 12. Create a set from tuple elements
**Description:** Convert a tuple to a set, removing duplicates.
**Sample Input:** `(1, 2, 3, 2, 4)`
**Sample Output:** `{1, 2, 3, 4}`

### 13. Pop a random element from a set
**Description:** Use `pop()` to remove and return an arbitrary element.
**Sample Input:** `my_set = {1, 2, 3}`
**Sample Output:** `1 (or 2, or 3), remaining set: {2, 3}`

### 14. Create a set with mixed data types
**Description:** Create a set containing different data types.
**Sample Input:** `[1, 'hello', 3.14, True]`
**Sample Output:** `{1, 'hello', 3.14}`

### 15. Find unique words in a sentence
**Description:** Split a sentence and create a set of unique words.
**Sample Input:** `"the cat sat on the mat"`
**Sample Output:** `{'the', 'cat', 'sat', 'on', 'mat'}`

### 16. Check if two sets have the same length
**Description:** Compare the sizes of two sets.
**Sample Input:** `set1 = {1, 2, 3}, set2 = {4, 5, 6}`
**Sample Output:** `True`

### 17. Create a set from the first n natural numbers
**Description:** Generate a set containing numbers from 1 to n.
**Sample Input:** `n = 5`
**Sample Output:** `{1, 2, 3, 4, 5}`

### 18. Remove duplicates from a list of email addresses
**Description:** Use sets to deduplicate email addresses.
**Sample Input:** `['user@email.com', 'admin@email.com', 'user@email.com']`
**Sample Output:** `{'user@email.com', 'admin@email.com'}`

### 19. Create a set of even numbers from 1 to 10
**Description:** Filter even numbers and create a set.
**Sample Input:** `range(1, 11)`
**Sample Output:** `{2, 4, 6, 8, 10}`

### 20. Check if a set contains only positive numbers
**Description:** Verify all elements are positive.
**Sample Input:** `my_set = {1, 2, 3, 4}`
**Sample Output:** `True`

### 21. Create a set of vowels
**Description:** Create a set containing all vowels.
**Sample Input:** `None`
**Sample Output:** `{'a', 'e', 'i', 'o', 'u'}`

### 22. Find unique characters in two strings combined
**Description:** Combine characters from two strings into one set.
**Sample Input:** `str1 = 'hello', str2 = 'world'`
**Sample Output:** `{'h', 'e', 'l', 'o', 'w', 'r', 'd'}`

### 23. Create a set of squares from 1 to 5
**Description:** Generate a set of squared numbers.
**Sample Input:** `range(1, 6)`
**Sample Output:** `{1, 4, 9, 16, 25}`

### 24. Check if a string contains duplicate characters
**Description:** Determine if any character appears more than once.
**Sample Input:** `"hello"`
**Sample Output:** `True (because 'l' appears twice)`

### 25. Create a set from dictionary keys
**Description:** Extract dictionary keys into a set.
**Sample Input:** `{'a': 1, 'b': 2, 'c': 3}`
**Sample Output:** `{'a', 'b', 'c'}`

### 26. Remove all vowels from a set of characters
**Description:** Filter out vowel characters from a set.
**Sample Input:** `{'a', 'b', 'c', 'e', 'f'}`
**Sample Output:** `{'b', 'c', 'f'}`

### 27. Check if a set is a singleton
**Description:** Determine if a set contains exactly one element.
**Sample Input:** `my_set = {42}`
**Sample Output:** `True`

### 28. Create a set of file extensions from filenames
**Description:** Extract file extensions from a list of filenames.
**Sample Input:** `['file1.txt', 'file2.pdf', 'file3.txt', 'file4.jpg']`
**Sample Output:** `{'.txt', '.pdf', '.jpg'}`

### 29. Find common characters between your name and 'python'
**Description:** Find intersection of characters between two strings.
**Sample Input:** `name = 'john'`
**Sample Output:** `{'h', 'n', 'o'}`

### 30. Create a set of prime numbers less than 20
**Description:** Generate a set of prime numbers in a given range.
**Sample Input:** `range(2, 20)`
**Sample Output:** `{2, 3, 5, 7, 11, 13, 17, 19}`

### 31. Update a set by adding multiple elements at once
**Description:** Use `update()` to add multiple elements simultaneously.
**Sample Input:** `my_set = {1, 2}, elements = [3, 4, 5]`
**Sample Output:** `{1, 2, 3, 4, 5}`

### 32. Create a copy of a set
**Description:** Use `copy()` method to create a shallow copy.
**Sample Input:** `original = {1, 2, 3}`
**Sample Output:** `{1, 2, 3} (new set object)`

### 33. Check if all elements in a list are unique
**Description:** Compare list length with set length to check uniqueness.
**Sample Input:** `[1, 2, 3, 4, 5]`
**Sample Output:** `True`

### 34. Remove specific elements from a set based on condition
**Description:** Filter elements based on a given condition.
**Sample Input:** `my_set = {1, 2, 3, 4, 5}, condition: remove even numbers`
**Sample Output:** `{1, 3, 5}`

### 35. Create a set of unique lengths from strings
**Description:** Get unique string lengths from a list of strings.
**Sample Input:** `['cat', 'dog', 'elephant', 'fox']`
**Sample Output:** `{3, 8}`

### 36. Check if a set contains any negative numbers
**Description:** Test for presence of negative values.
**Sample Input:** `my_set = {1, -2, 3, 4}`
**Sample Output:** `True`

### 37. Create a set from the digits of a number
**Description:** Extract unique digits from a number.
**Sample Input:** `12321`
**Sample Output:** `{'1', '2', '3'}`

### 38. Find maximum and minimum values in a set
**Description:** Use built-in functions to find extremes.
**Sample Input:** `my_set = {3, 7, 1, 9, 5}`
**Sample Output:** `max: 9, min: 1`

### 39. Create a set of unique first letters from words
**Description:** Extract first character from each word.
**Sample Input:** `['apple', 'banana', 'cherry', 'avocado']`
**Sample Output:** `{'a', 'b', 'c'}`

### 40. Check if a set contains only alphabetic strings
**Description:** Verify all elements are alphabetic strings.
**Sample Input:** `my_set = {'hello', 'world', 'python'}`
**Sample Output:** `True`

---

## 🟡 INTERMEDIATE QUESTIONS (41-80)

### 41. Find the union of two sets
**Description:** Combine all unique elements from two sets using `union()` or `|`.
**Sample Input:** `set1 = {1, 2, 3}, set2 = {3, 4, 5}`
**Sample Output:** `{1, 2, 3, 4, 5}`

### 42. Find the intersection of two sets
**Description:** Find common elements using `intersection()` or `&`.
**Sample Input:** `set1 = {1, 2, 3}, set2 = {2, 3, 4}`
**Sample Output:** `{2, 3}`

### 43. Find the difference between two sets
**Description:** Elements in first set but not in second using `difference()` or `-`.
**Sample Input:** `set1 = {1, 2, 3, 4}, set2 = {3, 4, 5}`
**Sample Output:** `{1, 2}`

### 44. Find the symmetric difference between two sets
**Description:** Elements in either set but not both using `symmetric_difference()` or `^`.
**Sample Input:** `set1 = {1, 2, 3}, set2 = {3, 4, 5}`
**Sample Output:** `{1, 2, 4, 5}`

### 45. Check if one set is a subset of another
**Description:** Use `issubset()` or `<=` to test subset relationship.
**Sample Input:** `set1 = {1, 2}, set2 = {1, 2, 3, 4}`
**Sample Output:** `True`

### 46. Check if one set is a superset of another
**Description:** Use `issuperset()` or `>=` to test superset relationship.
**Sample Input:** `set1 = {1, 2, 3, 4}, set2 = {2, 3}`
**Sample Output:** `True`

### 47. Check if two sets are disjoint
**Description:** Use `isdisjoint()` to check if sets have no common elements.
**Sample Input:** `set1 = {1, 2, 3}, set2 = {4, 5, 6}`
**Sample Output:** `True`

### 48. Update a set with the union of another set
**Description:** Use `update()` or `|=` to modify original set with union.
**Sample Input:** `set1 = {1, 2}, set2 = {3, 4}`
**Sample Output:** `set1 becomes {1, 2, 3, 4}`

### 49. Update a set with the intersection of another set
**Description:** Use `intersection_update()` or `&=` to keep only common elements.
**Sample Input:** `set1 = {1, 2, 3}, set2 = {2, 3, 4}`
**Sample Output:** `set1 becomes {2, 3}`

### 50. Update a set with the difference of another set
**Description:** Use `difference_update()` or `-=` to remove common elements.
**Sample Input:** `set1 = {1, 2, 3, 4}, set2 = {3, 4}`
**Sample Output:** `set1 becomes {1, 2}`

### 51. Find common elements across multiple sets
**Description:** Find intersection of more than two sets.
**Sample Input:** `sets = [{1,2,3}, {2,3,4}, {2,3,5}]`
**Sample Output:** `{2, 3}`

### 52. Filter a set using set comprehension
**Description:** Create a new set with elements meeting a condition.
**Sample Input:** `numbers = {1, 2, 3, 4, 5, 6}, condition: even numbers`
**Sample Output:** `{2, 4, 6}`

### 53. Create a set of squared even numbers
**Description:** Combine filtering and transformation in set comprehension.
**Sample Input:** `range(1, 11)`
**Sample Output:** `{4, 16, 36, 64, 100}`

### 54. Find elements in exactly one of two sets
**Description:** Elements that appear in one set but not both (symmetric difference).
**Sample Input:** `set1 = {1, 2, 3}, set2 = {3, 4, 5}`
**Sample Output:** `{1, 2, 4, 5}`

### 55. Check if a set is a proper subset
**Description:** Use `<` operator to check if subset is strictly smaller.
**Sample Input:** `set1 = {1, 2}, set2 = {1, 2, 3}`
**Sample Output:** `True`

### 56. Flatten nested lists and create unique set
**Description:** Convert nested structure to flat set of unique elements.
**Sample Input:** `[[1, 2], [2, 3], [3, 4, 1]]`
**Sample Output:** `{1, 2, 3, 4}`

### 57. Find union of multiple sets
**Description:** Combine all elements from a list of sets.
**Sample Input:** `sets = [{1, 2}, {2, 3}, {3, 4}]`
**Sample Output:** `{1, 2, 3, 4}`

### 58. Remove common elements from two sets mutually
**Description:** Update both sets to remove their intersection.
**Sample Input:** `set1 = {1, 2, 3, 4}, set2 = {3, 4, 5, 6}`
**Sample Output:** `set1: {1, 2}, set2: {5, 6}`

### 59. Check hierarchical relationship in sets
**Description:** Verify if sets form a subset chain.
**Sample Input:** `sets = [{1}, {1, 2}, {1, 2, 3}]`
**Sample Output:** `True (each is subset of next)`

### 60. Find unique elements across all sets
**Description:** Get union of multiple sets.
**Sample Input:** `sets = [{1, 2}, {2, 3}, {4, 5}]`
**Sample Output:** `{1, 2, 3, 4, 5}`

### 61. Create a blacklist filter using sets
**Description:** Remove blacklisted items from a dataset using set difference.
**Sample Input:** `data = {1, 2, 3, 4, 5}, blacklist = {2, 4}`
**Sample Output:** `{1, 3, 5}`

### 62. Find elements exclusive to first set
**Description:** Elements present in first set but not in any others.
**Sample Input:** `set1 = {1, 2, 3, 4}, others = [{2, 3}, {3, 5}]`
**Sample Output:** `{1, 4}`

### 63. Group elements by set membership
**Description:** Categorize elements based on their presence in sets.
**Sample Input:** `set1 = {1, 2, 3}, set2 = {2, 3, 4}`
**Sample Output:** `only_in_set1: {1}, common: {2, 3}, only_in_set2: {4}`

### 64. Check if any set in list is empty
**Description:** Test for empty sets in a collection.
**Sample Input:** `sets = [{1, 2}, set(), {3, 4}]`
**Sample Output:** `True`

### 65. Find the largest set
**Description:** Determine which set has the most elements.
**Sample Input:** `sets = [{1}, {1, 2, 3}, {1, 2}]`
**Sample Output:** `{1, 2, 3}`

### 66. Find common file extensions
**Description:** Extract and find common file extensions across directories.
**Sample Input:** `dir1 = {'file1.txt', 'file2.pdf'}, dir2 = {'file3.txt', 'file4.jpg'}`
**Sample Output:** `{'.txt'}`

### 67. Filter valid email domains
**Description:** Keep only emails from approved domains.
**Sample Input:** `emails = {'user@gmail.com', 'admin@yahoo.com'}, valid_domains = {'gmail.com', 'outlook.com'}`
**Sample Output:** `{'user@gmail.com'}`

### 68. Find common blog post tags
**Description:** Identify tags that appear in multiple posts.
**Sample Input:** `post1_tags = {'python', 'coding', 'tutorial'}, post2_tags = {'python', 'programming', 'tutorial'}`
**Sample Output:** `{'python', 'tutorial'}`

### 69. Create user permission intersection
**Description:** Find common permissions across user roles.
**Sample Input:** `role1 = {'read', 'write'}, role2 = {'read', 'execute'}`
**Sample Output:** `{'read'}`

### 70. Check user permissions
**Description:** Verify if user has all required permissions.
**Sample Input:** `user_permissions = {'read', 'write', 'execute'}, required = {'read', 'write'}`
**Sample Output:** `True`

### 71. Find mutual friends
**Description:** Discover common friends between two users.
**Sample Input:** `user1_friends = {'Alice', 'Bob', 'Charlie'}, user2_friends = {'Bob', 'Charlie', 'David'}`
**Sample Output:** `{'Bob', 'Charlie'}`

### 72. Aggregate unique skills from job requirements
**Description:** Collect all unique skills needed across multiple jobs.
**Sample Input:** `job1 = {'Python', 'SQL'}, job2 = {'Python', 'JavaScript', 'SQL'}`
**Sample Output:** `{'Python', 'SQL', 'JavaScript'}`

### 73. Filter products by store availability
**Description:** Find products available in all specified stores.
**Sample Input:** `store1 = {'laptop', 'mouse'}, store2 = {'laptop', 'keyboard'}`
**Sample Output:** `available_everywhere = {'laptop'}`

### 74. Collect recipe ingredients
**Description:** Gather all unique ingredients needed for multiple recipes.
**Sample Input:** `recipe1 = {'flour', 'eggs', 'milk'}, recipe2 = {'flour', 'sugar'}`
**Sample Output:** `all_ingredients = {'flour', 'eggs', 'milk', 'sugar'}`

### 75. Implement voting system logic
**Description:** Track voting results and abstentions using set operations.
**Sample Input:** `votes_for = {'Alice', 'Bob'}, votes_against = {'Charlie'}, all_members = {'Alice', 'Bob', 'Charlie', 'David'}`
**Sample Output:** `abstained = {'David'}`

### 76. Detect course conflicts
**Description:** Check if student's enrolled courses have scheduling conflicts.
**Sample Input:** `enrolled = {'Math101', 'Physics101'}, conflicts = [{'Math101', 'Math102'}, {'Physics101', 'Chemistry101'}]`
**Sample Output:** `has_conflicts = False`

### 77. Find available courses
**Description:** Determine which courses have all prerequisites satisfied.
**Sample Input:** `completed = {'Math101', 'Physics101'}, course_prereqs = {'Math201': {'Math101'}, 'Physics201': {'Physics101', 'Math101'}}`
**Sample Output:** `available_courses = {'Math201', 'Physics201'}`

### 78. Content filtering system
**Description:** Calculate content relevance based on keyword matching.
**Sample Input:** `content_keywords = {'python', 'programming', 'tutorial'}, user_interests = {'python', 'data science'}`
**Sample Output:** `relevance_score = 1 (number of matching keywords)`

### 79. Feature selection for machine learning
**Description:** Select optimal features based on importance.
**Sample Input:** `available_features = {'age', 'income', 'education'}, important_features = {'age', 'income'}`
**Sample Output:** `selected_features = {'age', 'income'}`

### 80. Simple recommendation system
**Description:** Calculate user similarity using Jaccard similarity on preferences.
**Sample Input:** `user1_likes = {'movie1', 'movie2'}, user2_likes = {'movie2', 'movie3'}`
**Sample Output:** `similarity = 0.33 (Jaccard similarity: intersection/union)`

---

## 🔴 ADVANCED/TRICKY QUESTIONS (81-100)

### 81. Create frozenset as dictionary key
**Description:** Use immutable frozenset as a dictionary key for complex data structures.
**Sample Input:** `data = [1, 2, 3]`
**Sample Output:** `{frozenset({1, 2, 3}): 'some_value'}`

### 82. Nested set operations with frozenset
**Description:** Perform set operations on collections of frozensets.
**Sample Input:** `sets = [frozenset({1, 2}), frozenset({2, 3})]`
**Sample Output:** `intersection of all sets`

### 83. Generate power set
**Description:** Create all possible subsets of a given set.
**Sample Input:** `{1, 2, 3}`
**Sample Output:** `{frozenset(), frozenset({1}), frozenset({2}), frozenset({3}), frozenset({1,2}), frozenset({1,3}), frozenset({2,3}), frozenset({1,2,3})}`

### 84. Custom set class with logging
**Description:** Implement a set subclass that logs all operations.
**Sample Input:** `operations: add, remove, intersection`
**Sample Output:** `custom set with operation history`

### 85. Set cover problem
**Description:** Find minimum number of sets to cover all elements (NP-hard problem).
**Sample Input:** `universe = {1,2,3,4,5}, sets = [{1,2,3}, {2,4}, {3,4}, {4,5}]`
**Sample Output:** `minimum cover: [{1,2,3}, {4,5}]`

### 86. All possible intersections
**Description:** Find every possible intersection between sets in a collection.
**Sample Input:** `sets = [{1,2,3}, {2,3,4}, {3,4,5}]`
**Sample Output:** `all_intersections = [{2,3}, {3,4}, {3}, ...]`

### 87. Set-based graph operations
**Description:** Use sets to represent graphs and find connected components.
**Sample Input:** `edges = {(1,2), (2,3), (4,5)}, vertices = {1,2,3,4,5}`
**Sample Output:** `components = [{1,2,3}, {4,5}]`

### 88. Memory-efficient bitset
**Description:** Implement a set for large integer ranges using bit manipulation.
**Sample Input:** `large range of integers`
**Sample Output:** `bitset implementation`

### 89. Custom hashable objects in sets
**Description:** Create and use custom objects with proper `__hash__` and `__eq__` methods.
**Sample Input:** `custom objects with __hash__ and __eq__`
**Sample Output:** `set operations with custom objects`

### 90. Fuzzy set operations
**Description:** Implement sets with approximate membership degrees.
**Sample Input:** `elements with membership degrees`
**Sample Output:** `fuzzy union, intersection results`

### 91. Set representation conversion
**Description:** Convert between bitstrings, lists, and sets efficiently.
**Sample Input:** `bitstring = '101010', max_element = 6`
**Sample Output:** `set = {1, 3, 5}`

### 92. Maximum independent set
**Description:** Find largest set of vertices with no edges between them.
**Sample Input:** `graph adjacency represented as sets`
**Sample Output:** `maximum independent set`

### 93. Set-based caching with TTL
**Description:** Implement a cache using frozensets with time-based expiration.
**Sample Input:** `cache operations with expiration`
**Sample Output:** `cache with automatic cleanup`

### 94. Graph coloring problem
**Description:** Find minimum colors needed to color graph vertices.
**Sample Input:** `graph = {1: {2,3}, 2: {1,3}, 3: {1,2,4}, 4: {3}}`
**Sample Output:** `min_colors = 3`

### 95. Bloom filter implementation
**Description:** Create probabilistic set membership testing structure.
**Sample Input:** `elements to add and test`
**Sample Output:** `probabilistic membership results`

### 96. Handle None and empty set edge cases
**Description:** Properly handle sets containing None values and empty sets.
**Sample Input:** `set_with_none = {None, 1, 2}, empty_set = set()`
**Sample Output:** `proper handling of None values`

### 97. Mixed numeric types in sets
**Description:** Handle sets with int, float, and Decimal types correctly.
**Sample Input:** `mixed_set = {1, 1.0, Decimal('1.0')}`
**Sample Output:** `handle type coercion correctly`

### 98. Thread-safe set implementation
**Description:** Create a set that can be safely used in multithreaded environments.
**Sample Input:** `concurrent operations on shared set`
**Sample Output:** `thread-safe set operations`

### 99. Set partitioning algorithm
**Description:** Divide a set into subsets with equal sums (partition problem).
**Sample Input:** `numbers = {1, 2, 3, 4, 5, 6}`
**Sample Output:** `partitions = [{1, 2, 6}, {3, 4, 5}] or False if impossible`

### 100. Optimized large set intersection
**Description:** Efficiently find intersection of multiple large sets with memory optimization.
**Sample Input:** `multiple large sets with millions of elements`
**Sample Output:** `optimized intersection algorithm with memory management`

---

## 📝 Notes

- All questions focus exclusively on set operations and logic
- Questions progress from basic membership testing to advanced algorithmic challenges
- Real-world use cases are emphasized throughout (email filtering, user permissions, etc.)
- Edge cases and performance considerations are included in advanced questions
- Solutions should avoid external libraries and focus on Python's built-in set functionality

**Target Audience:** Python learners, interview candidates, and developers building coding portfolios.