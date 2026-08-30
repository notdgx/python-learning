# 100 Python Dictionary Solutions
# Author: AI Assistant
# Created for Python learners preparing for interviews and competitive programming

# from collections import defaultdict, Counter, OrderedDict
# from typing import Dict, List, Any, Tuple

# ===============================
# BASIC LEVEL (Questions 1-40)
# ===============================

# 1. Create an empty dictionary and print it
def solution_1():
    my_dict = {}
    print(my_dict)
    return my_dict

# 2. Create a dictionary with keys 'name', 'age', 'city' and values 'Alice', 25, 'Boston'
def solution_2():
    my_dict = {'name': 'Alice', 'age': 25, 'city': 'Boston'}
    return my_dict

# 3. Access the value of key 'name' from dictionary
def solution_3():
    my_dict = {'name': 'Bob', 'age': 30}
    return my_dict['name']

# 4. Add a new key-value pair to dictionary
def solution_4():
    my_dict = {'name': 'Carol', 'age': 28}
    my_dict['country'] = 'USA'
    return my_dict

# 5. Remove the key 'age' from dictionary
def solution_5():
    my_dict = {'name': 'David', 'age': 35, 'city': 'NYC'}
    del my_dict['age']
    return my_dict

# 6. Get all keys from dictionary and convert to list
def solution_6():
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    return list(my_dict.keys())

# 7. Get all values from dictionary and convert to list
def solution_7():
    my_dict = {'x': 10, 'y': 20, 'z': 30}
    return list(my_dict.values())

# 8. Get all key-value pairs as list of tuples
def solution_8():
    my_dict = {'p': 5, 'q': 6}
    return list(my_dict.items())

# 9. Check if key exists in dictionary
def solution_9():
    my_dict = {'name': 'Eve', 'age': 22}
    return 'name' in my_dict

# 10. Use get() method with default value
def solution_10():
    my_dict = {'name': 'Frank'}
    return my_dict.get('salary', 0)

# 11. Update dictionary with another dictionary
def solution_11():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    dict1.update(dict2)
    return dict1

# 12. Clear all elements from dictionary
def solution_12():
    my_dict = {'x': 100, 'y': 200}
    my_dict.clear()
    return my_dict

# 13. Create a copy of dictionary
def solution_13():
    my_dict = {'name': 'Grace', 'score': 95}
    return my_dict.copy()

# 14. Use pop() to remove and return value
def solution_14():
    my_dict = {'name': 'Helen', 'age': 29}
    return my_dict.pop('age')

# 15. Use popitem() to remove last key-value pair
def solution_15():
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    return my_dict.popitem()

# 16. Use setdefault() to get value with default
def solution_16():
    my_dict = {'name': 'Ivan'}
    return my_dict.setdefault('phone', 'N/A')

# 17. Create dictionary from two lists
def solution_17():
    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    return dict(zip(keys, values))

# 18. Find length of dictionary
def solution_18():
    my_dict = {'math': 90, 'science': 85, 'english': 88}
    return len(my_dict)

# 19. Iterate through dictionary keys
def solution_19():
    my_dict = {'red': 1, 'blue': 2}
    for key in my_dict:
        print(key)

# 20. Iterate through dictionary values
def solution_20():
    my_dict = {'cat': 'meow', 'dog': 'bark'}
    for value in my_dict.values():
        print(value)

# 21. Iterate through key-value pairs
def solution_21():
    my_dict = {'apple': 5, 'banana': 3}
    for key, value in my_dict.items():
        print(key, value)

# 22. Check if dictionary is empty
def solution_22():
    my_dict = {'name': 'John'}
    return len(my_dict) == 0

# 23. Convert dictionary to list of tuples
def solution_23():
    my_dict = {'x': 1, 'y': 2}
    return list(my_dict.items())

# 24. Convert list of tuples to dictionary
def solution_24():
    tuple_list = [('a', 1), ('b', 2)]
    return dict(tuple_list)

# 25. Create dictionary using fromkeys()
def solution_25():
    keys = ['p', 'q', 'r']
    return dict.fromkeys(keys, 0)

# 26. Replace value of specific key
def solution_26():
    my_dict = {'name': 'Kate', 'score': 75}
    my_dict['score'] = 85
    return my_dict

# 27. Check if value exists in dictionary
def solution_27():
    my_dict = {'a': 50, 'b': 100, 'c': 75}
    return 100 in my_dict.values()

# 28. Get maximum value from dictionary
def solution_28():
    my_dict = {'x': 10, 'y': 25, 'z': 15}
    return max(my_dict.values())

# 29. Get minimum value from dictionary
def solution_29():
    my_dict = {'p': 8, 'q': 3, 'r': 12}
    return min(my_dict.values())

# 30. Count total key-value pairs
def solution_30():
    my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    return len(my_dict)

# 31. Create dictionary with integer keys
def solution_31():
    return {1: 'one', 2: 'two', 3: 'three'}

# 32. Access multiple values using specific keys
def solution_32():
    my_dict = {'name': 'Leo', 'age': 24, 'city': 'LA'}
    return [my_dict['name'], my_dict['city']]

# 33. Check if key is NOT in dictionary
def solution_33():
    my_dict = {'name': 'Max', 'email': 'max@email.com'}
    return 'phone' not in my_dict

# 34. Get sum of all values
def solution_34():
    my_dict = {'a': 10, 'b': 20, 'c': 30}
    return sum(my_dict.values())

# 35. Create dictionary with tuple keys
def solution_35():
    return {(1, 2): 'coordinates', (3, 4): 'point'}

# 36. Remove key using del keyword
def solution_36():
    my_dict = {'name': 'Nina', 'temp': 'delete'}
    del my_dict['temp']
    return my_dict

# 37. Check if two dictionaries are equal
def solution_37():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 2, 'a': 1}
    return dict1 == dict2

# 38. Create dictionary from string with character positions
def solution_38():
    text = 'hello'
    # Note: This creates a dict where each char maps to its LAST position
    return {char: i for i, char in enumerate(text)}

# 39. Convert dictionary keys to uppercase
def solution_39():
    my_dict = {'name': 'Oscar', 'age': 31}
    return {key.upper(): value for key, value in my_dict.items()}

# 40. Get first key-value pair
def solution_40():
    my_dict = {'first': 1, 'second': 2, 'third': 3}
    return next(iter(my_dict.items()))

# ===============================
# INTERMEDIATE LEVEL (Questions 41-80)
# ===============================

# 41. Create nested dictionary
def solution_41():
    return {'person': {'name': 'Alice', 'details': {'age': 25, 'city': 'Boston'}}}

# 42. Access value from nested dictionary
def solution_42():
    my_dict = {'student': {'info': {'name': 'Bob', 'age': 20}}}
    return my_dict['student']['info']['age']

# 43. Dictionary comprehension for squares
def solution_43():
    return {x: x**2 for x in range(1, 6)}

# 44. Count character frequency using dictionary
def solution_44():
    text = 'hello world'
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq

# 45. Merge dictionaries using ** operator
def solution_45():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    return {**dict1, **dict2}

# 46. Sort dictionary by keys
def solution_46():
    my_dict = {'b': 2, 'a': 1, 'c': 3}
    return dict(sorted(my_dict.items()))

# 47. Sort dictionary by values
def solution_47():
    my_dict = {'alice': 85, 'bob': 90, 'charlie': 75}
    return dict(sorted(my_dict.items(), key=lambda x: x[1]))

# 48. Find key with maximum value
def solution_48():
    my_dict = {'x': 10, 'y': 25, 'z': 15}
    return max(my_dict, key=my_dict.get)

# 49. Find key with minimum value
def solution_49():
    my_dict = {'p': 8, 'q': 3, 'r': 12}
    return min(my_dict, key=my_dict.get)

# 50. Group words by first letter
def solution_50():
    words = ['apple', 'banana', 'cherry', 'apricot']
    groups = {}
    for word in words:
        first_letter = word[0]
        if first_letter not in groups:
            groups[first_letter] = []
        groups[first_letter].append(word)
    return groups

# 51. Invert dictionary (swap keys and values)
def solution_51():
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    return {value: key for key, value in my_dict.items()}

# 52. Filter dictionary by values
def solution_52():
    my_dict = {'a': 10, 'b': 5, 'c': 15, 'd': 8}
    return {k: v for k, v in my_dict.items() if v > 7}

# 53. Create dictionary of word lengths
def solution_53():
    words = ['cat', 'elephant', 'dog']
    return {word: len(word) for word in words}

# 54. Combine dictionaries by extending lists
def solution_54():
    dict1 = {'a': [1, 2]}
    dict2 = {'a': [3, 4], 'b': [5]}
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            result[key].extend(value)
        else:
            result[key] = value
    return result

# 55. Get all keys from nested dictionary
def solution_55():
    my_dict = {'outer': {'inner1': 1, 'inner2': 2}}
    keys = []
    def get_keys(d, key_list):
        for key, value in d.items():
            key_list.append(key)
            if isinstance(value, dict):
                get_keys(value, key_list)
    get_keys(my_dict, keys)
    return keys

# 56. Count vowels and consonants
def solution_56():
    text = 'programming'
    vowels = 'aeiouAEIOU'
    counts = {'vowels': 0, 'consonants': 0}
    for char in text:
        if char.isalpha():
            if char in vowels:
                counts['vowels'] += 1
            else:
                counts['consonants'] += 1
    return counts

# 57. Calculate average from grades dictionary
def solution_57():
    grades = {'alice': 85, 'bob': 92, 'charlie': 78}
    return sum(grades.values()) / len(grades)

# 58. Remove keys with None values
def solution_58():
    my_dict = {'a': 1, 'b': None, 'c': 3, 'd': None}
    return {k: v for k, v in my_dict.items() if v is not None}

# 59. Dictionary comprehension for even numbers
def solution_59():
    return {x: 'even' for x in range(10) if x % 2 == 0}

# 60. Transform dictionary values to uppercase
def solution_60():
    my_dict = {'a': 'hello', 'b': 'world'}
    return {k: v.upper() for k, v in my_dict.items()}

# 61. Find common keys between dictionaries
def solution_61():
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'b': 4, 'c': 5, 'd': 6}
    return list(set(dict1.keys()) & set(dict2.keys()))

# 62. Create frequency counter using dict comprehension
def solution_62():
    data = [1, 2, 2, 3, 3, 3]
    return {item: data.count(item) for item in set(data)}

# 63. Merge multiple dictionaries
def solution_63():
    dicts = [{'a': 1}, {'b': 2}, {'c': 3}]
    result = {}
    for d in dicts:
        result.update(d)
    return result

# 64. Extract subset of dictionary
def solution_64():
    my_dict = {'name': 'John', 'age': 30, 'city': 'NYC'}
    keys = ['name', 'city']
    return {k: my_dict[k] for k in keys if k in my_dict}

# 65. Create nested dictionary from flat dict
def solution_65():
    flat_dict = {'a.b': 1, 'a.c': 2, 'b.d': 3}
    nested = {}
    for key, value in flat_dict.items():
        parts = key.split('.')
        current = nested
        for part in parts[:-1]:
            if part not in current:
                current[part] = {}
            current = current[part]
        current[parts[-1]] = value
    return nested

# 66. Sum values for each key across multiple dicts
def solution_66():
    dicts = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]
    result = {}
    for d in dicts:
        for key, value in d.items():
            result[key] = result.get(key, 0) + value
    return result

# 67. Sort dictionary by values in descending order
def solution_67():
    my_dict = {'x': 10, 'y': 30, 'z': 20}
    return dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))

# 68. Create dictionary from zip with duplicate handling
def solution_68():
    keys = [1, 2, 2, 3]
    values = ['a', 'b', 'c', 'd']
    # This will keep the last occurrence of each key
    return dict(zip(keys, values))

# 69. Find keys where value > threshold
def solution_69():
    my_dict = {'a': 10, 'b': 5, 'c': 15}
    return [k for k, v in my_dict.items() if v > 7]

# 70. Update nested dictionary
def solution_70():
    my_dict = {'person': {'name': 'Alice', 'age': 25}}
    my_dict['person']['phone'] = '123-456'
    return my_dict

# 71. Count unique words in text
def solution_71():
    text = 'the cat and the dog'
    words = text.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

# 72. Create multiplication table dictionary
def solution_72():
    return {i: {j: i*j for j in range(1, 4)} for i in range(1, 4)}

# 73. Swap keys and values
def solution_73():
    my_dict = {'name': 'John', 'age': '30'}
    return {v: k for k, v in my_dict.items()}

# 74. Group students by grade
def solution_74():
    students = [{'name': 'A', 'grade': 'B'}, {'name': 'C', 'grade': 'A'}, {'name': 'D', 'grade': 'B'}]
    groups = {}
    for student in students:
        grade = student['grade']
        if grade not in groups:
            groups[grade] = []
        groups[grade].append(student['name'])
    return groups

# 75. Find intersection of dictionary values
def solution_75():
    my_dict = {'a': [1, 2, 3], 'b': [2, 3, 4]}
    values = list(my_dict.values())
    if len(values) < 2:
        return []
    intersection = set(values[0])
    for value_list in values[1:]:
        intersection = intersection.intersection(set(value_list))
    return list(intersection)

# 76. Create running sum dictionary
def solution_76():
    data = [1, 2, 3, 4, 5]
    running_sum = 0
    result = {}
    for num in data:
        running_sum += num
        result[num] = running_sum
    return result

# 77. Validate dictionary structure
def solution_77():
    data_dict = {'name': 'John', 'age': 25}
    type_dict = {'name': str, 'age': int}
    return all(isinstance(data_dict.get(k), v) for k, v in type_dict.items())

# 78. Create pivot table
def solution_78():
    data = [{'name': 'A', 'subject': 'math', 'score': 90}]
    result = {}
    for record in data:
        name = record['name']
        subject = record['subject']
        score = record['score']
        if name not in result:
            result[name] = {}
        result[name][subject] = score
    return result

# 79. Calculate percentage distribution
def solution_79():
    my_dict = {'apples': 20, 'oranges': 30, 'bananas': 50}
    total = sum(my_dict.values())
    return {k: (v / total) * 100 for k, v in my_dict.items()}

# 80. Find most frequent element
def solution_80():
    data = ['a', 'b', 'a', 'c', 'a']
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    return max(freq, key=freq.get)

# ===============================
# ADVANCED LEVEL (Questions 81-100)
# ===============================

# 81. Use defaultdict to group words by length
def solution_81():
    words = ['cat', 'elephant', 'dog', 'bird']
    groups = defaultdict(list)
    for word in words:
        groups[len(word)].append(word)
    return groups

# 82. Use Counter to find most common elements
def solution_82():
    data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    counter = Counter(data)
    return counter.most_common(3)

# 83. Flatten nested dictionary with dot notation
def solution_83():
    def flatten_dict(d, parent_key='', sep='.'):
        items = []
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(flatten_dict(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)

    my_dict = {'a': {'b': {'c': 1, 'd': 2}}, 'e': 3}
    return flatten_dict(my_dict)

# 84. Create reverse lookup dictionary
def solution_84():
    my_dict = {'a': [1, 2], 'b': [2, 3]}
    reverse_lookup = defaultdict(list)
    for key, values in my_dict.items():
        for value in values:
            reverse_lookup[value].append(key)
    return dict(reverse_lookup)

# 85. Dictionary with tuple keys for coordinates
def solution_85():
    return {(0, 0): 'origin', (1, 1): 'diagonal'}

# 86. Deep merge dictionaries with numeric value summing
def solution_86():
    def deep_merge(dict1, dict2):
        result = dict1.copy()
        for key, value in dict2.items():
            if key in result:
                if isinstance(result[key], dict) and isinstance(value, dict):
                    result[key] = deep_merge(result[key], value)
                elif isinstance(result[key], (int, float)) and isinstance(value, (int, float)):
                    result[key] = result[key] + value
                else:
                    result[key] = value
            else:
                result[key] = value
        return result

    dict1 = {'a': {'x': 1, 'y': 2}}
    dict2 = {'a': {'x': 3, 'z': 4}}
    return deep_merge(dict1, dict2)

# 87. Transform nested list to dict with list values
def solution_87():
    data = [['a', 1], ['b', 2], ['a', 3]]
    result = defaultdict(list)
    for key, value in data:
        result[key].append(value)
    return dict(result)

# 88. Conditional dictionary comprehension
def solution_88():
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    return {k: v for k, v in my_dict.items() if k != 'b' and v > 1}

# 89. Sliding window frequency counter
def solution_89():
    text = 'abcabc'
    window_size = 3
    freq = defaultdict(int)
    for i in range(len(text) - window_size + 1):
        window = text[i:i + window_size]
        freq[window] += 1
    return dict(freq)

# 90. Use defaultdict(Counter) for character frequencies per word
def solution_90():
    words = ['hello', 'world']
    word_char_freq = defaultdict(Counter)
    for word in words:
        word_char_freq[word] = Counter(word)
    return word_char_freq

# 91. Sort by multiple criteria
def solution_91():
    my_dict = {'b': 2, 'a': 2, 'c': 1}
    # Sort by value desc, then by key asc
    return dict(sorted(my_dict.items(), key=lambda x: (-x[1], x[0])))

# 92. Dictionary of sets for many-to-many relationships
def solution_92():
    relationships = [('Alice', 'Math'), ('Bob', 'Math'), ('Alice', 'Science')]
    student_courses = defaultdict(set)
    for student, course in relationships:
        student_courses[student].add(course)
    return dict(student_courses)

# 93. LRU cache using OrderedDict
def solution_93():
    class LRUCache:
        def __init__(self, capacity: int):
            self.capacity = capacity
            self.cache = OrderedDict()

        def get(self, key: int):
            if key in self.cache:
                self.cache.move_to_end(key)
                return self.cache[key]
            return None

        def put(self, key: int, value):
            if key in self.cache:
                self.cache.move_to_end(key)
            elif len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
            self.cache[key] = value

        def get_cache(self):
            return self.cache

    # Simulate operations
    lru = LRUCache(3)
    lru.get(1)
    lru.put(1, 'a')
    lru.put(2, 'b')
    lru.get(1)
    lru.put(3, 'c')
    lru.put(4, 'd')
    return lru.get_cache()

# 94. Extract all 'id' fields recursively
def solution_94():
    def extract_ids(obj):
        ids = []
        if isinstance(obj, dict):
            if 'id' in obj:
                ids.append(obj['id'])
            for value in obj.values():
                ids.extend(extract_ids(value))
        elif isinstance(obj, list):
            for item in obj:
                ids.extend(extract_ids(item))
        return ids

    data = {'users': [{'id': 1, 'profile': {'id': 2}}, {'id': 3}]}
    return extract_ids(data)

# 95. Frequency distribution with percentiles
def solution_95():
    data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    freq = Counter(data)
    total = len(data)
    return {k: {'count': v, 'percentage': (v / total) * 100} for k, v in freq.items()}

# 96. Custom dictionary with lowercase keys
def solution_96():
    class CustomDict(dict):
        def __setitem__(self, key, value):
            if isinstance(key, str):
                key = key.lower()
            super().__setitem__(key, value)

        def __init__(self, *args, **kwargs):
            super().__init__()
            if args:
                if len(args) == 1 and isinstance(args[0], dict):
                    for key, value in args[0].items():
                        self[key] = value
            for key, value in kwargs.items():
                self[key] = value

    return CustomDict({'Name': 'John', 'AGE': 30})

# 97. Word co-occurrence matrix
def solution_97():
    sentence = 'the cat sat on the mat'
    words = sentence.split()
    window = 2
    cooccurrence = defaultdict(lambda: defaultdict(int))

    for i, word in enumerate(words):
        for j in range(max(0, i - window), min(len(words), i + window + 1)):
            if i != j:
                cooccurrence[word][words[j]] += 1

    return {k: dict(v) for k, v in cooccurrence.items()}

# 98. Merge dicts with conflict resolution
def solution_98():
    dicts = [{'a': 1, 'b': 'x'}, {'a': 2, 'b': 'y', 'c': 3}]
    result = {}

    for d in dicts:
        for key, value in d.items():
            if key in result:
                if isinstance(result[key], (int, float)) and isinstance(value, (int, float)):
                    result[key] += value
                elif isinstance(result[key], str) and isinstance(value, str):
                    result[key] = f"{result[key]}|{value}"
            else:
                result[key] = value

    return result

# 99. Transform hierarchical to flat and vice versa
def solution_99():
    def flatten_hierarchical(d, separator='/'):
        def _flatten(obj, parent_key=''):
            items = []
            if isinstance(obj, dict):
                for k, v in obj.items():
                    new_key = f"{parent_key}{separator}{k}" if parent_key else k
                    if isinstance(v, dict):
                        items.extend(_flatten(v, new_key).items())
                    else:
                        items.append((new_key, v))
            return dict(items)
        return _flatten(d)

    data = {'a': {'b': {'c': 1}}}
    return flatten_hierarchical(data)

# 100. Dictionary-based state machine
def solution_100():
    class StateMachine:
        def __init__(self, states, transitions, initial_state=None):
            self.states = states
            self.transitions = transitions
            self.current = initial_state or states[0] if states else None
            self.history = []

        def transition(self, new_state):
            if new_state in self.transitions.get(self.current, []):
                self.history.append(self.current)
                self.current = new_state
                return True
            return False

        def to_dict(self):
            return {
                'current': self.current,
                'transitions': self.transitions,
                'history': self.history
            }

    states = ['A', 'B', 'C']
    transitions = {'A': ['B'], 'B': ['C'], 'C': ['A']}
    sm = StateMachine(states, transitions, 'A')
    return sm.to_dict()

# Test function to run specific solutions
def test_solution(solution_num: int):
    """Test a specific solution by number"""
    function_name = f"solution_{solution_num}"
    if function_name in globals():
        try:
            result = globals()[function_name]()
            print(f"Solution {solution_num}: {result}")
            return result
        except Exception as e:
            print(f"Error in solution {solution_num}: {e}")
            return None
    else:
        print(f"Solution {solution_num} not found")
        return None

# Example usage:
if __name__ == "__main__":
    # Test a few solutions
    print("Testing some solutions:")
    test_solution(1)
    test_solution(43)
    test_solution(81)
    test_solution(100)
