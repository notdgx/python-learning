# ImportantQuestionsFSets1

--- 

## Metadata

- **Day :** Wednesday
- **Date :** 2025-09-16
- **Time :** 14:21
- **Tags :** #python #fsets #importantquestions1 #Revised 
- **References :** [[FunctionsFSets]],[[RevisedNotesFSets]] , [[ImportantQuestions1]]
- **Branch of :** Python > Importantquestions1 > ImportantQuestionsFsets
- **Author :**  dx

---

# Notes

---

* basic frozenset making
```python
Basic Frozenset Creation

def solution_1():
    data = [1, 2, 3, 4, 5]
    result = frozenset(data)
```

* empty frozenset creation : a = frozenset()
* Frozenset from String
```python
    data = "hello"
    result = frozenset(data)
```

* Frozenset from Tuple

```python
def solution_4():
    data = (10, 20, 30, 20, 10)
    result = frozenset(data)
    print(f"Input: {data}")
    print(f"Output: {result}")
    return result
    
    
    
    Check Membership

def solution_5()
    fs = frozenset({'a', 'b', 'c', 'x', 'y'})
    element = 'x'
    result = element in fs
    print(f"Input: {fs}, '{element}'")
    print(f"Output: {result}")
    return result
    
    
    
    Frozenset from Dictionary Keys

def solution_7():
    data = {'nam': 'John', 'age': 30, 'city': 'NYC'}
    result = frozenset(data.keys())
    print(f"Input: {data}")
    print(f"Output: {result}")
    return result



  
	Convert Set to Frozenset

def solution_8():
    data = {7, 8, 9}
    result = frozenset(data)
    print(f"Input: {data}")
    print(f"Output: {result}")
    return result
    
    
    
    Complex Difference

def solution_28():
    A = frozenset({1, 2, 3, 4, 5})
    B = frozenset({2, 3})
    C = frozenset({4, 5})
    result = A.difference(B).difference(C)
    print(f"Input: A={A}, B={B}, C={C}")
    print(f"Output: {result}")
    return result
    
    
    
    
```

---
