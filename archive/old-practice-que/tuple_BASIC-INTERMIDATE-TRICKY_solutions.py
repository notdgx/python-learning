# Python Tuple Solutions
# 100 coding question solutions for tuple operations

# 1. Create Tuple Length
def tuple_length():
    t = (1, 2, 3, 4, 5)
    return len(t)

# 2. Access Third Element
def access_third_element():
    t = (10, 20, 30, 40, 50)
    return t[2]

# 3. Single Element Tuple
def single_element_tuple():
    return (42,)

# 4. Element Existence Check
def element_exists():
    t = (15, 25, 35, 45)
    return 25 in t

# 5. Tuple Concatenation
def concatenate_tuples():
    t1 = (1, 2)
    t2 = (3, 4)
    return t1 + t2

# 6. Tuple Repetition
def repeat_tuple():
    t = ('a', 'b')
    return t * 3

# 7. Basic Slicing
def slice_tuple():
    t = (1, 2, 3, 4, 5, 6)
    return t[2:5]

# 8. Negative Indexing
def last_element():
    t = ('apple', 'banana', 'cherry')
    return t[-1]

# 9. List to Tuple Conversion
def list_to_tuple():
    lst = [1, 2, 3]
    return tuple(lst)

# 10. Basic Unpacking
def unpack_tuple():
    t = (100, 200, 300)
    a, b, c = t
    return a, b, c

==================================================

# 11. Empty Tuple Creation
def empty_tuple():
    return ()

# 12. Maximum Element
def max_element():
    t = (45, 12, 78, 23, 56)
    return max(t)

# 13. Minimum Element
def min_element():
    t = (45, 12, 78, 23, 56)
    return min(t)

# 14. Sum Calculation
def sum_elements():
    t = (1, 2, 3, 4, 5)
    return sum(t)

# 15. Tuple to List Conversion
def tuple_to_list():
    t = (1, 2, 3)
    return list(t)

# 16. First Two Elements
def first_two():
    t = (10, 20, 30, 40)
    return t[:2]

# 17. Every Second Element
def every_second():
    t = (1, 2, 3, 4, 5, 6)
    return t[::2]

# 18. Reverse Tuple
def reverse_tuple():
    t = (1, 2, 3, 4, 5)
    return t[::-1]

# 19. Tuple Equality
def tuple_equality():
    t1 = (1, 2, 3)
    t2 = (1, 2, 3)
    return t1 == t2

# 20. Mixed Data Types
def mixed_tuple():
    return (10, 'hello', 3.14)

==================================================

# 21. Second-to-Last Element
def second_to_last():
    t = (10, 20, 30, 40, 50)
    return t[-2]

# 22. String to Tuple
def string_to_tuple():
    s = 'python'
    return tuple(s)

# 23. Empty Tuple Check
def is_empty():
    t = ()
    return len(t) == 0

# 24. Lexicographic Comparison
def compare_tuples():
    t1 = (1, 2)
    t2 = (1, 3)
    return t1 < t2

# 25. Duplicate Elements
def create_duplicates():
    return (1, 2, 2, 3, 3, 3)

# 26. Middle Element Access
def middle_element():
    t = (1, 2, 3, 4, 5)
    return t[len(t)//2]

# 27. Nested Tuple Length
def nested_length():
    t = ((1, 2), (3, 4))
    return len(t)

# 28. Range to Tuple
def range_to_tuple():
    return tuple(range(1, 6))

# 29. All Except First
def all_except_first():
    t = (10, 20, 30, 40, 50)
    return t[1:]

# 30. All Except Last
def all_except_last():
    t = (10, 20, 30, 40, 50)
    return t[:-1]

==================================================

# 31. Product of Elements
def product_elements():
    t = (2, 3, 4)
    result = 1
    for x in t:
        result *= x
    return result

# 32. Type Checking
def all_integers():
    t = (1, 2, 3)
    return all(isinstance(x, int) for x in t)

# 33. Squares Tuple
def squares_tuple():
    numbers = [1, 2, 3, 4]
    return tuple(x**2 for x in numbers)

# 34. Even Indices
def even_indices():
    t = (10, 20, 30, 40, 50)
    return t[::2]

# 35. String Join
def join_elements():
    t = ('a', 'b', 'c')
    return ''.join(t)

# 36. None Value Check
def has_none():
    t = (1, None, 3)
    return None in t

# 37. Boolean Tuple
def boolean_tuple():
    values = [True, False, True]
    return tuple(values)

# 38. Element Type
def element_type():
    t = (1, 'hello', 3.14)
    return type(t[0])

# 39. Character Tuple
def character_tuple():
    s = 'ABC'
    return tuple(s)

# 40. Conceptual Swap
def swap_ends():
    t = (1, 2, 3, 4, 5)
    return (t[-1],) + t[1:-1] + (t[0],)

==================================================

# 41. Count Method
def count_occurrences():
    t = (1, 2, 3, 3, 3, 4)
    return t.count(3)

# 42. Index Method
def find_index():
    t = ('banana', 'apple', 'cherry', 'apple')
    return t.index('apple')

# 43. Zip Combination
def zip_tuples():
    t1 = (1, 2, 3)
    t2 = ('a', 'b', 'c')
    return list(zip(t1, t2))

# 44. Enumerate Usage
def enumerate_tuple():
    t = ('x', 'y', 'z')
    return list(enumerate(t))

# 45. Sort Integers
def sort_integers():
    t = (5, 2, 8, 1, 9)
    return tuple(sorted(t))

# 46. Sort Strings
def sort_strings():
    t = ('banana', 'apple', 'cherry')
    return tuple(sorted(t))

# 47. All Indices
def all_indices():
    t = (1, 2, 3, 2, 4, 2)
    return [i for i, x in enumerate(t) if x == 2]

# 48. Unique Elements
def unique_elements():
    t = (1, 2, 2, 3, 3, 3, 4)
    return tuple(dict.fromkeys(t))

# 49. Filter Even Numbers
def filter_even():
    t = (1, 2, 3, 4, 5, 6, 7, 8)
    return tuple(x for x in t if x % 2 == 0)

# 50. Dictionary Keys
def tuple_as_keys():
    coords = [(0, 0), (1, 1), (2, 2)]
    return {coord: f'point{i}' if i else 'origin' for i, coord in enumerate(coords)}

==================================================

# 51. Tuple Iteration
def iterate_tuple():
    t = ('a', 'b', 'c')
    result = []
    for item in t:
        result.append(item)
    return '\n'.join(result)

# 52. Star Unpacking
def star_unpacking():
    t = (1, 2, 3, 4, 5)
    first, *rest = t
    return first, rest

# 53. Most Frequent Element
def most_frequent():
    t = (1, 2, 3, 2, 2, 4, 5)
    return max(set(t), key=t.count)

# 54. Zip Lists to Tuples
def zip_lists():
    names = ['Alice', 'Bob']
    ages = [25, 30]
    return list(zip(names, ages))

# 55. Flatten Nested Tuples
def flatten_tuples():
    t = ((1, 2), (3, 4), (5, 6))
    result = []
    for subtuple in t:
        result.extend(subtuple)
    return tuple(result)

# 56. Duplicate Detection
def find_duplicates():
    t = (1, 2, 3, 2, 4, 3, 5)
    seen = set()
    duplicates = set()
    for x in t:
        if x in seen:
            duplicates.add(x)
        seen.add(x)
    return tuple(duplicates)

# 57. Generator to Tuple
def generator_squares():
    numbers = [1, 2, 3, 4]
    return tuple(x**2 for x in numbers)

# 58. Consecutive Pairs
def consecutive_pairs():
    t = (1, 2, 3, 4, 5, 6)
    return [(t[i], t[i+1]) for i in range(0, len(t), 2)]

# 59. Tuple Intersection
def tuple_intersection():
    t1 = (1, 2, 3, 4)
    t2 = (3, 4, 5, 6)
    return tuple(x for x in t1 if x in t2)

# 60. Dictionary Keys to Tuple
def dict_keys_to_tuple():
    d = {'a': 1, 'b': 2, 'c': 3}
    return tuple(d.keys())

==================================================

# 61. Dictionary Values to Tuple
def dict_values_to_tuple():
    d = {'a': 1, 'b': 2, 'c': 3}
    return tuple(d.values())

# 62. Zip to Dictionary
def zip_to_dict():
    keys = ('name', 'age')
    values = ('John', 25)
    return dict(zip(keys, values))

# 63. Average Calculation
def calculate_average():
    t = (10, 20, 30, 40, 50)
    return sum(t) / len(t)

# 64. Second Largest
def second_largest():
    t = (5, 2, 8, 1, 9, 3)
    sorted_t = sorted(set(t), reverse=True)
    return sorted_t[1]

# 65. Element Replacement
def replace_elements():
    t = (1, 2, 3, 2, 4)
    old, new = 2, 9
    return tuple(new if x == old else x for x in t)

# 66. Cumulative Sums
def cumulative_sums():
    t = (1, 2, 3, 4, 5)
    result = []
    cumsum = 0
    for x in t:
        cumsum += x
        result.append(cumsum)
    return tuple(result)

# 67. Sorted Check
def is_sorted():
    t = (1, 2, 3, 4, 5)
    return t == tuple(sorted(t))

# 68. Left Rotation
def rotate_left():
    t = (1, 2, 3, 4, 5)
    n = 2
    return t[n:] + t[:n]

# 69. Filter with Condition
def filter_condition():
    t = (1, 2, 3, 4, 5, 6)
    return tuple(x for x in t if x > 3)

# 70. String to Integer Conversion
def convert_to_int():
    t = ('1', '2', '3', '4')
    return tuple(int(x) for x in t)

==================================================

# 71. Enumerate with Start
def enumerate_start():
    t = ('a', 'b', 'c')
    return list(enumerate(t, start=1))

# 72. Alternating Elements
def alternating_elements():
    t1 = (1, 3, 5)
    t2 = (2, 4, 6)
    result = []
    for i in range(len(t1)):
        result.extend([t1[i], t2[i]])
    return tuple(result)

# 73. Missing Number
def find_missing():
    t = (1, 2, 4, 5, 6)
    full_set = set(range(min(t), max(t) + 1))
    return list(full_set - set(t))[0]

# 74. Uniqueness Check
def all_unique():
    t = (1, 2, 3, 4, 5)
    return len(t) == len(set(t))

# 75. Multiple Tuple Merge
def merge_tuples():
    tuples = [(1, 2), (3, 4), (5, 6)]
    result = []
    for t in tuples:
        result.extend(t)
    return tuple(result)

# 76. Consecutive Differences
def consecutive_differences():
    t = (10, 15, 12, 20, 25)
    return tuple(t[i+1] - t[i] for i in range(len(t)-1))

# 77. Map Function Application
def map_function():
    t = (1, 2, 3, 4)
    return tuple(map(lambda x: x**2, t))

# 78. Longest String
def longest_string():
    t = ('cat', 'elephant', 'dog', 'butterfly')
    return max(t, key=len)

# 79. Tuple Partitioning
def partition_tuple():
    t = (1, 2, 3, 4, 5, 6)
    evens = tuple(x for x in t if x % 2 == 0)
    odds = tuple(x for x in t if x % 2 != 0)
    return evens, odds

# 80. Sliding Window
def sliding_window():
    t = (1, 2, 3, 4, 5)
    return [(t[i], t[i+1]) for i in range(len(t)-1)]

==================================================

# 81. Deep Nested Access
def deep_nested_access():
    t = (((1, 2), (3, 4)), ((5, 6), (7, 8)))
    return t[1][0][1]  # Access element 6

# 82. Nested Unpacking
def nested_unpacking():
    t = ((1, 2), (3, (4, 5)))
    (a, b), (c, (d, e)) = t
    return a, b, c, d, e

# 83. Complex Dictionary Keys
def complex_dict_keys():
    data = [((1, 2), 'A'), ((2, 3), 'B')]
    return dict(data)

# 84. Mutable Contents
def modify_mutable_contents():
    t = (1, [2, 3], 4)
    t[1].append(5)  # Modifies the list inside tuple
    return t

# 85. Recursive Flattening
def flatten_recursive(t):
    result = []
    for item in t:
        if isinstance(item, tuple):
            result.extend(flatten_recursive(item))
        else:
            result.append(item)
    return tuple(result)

def recursive_flatten():
    t = (1, (2, (3, 4)), 5)
    return flatten_recursive(t)

# 86. Function Parameter Unpacking
def distance(p1, p2):
    (x1, y1), (x2, y2) = p1, p2
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def parameter_unpacking():
    points = [(1, 2), (3, 4)]
    return distance(points[0], points[1])

# 87. Matrix Operations
def matrix_column():
    matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    col_index = 1
    return tuple(row[col_index] for row in matrix)

# 88. LRU Cache Keys
class TupleLRUCache:
    def __init__(self, maxsize):
        self.cache = {}
        self.maxsize = maxsize
        
    def get_key(self, func_name, args):
        return (func_name, args)
    
    def get(self, func_name, args):
        key = self.get_key(func_name, args)
        return self.cache.get(key)

# 89. Custom Tuple Comparison
def custom_sort():
    tuples = [(2, 1), (1, 3), (1, 2)]
    return sorted(tuples, key=lambda x: sum(x))

# 90. Multiple Assignment Loop
def multiple_assignment_loop():
    pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
    result = []
    for num, letter in pairs:
        result.append(f'{num}: {letter}')
    return result

==================================================

# 91. State Machine
class TupleStateMachine:
    def __init__(self, transitions):
        self.transitions = dict(transitions)
        
    def next_state(self, current_state, input_val):
        return self.transitions.get((current_state, input_val))

# 92. Combination Generator
def tuple_combinations():
    from itertools import combinations
    t = (1, 2, 3)
    return list(combinations(t, 2))

# 93. Args Unpacking
def func(*args):
    return sum(args)

def args_unpacking():
    t = (1, 2, 3, 4)
    return func(*t)

# 94. Coordinate Transformations
def rotate_90(points):
    return [(-y, x) for x, y in points]

def coordinate_transform():
    points = [(0, 0), (1, 1), (2, 2)]
    return rotate_90(points)

# 95. Graph Representation
def build_adjacency():
    edges = [(1, 2), (2, 3), (3, 4)]
    adj = {}
    for a, b in edges:
        if a not in adj:
            adj[a] = []
        if b not in adj:
            adj[b] = []
        adj[a].append(b)
        adj[b].append(a)
    return adj

# 96. Memoization
def fibonacci_memo():
    cache = {}
    
    def fib(n):
        key = ('fib', n)
        if key in cache:
            return cache[key]
        if n <= 1:
            result = n
        else:
            result = fib(n-1) + fib(n-2)
        cache[key] = result
        return result
    
    return fib(10)

# 97. Priority Queue
def priority_sort():
    items = [(3, 'task1'), (1, 'task2'), (2, 'task3')]
    return sorted(items, key=lambda x: x[0])

# 98. Configuration System
class TupleConfig:
    def __init__(self, config):
        self.config = config
        
    def get(self, section, key):
        return dict(dict(self.config)[section])[key]

# 99. Exception Unpacking
def operation_that_returns_tuple():
    try:
        result = 10 / 2
        return result, None
    except Exception as e:
        return None, str(e)

def exception_unpacking():
    result, error = operation_that_returns_tuple()
    if error:
        return f'Error: {error}'
    return f'Result: {result}'

# 100. Pattern Matching
def pattern_matcher():
    patterns = [(int, lambda x: f'Integer: {x}'),
                (str, lambda x: f'String: {x}'),
                (list, lambda x: f'List with {len(x)} items')]
    
    def match(value):
        for pattern_type, handler in patterns:
            if isinstance(value, pattern_type):
                return handler(value)
        return 'No match found'
    
    return match(42)

==================================================

# Test functions (uncomment to run individual tests)
"""
# Basic tests
print("1:", tuple_length())  # 5
print("2:", access_third_element())  # 30
print("3:", single_element_tuple())  # (42,)

# Intermediate tests  
print("41:", count_occurrences())  # 3
print("42:", find_index())  # 1
print("43:", zip_tuples())  # [(1, 'a'), (2, 'b'), (3, 'c')]

# Advanced tests
print("81:", deep_nested_access())  # 6
print("82:", nested_unpacking())  # (1, 2, 3, 4, 5)
print("85:", recursive_flatten())  # (1, 2, 3, 4, 5)
"""