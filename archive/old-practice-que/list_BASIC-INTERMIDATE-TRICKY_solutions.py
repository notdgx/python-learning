# Python List Solutions - 100 Problems

# ==================== BASIC LEVEL (1-40) ====================

# 1. Create and Display List
def create_display_list():
    """Create a list with numbers 1-5 and print it."""
    numbers = [1, 2, 3, 4, 5]
    print(numbers)
    return numbers

# 2. Access List Elements
def access_third_element(lst):
    """Access and return the third element (index 2)."""
    if len(lst) >= 3:
        return lst[2]
    return None

# 3. List Length
def get_list_length(lst):
    """Find the length of the list."""
    return len(lst)

# 4. Append Element
def append_element(lst, element):
    """Add element to the end of the list."""
    lst.append(element)
    return lst

# 5. Insert Element
def insert_element(lst, index, element):
    """Insert element at specified index."""
    lst.insert(index, element)
    return lst

# 6. Remove Element by Value
def remove_by_value(lst, value):
    """Remove first occurrence of value from list."""
    if value in lst:
        lst.remove(value)
    return lst

# 7. Remove Element by Index
def remove_by_index(lst, index):
    """Remove element at specified index."""
    if 0 <= index < len(lst):
        lst.pop(index)
    return lst

# 8. Check if Element Exists
def element_exists(lst, element):
    """Check if element exists in list."""
    return element in lst

# 9. Find Index of Element
def find_index(lst, element):
    """Find the index of element in list."""
    try:
        return lst.index(element)
    except ValueError:
        return -1

# 10. Count Occurrences
def count_occurrences(lst, element):
    """Count how many times element appears in list."""
    return lst.count(element)

# 11. Basic List Slicing
def slice_list(lst, start, end):
    """Extract elements from start to end index."""
    return lst[start:end+1]

# 12. Negative Indexing
def get_last_element(lst):
    """Get last element using negative indexing."""
    return lst[-1] if lst else None

# 13. Replace Element
def replace_element(lst, index, new_value):
    """Replace element at index with new value."""
    if 0 <= index < len(lst):
        lst[index] = new_value
    return lst

# 14. Extend List
def extend_list(lst1, lst2):
    """Extend first list with second list."""
    lst1.extend(lst2)
    return lst1

# 15. Clear List
def clear_list(lst):
    """Clear all elements from list."""
    lst.clear()
    return lst

# 16. Copy List
def copy_list(lst):
    """Create a copy of the list."""
    return lst.copy()

# 17. Concatenate Lists
def concatenate_lists(lst1, lst2):
    """Concatenate two lists using + operator."""
    return lst1 + lst2

# 18. Repeat List
def repeat_list(lst, times):
    """Repeat list specified number of times."""
    return lst * times

# 19. Check Empty List
def is_empty_list(lst):
    """Check if list is empty."""
    return len(lst) == 0

# 20. Minimum in List
def find_minimum(lst):
    """Find minimum value in list."""
    return min(lst) if lst else None

# 21. Maximum in List
def find_maximum(lst):
    """Find maximum value in list."""
    return max(lst) if lst else None

# 22. Sum of List Elements
def sum_list_elements(lst):
    """Calculate sum of all elements in list."""
    return sum(lst)

# 23. List of Squares
def create_squares_list(n):
    """Create list of squares from 1 to n."""
    return [i**2 for i in range(1, n+1)]

# 24. Even Numbers from List
def filter_even_numbers(lst):
    """Extract all even numbers from list."""
    return [num for num in lst if num % 2 == 0]

# 25. Odd Numbers from List
def filter_odd_numbers(lst):
    """Extract all odd numbers from list."""
    return [num for num in lst if num % 2 != 0]

# 26. List Iteration
def print_list_elements(lst):
    """Print each element on a new line."""
    for element in lst:
        print(element)

# 27. List of Strings Length
def get_string_lengths(lst):
    """Create list of string lengths."""
    return [len(s) for s in lst]

# 28. First and Last Elements
def get_first_last(lst):
    """Extract first and last elements."""
    if len(lst) >= 2:
        return [lst[0], lst[-1]]
    elif len(lst) == 1:
        return [lst[0], lst[0]]
    return []

# 29. Remove Last Element
def remove_last_element(lst):
    """Remove and return last element."""
    if lst:
        return lst.pop(), lst
    return None, lst

# 30. Reverse Slice
def reverse_slice(lst, start, end):
    """Get elements from end to start in reverse order."""
    return lst[start:end+1][::-1]

# 31. List Contains All
def all_even(lst):
    """Check if all elements are even."""
    return all(num % 2 == 0 for num in lst)

# 32. List Contains Any
def any_even(lst):
    """Check if any element is even."""
    return any(num % 2 == 0 for num in lst)

# 33. Replace Multiple Elements
def replace_all_occurrences(lst, old_value, new_value):
    """Replace all occurrences of old_value with new_value."""
    return [new_value if x == old_value else x for x in lst]

# 34. List Multiplication Table
def create_multiples(multiplier, limit):
    """Create list of multiples up to limit."""
    return [multiplier * i for i in range(1, (limit // multiplier) + 1)]

# 35. List Average
def calculate_average(lst):
    """Calculate average of list elements."""
    return sum(lst) / len(lst) if lst else 0

# 36. Convert to String List
def convert_to_strings(lst):
    """Convert all elements to strings."""
    return [str(x) for x in lst]

# 37. Convert String to List
def string_to_char_list(s):
    """Convert string to list of characters."""
    return list(s)

# 38. Join List Elements
def join_with_separator(lst, separator):
    """Join list elements with separator."""
    return separator.join(lst)

# 39. Split and Create List
def split_to_list(s, delimiter):
    """Split string by delimiter and create list."""
    return s.split(delimiter)

# 40. List Element Type Check
def all_integers(lst):
    """Check if all elements are integers."""
    return all(isinstance(x, int) for x in lst)

# ==================== INTERMEDIATE LEVEL (41-80) ====================

# 41. Sort List Ascending
def sort_ascending(lst):
    """Sort list in ascending order."""
    return sorted(lst)

# 42. Sort List Descending
def sort_descending(lst):
    """Sort list in descending order."""
    return sorted(lst, reverse=True)

# 43. Reverse List In-Place
def reverse_in_place(lst):
    """Reverse list in-place."""
    lst.reverse()
    return lst

# 44. List Comprehension - Squares
def squares_comprehension(n):
    """Create squares using list comprehension."""
    return [i**2 for i in range(1, n+1)]

# 45. List Comprehension with Condition
def even_squares(n):
    """Get squares of even numbers using list comprehension."""
    return [i**2 for i in range(1, n+1) if i % 2 == 0]

# 46. Nested List Access
def access_nested_element(matrix, row, col):
    """Access element from nested list."""
    return matrix[row][col]

# 47. Nested List Modification
def modify_nested_element(matrix, row, col, new_value):
    """Modify element in nested list."""
    matrix[row][col] = new_value
    return matrix

# 48. Remove Duplicates Simple
def remove_duplicates_simple(lst):
    """Remove duplicates (order doesn't matter)."""
    return list(set(lst))

# 49. Find Second Largest
def find_second_largest(lst):
    """Find second largest number."""
    unique_sorted = sorted(set(lst), reverse=True)
    return unique_sorted[1] if len(unique_sorted) >= 2 else None

# 50. List Intersection
def list_intersection(lst1, lst2):
    """Find common elements between two lists."""
    return list(set(lst1) & set(lst2))

# 51. List Union
def list_union(lst1, lst2):
    """Find union of two lists."""
    return list(set(lst1) | set(lst2))

# 52. List Difference
def list_difference(lst1, lst2):
    """Find elements in lst1 not in lst2."""
    return list(set(lst1) - set(lst2))

# 53. Rotate List Left
def rotate_left(lst, positions):
    """Rotate list left by positions."""
    if not lst:
        return lst
    positions = positions % len(lst)
    return lst[positions:] + lst[:positions]

# 54. Rotate List Right
def rotate_right(lst, positions):
    """Rotate list right by positions."""
    if not lst:
        return lst
    positions = positions % len(lst)
    return lst[-positions:] + lst[:-positions]

# 55. Chunk List
def chunk_list(lst, chunk_size):
    """Split list into chunks of specified size."""
    return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]

# 56. Filter List by Length
def filter_by_length(lst, min_length):
    """Filter strings by minimum length."""
    return [word for word in lst if len(word) > min_length]

# 57. List Comprehension with Multiple Conditions
def divisible_by_2_and_3(n):
    """Get numbers divisible by both 2 and 3."""
    return [i for i in range(1, n+1) if i % 2 == 0 and i % 3 == 0]

# 58. Enumerate List
def enumerate_list(lst):
    """Create list of tuples with index and value."""
    return list(enumerate(lst))

# 59. Zip Two Lists
def zip_lists(lst1, lst2):
    """Combine two lists into tuples."""
    return list(zip(lst1, lst2))

# 60. List of Dictionaries
def create_dict_list(keys, values_list):
    """Create list of dictionaries from keys and values."""
    return [dict(zip(keys, values)) for values in values_list]

# 61. Group Elements by Property
def group_by_first_letter(words):
    """Group words by their first letter."""
    groups = {}
    for word in words:
        first_letter = word[0].lower()
        if first_letter not in groups:
            groups[first_letter] = []
        groups[first_letter].append(word)
    return groups

# 62. Find All Indices
def find_all_indices(lst, target):
    """Find all indices where target appears."""
    return [i for i, x in enumerate(lst) if x == target]

# 63. Replace at Multiple Indices
def replace_at_indices(lst, indices, new_value):
    """Replace elements at specified indices."""
    result = lst.copy()
    for index in indices:
        if 0 <= index < len(result):
            result[index] = new_value
    return result

# 64. List Palindrome Check
def is_palindrome_list(lst):
    """Check if list is a palindrome."""
    return lst == lst[::-1]

# 65. Transpose 2D List
def transpose_matrix(matrix):
    """Transpose 2D list."""
    return list(zip(*matrix))

# 66. Merge Sorted Lists
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

# 67. Running Sum
def running_sum(lst):
    """Calculate running sum."""
    result = []
    total = 0
    for num in lst:
        total += num
        result.append(total)
    return result

# 68. Running Maximum
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

# 69. List Elements Frequency
def element_frequency(lst):
    """Count frequency of each element."""
    freq = {}
    for element in lst:
        freq[element] = freq.get(element, 0) + 1
    return freq

# 70. Remove Elements by Condition
def remove_greater_than(lst, threshold):
    """Remove elements greater than threshold."""
    return [x for x in lst if x <= threshold]

# 71. List Moving Average
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

# 72. Interleave Two Lists
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

# 73. List Partition
def partition_even_odd(lst):
    """Partition list into even and odd numbers."""
    even = [x for x in lst if x % 2 == 0]
    odd = [x for x in lst if x % 2 != 0]
    return even, odd

# 74. Find Missing Number
def find_missing_number(lst, n):
    """Find missing number in range 1 to n."""
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(lst)
    return expected_sum - actual_sum

# 75. List Binary Search
def binary_search(lst, target):
    """Binary search in sorted list."""
    left, right = 0, len(lst) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 76. Longest Increasing Subsequence Length
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

# 77. Remove by Multiple Values
def remove_multiple_values(lst, values_to_remove):
    """Remove all occurrences of multiple values."""
    return [x for x in lst if x not in values_to_remove]

# 78. List Sliding Window Maximum
def sliding_window_maximum(lst, window_size):
    """Find maximum in each sliding window."""
    if len(lst) < window_size:
        return []
    
    result = []
    for i in range(len(lst) - window_size + 1):
        window = lst[i:i + window_size]
        result.append(max(window))
    return result

# 79. Compare Lists Element-wise
def compare_lists_elementwise(lst1, lst2):
    """Compare two lists element by element."""
    min_len = min(len(lst1), len(lst2))
    return [lst1[i] == lst2[i] for i in range(min_len)]

# 80. List Permutation Check
def is_permutation(lst1, lst2):
    """Check if one list is permutation of another."""
    return sorted(lst1) == sorted(lst2)

# ==================== ADVANCED/TRICKY LEVEL (81-100) ====================

# 81. Flatten Nested List
def flatten_list(nested_list):
    """Flatten one level of nesting."""
    return [item for sublist in nested_list for item in sublist]

# 82. Deep Flatten Nested List
def deep_flatten(lst):
    """Recursively flatten deeply nested list."""
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(deep_flatten(item))
        else:
            result.append(item)
    return result

# 83. Remove Duplicates Preserve Order
def remove_duplicates_preserve_order(lst):
    """Remove duplicates while preserving order."""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# 84. Cartesian Product of Lists
def cartesian_product(lst1, lst2):
    """Generate cartesian product of two lists."""
    return [(x, y) for x in lst1 for y in lst2]

# 85. List Combinations
def generate_combinations(lst, r):
    """Generate all combinations of length r."""
    from itertools import combinations
    return list(combinations(lst, r))

# 86. List Permutations
def generate_permutations(lst):
    """Generate all permutations of list."""
    from itertools import permutations
    return list(permutations(lst))

# 87. Multi-condition Filter
def multi_condition_filter(start, end):
    """Filter with complex conditions."""
    return [x for x in range(start, end) 
            if (x % 2 == 0 or x % 3 == 0) and x > 5]

# 88. Nested List Comprehension Matrix
def create_multiplication_matrix(n):
    """Create nxn matrix where element is i*j."""
    return [[i * j for j in range(n)] for i in range(n)]

# 89. List Memory Optimization
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

# 90. Zip Multiple Lists Unequal Length
def zip_unequal_lists(*lists):
    """Zip multiple lists of different lengths."""
    return list(zip(*lists))

# 91. List Spiral Order
def spiral_order(matrix):
    """Traverse 2D list in spiral order."""
    if not matrix or not matrix[0]:
        return []
    
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # Go right
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1
        
        # Go down
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        
        # Go left
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
        
        # Go up
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1
    
    return result

# 92. Custom Sort with Multiple Criteria
def custom_sort_tuples(lst):
    """Sort tuples by second element desc, then first asc."""
    return sorted(lst, key=lambda x: (-x[1], x[0]))

# 93. List Pattern Matching
def find_local_maxima_sublists(lst, window_size=3):
    """Find sublists where middle element is maximum."""
    result = []
    for i in range(len(lst) - window_size + 1):
        window = lst[i:i + window_size]
        middle_idx = window_size // 2
        if window[middle_idx] == max(window):
            result.append(window)
    return result

# 94. Merge Overlapping Intervals
def merge_intervals(intervals):
    """Merge overlapping intervals."""
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        if current[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], current[1])
        else:
            merged.append(current)
    
    return merged

# 95. List Edit Distance
def edit_distance(lst1, lst2):
    """Calculate minimum edit distance between two lists."""
    m, n = len(lst1), len(lst2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if lst1[i-1] == lst2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j],    # deletion
                                   dp[i][j-1],    # insertion
                                   dp[i-1][j-1])  # substitution
    
    return dp[m][n]

# 96. Generate Pascal's Triangle
def generate_pascals_triangle(n):
    """Generate first n rows of Pascal's triangle."""
    triangle = []
    
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    
    return triangle

# 97. List Cycle Detection
def has_cycle_simulation(lst):
    """Simulate cycle detection in list."""
    # This simulates cycle detection where each value points to next index
    visited = set()
    current = 0
    
    while current < len(lst) and current not in visited:
        visited.add(current)
        current = lst[current]
        
        # Check bounds to avoid infinite loops
        if current >= len(lst) or current < 0:
            return False
    
    return current < len(lst)

# 98. Maximum Subarray Sum (Kadane's Algorithm)
def max_subarray_sum(lst):
    """Find maximum sum of contiguous subarray."""
    if not lst:
        return 0
    
    max_sum = current_sum = lst[0]
    
    for num in lst[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# 99. List Anagram Groups
def group_anagrams(strs):
    """Group strings that are anagrams of each other."""
    anagram_groups = {}
    
    for s in strs:
        # Sort characters to create key
        key = ''.join(sorted(s))
        if key not in anagram_groups:
            anagram_groups[key] = []
        anagram_groups[key].append(s)
    
    return list(anagram_groups.values())

# 100. Multi-dimensional List Search
def search_2d_matrix(matrix, target):
    """Search target in row-wise and column-wise sorted matrix."""
    if not matrix or not matrix[0]:
        return False
    
    row, col = 0, len(matrix[0]) - 1
    
    while row < len(matrix) and col >= 0:
        current = matrix[row][col]
        if current == target:
            return True
        elif current > target:
            col -= 1
        else:
            row += 1
    
    return False

# ==================== TEST FUNCTIONS ====================

def run_basic_tests():
    """Run tests for basic level questions."""
    print("=== BASIC LEVEL TESTS ===")
    
    # Test a few basic functions
    print("1. Create list:", create_display_list())
    print("2. Third element:", access_third_element([10, 20, 30, 40, 50]))
    print("3. List length:", get_list_length(['apple', 'banana', 'cherry', 'date']))
    print("4. Even numbers:", filter_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print("5. List average:", calculate_average([10, 20, 30, 40, 50]))

def run_intermediate_tests():
    """Run tests for intermediate level questions."""
    print("\n=== INTERMEDIATE LEVEL TESTS ===")
    
    print("41. Sort ascending:", sort_ascending([64, 34, 25, 12, 22, 11, 90]))
    print("50. List intersection:", list_intersection([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]))
    print("67. Running sum:", running_sum([1, 2, 3, 4, 5]))
    print("75. Binary search:", binary_search([1, 3, 5, 7, 9, 11], 7))

def run_advanced_tests():
    """Run tests for advanced level questions."""
    print("\n=== ADVANCED LEVEL TESTS ===")
    
    print("81. Flatten list:", flatten_list([[1, 2], [3, 4, 5], [6]]))
    print("83. Remove duplicates preserve order:", 
          remove_duplicates_preserve_order([3, 1, 4, 1, 5, 9, 2, 6, 5]))
    print("98. Max subarray sum:", max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))
    print("99. Group anagrams:", group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))

if __name__ == "__main__":
    run_basic_tests()
    run_intermediate_tests() 
    run_advanced_tests()
    print("\n🎉 All 100 Python List questions implemented!")