# 100 Python String Coding Questions

## Basic Level (1-40)

1. **Reverse a String**
   - Write a function to reverse a given string.
   - Input: "hello"
   - Output: "olleh"

2. **Count Characters**
   - Count the number of characters in a string (excluding spaces).
   - Input: "hello world"
   - Output: 10

3. **First and Last Character**
   - Return the first and last character of a string concatenated.
   - Input: "python"
   - Output: "pn"

4. **String Length Without len()**
   - Find the length of a string without using the len() function.
   - Input: "coding"
   - Output: 6

5. **Check if String Contains Only Digits**
   - Check if a string contains only numeric digits.
   - Input: "12345"
   - Output: True

6. **Convert to Uppercase**
   - Convert all lowercase letters in a string to uppercase.
   - Input: "Hello World"
   - Output: "HELLO WORLD"

7. **Count Vowels**
   - Count the number of vowels in a string.
   - Input: "programming"
   - Output: 3

8. **Remove Spaces**
   - Remove all spaces from a string.
   - Input: "hello world python"
   - Output: "helloworldpython"

9. **Check Empty String**
   - Check if a string is empty or contains only whitespace.
   - Input: "   "
   - Output: True

10. **String Slicing Practice**
    - Extract every second character from a string.
    - Input: "abcdef"
    - Output: "ace"

11. **Count Specific Character**
    - Count occurrences of a specific character in a string.
    - Input: "hello", character: "l"
    - Output: 2

12. **String Comparison (Case Insensitive)**
    - Compare two strings ignoring case sensitivity.
    - Input: "Hello", "HELLO"
    - Output: True

13. **Extract Numbers from String**
    - Extract all numeric characters from a string.
    - Input: "abc123def456"
    - Output: "123456"

14. **Check if String is Alphabetic**
    - Check if a string contains only alphabetic characters.
    - Input: "HelloWorld"
    - Output: True

15. **Repeat String N Times**
    - Repeat a string n times with a separator.
    - Input: "hi", n=3, separator="-"
    - Output: "hi-hi-hi"

16. **Find Character at Index**
    - Return the character at a given index, handle out of bounds.
    - Input: "python", index=2
    - Output: "t"

17. **Check String Starts With**
    - Check if a string starts with a given prefix.
    - Input: "hello world", prefix="hello"
    - Output: True

18. **Check String Ends With**
    - Check if a string ends with a given suffix.
    - Input: "python.py", suffix=".py"
    - Output: True

19. **Convert Snake Case to Title**
    - Convert snake_case string to Title Case.
    - Input: "hello_world_python"
    - Output: "Hello World Python"

20. **Count Words**
    - Count the number of words in a string.
    - Input: "hello world python"
    - Output: 3

21. **Check Palindrome (Simple)**
    - Check if a string is a palindrome (case sensitive).
    - Input: "racecar"
    - Output: True

22. **Remove Character**
    - Remove all occurrences of a specific character from a string.
    - Input: "hello world", character="l"
    - Output: "heo word"

23. **String to List of Characters**
    - Convert a string to a list of its characters.
    - Input: "abc"
    - Output: ['a', 'b', 'c']

24. **Join List to String**
    - Join a list of strings with a delimiter.
    - Input: ['a', 'b', 'c'], delimiter="-"
    - Output: "a-b-c"

25. **Check if All Characters are Same**
    - Check if all characters in a string are the same.
    - Input: "aaaa"
    - Output: True

26. **Get Middle Character(s)**
    - Return the middle character(s) of a string.
    - Input: "python"
    - Output: "th"

27. **Capitalize First Letter**
    - Capitalize only the first letter of a string.
    - Input: "hello world"
    - Output: "Hello world"

28. **Check if String Contains Substring**
    - Check if a string contains a given substring.
    - Input: "hello world", substring="wor"
    - Output: True

29. **String Rotation Check (Basic)**
    - Check if one string is a rotation of another (simple case).
    - Input: "abcde", "cdeab"
    - Output: True

30. **Remove Duplicates (Preserve Order)**
    - Remove duplicate characters while preserving order.
    - Input: "aabbcc"
    - Output: "abc"

31. **Count Consonants**
    - Count the number of consonants in a string.
    - Input: "hello"
    - Output: 3

32. **Swap Case**
    - Swap the case of each character in a string.
    - Input: "Hello World"
    - Output: "hELLO wORLD"

33. **Find First Non-Repeated Character**
    - Find the first character that appears only once.
    - Input: "abccba"
    - Output: None (or empty string)

34. **String Padding**
    - Pad a string to a specific length with a character.
    - Input: "hello", length=10, char="*"
    - Output: "***hello**"

35. **Check if String is Numeric**
    - Check if a string represents a valid number (including decimals).
    - Input: "123.45"
    - Output: True

36. **Extract Alphabetic Characters**
    - Extract only alphabetic characters from a string.
    - Input: "abc123def456"
    - Output: "abcdef"

37. **Count Lines in String**
    - Count the number of lines in a multi-line string.
    - Input: "line1\nline2\nline3"
    - Output: 3

38. **Check if Two Strings Have Same Characters**
    - Check if two strings contain the same set of characters.
    - Input: "abc", "bca"
    - Output: True

39. **Find Longest Word**
    - Find the longest word in a sentence.
    - Input: "The quick brown fox"
    - Output: "quick"

40. **Replace Character at Specific Index**
    - Replace a character at a specific index with another character.
    - Input: "hello", index=1, new_char="a"
    - Output: "hallo"

## Intermediate Level (41-80)

41. **String Compression**
    - Compress a string by counting consecutive characters.
    - Input: "aaabbcc"
    - Output: "a3b2c2"

42. **Expand Compressed String**
    - Expand a compressed string back to original form.
    - Input: "a3b2c2"
    - Output: "aaabbcc"

43. **Word Frequency Counter**
    - Count frequency of each word in a sentence.
    - Input: "hello world hello"
    - Output: {'hello': 2, 'world': 1}

44. **Reverse Words in Sentence**
    - Reverse the order of words in a sentence.
    - Input: "hello world python"
    - Output: "python world hello"

45. **Remove Extra Spaces**
    - Remove extra spaces between words, keep single spaces.
    - Input: "hello    world   python"
    - Output: "hello world python"

46. **Check if Strings are Anagrams**
    - Check if two strings are anagrams of each other.
    - Input: "listen", "silent"
    - Output: True

47. **Find All Substrings**
    - Generate all possible substrings of a string.
    - Input: "abc"
    - Output: ['a', 'b', 'c', 'ab', 'bc', 'abc']

48. **Longest Common Prefix**
    - Find the longest common prefix among a list of strings.
    - Input: ["flower", "flow", "flight"]
    - Output: "fl"

49. **String Rotation with K positions**
    - Rotate string left by k positions.
    - Input: "abcdef", k=2
    - Output: "cdefab"

50. **Check Balanced Parentheses**
    - Check if parentheses in a string are balanced.
    - Input: "((()))"
    - Output: True

51. **Convert CamelCase to Snake Case**
    - Convert CamelCase string to snake_case.
    - Input: "HelloWorldPython"
    - Output: "hello_world_python"

52. **Find Missing Characters for Pangram**
    - Find which letters are missing to make a string a pangram.
    - Input: "The quick brown fox jumps"
    - Output: "adglvyz"

53. **String Interleaving**
    - Interleave characters from two strings alternately.
    - Input: "abc", "123"
    - Output: "a1b2c3"

54. **Remove Palindromic Substrings**
    - Remove all palindromic substrings of length > 1.
    - Input: "abccba"
    - Output: (depends on interpretation)

55. **Count Character Frequency**
    - Create a frequency map of all characters in a string.
    - Input: "hello"
    - Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

56. **Check if String is Subsequence**
    - Check if one string is a subsequence of another.
    - Input: "ace", "abcde"
    - Output: True

57. **Find Unique Characters**
    - Find all unique characters in a string.
    - Input: "hello world"
    - Output: "heworl d"

58. **String Difference**
    - Find characters that are in string1 but not in string2.
    - Input: "abcde", "ace"
    - Output: "bd"

59. **Zigzag String Conversion**
    - Convert string in zigzag pattern with given number of rows.
    - Input: "PAYPALISHIRING", rows=3
    - Output: "PAHNAPLSIIGYIR"

60. **Find Repeating Character Pattern**
    - Find the shortest repeating pattern in a string.
    - Input: "abcabcabc"
    - Output: "abc"

61. **Validate Email Format (Basic)**
    - Check if a string matches basic email format.
    - Input: "user@example.com"
    - Output: True

62. **Extract Domain from Email**
    - Extract domain name from an email address.
    - Input: "user@example.com"
    - Output: "example.com"

63. **Count Substring Occurrences**
    - Count non-overlapping occurrences of a substring.
    - Input: "aaaa", substring="aa"
    - Output: 2

64. **Title Case Conversion**
    - Convert string to title case with proper handling.
    - Input: "hello world from python"
    - Output: "Hello World From Python"

65. **Check Strong Password**
    - Check if password meets criteria (length, uppercase, lowercase, digit).
    - Input: "Password123"
    - Output: True

66. **Format Phone Number**
    - Format a 10-digit number as (XXX) XXX-XXXX.
    - Input: "1234567890"
    - Output: "(123) 456-7890"

67. **Split String by Multiple Delimiters**
    - Split string using multiple delimiters.
    - Input: "apple,banana;orange:grape", delimiters=",;:"
    - Output: ["apple", "banana", "orange", "grape"]

68. **Find Common Characters**
    - Find characters common to all strings in a list.
    - Input: ["hello", "world", "goal"]
    - Output: "lo"

69. **String Permutation Check**
    - Check if one string is a permutation of another.
    - Input: "abc", "bca"
    - Output: True

70. **Remove HTML Tags**
    - Remove all HTML tags from a string.
    - Input: "<p>Hello <b>World</b></p>"
    - Output: "Hello World"

71. **Caesar Cipher Encode**
    - Encode string using Caesar cipher with given shift.
    - Input: "hello", shift=3
    - Output: "khoor"

72. **Caesar Cipher Decode**
    - Decode string using Caesar cipher with given shift.
    - Input: "khoor", shift=3
    - Output: "hello"

73. **Find Shortest Word**
    - Find the shortest word in a sentence.
    - Input: "The quick brown fox"
    - Output: "The"

74. **Check if String Has Unique Characters**
    - Check if all characters in a string are unique.
    - Input: "abcdef"
    - Output: True

75. **String Distance (Hamming)**
    - Calculate Hamming distance between two strings of same length.
    - Input: "karolin", "kathrin"
    - Output: 3

76. **Extract Initials**
    - Extract initials from a full name.
    - Input: "John Doe Smith"
    - Output: "JDS"

77. **Check Palindrome (Ignore Case and Spaces)**
    - Check palindrome ignoring case, spaces, and punctuation.
    - Input: "A man a plan a canal Panama"
    - Output: True

78. **Find Longest Palindromic Substring**
    - Find the longest palindromic substring in a string.
    - Input: "babad"
    - Output: "bab" or "aba"

79. **Convert Number to Words**
    - Convert a number string to words (0-99).
    - Input: "23"
    - Output: "twenty three"

80. **Validate Parentheses with Multiple Types**
    - Check if parentheses, brackets, and braces are balanced.
    - Input: "({[]})"
    - Output: True

## Advanced/Tricky Level (81-100)

81. **Longest Substring Without Repeating Characters**
    - Find length of longest substring without repeating characters.
    - Input: "abcabcbb"
    - Output: 3

82. **Group Anagrams**
    - Group strings that are anagrams of each other.
    - Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
    - Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

83. **Minimum Window Substring**
    - Find minimum window substring that contains all characters of pattern.
    - Input: s="ADOBECODEBANC", t="ABC"
    - Output: "BANC"

84. **Regular Expression Matching (Basic)**
    - Implement basic regex matching with '.' and '*'.
    - Input: s="aa", p="a*"
    - Output: True

85. **Edit Distance (Levenshtein)**
    - Calculate minimum edit distance between two strings.
    - Input: "kitten", "sitting"
    - Output: 3

86. **Longest Common Subsequence**
    - Find length of longest common subsequence between two strings.
    - Input: "abcde", "ace"
    - Output: 3

87. **String Matching with Wildcards**
    - Match string with pattern containing '?' and '*' wildcards.
    - Input: s="abcdef", p="a*f"
    - Output: True

88. **Find All Palindromic Substrings**
    - Find all palindromic substrings in a string.
    - Input: "aaa"
    - Output: ["a", "a", "a", "aa", "aa", "aaa"]

89. **Decode String with Numbers**
    - Decode string like "3[a2[c]]" to "accaccacc".
    - Input: "3[a2[c]]"
    - Output: "accaccacc"

90. **KMP String Search**
    - Implement KMP algorithm to find pattern in text.
    - Input: text="ababcababa", pattern="ababa"
    - Output: 5

91. **Manacher's Algorithm (Longest Palindrome)**
    - Find longest palindromic substring using Manacher's algorithm.
    - Input: "babad"
    - Output: "bab"

92. **String Compression with Run Length Encoding**
    - Advanced compression handling edge cases.
    - Input: "aabcccccaaa"
    - Output: "a2b1c5a3"

93. **Check if String Follows Pattern**
    - Check if string follows a given pattern (like "abba").
    - Input: s="dog cat cat dog", pattern="abba"
    - Output: True

94. **Generate All Valid Parentheses**
    - Generate all valid combinations of parentheses for n pairs.
    - Input: n=3
    - Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]

95. **Word Break Problem**
    - Check if string can be segmented into dictionary words.
    - Input: s="leetcode", dict=["leet", "code"]
    - Output: True

96. **Palindrome Partitioning**
    - Find all ways to partition string into palindromes.
    - Input: "aab"
    - Output: [["a", "a", "b"], ["aa", "b"]]

97. **Text Justification**
    - Justify text to fit within given width.
    - Input: words=["This", "is", "an", "example"], width=16
    - Output: ["This    is    an", "example         "]

98. **Sliding Window Maximum in String**
    - Find lexicographically largest substring of given length.
    - Input: s="abcdef", k=3
    - Output: "def"

99. **Interleaving String Check**
    - Check if string s3 is formed by interleaving s1 and s2.
    - Input: s1="aabcc", s2="dbbca", s3="aadbbcbcac"
    - Output: True

100. **Shortest Superstring Problem**
    - Find shortest string that contains all given strings as substrings.
    - Input: ["catg", "ctaagt", "gcta", "ttca", "atgcatc"]
    - Output: "gctaagttcatgcatc"