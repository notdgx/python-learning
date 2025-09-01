# 100 Python String Solutions

# Basic Level (1-40)

# 1. Reverse a String
def reverse_string(s):
    return s[::-1]

# 2. Count Characters
def count_characters(s):
    return len(s.replace(' ', ''))

# 3. First and Last Character
def first_last_char(s):
    if len(s) == 0:
        return ""
    return s[0] + s[-1]

# 4. String Length Without len()
def string_length(s):
    count = 0
    for char in s:
        count += 1
    return count

# 5. Check if String Contains Only Digits
def is_only_digits(s):
    return s.isdigit()

# 6. Convert to Uppercase
def to_uppercase(s):
    return s.upper()

# 7. Count Vowels
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# 8. Remove Spaces
def remove_spaces(s):
    return s.replace(' ', '')

# 9. Check Empty String
def is_empty_or_whitespace(s):
    return s.strip() == ""

# 10. String Slicing Practice
def every_second_char(s):
    return s[::2]

# 11. Count Specific Character
def count_specific_char(s, char):
    return s.count(char)

# 12. String Comparison (Case Insensitive)
def case_insensitive_compare(s1, s2):
    return s1.lower() == s2.lower()

# 13. Extract Numbers from String
def extract_numbers(s):
    return ''.join(char for char in s if char.isdigit())

# 14. Check if String is Alphabetic
def is_alphabetic(s):
    return s.isalpha()

# 15. Repeat String N Times
def repeat_string(s, n, separator):
    return separator.join([s] * n)

# 16. Find Character at Index
def char_at_index(s, index):
    if 0 <= index < len(s):
        return s[index]
    return None

# 17. Check String Starts With
def starts_with(s, prefix):
    return s.startswith(prefix)

# 18. Check String Ends With
def ends_with(s, suffix):
    return s.endswith(suffix)

# 19. Convert Snake Case to Title
def snake_to_title(s):
    return ' '.join(word.capitalize() for word in s.split('_'))

# 20. Count Words
def count_words(s):
    return len(s.split())

# 21. Check Palindrome (Simple)
def is_palindrome_simple(s):
    return s == s[::-1]

# 22. Remove Character
def remove_character(s, char):
    return s.replace(char, '')

# 23. String to List of Characters
def string_to_char_list(s):
    return list(s)

# 24. Join List to String
def join_list_to_string(char_list, delimiter):
    return delimiter.join(char_list)

# 25. Check if All Characters are Same
def all_same_chars(s):
    return len(set(s)) <= 1

# 26. Get Middle Character(s)
def get_middle_chars(s):
    length = len(s)
    if length % 2 == 0:
        return s[length//2-1:length//2+1]
    else:
        return s[length//2]

# 27. Capitalize First Letter
def capitalize_first(s):
    if not s:
        return s
    return s[0].upper() + s[1:]

# 28. Check if String Contains Substring
def contains_substring(s, substring):
    return substring in s

# 29. String Rotation Check (Basic)
def is_rotation(s1, s2):
    return len(s1) == len(s2) and s1 in s2 + s2

# 30. Remove Duplicates (Preserve Order)
def remove_duplicates_preserve_order(s):
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

# 31. Count Consonants
def count_consonants(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char.isalpha() and char not in vowels)

# 32. Swap Case
def swap_case(s):
    return s.swapcase()

# 33. Find First Non-Repeated Character
def first_non_repeated_char(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    for char in s:
        if char_count[char] == 1:
            return char
    return None

# 34. String Padding
def string_padding(s, length, char):
    if len(s) >= length:
        return s
    padding_needed = length - len(s)
    left_padding = padding_needed // 2
    right_padding = padding_needed - left_padding
    return char * left_padding + s + char * right_padding

# 35. Check if String is Numeric
def is_numeric(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# 36. Extract Alphabetic Characters
def extract_alphabetic(s):
    return ''.join(char for char in s if char.isalpha())

# 37. Count Lines in String
def count_lines(s):
    return s.count('\n') + 1 if s else 0

# 38. Check if Two Strings Have Same Characters
def same_characters(s1, s2):
    return set(s1) == set(s2)

# 39. Find Longest Word
def find_longest_word(s):
    words = s.split()
    return max(words, key=len) if words else ""

# 40. Replace Character at Specific Index
def replace_char_at_index(s, index, new_char):
    if 0 <= index < len(s):
        return s[:index] + new_char + s[index+1:]
    return s

# Intermediate Level (41-80)

# 41. String Compression
def string_compression(s):
    if not s:
        return ""
    result = []
    current_char = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(current_char + str(count))
            current_char = s[i]
            count = 1
    result.append(current_char + str(count))
    return ''.join(result)

# 42. Expand Compressed String
def expand_compressed_string(s):
    result = []
    i = 0
    while i < len(s):
        char = s[i]
        i += 1
        count_str = ""
        while i < len(s) and s[i].isdigit():
            count_str += s[i]
            i += 1
        count = int(count_str) if count_str else 1
        result.append(char * count)
    return ''.join(result)

# 43. Word Frequency Counter
def word_frequency_counter(s):
    words = s.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

# 44. Reverse Words in Sentence
def reverse_words(s):
    return ' '.join(s.split()[::-1])

# 45. Remove Extra Spaces
def remove_extra_spaces(s):
    return ' '.join(s.split())

# 46. Check if Strings are Anagrams
def are_anagrams(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

# 47. Find All Substrings
def find_all_substrings(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])
    return substrings

# 48. Longest Common Prefix
def longest_common_prefix(strings):
    if not strings:
        return ""
    prefix = strings[0]
    for s in strings[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

# 49. String Rotation with K positions
def rotate_string_left(s, k):
    if not s:
        return s
    k = k % len(s)
    return s[k:] + s[:k]

# 50. Check Balanced Parentheses
def is_balanced_parentheses(s):
    count = 0
    for char in s:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            if count < 0:
                return False
    return count == 0

# 51. Convert CamelCase to Snake Case
def camel_to_snake(s):
    result = []
    for i, char in enumerate(s):
        if char.isupper() and i > 0:
            result.append('_')
        result.append(char.lower())
    return ''.join(result)

# 52. Find Missing Characters for Pangram
def missing_pangram_chars(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    present = set(s.lower())
    missing = alphabet - present
    return ''.join(sorted(missing))

# 53. String Interleaving
def interleave_strings(s1, s2):
    result = []
    min_len = min(len(s1), len(s2))
    for i in range(min_len):
        result.append(s1[i])
        result.append(s2[i])
    result.append(s1[min_len:])
    result.append(s2[min_len:])
    return ''.join(result)

# 54. Remove Palindromic Substrings
def remove_palindromic_substrings(s):
    # Simple implementation - remove longest palindromic substring
    def is_palindrome(string):
        return string == string[::-1]
    
    for length in range(len(s), 1, -1):
        for i in range(len(s) - length + 1):
            substring = s[i:i+length]
            if is_palindrome(substring):
                return s[:i] + s[i+length:]
    return s

# 55. Count Character Frequency
def char_frequency(s):
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency

# 56. Check if String is Subsequence
def is_subsequence(s, t):
    i = 0
    for char in t:
        if i < len(s) and char == s[i]:
            i += 1
    return i == len(s)

# 57. Find Unique Characters
def find_unique_chars(s):
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

# 58. String Difference
def string_difference(s1, s2):
    set2 = set(s2)
    return ''.join(char for char in s1 if char not in set2)

# 59. Zigzag String Conversion
def zigzag_conversion(s, num_rows):
    if num_rows == 1:
        return s
    rows = [''] * min(num_rows, len(s))
    current_row = 0
    going_down = False
    
    for char in s:
        rows[current_row] += char
        if current_row == 0 or current_row == num_rows - 1:
            going_down = not going_down
        current_row += 1 if going_down else -1
    
    return ''.join(rows)

# 60. Find Repeating Character Pattern
def find_repeating_pattern(s):
    for length in range(1, len(s) // 2 + 1):
        pattern = s[:length]
        if pattern * (len(s) // length) == s[:length * (len(s) // length)]:
            if len(s) % length == 0:
                return pattern
    return s

# 61. Validate Email Format (Basic)
def validate_email_basic(email):
    return '@' in email and '.' in email.split('@')[-1]

# 62. Extract Domain from Email
def extract_domain(email):
    if '@' in email:
        return email.split('@')[-1]
    return ""

# 63. Count Substring Occurrences
def count_substring_occurrences(s, substring):
    count = 0
    start = 0
    while True:
        pos = s.find(substring, start)
        if pos == -1:
            break
        count += 1
        start = pos + len(substring)
    return count

# 64. Title Case Conversion
def title_case_conversion(s):
    return s.title()

# 65. Check Strong Password
def check_strong_password(password):
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return has_upper and has_lower and has_digit

# 66. Format Phone Number
def format_phone_number(number):
    if len(number) == 10:
        return f"({number[:3]}) {number[3:6]}-{number[6:]}"
    return number

# 67. Split String by Multiple Delimiters
def split_by_multiple_delimiters(s, delimiters):
    import re
    pattern = '[' + ''.join(re.escape(d) for d in delimiters) + ']'
    return re.split(pattern, s)

# 68. Find Common Characters
def find_common_characters(strings):
    if not strings:
        return ""
    common = set(strings[0])
    for s in strings[1:]:
        common &= set(s)
    return ''.join(sorted(common))

# 69. String Permutation Check
def is_permutation(s1, s2):
    return sorted(s1) == sorted(s2)

# 70. Remove HTML Tags
def remove_html_tags(s):
    import re
    return re.sub(r'<.*?>', '', s)

# 71. Caesar Cipher Encode
def caesar_cipher_encode(s, shift):
    result = []
    for char in s:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - ascii_offset + shift) % 26
            result.append(chr(shifted + ascii_offset))
        else:
            result.append(char)
    return ''.join(result)

# 72. Caesar Cipher Decode
def caesar_cipher_decode(s, shift):
    return caesar_cipher_encode(s, -shift)

# 73. Find Shortest Word
def find_shortest_word(s):
    words = s.split()
    return min(words, key=len) if words else ""

# 74. Check if String Has Unique Characters
def has_unique_characters(s):
    return len(s) == len(set(s))

# 75. String Distance (Hamming)
def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        return -1
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

# 76. Extract Initials
def extract_initials(name):
    return ''.join(word[0].upper() for word in name.split() if word)

# 77. Check Palindrome (Ignore Case and Spaces)
def is_palindrome_ignore_case_spaces(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

# 78. Find Longest Palindromic Substring
def longest_palindromic_substring(s):
    if not s:
        return ""
    
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
    
    longest = ""
    for i in range(len(s)):
        palindrome1 = expand_around_center(i, i)
        palindrome2 = expand_around_center(i, i + 1)
        current_longest = palindrome1 if len(palindrome1) > len(palindrome2) else palindrome2
        if len(current_longest) > len(longest):
            longest = current_longest
    
    return longest

# 79. Convert Number to Words
def number_to_words(num_str):
    num = int(num_str)
    if num == 0:
        return "zero"
    
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    if num < 10:
        return ones[num]
    elif num < 20:
        return teens[num - 10]
    elif num < 100:
        return tens[num // 10] + ("" if num % 10 == 0 else " " + ones[num % 10])
    
    return num_str

# 80. Validate Parentheses with Multiple Types
def validate_multiple_parentheses(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        elif char in mapping.values():
            stack.append(char)
    
    return not stack

# Advanced/Tricky Level (81-100)

# 81. Longest Substring Without Repeating Characters
def longest_substring_without_repeating(s):
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length

# 82. Group Anagrams
def group_anagrams(strings):
    anagram_groups = {}
    for s in strings:
        key = ''.join(sorted(s))
        if key not in anagram_groups:
            anagram_groups[key] = []
        anagram_groups[key].append(s)
    return list(anagram_groups.values())

# 83. Minimum Window Substring
def minimum_window_substring(s, t):
    from collections import Counter
    
    if not s or not t:
        return ""
    
    dict_t = Counter(t)
    required = len(dict_t)
    left, right = 0, 0
    formed = 0
    window_counts = {}
    ans = float("inf"), None, None
    
    while right < len(s):
        character = s[right]
        window_counts[character] = window_counts.get(character, 0) + 1
        
        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1
        
        while left <= right and formed == required:
            character = s[left]
            
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
            
            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1
            
            left += 1
        
        right += 1
    
    return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]

# 84. Regular Expression Matching (Basic)
def regex_match_basic(s, p):
    def match_helper(i, j):
        if j == len(p):
            return i == len(s)
        
        first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')
        
        if j + 1 < len(p) and p[j + 1] == '*':
            return match_helper(i, j + 2) or (first_match and match_helper(i + 1, j))
        else:
            return first_match and match_helper(i + 1, j + 1)
    
    return match_helper(0, 0)

# 85. Edit Distance (Levenshtein)
def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    
    return dp[m][n]

# 86. Longest Common Subsequence
def longest_common_subsequence(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

# 87. String Matching with Wildcards
def wildcard_match(s, p):
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    
    for j in range(1, n + 1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-1]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j-1] == s[i-1] or p[j-1] == '?':
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*':
                dp[i][j] = dp[i-1][j] or dp[i][j-1]
    
    return dp[m][n]

# 88. Find All Palindromic Substrings
def find_all_palindromic_substrings(s):
    def expand_around_center(left, right):
        palindromes = []
        while left >= 0 and right < len(s) and s[left] == s[right]:
            palindromes.append(s[left:right+1])
            left -= 1
            right += 1
        return palindromes
    
    result = []
    for i in range(len(s)):
        result.extend(expand_around_center(i, i))
        result.extend(expand_around_center(i, i + 1))
    
    return result

# 89. Decode String with Numbers
def decode_string(s):
    stack = []
    current_string = ""
    current_num = 0
    
    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append((current_string, current_num))
            current_string = ""
            current_num = 0
        elif char == ']':
            prev_string, num = stack.pop()
            current_string = prev_string + current_string * num
        else:
            current_string += char
    
    return current_string

# 90. KMP String Search
def kmp_search(text, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
    
    if not pattern:
        return 0
    
    lps = compute_lps(pattern)
    i = j = 0
    
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == len(pattern):
            return i - j
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return -1

# 91. Manacher's Algorithm (Longest Palindrome)
def manacher_longest_palindrome(s):
    # Transform string
    transformed = '#'.join('^{}$'.format(s))
    n = len(transformed)
    p = [0] * n
    center = right = 0
    
    for i in range(1, n - 1):
        mirror = 2 * center - i
        
        if i < right:
            p[i] = min(right - i, p[mirror])
        
        while transformed[i + (1 + p[i])] == transformed[i - (1 + p[i])]:
            p[i] += 1
        
        if i + p[i] > right:
            center, right = i, i + p[i]
    
    max_len = max(p[1:-1])
    center_index = p.index(max_len)
    start = (center_index - max_len) // 2
    
    return s[start:start + max_len]

# 92. String Compression with Run Length Encoding
def advanced_string_compression(s):
    if not s:
        return ""
    
    compressed = []
    i = 0
    
    while i < len(s):
        current_char = s[i]
        count = 1
        
        while i + 1 < len(s) and s[i + 1] == current_char:
            count += 1
            i += 1
        
        compressed.append(current_char + str(count))
        i += 1
    
    compressed_str = ''.join(compressed)
    return compressed_str if len(compressed_str) < len(s) else s

# 93. Check if String Follows Pattern
def follows_pattern(s, pattern):
    words = s.split()
    if len(words) != len(pattern):
        return False
    
    char_to_word = {}
    word_to_char = {}
    
    for char, word in zip(pattern, words):
        if char in char_to_word:
            if char_to_word[char] != word:
                return False
        else:
            char_to_word[char] = word
        
        if word in word_to_char:
            if word_to_char[word] != char:
                return False
        else:
            word_to_char[word] = char
    
    return True

# 94. Generate All Valid Parentheses
def generate_parentheses(n):
    result = []
    
    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append(current)
            return
        
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)
    
    backtrack('', 0, 0)
    return result

# 95. Word Break Problem
def word_break(s, word_dict):
    word_set = set(word_dict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    
    return dp[len(s)]

# 96. Palindrome Partitioning
def palindrome_partitioning(s):
    def is_palindrome(string):
        return string == string[::-1]
    
    def backtrack(start, path):
        if start == len(s):
            result.append(path[:])
            return
        
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                path.append(substring)
                backtrack(end, path)
                path.pop()
    
    result = []
    backtrack(0, [])
    return result

# 97. Text Justification
def text_justification(words, max_width):
    result = []
    current_line = []
    current_length = 0
    
    for word in words:
        if current_length + len(word) + len(current_line) > max_width:
            # Justify current line
            if len(current_line) == 1:
                line = current_line[0] + ' ' * (max_width - len(current_line[0]))
            else:
                total_spaces = max_width - current_length
                gaps = len(current_line) - 1
                space_per_gap = total_spaces // gaps
                extra_spaces = total_spaces % gaps
                
                line = ""
                for i in range(len(current_line) - 1):
                    line += current_line[i] + ' ' * space_per_gap
                    if i < extra_spaces:
                        line += ' '
                line += current_line[-1]
            
            result.append(line)
            current_line = [word]
            current_length = len(word)
        else:
            current_line.append(word)
            current_length += len(word)
    
    # Handle last line (left-justified)
    if current_line:
        last_line = ' '.join(current_line)
        last_line += ' ' * (max_width - len(last_line))
        result.append(last_line)
    
    return result

# 98. Sliding Window Maximum in String
def sliding_window_max_string(s, k):
    if not s or k <= 0:
        return ""
    
    max_substring = ""
    for i in range(len(s) - k + 1):
        substring = s[i:i + k]
        if substring > max_substring:
            max_substring = substring
    
    return max_substring

# 99. Interleaving String Check
def is_interleaving(s1, s2, s3):
    if len(s1) + len(s2) != len(s3):
        return False
    
    dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    dp[0][0] = True
    
    for i in range(1, len(s1) + 1):
        dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
    
    for j in range(1, len(s2) + 1):
        dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
    
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or \
                       (dp[i][j-1] and s2[j-1] == s3[i+j-1])
    
    return dp[len(s1)][len(s2)]

# 100. Shortest Superstring Problem
def shortest_superstring(strings):
    def overlap(s1, s2):
        max_overlap = 0
        for i in range(1, min(len(s1), len(s2)) + 1):
            if s1[-i:] == s2[:i]:
                max_overlap = i
        return max_overlap
    
    def merge(s1, s2, overlap_len):
        return s1 + s2[overlap_len:]
    
    while len(strings) > 1:
        max_overlap = -1
        merge_indices = (0, 1)
        
        for i in range(len(strings)):
            for j in range(len(strings)):
                if i != j:
                    o = overlap(strings[i], strings[j])
                    if o > max_overlap:
                        max_overlap = o
                        merge_indices = (i, j)
        
        i, j = merge_indices
        merged = merge(strings[i], strings[j], max_overlap)
        strings = [s for k, s in enumerate(strings) if k != i and k != j] + [merged]
    
    return strings[0]