"""100 Python Set Coding Questions - Solutions

This file contains clean Python solutions for all 100 set-related coding questions.
Each solution is numbered to match the corresponding question in set_questions.md

Author: Generated for Python learners and coding interview preparation
Focus: Set operations, logic, and real-world applications
"""

# 1. Create a set from a list and remove duplicates
def remove_duplicates(lst):
    return set(lst)

# Test
my_list = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates(my_list)
print(f"Input: {my_list}")
print(f"Output: {result}")

# 2. Check if an element exists in a set
def element_exists(my_set, element):
    return element in my_set

# Test
my_set = {1, 2, 3}
element = 2
result = element_exists(my_set, element)
print(f"Set: {my_set}, Element: {element}")
print(f"Exists: {result}")

# 3. Add a single element to a set
def add_element(my_set, element):
    my_set_copy = my_set.copy()
    my_set_copy.add(element)
    return my_set_copy

# Test
my_set = {1, 2, 3}
element = 4
result = add_element(my_set, element)
print(f"Original: {my_set}")
print(f"After adding {element}: {result}")

# 4. Remove an element from a set using remove()
def remove_element(my_set, element):
    my_set_copy = my_set.copy()
    my_set_copy.remove(element)  # Raises KeyError if not found
    return my_set_copy

# Test
my_set = {1, 2, 3}
element = 2
result = remove_element(my_set, element)
print(f"Original: {my_set}")
print(f"After removing {element}: {result}")

# 5. Remove an element from a set using discard()
def discard_element(my_set, element):
    my_set_copy = my_set.copy()
    my_set_copy.discard(element)  # No error if element not found
    return my_set_copy

# Test
my_set = {1, 2, 3}
element = 5
result = discard_element(my_set, element)
print(f"Original: {my_set}")
print(f"After discarding {element}: {result}")

# 6. Get the length of a set
def get_set_length(my_set):
    return len(my_set)

# Test
my_set = {1, 2, 3, 4, 5}
result = get_set_length(my_set)
print(f"Set: {my_set}")
print(f"Length: {result}")

# 7. Check if a set is empty
def is_empty_set(my_set):
    return len(my_set) == 0
    # Alternative: return not my_set

# Test
empty_set = set()
non_empty_set = {1, 2, 3}
print(f"Empty set {empty_set} is empty: {is_empty_set(empty_set)}")
print(f"Non-empty set {non_empty_set} is empty: {is_empty_set(non_empty_set)}")

# 8. Create an empty set
def create_empty_set():
    return set()

# Test
result = create_empty_set()
print(f"Empty set: {result}")
print(f"Type: {type(result)}")

# 9. Convert a string to a set of characters
def string_to_char_set(s):
    return set(s)

# Test
text = "hello"
result = string_to_char_set(text)
print(f"String: '{text}'")
print(f"Character set: {result}")

# 10. Check if an element is NOT in a set
def element_not_in_set(my_set, element):
    return element not in my_set

# Test
my_set = {1, 2, 3}
element = 5
result = element_not_in_set(my_set, element)
print(f"Set: {my_set}, Element: {element}")
print(f"Element NOT in set: {result}")

# 11. Clear all elements from a set
def clear_set(my_set):
    cleared_set = my_set.copy()
    cleared_set.clear()
    return cleared_set

# Test
my_set = {1, 2, 3}
result = clear_set(my_set)
print(f"Original: {my_set}")
print(f"After clearing: {result}")

# 12. Create a set from tuple elements
def tuple_to_set(tpl):
    return set(tpl)

# Test
my_tuple = (1, 2, 3, 2, 4)
result = tuple_to_set(my_tuple)
print(f"Tuple: {my_tuple}")
print(f"Set: {result}")

# 13. Pop a random element from a set
def pop_element(my_set):
    my_set_copy = my_set.copy()
    if my_set_copy:
        popped = my_set_copy.pop()
        return popped, my_set_copy
    return None, my_set_copy

# Test
my_set = {1, 2, 3}
popped, remaining = pop_element(my_set)
print(f"Original: {my_set}")
print(f"Popped: {popped}")
print(f"Remaining: {remaining}")

# 14. Create a set with mixed data types
def create_mixed_set(data_list):
    return set(data_list)

# Test
mixed_data = [1, 'hello', 3.14, True]
result = create_mixed_set(mixed_data)
print(f"Input: {mixed_data}")
print(f"Mixed set: {result}")

# 15. Find unique words in a sentence
def unique_words(sentence):
    words = sentence.lower().split()
    return set(words)

# Test
sentence = "the cat sat on the mat"
result = unique_words(sentence)
print(f"Sentence: '{sentence}'")
print(f"Unique words: {result}")

# 16. Check if two sets have the same length
def same_length(set1, set2):
    return len(set1) == len(set2)

# Test
set1 = {1, 2, 3}
set2 = {4, 5, 6}
result = same_length(set1, set2)
print(f"Set1: {set1} (length: {len(set1)})")
print(f"Set2: {set2} (length: {len(set2)})")
print(f"Same length: {result}")

# 17. Create a set from the first n natural numbers
def first_n_naturals(n):
    return set(range(1, n + 1))

# Test
n = 5
result = first_n_naturals(n)
print(f"First {n} natural numbers: {result}")

# 18. Remove duplicates from a list of email addresses
def deduplicate_emails(email_list):
    return set(email_list)

# Test
emails = ['user@email.com', 'admin@email.com', 'user@email.com']
result = deduplicate_emails(emails)
print(f"Original emails: {emails}")
print(f"Unique emails: {result}")

# 19. Create a set of even numbers from 1 to 10
def even_numbers_1_to_10():
    return {x for x in range(1, 11) if x % 2 == 0}

# Test
result = even_numbers_1_to_10()
print(f"Even numbers from 1 to 10: {result}")

# 20. Check if a set contains only positive numbers
def all_positive(my_set):
    return all(x > 0 for x in my_set if isinstance(x, (int, float)))

# Test
positive_set = {1, 2, 3, 4}
mixed_set = {1, -2, 3, 4}
print(f"Set {positive_set} all positive: {all_positive(positive_set)}")
print(f"Set {mixed_set} all positive: {all_positive(mixed_set)}")

# 21. Create a set of vowels
def create_vowel_set():
    return {'a', 'e', 'i', 'o', 'u'}

# Test
result = create_vowel_set()
print(f"Vowels: {result}")

# 22. Find unique characters in two strings combined
def unique_chars_combined(str1, str2):
    return set(str1 + str2)

# Test
str1 = 'hello'
str2 = 'world'
result = unique_chars_combined(str1, str2)
print(f"String 1: '{str1}'")
print(f"String 2: '{str2}'")
print(f"Unique characters: {result}")

# 23. Create a set of squares from 1 to 5
def squares_1_to_5():
    return {x**2 for x in range(1, 6)}

# Test
result = squares_1_to_5()
print(f"Squares from 1 to 5: {result}")

# 24. Check if a string contains duplicate characters
def has_duplicate_chars(s):
    return len(s) != len(set(s))

# Test
test_strings = ["hello", "world", "python"]
for s in test_strings:
    result = has_duplicate_chars(s)
    print(f"'{s}' has duplicates: {result}")

# 25. Create a set from dictionary keys
def dict_keys_to_set(dictionary):
    return set(dictionary.keys())

# Test
my_dict = {'a': 1, 'b': 2, 'c': 3}
result = dict_keys_to_set(my_dict)
print(f"Dictionary: {my_dict}")
print(f"Keys as set: {result}")

# 26. Remove all vowels from a set of characters
def remove_vowels(char_set):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    return char_set - vowels

# Test
chars = {'a', 'b', 'c', 'e', 'f'}
result = remove_vowels(chars)
print(f"Original: {chars}")
print(f"Without vowels: {result}")

# 27. Check if a set is a singleton (contains exactly one element)
def is_singleton(my_set):
    return len(my_set) == 1

# Test
singleton_set = {42}
multi_set = {1, 2, 3}
empty_set = set()
print(f"Set {singleton_set} is singleton: {is_singleton(singleton_set)}")
print(f"Set {multi_set} is singleton: {is_singleton(multi_set)}")
print(f"Set {empty_set} is singleton: {is_singleton(empty_set)}")

# 28. Create a set of file extensions from filenames
def get_file_extensions(filenames):
    extensions = set()
    for filename in filenames:
        if '.' in filename:
            ext = '.' + filename.split('.')[-1]
            extensions.add(ext)
    return extensions

# Test
files = ['file1.txt', 'file2.pdf', 'file3.txt', 'file4.jpg']
result = get_file_extensions(files)
print(f"Files: {files}")
print(f"Extensions: {result}")

# 29. Find common characters between your name and 'python'
def common_chars_with_python(name):
    python_chars = set('python')
    name_chars = set(name.lower())
    return python_chars & name_chars

# Test
name = 'john'
result = common_chars_with_python(name)
print(f"Name: '{name}'")
print(f"Common chars with 'python': {result}")

# 30. Create a set of prime numbers less than 20
def primes_less_than_20():
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return {n for n in range(2, 20) if is_prime(n)}

# Test
result = primes_less_than_20()
print(f"Prime numbers less than 20: {result}")

# 31. Update a set by adding multiple elements at once
def update_set_multiple(my_set, elements):
    updated_set = my_set.copy()
    updated_set.update(elements)
    return updated_set

# Test
my_set = {1, 2}
elements = [3, 4, 5]
result = update_set_multiple(my_set, elements)
print(f"Original: {my_set}")
print(f"Elements to add: {elements}")
print(f"Updated: {result}")

# 32. Create a copy of a set
def copy_set(original):
    return original.copy()

# Test
original = {1, 2, 3}
copied = copy_set(original)
print(f"Original: {original}")
print(f"Copy: {copied}")
print(f"Same object: {original is copied}")
print(f"Equal content: {original == copied}")

# 33. Check if all elements in a list are unique
def all_unique(lst):
    return len(lst) == len(set(lst))

# Test
unique_list = [1, 2, 3, 4, 5]
duplicate_list = [1, 2, 2, 3, 4]
print(f"List {unique_list} all unique: {all_unique(unique_list)}")
print(f"List {duplicate_list} all unique: {all_unique(duplicate_list)}")

# 34. Remove specific elements from a set based on condition
def filter_set(my_set, condition):
    return {x for x in my_set if not condition(x)}

# Test
my_set = {1, 2, 3, 4, 5}
# Remove even numbers
result = filter_set(my_set, lambda x: x % 2 == 0)
print(f"Original: {my_set}")
print(f"After removing evens: {result}")

# 35. Create a set of unique lengths from strings
def unique_string_lengths(strings):
    return {len(s) for s in strings}

# Test
strings = ['cat', 'dog', 'elephant', 'fox']
result = unique_string_lengths(strings)
print(f"Strings: {strings}")
print(f"Unique lengths: {result}")

# 36. Check if a set contains any negative numbers
def has_negative_numbers(my_set):
    return any(x < 0 for x in my_set if isinstance(x, (int, float)))

# Test
positive_set = {1, 2, 3, 4}
mixed_set = {1, -2, 3, 4}
print(f"Set {positive_set} has negatives: {has_negative_numbers(positive_set)}")
print(f"Set {mixed_set} has negatives: {has_negative_numbers(mixed_set)}")

# 37. Create a set from the digits of a number
def digits_to_set(number):
    return set(str(abs(number)))

# Test
number = 12321
result = digits_to_set(number)
print(f"Number: {number}")
print(f"Unique digits: {result}")

# 38. Find maximum and minimum values in a set
def find_min_max(my_set):
    if not my_set:
        return None, None
    numeric_values = [x for x in my_set if isinstance(x, (int, float))]
    if not numeric_values:
        return None, None
    return min(numeric_values), max(numeric_values)

# Test
my_set = {3, 7, 1, 9, 5}
min_val, max_val = find_min_max(my_set)
print(f"Set: {my_set}")
print(f"Min: {min_val}, Max: {max_val}")

# 39. Create a set of unique first letters from words
def first_letters_set(words):
    return {word[0].lower() for word in words if word}

# Test
words = ['apple', 'banana', 'cherry', 'avocado']
result = first_letters_set(words)
print(f"Words: {words}")
print(f"First letters: {result}")

# 40. Check if a set contains only alphabetic strings
def all_alphabetic_strings(my_set):
    return all(isinstance(x, str) and x.isalpha() for x in my_set)

# Test
alpha_set = {'hello', 'world', 'python'}
mixed_set = {'hello', 123, 'world'}
print(f"Set {alpha_set} all alphabetic: {all_alphabetic_strings(alpha_set)}")
print(f"Set {mixed_set} all alphabetic: {all_alphabetic_strings(mixed_set)}")

# 41. Find the union of two sets
def set_union(set1, set2):
    return set1 | set2  # or set1.union(set2)

# Test
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set_union(set1, set2)
print(f"Set1: {set1}")
print(f"Set2: {set2}")
print(f"Union: {result}")

# 42. Find the intersection of two sets
def set_intersection(set1, set2):
    return set1 & set2  # or set1.intersection(set2)

# Test
set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set_intersection(set1, set2)
print(f"Set1: {set1}")
print(f"Set2: {set2}")
print(f"Intersection: {result}")

# 43. Find the difference between two sets
def set_difference(set1, set2):
    return set1 - set2  # or set1.difference(set2)

# Test
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
result = set_difference(set1, set2)
print(f"Set1: {set1}")
print(f"Set2: {set2}")
print(f"Difference (set1 - set2): {result}")

# 44. Find the symmetric difference between two sets
def symmetric_difference(set1, set2):
    return set1 ^ set2  # or set1.symmetric_difference(set2)

# Test
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = symmetric_difference(set1, set2)
print(f"Set1: {set1}")
print(f"Set2: {set2}")
print(f"Symmetric difference: {result}")

# 45. Check if one set is a subset of another
def is_subset(set1, set2):
    return set1 <= set2  # or set1.issubset(set2)

# Test
set1 = {1, 2}
set2 = {1, 2, 3, 4}
result = is_subset(set1, set2)
print(f"Set1: {set1}")
print(f"Set2: {set2}")
print(f"Set1 is subset of Set2: {result}")

# 46. Check if one set is a superset of another
def is_superset(set1, set2):
    return set1 >= set2  # or set1.issuperset(set2)

# Test
set1 = {1, 2, 3, 4}
set2 = {2, 3}
result = is_superset(set1, set2)
print(f"Set1: {set1}")
print(f"Set2: {set2}")
print(f"Set1 is superset of Set2: {result}")

# 47. Check if two sets are disjoint
def are_disjoint(set1, set2):
    return set1.isdisjoint(set2)

# Test
set1 = {1, 2, 3}
set2 = {4, 5, 6}  q
result = are_disjoint(set1, set2)
print(f"Set1: {set1}")
print(f"Set2: {set2}")
print(f"Sets are disjoint: {result}")

# 48. Update a set with the union of another set
def update_with_union(set1, set2):
    updated_set = set1.copy()
    updated_set |= set2  # or updated_set.update(set2)
    return updated_set

# Test
set1 = {1, 2}
set2 = {3, 4}
result = update_with_union(set1, set2)
print(f"Original Set1: {set1}")
print(f"Set2: {set2}")
print(f"Updated Set1: {result}")

# 49. Update a set with the intersection of another set
def update_with_intersection(set1, set2):
    updated_set = set1.copy()
    updated_set &= set2  # or updated_set.intersection_update(set2)
    return updated_set

# Test
set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = update_with_intersection(set1, set2)
print(f"Original Set1: {set1}")
print(f"Set2: {set2}")
print(f"Updated Set1 (intersection): {result}")

# 50. Update a set with the difference of another set
def update_with_difference(set1, set2):
    updated_set = set1.copy()
    updated_set -= set2  # or updated_set.difference_update(set2)
    return updated_set

# Test
set1 = {1, 2, 3, 4}
set2 = {3, 4}
result = update_with_difference(set1, set2)
print(f"Original Set1: {set1}")
print(f"Set2: {set2}")
print(f"Updated Set1 (difference): {result}")

# 51. Find common elements across multiple sets
def intersection_multiple_sets(sets):
    if not sets:
        return set()
    result = sets[0].copy()
    for s in sets[1:]:
        result &= s
    return result

# Test
sets = [{1, 2, 3}, {2, 3, 4}, {2, 3, 5}]
result = intersection_multiple_sets(sets)
print(f"Sets: {sets}")
print(f"Common elements: {result}")

# 52. Filter a set using set comprehension
def filter_set_comprehension(my_set, condition):
    return {x for x in my_set if condition(x)}

# Test
numbers = {1, 2, 3, 4, 5, 6}
evens = filter_set_comprehension(numbers, lambda x: x % 2 == 0)
print(f"Original: {numbers}")
print(f"Even numbers: {evens}")

# 53. Create a set of squared even numbers
def squared_evens(start, end):
    return {x**2 for x in range(start, end + 1) if x % 2 == 0}

# Test
result = squared_evens(1, 10)
print(f"Squared even numbers from 1 to 10: {result}")

# 54. Find elements in exactly one of two sets
def elements_in_one_set_only(set1, set2):
    return (set1 - set2) | (set2 - set1)  # symmetric difference

# Test
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = elements_in_one_set_only(set1, set2)
print(f"Set1: {set1}")
print(f"Set2: {set2}")
print(f"In exactly one set: {result}")

# 55. Check if a set is a proper subset
def is_proper_subset(set1, set2):
    return set1 < set2  # proper subset (strict)

# Test
set1 = {1, 2}
set2 = {1, 2, 3}
result = is_proper_subset(set1, set2)
print(f"Set1: {set1}")
print(f"Set2: {set2}")
print(f"Set1 is proper subset of Set2: {result}")

# 56. Flatten nested lists and create unique set
def flatten_to_set(nested_lists):
    result = set()
    for sublist in nested_lists:
        result.update(sublist)
    return result

# Test
nested = [[1, 2], [2, 3], [3, 4, 1]]
result = flatten_to_set(nested)
print(f"Nested lists: {nested}")
print(f"Flattened unique set: {result}")

# 57. Find union of multiple sets
def union_multiple_sets(sets):
    result = set()
    for s in sets:
        result |= s
    return result

# Test
sets = [{1, 2}, {2, 3}, {3, 4}]
result = union_multiple_sets(sets)
print(f"Sets: {sets}")
print(f"Union: {result}")

# 58. Remove common elements from two sets mutually
def mutual_difference(set1, set2):
    common = set1 & set2
    return set1 - common, set2 - common

# Test
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result1, result2 = mutual_difference(set1, set2)
print(f"Original Set1: {set1}")
print(f"Original Set2: {set2}")
print(f"After mutual difference - Set1: {result1}, Set2: {result2}")

# 59. Check hierarchical relationship in sets
def has_subset_chain(sets):
    sorted_sets = sorted(sets, key=len)
    for i in range(len(sorted_sets) - 1):
        if not sorted_sets[i] <= sorted_sets[i + 1]:
            return False
    return True

# Test
sets = [{1}, {1, 2}, {1, 2, 3}]
result = has_subset_chain(sets)
print(f"Sets: {sets}")
print(f"Forms subset chain: {result}")

# 60. Find unique elements across all sets
def unique_across_all_sets(sets):
    all_elements = set()
    for s in sets:
        all_elements |= s
    return all_elements

# Test
sets = [{1, 2}, {2, 3}, {4, 5}]
result = unique_across_all_sets(sets)
print(f"Sets: {sets}")
print(f"All unique elements: {result}")

# 61. Create a blacklist filter using sets
def apply_blacklist_filter(data, blacklist):
    return data - blacklist

# Test
data = {1, 2, 3, 4, 5}
blacklist = {2, 4}
result = apply_blacklist_filter(data, blacklist)
print(f"Data: {data}")
print(f"Blacklist: {blacklist}")
print(f"Filtered data: {result}")

# 62. Find elements exclusive to first set
def exclusive_to_first(first_set, other_sets):
    combined_others = set()
    for s in other_sets:
        combined_others |= s
    return first_set - combined_others

# Test
set1 = {1, 2, 3, 4}
others = [{2, 3}, {3, 5}]
result = exclusive_to_first(set1, others)
print(f"First set: {set1}")
print(f"Other sets: {others}")
print(f"Exclusive to first: {result}")

# 63. Group elements by set membership
def group_by_membership(set1, set2):
    only_in_set1 = set1 - set2
    common = set1 & set2
    only_in_set2 = set2 - set1
    return {
        'only_in_set1': only_in_set1,
        'common': common,
        'only_in_set2': only_in_set2
    }

# Test
set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = group_by_membership(set1, set2)
print(f"Set1: {set1}")
print(f"Set2: {set2}")
for key, value in result.items():
    print(f"{key}: {value}")

# 64. Check if any set in list is empty
def has_empty_set(sets):
    return any(len(s) == 0 for s in sets)

# Test
sets = [{1, 2}, set(), {3, 4}]
result = has_empty_set(sets)
print(f"Sets: {sets}")
print(f"Has empty set: {result}")

# 65. Find the largest set
def find_largest_set(sets):
    if not sets:
        return None
    return max(sets, key=len)

# Test
sets = [{1}, {1, 2, 3}, {1, 2}]
result = find_largest_set(sets)
print(f"Sets: {sets}")
print(f"Largest set: {result}")

# 66. Find common file extensions
def common_file_extensions(dir_sets):
    ext_sets = []
    for file_set in dir_sets:
        extensions = set()
        for filename in file_set:
            if '.' in filename:
                ext = '.' + filename.split('.')[-1]
                extensions.add(ext)
        ext_sets.append(extensions)

    if not ext_sets:
        return set()

    common = ext_sets[0]
    for ext_set in ext_sets[1:]:
        common &= ext_set
    return common

# Test
dir1 = {'file1.txt', 'file2.pdf'}
dir2 = {'file3.txt', 'file4.jpg'}
result = common_file_extensions([dir1, dir2])
print(f"Directory 1: {dir1}")
print(f"Directory 2: {dir2}")
print(f"Common extensions: {result}")

# 67. Filter valid email domains
def filter_valid_emails(emails, valid_domains):
    valid_emails = set()
    for email in emails:
        if '@' in email:
            domain = email.split('@')[1]
            if domain in valid_domains:
                valid_emails.add(email)
    return valid_emails

# Test
emails = {'user@gmail.com', 'admin@yahoo.com', 'test@outlook.com'}
valid_domains = {'gmail.com', 'outlook.com'}
result = filter_valid_emails(emails, valid_domains)
print(f"Emails: {emails}")
print(f"Valid domains: {valid_domains}")
print(f"Filtered emails: {result}")

# 68. Find common blog post tags
def common_post_tags(post_tags_list):
    if not post_tags_list:
        return set()

    common = post_tags_list[0].copy()
    for tags in post_tags_list[1:]:
        common &= tags
    return common

# Test
post1_tags = {'python', 'coding', 'tutorial'}
post2_tags = {'python', 'programming', 'tutorial'}
result = common_post_tags([post1_tags, post2_tags])
print(f"Post 1 tags: {post1_tags}")
print(f"Post 2 tags: {post2_tags}")
print(f"Common tags: {result}")

# 69. Create user permission intersection
def permission_intersection(role_permissions):
    if not role_permissions:
        return set()

    common = role_permissions[0].copy()
    for permissions in role_permissions[1:]:
        common &= permissions
    return common

# Test
role1 = {'read', 'write'}
role2 = {'read', 'execute'}
result = permission_intersection([role1, role2])
print(f"Role 1 permissions: {role1}")
print(f"Role 2 permissions: {role2}")
print(f"Common permissions: {result}")

# 70. Check user permissions
def has_required_permissions(user_permissions, required_permissions):
    return required_permissions <= user_permissions

# Test
user_permissions = {'read', 'write', 'execute'}
required = {'read', 'write'}
result = has_required_permissions(user_permissions, required)
print(f"User permissions: {user_permissions}")
print(f"Required permissions: {required}")
print(f"Has all required: {result}")

# 71. Find mutual friends
def mutual_friends(user1_friends, user2_friends):
    return user1_friends & user2_friends

# Test
user1_friends = {'Alice', 'Bob', 'Charlie'}
user2_friends = {'Bob', 'Charlie', 'David'}
result = mutual_friends(user1_friends, user2_friends)
print(f"User 1 friends: {user1_friends}")
print(f"User 2 friends: {user2_friends}")
print(f"Mutual friends: {result}")

# 72. Aggregate unique skills from job requirements
def aggregate_job_skills(job_requirements):
    all_skills = set()
    for skills in job_requirements:
        all_skills |= skills
    return all_skills

# Test
job1 = {'Python', 'SQL'}
job2 = {'Python', 'JavaScript', 'SQL'}
result = aggregate_job_skills([job1, job2])
print(f"Job 1 skills: {job1}")
print(f"Job 2 skills: {job2}")
print(f"All unique skills: {result}")

# 73. Filter products by store availability
def products_in_all_stores(store_inventories):
    if not store_inventories:
        return set()

    common = store_inventories[0].copy()
    for inventory in store_inventories[1:]:
        common &= inventory
    return common

# Test
store1 = {'laptop', 'mouse'}
store2 = {'laptop', 'keyboard'}
result = products_in_all_stores([store1, store2])
print(f"Store 1: {store1}")
print(f"Store 2: {store2}")
print(f"Available everywhere: {result}")

# 74. Collect recipe ingredients
def collect_all_ingredients(recipes):
    all_ingredients = set()
    for ingredients in recipes:
        all_ingredients |= ingredients
    return all_ingredients

# Test
recipe1 = {'flour', 'eggs', 'milk'}
recipe2 = {'flour', 'sugar'}
result = collect_all_ingredients([recipe1, recipe2])
print(f"Recipe 1: {recipe1}")
print(f"Recipe 2: {recipe2}")
print(f"All ingredients: {result}")

# 75. Implement voting system logic
def analyze_voting(votes_for, votes_against, all_members):
    voted = votes_for | votes_against
    abstained = all_members - voted
    return {
        'for': votes_for,
        'against': votes_against,
        'abstained': abstained
    }

# Test
votes_for = {'Alice', 'Bob'}
votes_against = {'Charlie'}
all_members = {'Alice', 'Bob', 'Charlie', 'David'}
result = analyze_voting(votes_for, votes_against, all_members)
print(f"Votes for: {result['for']}")
print(f"Votes against: {result['against']}")
print(f"Abstained: {result['abstained']}")

# 76. Detect course conflicts
def has_course_conflicts(enrolled_courses, conflict_pairs):
    for conflict_set in conflict_pairs:
        if len(enrolled_courses & conflict_set) > 1:
            return True
    return False

# Test
enrolled = {'Math101', 'Physics101'}
conflicts = [{'Math101', 'Math102'}, {'Physics101', 'Chemistry101'}]
result = has_course_conflicts(enrolled, conflicts)
print(f"Enrolled: {enrolled}")
print(f"Conflict pairs: {conflicts}")
print(f"Has conflicts: {result}")

# 77. Find available courses
def find_available_courses(completed_courses, course_prereqs):
    available = set()
    for course, prereqs in course_prereqs.items():
        if prereqs <= completed_courses:
            available.add(course)
    return available

# Test
completed = {'Math101', 'Physics101'}
course_prereqs = {
    'Math201': {'Math101'},
    'Physics201': {'Physics101', 'Math101'},
    'Chemistry101': {'Physics101', 'Chemistry100'}
}
result = find_available_courses(completed, course_prereqs)
print(f"Completed: {completed}")
print(f"Available courses: {result}")

# 78. Content filtering system
def calculate_relevance_score(content_keywords, user_interests):
    matches = content_keywords & user_interests
    return len(matches)

# Test
content_keywords = {'python', 'programming', 'tutorial'}
user_interests = {'python', 'data science'}
score = calculate_relevance_score(content_keywords, user_interests)
print(f"Content keywords: {content_keywords}")
print(f"User interests: {user_interests}")
print(f"Relevance score: {score}")

# 79. Feature selection for machine learning
def select_optimal_features(available_features, important_features):
    return available_features & important_features

# Test
available_features = {'age', 'income', 'education', 'location'}
important_features = {'age', 'income'}
result = select_optimal_features(available_features, important_features)
print(f"Available features: {available_features}")
print(f"Important features: {important_features}")
print(f"Selected features: {result}")

# 80. Simple recommendation system
def jaccard_similarity(set1, set2):
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union if union > 0 else 0

# Test
user1_likes = {'movie1', 'movie2', 'movie3'}
user2_likes = {'movie2', 'movie3', 'movie4'}
similarity = jaccard_similarity(user1_likes, user2_likes)
print(f"User 1 likes: {user1_likes}")
print(f"User 2 likes: {user2_likes}")
print(f"Jaccard similarity: {similarity:.2f}")

# 81. Create frozenset as dictionary key
def frozenset_as_key(data_list):
    fs = frozenset(data_list)
    return {fs: f'data_for_{len(fs)}_elements'}

# Test
data = [1, 2, 3]
result = frozenset_as_key(data)
print(f"Data: {data}")
print(f"Dictionary with frozenset key: {result}")

# 82. Nested set operations with frozenset
def frozenset_operations(frozensets_list):
    if not frozensets_list:
        return frozenset()

    intersection = frozensets_list[0]
    union = frozensets_list[0]

    for fs in frozensets_list[1:]:
        intersection = intersection & fs
        union = union | fs

    return {'intersection': intersection, 'union': union}

# Test
fs1 = frozenset({1, 2, 3})
fs2 = frozenset({2, 3, 4})
fs3 = frozenset({3, 4, 5})
result = frozenset_operations([fs1, fs2, fs3])
print(f"Frozensets: {[fs1, fs2, fs3]}")
print(f"Operations result: {result}")

# 83. Generate power set
def power_set(s):
    from itertools import combinations
    power_set_list = []
    for r in range(len(s) + 1):
        for combo in combinations(s, r):
            power_set_list.append(frozenset(combo))
    return set(power_set_list)

# Test
original_set = {1, 2, 3}
result = power_set(original_set)
print(f"Original set: {original_set}")
print(f"Power set: {result}")
print(f"Power set size: {len(result)} (should be 2^{len(original_set)} = {2**len(original_set)})")

# 84. Custom set class with logging
class LoggingSet:
    def __init__(self, initial_data=None):
        self._data = set(initial_data) if initial_data else set()
        self._log = []

    def add(self, element):
        self._data.add(element)
        self._log.append(f"Added: {element}")

    def remove(self, element):
        self._data.remove(element)
        self._log.append(f"Removed: {element}")

    def intersection(self, other):
        if isinstance(other, LoggingSet):
            result = self._data & other._data
        else:
            result = self._data & other
        self._log.append(f"Intersection with {other}")
        return result

    def get_log(self):
        return self._log.copy()

    def __str__(self):
        return str(self._data)

# Test
logged_set = LoggingSet([1, 2, 3])
logged_set.add(4)
logged_set.remove(1)
intersection_result = logged_set.intersection({2, 3, 4, 5})
print(f"Set: {logged_set}")
print(f"Intersection result: {intersection_result}")
print(f"Operation log: {logged_set.get_log()}")

# 85. Set cover problem (greedy approximation)
def set_cover_greedy(universe, sets):
    universe = universe.copy()
    selected_sets = []

    while universe:
        # Find set that covers most uncovered elements
        best_set = None
        best_coverage = 0

        for s in sets:
            coverage = len(s & universe)
            if coverage > best_coverage:
                best_coverage = coverage
                best_set = s

        if best_set is None:
            break

        selected_sets.append(best_set)
        universe -= best_set
        sets = [s for s in sets if s != best_set]

    return selected_sets

# Test
universe = {1, 2, 3, 4, 5}
sets = [{1, 2, 3}, {2, 4}, {3, 4}, {4, 5}]
result = set_cover_greedy(universe, sets)
print(f"Universe: {universe}")
print(f"Available sets: {sets}")
print(f"Greedy cover: {result}")

# 86. All possible intersections
def all_intersections(sets):
    from itertools import combinations
    all_intersections_dict = {}

    for r in range(2, len(sets) + 1):
        for combo in combinations(sets, r):
            intersection = combo[0].copy()
            for s in combo[1:]:
                intersection &= s
            if intersection:  # Only store non-empty intersections
                key = f"intersection_of_{len(combo)}_sets"
                if key not in all_intersections_dict:
                    all_intersections_dict[key] = []
                all_intersections_dict[key].append(intersection)

    return all_intersections_dict

# Test
sets_list = [{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]
result = all_intersections(sets_list)
print(f"Sets: {sets_list}")
print("All non-empty intersections:")
for key, intersections in result.items():
    print(f"  {key}: {intersections}")

# 87. Set-based graph operations (connected components)
def find_connected_components(edges, vertices):
    # Build adjacency representation using sets
    adj = {v: set() for v in vertices}
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)

    visited = set()
    components = []

    def dfs(vertex, component):
        visited.add(vertex)
        component.add(vertex)
        for neighbor in adj[vertex]:
            if neighbor not in visited:
                dfs(neighbor, component)

    for vertex in vertices:
        if vertex not in visited:
            component = set()
            dfs(vertex, component)
            components.append(component)

    return components

# Test
edges = {(1, 2), (2, 3), (4, 5)}
vertices = {1, 2, 3, 4, 5}
result = find_connected_components(edges, vertices)
print(f"Edges: {edges}")
print(f"Vertices: {vertices}")
print(f"Connected components: {result}")

# 88. Memory-efficient bitset
class BitSet:
    def __init__(self, max_value):
        self.max_value = max_value
        self.bits = 0

    def add(self, value):
        if 0 <= value <= self.max_value:
            self.bits |= (1 << value)

    def remove(self, value):
        if 0 <= value <= self.max_value:
            self.bits &= ~(1 << value)

    def contains(self, value):
        if 0 <= value <= self.max_value:
            return bool(self.bits & (1 << value))
        return False

    def to_set(self):
        result = set()
        for i in range(self.max_value + 1):
            if self.bits & (1 << i):
                result.add(i)
        return result

    def __len__(self):
        return bin(self.bits).count('1')

# Test
bitset = BitSet(10)
bitset.add(1)
bitset.add(3)
bitset.add(5)
print(f"BitSet contains 3: {bitset.contains(3)}")
print(f"BitSet contains 4: {bitset.contains(4)}")
print(f"BitSet as set: {bitset.to_set()}")
print(f"BitSet size: {len(bitset)}")

# 89. Custom hashable objects in sets
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __hash__(self):
        return hash((self.name, self.age))

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

def people_set_operations(people_list1, people_list2):
    set1 = set(people_list1)
    set2 = set(people_list2)

    return {
        'union': set1 | set2,
        'intersection': set1 & set2,
        'difference': set1 - set2
    }

# Test
people1 = [Person("Alice", 25), Person("Bob", 30)]
people2 = [Person("Bob", 30), Person("Charlie", 35)]
result = people_set_operations(people1, people2)
print("Set operations with custom Person objects:")
for operation, people_set in result.items():
    print(f"{operation}: {people_set}")

# 90. Fuzzy set operations
class FuzzySet:
    def __init__(self, membership_dict=None):
        # membership_dict maps elements to membership degrees (0.0 to 1.0)
        self.membership = membership_dict or {}

    def add(self, element, degree):
        if 0 <= degree <= 1:
            self.membership[element] = degree

    def fuzzy_union(self, other):
        result = FuzzySet()
        all_elements = set(self.membership.keys()) | set(other.membership.keys())

        for element in all_elements:
            degree1 = self.membership.get(element, 0)
            degree2 = other.membership.get(element, 0)
            result.membership[element] = max(degree1, degree2)

        return result

    def fuzzy_intersection(self, other):
        result = FuzzySet()
        all_elements = set(self.membership.keys()) | set(other.membership.keys())

        for element in all_elements:
            degree1 = self.membership.get(element, 0)
            degree2 = other.membership.get(element, 0)
            result.membership[element] = min(degree1, degree2)

        return result

    def __repr__(self):
        return f"FuzzySet({self.membership})"

# Test
fuzzy1 = FuzzySet({'a': 0.8, 'b': 0.6, 'c': 0.4})
fuzzy2 = FuzzySet({'b': 0.7, 'c': 0.9, 'd': 0.5})

union_result = fuzzy1.fuzzy_union(fuzzy2)
intersection_result = fuzzy1.fuzzy_intersection(fuzzy2)

print(f"Fuzzy set 1: {fuzzy1}")
print(f"Fuzzy set 2: {fuzzy2}")
print(f"Fuzzy union: {union_result}")
print(f"Fuzzy intersection: {intersection_result}")

# 91. Set representation conversion
def bitstring_to_set(bitstring, max_element):
    result = set()
    for i, bit in enumerate(reversed(bitstring)):
        if bit == '1' and i <= max_element:
            result.add(i)
    return result

def set_to_bitstring(s, max_element):
    bitstring = ['0'] * (max_element + 1)
    for element in s:
        if 0 <= element <= max_element:
            bitstring[max_element - element] = '1'
    return ''.join(bitstring)

def list_to_set_with_dedup(lst):
    return set(lst)

# Test
bitstring = '101010'
max_elem = 5
set_from_bits = bitstring_to_set(bitstring, max_elem)
print(f"Bitstring '{bitstring}' to set: {set_from_bits}")

test_set = {1, 3, 5}
bits_from_set = set_to_bitstring(test_set, max_elem)
print(f"Set {test_set} to bitstring: '{bits_from_set}'")

test_list = [1, 2, 2, 3, 3, 4]
deduped_set = list_to_set_with_dedup(test_list)
print(f"List {test_list} deduplicated: {deduped_set}")

# 92. Maximum independent set (greedy approximation)
def max_independent_set_greedy(graph_adj):
    # graph_adj: dict mapping vertices to sets of adjacent vertices
    independent_set = set()
    remaining_vertices = set(graph_adj.keys())

    while remaining_vertices:
        # Choose vertex with minimum degree among remaining
        min_degree_vertex = min(remaining_vertices, 
                               key=lambda v: len(graph_adj[v] & remaining_vertices))

        independent_set.add(min_degree_vertex)

        # Remove this vertex and all its neighbors
        to_remove = {min_degree_vertex} | (graph_adj[min_degree_vertex] & remaining_vertices)
        remaining_vertices -= to_remove

    return independent_set

# Test
# Graph: 1-2-3-4 (path graph)
graph = {
    1: {2},
    2: {1, 3},
    3: {2, 4},
    4: {3}
}
result = max_independent_set_greedy(graph)
print(f"Graph adjacency: {graph}")
print(f"Maximum independent set (greedy): {result}")

# 93. Set-based caching with TTL
import time

class TTLCache:
    def __init__(self):
        self.cache = {}  # frozenset -> (value, expiry_time)
        self.default_ttl = 60  # seconds

    def put(self, key_set, value, ttl=None):
        key = frozenset(key_set)
        expiry = time.time() + (ttl or self.default_ttl)
        self.cache[key] = (value, expiry)

    def get(self, key_set):
        key = frozenset(key_set)
        if key in self.cache:
            value, expiry = self.cache[key]
            if time.time() < expiry:
                return value
            else:
                del self.cache[key]
        return None

    def cleanup_expired(self):
        current_time = time.time()
        expired_keys = [k for k, (_, expiry) in self.cache.items() if current_time >= expiry]
        for key in expired_keys:
            del self.cache[key]
        return len(expired_keys)

# Test
cache = TTLCache()
key_set = {1, 2, 3}
cache.put(key_set, "cached_value", ttl=2)

print(f"Cached value: {cache.get(key_set)}")
time.sleep(0.1)  # Small delay
print(f"Still cached: {cache.get(key_set)}")
print(f"Cache state: {len(cache.cache)} items")

# 94. Graph coloring (greedy algorithm)
def graph_coloring_greedy(vertices, edges):
    # Build adjacency sets
    adj = {v: set() for v in vertices}
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)

    coloring = {}

    # Sort vertices by degree (highest first for better results)
    sorted_vertices = sorted(vertices, key=lambda v: len(adj[v]), reverse=True)

    for vertex in sorted_vertices:
        # Find used colors by neighbors
        used_colors = set()
        for neighbor in adj[vertex]:
            if neighbor in coloring:
                used_colors.add(coloring[neighbor])

        # Assign smallest available color
        color = 0
        while color in used_colors:
            color += 1
        coloring[vertex] = color

    num_colors = len(set(coloring.values()))
    return coloring, num_colors

# Test
vertices = {1, 2, 3, 4}
edges = {(1, 2), (1, 3), (2, 3), (3, 4)}
coloring, num_colors = graph_coloring_greedy(vertices, edges)
print(f"Vertices: {vertices}")
print(f"Edges: {edges}")
print(f"Coloring: {coloring}")
print(f"Number of colors needed: {num_colors}")

# 95. Bloom filter implementation
class BloomFilter:
    def __init__(self, capacity, error_rate=0.01):
        import math
        self.capacity = capacity
        self.error_rate = error_rate

        # Calculate optimal bit array size and number of hash functions
        self.bit_size = int(-capacity * math.log(error_rate) / (math.log(2) ** 2))
        self.hash_count = int(self.bit_size * math.log(2) / capacity)

        self.bit_array = set()  # Using set to simulate bit array

    def _hash(self, item, seed):
        return hash((item, seed)) % self.bit_size

    def add(self, item):
        for i in range(self.hash_count):
            bit_index = self._hash(item, i)
            self.bit_array.add(bit_index)

    def might_contain(self, item):
        for i in range(self.hash_count):
            bit_index = self._hash(item, i)
            if bit_index not in self.bit_array:
                return False
        return True

# Test
bf = BloomFilter(1000, 0.01)
test_items = ['apple', 'banana', 'cherry']

for item in test_items:
    bf.add(item)

print(f"Added items: {test_items}")
print(f"'apple' might be in filter: {bf.might_contain('apple')}")
print(f"'orange' might be in filter: {bf.might_contain('orange')}")
print(f"Bit array size: {len(bf.bit_array)}")

# 96. Handle None and empty set edge cases
def safe_set_operations(set_with_none, empty_set, regular_set):
    # Handle operations with None values and empty sets
    results = {}

    # Union with None handling
    try:
        results['union_with_none'] = set_with_none | regular_set
    except TypeError as e:
        results['union_with_none'] = f"Error: {e}"

    # Intersection with empty set
    results['intersection_with_empty'] = regular_set & empty_set

    # Check if None is in set
    results['none_membership'] = None in set_with_none

    # Length operations
    results['lengths'] = {
        'set_with_none': len(set_with_none),
        'empty_set': len(empty_set),
        'regular_set': len(regular_set)
    }

    # Filter out None values
    results['filtered_none'] = {x for x in set_with_none if x is not None}

    return results

# Test
set_with_none = {None, 1, 2}
empty_set = set()
regular_set = {2, 3, 4}

results = safe_set_operations(set_with_none, empty_set, regular_set)
print("Edge case handling results:")
for key, value in results.items():
    print(f"{key}: {value}")

# 97. Mixed numeric types in sets
from decimal import Decimal

def handle_mixed_numeric_types():
    # Demonstrate how Python handles different numeric types in sets
    mixed_set = {1, 1.0, Decimal('1.0'), 2, 2.0}

    results = {
        'original_mixed_set': mixed_set,
        'set_length': len(mixed_set),
        'contains_int_1': 1 in mixed_set,
        'contains_float_1': 1.0 in mixed_set,
        'contains_decimal_1': Decimal('1.0') in mixed_set
    }

    # Show type coercion in action
    int_set = {1, 2, 3}
    float_set = {1.0, 2.0, 3.0}

    results['int_float_intersection'] = int_set & float_set
    results['types_are_equal'] = 1 == 1.0 == Decimal('1.0')

    # Create properly separated sets if needed
    int_only = {i for i in mixed_set if type(i) == int}
    float_only = {f for f in mixed_set if type(f) == float}
    decimal_only = {d for d in mixed_set if type(d) == Decimal}

    results['separated_by_type'] = {
        'int_only': int_only,
        'float_only': float_only,
        'decimal_only': decimal_only
    }

    return results

# Test
results = handle_mixed_numeric_types()
print("Mixed numeric types handling:")
for key, value in results.items():
    print(f"{key}: {value}")

# 98. Thread-safe set implementation
import threading

class ThreadSafeSet:
    def __init__(self, initial_data=None):
        self._set = set(initial_data) if initial_data else set()
        self._lock = threading.RLock()

    def add(self, element):
        with self._lock:
            self._set.add(element)

    def remove(self, element):
        with self._lock:
            self._set.remove(element)

    def discard(self, element):
        with self._lock:
            self._set.discard(element)

    def __contains__(self, element):
        with self._lock:
            return element in self._set

    def __len__(self):
        with self._lock:
            return len(self._set)

    def copy(self):
        with self._lock:
            return ThreadSafeSet(self._set.copy())

    def union(self, other):
        with self._lock:
            if isinstance(other, ThreadSafeSet):
                with other._lock:
                    return ThreadSafeSet(self._set | other._set)
            else:
                return ThreadSafeSet(self._set | other)

    def __str__(self):
        with self._lock:
            return str(self._set)

# Test
thread_safe_set = ThreadSafeSet([1, 2, 3])
thread_safe_set.add(4)
thread_safe_set.discard(1)

print(f"Thread-safe set: {thread_safe_set}")
print(f"Contains 2: {2 in thread_safe_set}")
print(f"Length: {len(thread_safe_set)}")

# Union with regular set
regular_set = {3, 4, 5}
union_result = thread_safe_set.union(regular_set)
print(f"Union result: {union_result}")

# 99. Set partitioning algorithm
def can_partition_equal_sum(numbers_set):
    numbers = list(numbers_set)
    total_sum = sum(numbers)

    # If total sum is odd, cannot partition into equal sums
    if total_sum % 2 != 0:
        return False, None

    target = total_sum // 2
    n = len(numbers)

    # Dynamic programming approach
    dp = [[False] * (target + 1) for _ in range(n + 1)]

    # Base case: sum 0 is always possible with empty set
    for i in range(n + 1):
        dp[i][0] = True

    # Fill dp table
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            dp[i][j] = dp[i-1][j]  # Don't include current number
            if j >= numbers[i-1]:
                dp[i][j] = dp[i][j] or dp[i-1][j-numbers[i-1]]

    if not dp[n][target]:
        return False, None

    # Reconstruct the partition
    subset1 = set()
    i, j = n, target
    while i > 0 and j > 0:
        if not dp[i-1][j]:  # Current number must be included
            subset1.add(numbers[i-1])
            j -= numbers[i-1]
        i -= 1

    subset2 = numbers_set - subset1
    return True, [subset1, subset2]

# Test
numbers = {1, 2, 3, 4, 5, 6}  # Sum = 21, target = 10.5 (impossible)
can_partition, partitions = can_partition_equal_sum(numbers)
print(f"Numbers: {numbers}")
print(f"Can partition into equal sums: {can_partition}")
if can_partition:
    print(f"Partitions: {partitions}")
    print(f"Partition sums: {[sum(p) for p in partitions]}")

# Test with even sum
numbers2 = {1, 2, 3, 6}  # Sum = 12, target = 6
can_partition2, partitions2 = can_partition_equal_sum(numbers2)
print(f"\nNumbers: {numbers2}")
print(f"Can partition into equal sums: {can_partition2}")
if can_partition2:
    print(f"Partitions: {partitions2}")
    print(f"Partition sums: {[sum(p) for p in partitions2]}")

# 100. Optimized large set intersection
def optimized_large_set_intersection(sets, memory_limit_mb=100):
    """
    Efficiently find intersection of multiple large sets with memory management.
    Uses iterative approach and memory monitoring.
    """
    import sys
    import gc

    if not sets:
        return set()

    # Sort sets by size (smallest first for efficiency)
    sorted_sets = sorted(sets, key=len)

    # Start with smallest set
    result = sorted_sets[0].copy()

    # Track memory usage (simplified)
    def get_memory_usage_mb():
        return sys.getsizeof(result) / (1024 * 1024)

    # Iteratively intersect with remaining sets
    for i, current_set in enumerate(sorted_sets[1:], 1):
        # If result is getting too large, use generator approach
        if get_memory_usage_mb() > memory_limit_mb:
            print(f"Memory limit reached at iteration {i}, using generator approach")
            result = {elem for elem in result if elem in current_set}
        else:
            result &= current_set

        # Early termination if result becomes empty
        if not result:
            break

        # Periodic garbage collection for large operations
        if i % 10 == 0:
            gc.collect()

    return result

def generate_large_test_sets(num_sets=5, set_size=10000, overlap_ratio=0.1):
    """Generate test sets with controlled overlap for testing."""
    import random

    # Create base elements for overlap
    overlap_size = int(set_size * overlap_ratio)
    base_elements = set(range(overlap_size))

    sets = []
    for i in range(num_sets):
        # Each set contains the base elements plus unique elements
        unique_elements = set(range(overlap_size + i * set_size, 
                                  overlap_size + (i + 1) * set_size))
        test_set = base_elements | unique_elements
        sets.append(test_set)

    return sets

# Test with smaller sets for demonstration
test_sets = generate_large_test_sets(num_sets=3, set_size=1000, overlap_ratio=0.05)
print(f"Generated {len(test_sets)} test sets")
print(f"Set sizes: {[len(s) for s in test_sets]}")

intersection_result = optimized_large_set_intersection(test_sets)
print(f"Intersection size: {len(intersection_result)}")
print(f"Intersection (first 10 elements): {list(intersection_result)[:10]}")

"""End of 100 Python Set Coding Questions - Solutions

These solutions demonstrate:
- Basic set operations and membership testing
- Intermediate set methods and real-world applications
- Advanced algorithms, custom implementations, and edge cases
- Memory-efficient techniques and thread-safety considerations

Each solution is designed to be clean, readable, and educational.
Perfect for coding interviews, portfolio projects, and skill development!
"""