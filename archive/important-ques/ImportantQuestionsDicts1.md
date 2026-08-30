# ImportantQuestionsDicts1

--- 

## Metadata

- **Day :** Friday
- **Date :** 2025-09-12
- **Time :** 12:46
- **Tags :** #python #dicts #importantquestions1 #revised 
- **References :** [[FunctionDicts]] , [[ImportantQuestions1]] , [[RevisedNotesDicts]]
- **Branch of :** Python > ImportantQuestions1 > ImportantQuestionsDict1
- **Author :**  dx

---

# Notes

---

* always use dict.get(key , default ) to get a value in dict or
```python
d[key ] if key in d else "NOt present"
```
to avoid the ValueEerror if not present

* merging two dict with ** 
```python
Merge dictionaries using ** operator

def solution_45():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    return {**dict1, **dict2}
```

* sort dictionary with keys
```python
 Sort dictionary by keys

def solution_46():
    my_dict = {'b': 2, 'a': 1, 'c': 3}
    return dict(sorted(my_dict.items()))
```

* sort dict with vslues

```python
Sort dictionary by values

def solution_47():
    my_dict = {'alice': 85, 'bob': 90, 'charlie': 75}
    return dict(sorted(my_dict.items(), key=lambda x: x[1]))
```

* find key with max value

```python
 Find key with maximum value

def solution_48():
    my_dict = {'x': 10, 'y': 25, 'z': 15}
    return max(my_dict, key=my_dict.get)
```

* grop words by their first letter

```python
Group words by first letter

def solution_50():
    words = ['apple', 'banana', 'cherry', 'apricot']
    groups = {}
    for word in words
        first_letter = word[0]
        if first_letter not in groups:
            groups[first_letter] = []
        groups[first_letter].append(word)
    return groups
    
    
    def que50():
    d=['apple', 'banana', 'cherry', 'apricot']
    d2=dict()
    for i in d:
        x=[]
        for j in d:
            if i[0].lower()==j[0].lower():
                x.append(j
        d2[i[0]]=x
    return d2
    
    
```


* swap values to keys

```python
Invert dictionary (swap keys and values)
def solution_51():
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    return {value: key for key, value in my_dict.items()}
```

* filter dictionary with a condition
```python
 Filter dictionary by values
def solution_52():
    my_dict = {'a': 10, 'b': 5, 'c': 15, 'd': 8}
    return {k: v for k, v in my_dict.items() if v > 7}
```

* create a dict with length as a value 
```python
 Create dictionary of word lengths

def solution_53():
    words = ['cat', 'elephant', 'dog']
    return {word: len(word) for word in words}
```


* extending dict without any overwrite
* **Input:** `{'a': [1, 2]}, {'a': [3, 4], 'b': [5]}` **Output:** `{'a': [1, 2, 3, 4], 'b': [5]}`
```python
  

# 54. Combine dictionaries by extending lists

def solution_54():
    dict1 = {'a': [1, 2]}
    dict2 = {'a': [3, 4], 'b': [5]}
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result
            result[key].extend(value)
        else:
            result[key] = value
    return result
```

* Get all keys from nested dictionary {'outer': {'inner1': 1, 'inner2': 2}}.
**Input:** `{'outer': {'inner1': 1, 'inner2': 2}}` **Output:** `['outer', 'inner1', 'inner2']`

```python
def que55():

    a={'outer': {'inner1': 1, 'inner2': 2}}
    l=[]
    for i,j in a.items():
        l.append(i)
        if isinstance(j,dict):
            l.extend(j.keys())

  

    # #recurrsive version

    # def get_all_keys(d):
    # keys = []
    # for k, v in d.items():
    #     keys.append(k)
    #     if isinstance(v, dict):
    #         keys.extend(get_all_keys(v))
    # return keys
    return l

# print(que55())
```

* count vowels

```python
  

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
```

* Calculate average from grades dictionary
```python
def solution_57():
    grades = {'alice': 85, 'bob': 92, 'charlie': 78}
    return sum(grades.values()) / len(grades)
```

* remove keys with none values
```python
Remove keys with None values

def solution_58():
    my_dict = {'a': 1, 'b': None, 'c': 3, 'd': None}
    return {k: v for k, v in my_dict.items() if v is not None}
```

* Transform dictionary values to uppercase
```python
def solution_60():
    my_dict = {'a': 'hello', 'b': 'world'}
    return {k: v.upper() for k, v in my_dict.items()}
```

*  Find common keys between dictionaries
```python
def solution_61():
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'b': 4, 'c': 5, 'd': 6}
    return list(set(dict1.keys()) & set(dict2.keys()))
```

* Extract subset of dictionary
```python
def solution_64():
    my_dict = {'name': 'John', 'age': 30, 'city': 'NYC'}
    keys = ['name', 'city']
    return {k: my_dict[k] for k in keys if k in my_dict}
```

* Create nested dictionary from flat dict {'a.b': 1, 'a.c': 2, 'b.d': 3}.
**Input:** `{'a.b': 1, 'a.c': 2, 'b.d': 3}` **Output:** `{'a': {'b': 1, 'c': 2}, 'b': {'d': 3}}`

```python 
    d = {'a.b': 1, 'a.c': 2, 'b.d': 3}
    out = {}
    for k, v in d.items():
        cur = out
        parts = k.split('.')
        for p in parts[:-1]:
            cur = cur.setdefault(p, {})
        cur[parts[-1]] = v
    return out
```

*  Sort dictionary by values in descending order
```python
def solution_67():
    my_dict = {'x': 10, 'y': 30, 'z': 20}
    return dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
```


*  Find keys where value > threshold

```python
def solution_69():

    my_dict = {'a': 10, 'b': 5, 'c': 15}
    return [k for k, v in my_dict.items() if v > 7]
```

* Count unique words in text 'the cat and the dog' using dictionary.
**Input:** `'the cat and the dog'` **Output:** `{'the': 2, 'cat': 1, 'and': 1, 'dog': 1}`

```python
def solution_71():
    text = 'the cat and the dog'
    words = text.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count
```

* Create multiplication table dict: {i: {j: i*j for j in range(1, 4)} for i in range(1, 4)}.
**Input:** `range(1, 4)` **Output:** `{1: {1: 1, 2: 2, 3: 3}, 2: {1: 2, 2: 4, 3: 6}, 3: {1: 3, 2: 6, 3: 9}}`

```python
def solution_72():
    return {i: {j: i*j for j in range(1, 4)} for i in range(1, 4)}
```


* Group students by grade: [{'name': 'A', 'grade': 'B'}, {'name': 'C', 'grade': 'A'}, {'name': 'D', 'grade': 'B'}].
**Input:** `[{'name': 'A', 'grade': 'B'}, {'name': 'C', 'grade': 'A'}, {'name': 'D', 'grade': 'B'}]` **Output:** `{'B': ['A', 'D'], 'A': ['C']}`

```python
def solution_74():

    students = [{'name': 'A', 'grade': 'B'}, {'name': 'C', 'grade': 'A'}, {'name': 'D', 'grade': 'B'}]
    groups = {}
    for student in students:
        grade = student['grade']
        if grade not in groups:
            groups[grade] = []
        groups[grade].append(student['name'])
    return groups
```

* Find intersection of dictionary values: {'a': [1, 2, 3], 'b': [2, 3, 4]}.
**Input:** `{'a': [1, 2, 3], 'b': [2, 3, 4]}` **Output:** `[2, 3]`

```python
def que():
    my_dict = {'a': [1, 2, 3], 'b': [2, 3, 4]}
    values = list(my_dict.values())
    if len(values) < 2:
        return []
    intersection = set(values[0])
    for value_list in values[1:]:
        intersection = intersection.intersection(set(value_list))
    return list(intersection)
```

* Create running sum dictionary from list [1, 2, 3, 4, 5].
**Input:** `[1, 2, 3, 4, 5]` **Output:** `{1: 1, 2: 3, 3: 6, 4: 10, 5: 15}`

```python
Create running sum dictionary
def solution_76():
    data = [1, 2, 3, 4, 5]
    running_sum = 0
    result = {}
    for num in data:
        running_sum += num
        result[num] = running_sum
    return result
```

*  Create running sum dictionary from list [1, 2, 3, 4, 5].
**Input:** `[1, 2, 3, 4, 5]` **Output:** `{1: 1, 2: 3, 3: 6, 4: 10, 5: 15}`

```python
Validate dictionary structure
def solution_77():
    data_dict = {'name': 'John', 'age': 25}
    type_dict = {'name': str, 'age': int}
    return all(isinstance(data_dict.get(k), v) for k, v in type_dict.items())
```


* Create pivot table: convert [{'name': 'A', 'subject': 'math', 'score': 90}] to {'A': {'math': 90}}.
**Input:** `[{'name': 'A', 'subject': 'math', 'score': 90}]` **Output:** `{'A': {'math': 90}}`

```python
Create pivot table

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
```

* Calculate percentage distribution from {'apples': 20, 'oranges': 30, 'bananas': 50}.
**Input:** `{'apples': 20, 'oranges': 30, 'bananas': 50}` **Output:** `{'apples': 20.0, 'oranges': 30.0, 'bananas': 50.0}`

```python
Calculate percentage distribution
def solution_79():
    my_dict = {'apples': 20, 'oranges': 30, 'bananas': 50}
    total = sum(my_dict.values())
    return {k: (v / total) * 100 for k, v in my_dict.items()}
```

* Find most frequent element in list ['a', 'b', 'a', 'c', 'a'] using dictionary.
**Input:** `['a', 'b', 'a', 'c', 'a']` **Output:** `'a'`

```python
 Find most frequent element
def solution_80():
    data = ['a', 'b', 'a', 'c', 'a']
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    return max(freq, key=freq.get)
```

* Flatten nested dictionary {'a': {'b': {'c': 1, 'd': 2}}, 'e': 3} with dot notation keys.
**Input:** `{'a': {'b': {'c': 1, 'd': 2}}, 'e': 3}` **Output:** `{'a.b.c': 1, 'a.b.d': 2, 'e': 3}`

```python
Flatten nested dictionary with dot notation
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
```

---
