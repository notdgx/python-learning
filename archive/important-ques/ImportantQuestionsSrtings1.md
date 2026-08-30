# ImportantQuestionsSrtings1

--- 

## Metadata

- **Day :** Monday
- **Date :** 2025-09-08
- **Time :** 11:14
- **Tags :** #python #strings #importantquestions1  
- **References :** [[ImportantQuestions1]], [[RevisedNotesStrings]] , [[FunctionsStrings]]
- **Branch of :** python > ImportantQuestions1 > ImportantQuestionsStrings1
- **Author :**  dx
- **Not Done :** 29,54,59,63,78-100

---

# Notes

---


## STRING Important Questions NOTES

- best and fastest way to reverse a str is `str[::-1]`
    
- count characters without white spaces `len(str.replace(" ",""))`
    
- remove spaces `str.replace(" ","")`
    
- to check if a str is empty : `return not s.strip()` — `strip` will remove all white spaces if present and `not` will give True if empty (str empty is called false in python)
    
- string comparison case insensitive : `str1.lower() == str2.lower()`
    
- always use `"".join(char for char in s if char.isdigit())` in case of str compression want to use in one line
    
- I most of case use `str.find(substr,start,end)` to find a substr because `index` will return value error if not found — use `i = str.find(substr)` \n `return i if i != 0 else None`
    
- snake case = `my_python_program`, camelcase = `myPythonProgram`, PaskalCase = `MyPythonProgram`, kebab case = `my-python-program`
    
- to remove all occurance of a specific word `str.replace("str","")` to remove only first occurance `str.replace("str","",1)`
    
- to check whether a str contains all same char `len(set(str)) == 1`
    
- if we want to capatlize first character only and rest lowercase use `capitalize` function else use `s[0].upper() + s[1:]`
    
- to remove duplicate preserve order
    

```python
def remove_duplicates_preserve_order(s):
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)
```

- counts consonants
    

```python
vowels = "aeiouAEIOU"
return sum(1 for char in s if char.isalpha() and char not in vowels)
```

- first non repeated character
    

```python
def first_non_repeated_char(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    for char in s:
        if char_count[char] == 1:
            return char
    return None
```

- `max(iterable, 10)` it will compare the value in iterable and then compare it with 10 , if in place of iterable you give a number then it will give max of those two
    
- to pad left , right a number with specified char
    

```python
s = "hello"
le = 10
ch = "*"
n = max(le - len(s), 0)
left = n // 2 + (n % 2)  # put extra on the left to match "***hello**"
right = n - left
return ch * left + s + ch * right
```

- to count the lines in a str : `return 0 if not a else a.count("\n") + 1`
    
- to replace a char which may or may not present and only first occurance by index
    

```python
return a[:index] + new_char + a[index+1:] if (0 <= index < len(a)) and len(new_char) != 0 else None
```

- string compression
    

```python
if not a:
    return ""
output = []
count = 1
for i in range(1, len(a) + 1):
    if i < len(a) and a[i] == a[i - 1]:
        count += 1
    else:
        output.append(a[i - 1] + str(count))
        count = 1
return "".join(output)
```

- string decompression
    

```python
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
```

- words frequency counter
    

```python
def word_frequency_counter(s):
    words = s.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency
```

- what are anagrams
    

Anagrams are words or phrases made by rearranging the letters of another word or phrase, typically using all the original letters exactly once.

- best way to compare two strings is `sorted(str1) == sorted(str2)` add `lower()` if want case insensitvity
    
- to find all substrings
    

```python
def find_all_substrings(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])
    return substrings
```

- in questions involving string rotations use `k = k % len(k)` it will remove the case of index out of range error if `k > len(k)` it will avoid unnecessary 360s
    
- check balanced parentheses
    

```python
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
```

- camel case to snake case
    

```python
def camel_to_snake(s):
    result = []
    for i, char in enumerate(s):
        if char.isupper() and i > 0:
            result.append('_')
        result.append(char.lower())
    return ''.join(result)
```

- A pangram is a sentence that includes all letters of an alphabet at least once.
    
- interleave strings
    

```python
def que53():
    a = "abc"
    b = "123"
    s = "".join((i+j for i,j in zip(a,b)))
    return s + a[len(b):] + b[len(a):]
```

- character frequency dictionary
    

```python
def char_frequency(s):
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency
```

- check subsequence
    

```python
def is_subsequence(s, t):
    i = 0
    for char in t:
        if i < len(s) and char == s[i]:
            i += 1
    return i == len(s)
```

- for unique characters
    

```python
def find_unique_chars(s):
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)
```

- find repeating patterns
    

```python
def find_repeating_pattern(s):
    for length in range(1, len(s) // 2 + 1):
        pattern = s[:length]
        if pattern * (len(s) // length) == s[:length * (len(s) // length)]:
            if len(s) % length == 0:
                return pattern
    return s
```

- email validation
    

```python
# 61. Validate Email Format (Basic)
def validate_email_basic(email):
    return '@' in email and '.' in email.split('@')[-1]
```

- check strong pass
    

```python
def check_strong_password(password):
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return has_upper and has_lower and has_digit
```

- split with multiple delimiters
    

```python
def que67():
    s = "apple,banana;orange:grape"
    delimiters = ",;:"
    for d in delimiters:
        s = s.replace(d, ",")
    return s.split(",")
# print(que67())
```

- Find Common Characters
    

```python
def find_common_characters(strings):
    if not strings:
        return ""
    common = set(strings[0])
    for s in strings[1:]:
        common &= set(s)
    return ''.join(sorted(common))
```

- remove html tags
    

```python
s = "<p>Hello <b>World</b></p>"
result = ""
inside_tag = False
for ch in s:
    if ch == "<":
        inside_tag = True
    elif ch == ">":
        inside_tag = False
    elif not inside_tag:
        result += ch
return result
```

- caesar cipher encoding
    

```python
def que71():  # use ord() to convert to ascii value
    text = "hello"
    shift = 3
    result = ""
    for ch in text:
        if ch.isalpha():  # shift letters only
            offset = ord('a') if ch.islower() else ord('A')
            result += chr((ord(ch) - offset + shift) % 26 + offset)
        else:
            result += ch  # keep non-letters unchanged
    return result
```

- decoding
    

```python
text = "khoor"
shift = 3
result = ""
for ch in text:
    if ch.isalpha():
        offset = ord('a') if ch.islower() else ord('A')
        result += chr((ord(ch) - offset - shift) % 26 + offset)
    else:
        result += ch
return result
```

- to check if all char is unique
    

```python
def que74():
    s = "abcdef"
    seen = set()
    for ch in s:
        if ch in seen:
            return False
        seen.add(ch)
    return True
```

- The string Hamming distance is the number of positions at which two equal-length strings have different characters. It counts substitutions only and is defined only when the strings are the same length.
    

```python
s1 = "karolin"
s2 = "kathrin"
if len(s1) != len(s2):
    return None  # Hamming distance requires equal length
return sum(c1 != c2 for c1, c2 in zip(s1, s2))
```

- palindrome for a sentence
    

```python
# Check Palindrome (Ignore Case and Spaces)
def is_palindrome_ignore_case_spaces(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]
```