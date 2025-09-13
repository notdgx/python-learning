# RevisedNotesLists

--- 

## Metadata

- **Day :** Saturday
- **Date :** 2025-09-13
- **Time :** 11:16
- **Tags :** #python #Revised #lists   
- **References :** [[RevisedNotes]], [[ImportantQuestionsLists1]]
- **Branch of :** Python > RevisedNotes > RevisedNotesLists
- **Author :**  dx

---

# Notes

---

# # Python Lists — Methods & Built-in Functions

  ---

  

## Basic List Functions

  

• **`len(list)`** : gives their length of list `TypeError` if not iterable

• **`list(iterable)`** : it will create a list , without arg create a empty list, if str as arg it make list of each character as a element , if list(dict) then it will make list of keys.um if did list([1,2,3]) then give [1,2, 3]

  

• **`sorted(list,key=len,reverse=True)`** : it will always return a new list in ascending by default if reverse=True then in DESCENDING order , if we add key as arg it will sort it as per key like

Give TypeError if of mixed datatype

  

```python

# 1. Default sorting

sorted([3, 1, 2])  # [1, 2, 3]

  

# 2. Sort by length of strings

sorted(["python", "is", "great"], key=len)  # ['is', 'great', 'python']

  

# 3. Case-insensitive sort

sorted(["Banana", "apple", "Cherry"], key=str.lower)  # ['apple', 'Banana', 'Cherry']

  

# 4. Sort numbers by absolute value

sorted([-4, 2, -1, 3], key=abs)  # [-1, 2, 3, -4]

  

# 5. Sort tuples by 2nd element

sorted([(1, 3), (2, 1), (3, 2)], key=lambda x: x[1])  # [(2, 1), (3, 2), (1, 3)]

  

# 6. Sort by multiple criteria (2nd element, then 1st element)

sorted([("apple", 3), ("banana", 2), ("cherry", 2)], key=lambda x: (x[1], x[0]))

# [('banana', 2), ('cherry', 2), ('apple', 3)]

  

# 7. Sort by last character of string

sorted(["dog", "cat", "elephant"], key=lambda s: s[-1])  # ['elephant', 'dog', 'cat']

  

# 8. Sort list of dicts by a specific key

data = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 20}]

sorted(data, key=lambda d: d["age"])

# [{'name': 'Bob', 'age': 20}, {'name': 'Alice', 'age': 25}]

  

# 9. Sort objects by attribute

class Student:

    def __init__(self, name, marks):

        self.name = name

        self.marks = marks

students = [Student("Alice", 85), Student("Bob", 95), Student("Charlie", 90)]

[s.name for s in sorted(students, key=lambda s: s.marks)]

# ['Alice', 'Charlie', 'Bob']

  

# 10. Sort strings by numeric value inside

sorted(["item12", "item3", "item2"], key=lambda s: int(s[4:]))

# ['item2', 'item3', 'item12']

  

# 11. Sort by word count in string

sorted(["a quick fox", "hello", "two words here"], key=lambda s: len(s.split()))

# ['hello', 'a quick fox', 'two words here']

  

# 12. Reverse + key (largest first)

sorted([3, 1, 4, 2], key=lambda x: x, reverse=True)  # [4, 3, 2, 1]

  

# 13. Sort dict keys alphabetically

sorted({"b": 2, "a": 1, "c": 3})  # ['a', 'b', 'c']

  

# 14. Sort dict items by value

sorted({"b": 2, "a": 1, "c": 3}.items(), key=lambda x: x[1])

# [('a', 1), ('b', 2), ('c', 3)]

  

# 15. Sort with operator.itemgetter

from operator import itemgetter

sorted([(1, 3), (2, 1), (3, 2)], key=itemgetter(1))

# [(2, 1), (3, 2), (1, 3)]

  

# 16. Sort with operator.attrgetter

from operator import attrgetter

sorted(students, key=attrgetter("marks"))

# [Student(Alice,85), Student(Charlie,90), Student(Bob,95)]

```

  

---

  

## Aggregation Functions

  

• **`sum(list,start=0)`** : it will calculate the sum of iterable present and if of different datatype it will give error TypeError and if list empty it will not give 0 not error, and we can add start value in it what it will do is it will be added to the sum of the iterable result

  

• **`min(iterable,*args ,key=none,default=0)`, `max()`** : it will give ValueError if iterable is empty we can set default as it will not give valueerror then , it will give TypeError if of mixed datatype or non iterable , we can use it to calculate the min,max of list we can use unpacking operator in it * , we can use key as arg to manipulate the being used values , in list of booleans the min is False and max is True , we can also use min(* a,* b) as to unpack iterables a,b and then compare it

  

• **`enumerate(iterable, start=0)`** : it will do is it will return the enumerate object that contains index,value as a pair in tuple if we add a start value then it will start counting the index as from that value and give upto full elements even if it is overflowing the original index , we can access it by for loop as : for i,val in enumerate(list,start=1) , can be used with zip function as :

  

```python

for i, (n, a) in enumerate(zip(names, ages), start=100):

    print(i, n, a)

```

  

,if it is empty does not return error will give empty enu obj, it will raise TypeError if start is not int

  

---

  

## Iterator Functions

  

• **`reversed(iterable)`** : it takes only iterable as arg no extra arg, it gives reversed iterator that can be further be converted int list or tuple, it gives TypeError if not iterable

  

• **`zip(*iterables)` or `zip(list1,list2,……)`** : Returns a zip object (an iterator) of tuples, where each tuple contains the i-th elements of the input iterables.Stops at the shortest iterable. can be used like this

  

```python

pairs = [('Alice', 25), ('Bob', 30)]

names, ages = zip(*pairs)              , no errors , if non iterable TypeError

```

  

---

  

## Python `map()` Function — Important & Expected Uses

  

• **`map(function,iterables)`** : it returns map object which will contains the elements of iterables after applying a specific function to each element of it , no error , only TypeError if non iterable

  

### 1. **Basic Usage (Single Iterable)**

  

```python

nums = [1, 2, 3, 4]

def square(x):

    return x**2

result = map(square, nums)

print(list(result))  # [1, 4, 9, 16]

```

  

### 2. **Using Lambda**

  

```python

nums = [1, 2, 3, 4]

print(list(map(lambda x: x*2, nums)))  # [2, 4, 6, 8]

```

  

### 3. **Multiple Iterables**

  

```python

a = [1, 2, 3]

b = [4, 5, 6]

result = map(lambda x, y: x + y, a, b)

print(list(result))  # [5, 7, 9]

```

⚠️ Stops at shortest iterable (like zip).

  

### 4. **With Built-in Functions**

  

```python

nums = [1.1, 2.2, 3.3]

print(list(map(int, nums)))  # [1, 2, 3]

print(list(map(str, nums)))  # ['1.1', '2.2', '3.3']

```

  

### 5. **With Strings**

  

```python

words = ["1", "2", "3"]

print(list(map(int, words)))  # [1, 2, 3]

```

  

### 6. **Converting Boolean**

  

```python

nums = [0, 1, 2, 3]

print(list(map(bool, nums)))  # [False, True, True, True]

```

  

### 7. **Using with reversed() or sorted()**

  

```python

nums = [1, 4, 2, 3]

# square then sort descending

print(sorted(map(lambda x: x**2, nums), reverse=True))

# [16, 9, 4, 1]

```

  

### 8. **Using map + enumerate**

  

```python

nums = [1, 2, 3]

for i, val in enumerate(map(lambda x: x*10, nums)):

    print(i, val)

# 0 10

# 1 20

# 2 30

```

  

### 9. **Converting map to other types**

  

```python

nums = [1,2,3]

print(list(map(str, nums)))    # ['1','2','3']

print(tuple(map(str, nums)))   # ('1','2','3')

print(set(map(str, nums)))     # {'1','3','2'} (unordered)

```

  

### 10. **Edge Cases**

• **Non-iterable → TypeError:**

  

```python

map(lambda x: x*2, 5)  # ❌ TypeError

```

  

• **Multiple iterables → stops at shortest length:**

  

```python

map(lambda x,y: x+y, [1,2], [10])  # only first elements used

```

  

• **function=None → returns original elements:**

  

```python

nums = [1,2,3]

print(list(map(None, nums)))  # ❌ TypeError in Python 3

```

  

---

  

## Python `filter()` Function — Important & Expected Uses

  

• **`filter(function ,iterable)`** : it will give out filter object that contains the element who verified the function it filters the true elements of iterable as per function , no error, TypeError if not iterable

  

**`map(func, iterable)`** → applies func to all elements, returns values (truthy or not), same length as iterable; **`filter(func, iterable)`** → keeps elements where func returns truthy, may be shorter than iterable.

  

### 🔹 filter()

### ✅ Definition

  

**`filter(function, iterable)`**

• Applies a function to each element of an iterable.

• Returns only the elements where function returns True.

• Returns a filter object (iterator).

  

### 1. **Basic Usage (Single Iterable)**

  

```python

nums = [1, 2, 3, 4, 5]

def is_even(x):

    return x % 2 == 0

result = filter(is_even, nums)

print(list(result))  # [2, 4]

```

  

### 2. **Using Lambda**

  

```python

nums = [1, 2, 3, 4, 5]

print(list(filter(lambda x: x>3, nums)))  # [4, 5]

```

  

### 3. **Using None as function**

  

```python

data = [0, 1, "", "Hello", None, "Python"]

print(list(filter(None, data)))

# [1, 'Hello', 'Python'] → filters out falsy values (0, "", None)

```

  

### 4. **Works with Strings**

  

```python

words = ["apple", "bat", "cat", "ant"]

print(list(filter(lambda w: len(w)==3, words)))

# ['bat', 'cat', 'ant']

```

  

### 5. **Works with Multiple Iterables? ❌**

• Unlike map(), filter() works only with one iterable.

• If you want multiple, combine with zip():

  

```python

a = [1,2,3]

b = [4,5,6]

result = filter(lambda x: x[0] + x[1] > 5, zip(a,b))

print(list(result))  # [(2,4),(3,3),(3,6)]

```

  

### 6. **Edge Cases**

• **Empty iterable → returns empty iterator:**

  

```python

print(list(filter(lambda x: x>0, [])))  # []

```

  

• **Non-iterable → TypeError:**

  

```python

filter(lambda x: x>0, 5)  # ❌ TypeError

```

  

### 7. **Combine with map() or sorted()**

  

```python

nums = [1, 2, 3, 4, 5]

# double the numbers >2

print(list(map(lambda x:x*2, filter(lambda x:x>2, nums))))

# [6, 8, 10]

# sort filtered elements

print(sorted(filter(lambda x: x%2==0, nums)))

# [2, 4]

```

  

---

  

## map() vs filter() with Multiple Iterables

  

### 🔹 **map() with multiple iterables**

• Supports multiple iterables.

• The function must accept the same number of arguments as iterables.

• Iteration stops at the shortest iterable.

  

**Example**

  

```python

a = [1, 2, 3]

b = [4, 5, 6, 7]

result = map(lambda x, y: x + y, a, b)

print(list(result))  # [5, 7, 9] → stops at shortest (a)

```

  

• **Works with any number of iterables:**

  

```python

x = [1,2]

y = [10,20]

z = [100,200]

print(list(map(lambda a,b,c: a+b+c, x,y,z)))  # [111, 222]

```

  

### 🔹 **filter() with multiple iterables**

• Does NOT support multiple iterables directly.

• Only accepts one iterable.

• If you want to filter based on multiple sequences, combine them using zip():

  

**Example**

  

```python

a = [1, 2, 3]

b = [4, 5, 6]

result = filter(lambda x: x[0] + x[1] > 5, zip(a, b))

print(list(result))  # [(2,4), (3,3), (3,6)]

```

  

• Here, zip(a,b) creates tuples (a_i, b_i) which filter() can process.

  

### ⚡ Key Differences

  

| Function | **Multiple Iterables?** | **Notes** |

|----------|-------------------------|-----------|

| map() | ✅ Yes | Function must accept same number of args; stops at shortest iterable |

| filter() | ❌ No | Must combine iterables manually (e.g., with zip()) |

  

So basically:

• **map(f, a, b, c)** → works natively.

• **filter(f, a, b)** → must do filter(f, zip(a,b)).

  

---

  

## Python `all()` and `any()` Functions

  

• **`all()`** : give true if all the values in it is truth and TypeError is non iterable , no error

  

### 🔹 all()

### ✅ Definition

  

**`all(iterable)`**

• Returns True if all elements of the iterable are truthy.

• Returns False if any element is falsy.

• Works with any iterable: list, tuple, set, dict, etc.

  

### 1. **Basic Usage**

  

```python

nums = [1, 2, 3]

print(all(nums))  # True (all non-zero → truthy)

nums = [1, 0, 3]

print(all(nums))  # False (0 → falsy)

```

  

### 2. **With Boolean Values**

  

```python

flags = [True, True, False]

print(all(flags))  # False

```

  

### 3. **With Strings**

  

```python

words = ["hello", "world", ""]

print(all(words))  # False (empty string is falsy)

```

  

### 4. **With Empty Iterable**

  

```python

print(all([]))  # True → by definition, vacuously True

```

  

### 5. **With Dictionaries**

• Iterates over keys by default:

  

```python

d = {"a": 1, "b": 2, "c": 0}

print(all(d))  # True → keys are non-empty strings → truthy

print(all(d.values()))  # False → one value is 0

```

  

### 6. **Combine with map() / filter()**

  

```python

nums = [2, 4, 6, 8]

# check if all numbers are even

print(all(map(lambda x: x%2==0, nums)))  # True

# filter then check

print(all(filter(lambda x: x>0, nums)))   # True → all remaining >0

```

  

### ⚡ Key Notes

• all() checks truthiness, not numeric comparison directly.

• Empty iterable → True.

• Works with any iterable.

• Often used in validation, conditions, or combined with map() / filter().

  

---

  

• **`any(iterable)`** : give true if any of value in iterable is true , TypeError if non iterable

  

### 🔹 any()

### ✅ Definition

  

**`any(iterable)`**

• Returns True if any element of the iterable is truthy.

• Returns False if all elements are falsy.

• Works with any iterable: list, tuple, set, dict, etc.

  

### 1. **Basic Usage**

  

```python

nums = [0, 0, 3]

print(any(nums))  # True (3 is truthy)

nums = [0, 0, 0]

print(any(nums))  # False (all falsy)

```

  

### 2. **With Boolean Values**

  

```python

flags = [False, False, True]

print(any(flags))  # True

```

  

### 3. **With Strings**

  

```python

words = ["", "", "hello"]

print(any(words))  # True (non-empty string is truthy)

words = ["", ""]

print(any(words))  # False

```

  

### 4. **With Empty Iterable**

  

```python

print(any([]))  # False → no truthy element

```

  

### 5. **With Dictionaries**

• Iterates over keys by default:

  

```python

d = {"a": 0, "b": 0, "c": 0}

print(any(d))         # True → keys are non-empty strings

print(any(d.values())) # False → all values are 0

```

  

### 6. **Combine with map() / filter()**

  

```python

nums = [1, 3, 5, 8]

# check if any number is even

print(any(map(lambda x: x%2==0, nums)))  # True (8 is even)

# filter then check

print(any(filter(lambda x: x>10, nums)))  # False (all <=10)

```

  

### ⚡ Key Notes

• any() checks truthiness, not numeric comparison directly.

• Empty iterable → False.

• Works with any iterable.

• Often used in validation, conditions, or combined with map() / filter().

  

---

  

## Python `eval()` Function — Important & Expected Uses

  

• **`eval`** : it runs string as a python code

  

### 🔹 Concept

eval() takes a string that looks like a Python expression and runs it as if it were Python code, then returns the result.

Think of it like Python's interpreter reading a line of code dynamically at runtime.

  

### 🔹 Step-by-step Example

  

```python

x = 10

expr = "x + 5"

result = eval(expr)

print(result)

```

  

**What happens internally:**

1. eval() receives the string "x + 5".

2. It parses the string to understand it's an expression: x + 5.

3. It evaluates it using the current environment (variables and functions accessible).

   ○ Here x is 10.

4. Computes the result: 10 + 5 = 15.

5. Returns 15.

  

So it's like writing:

  

```python

result = x + 5

```

… but the code comes from a string dynamically.

  

### 🔹 Key Points

• **Expression only:** eval() can't execute statements like for, while, or print() alone.

  

```python

eval("for i in range(3): print(i)")  # ❌ SyntaxError

```

  

• **Dynamic execution:** You can build code as a string at runtime.

  

```python

a = 2

b = 3

expr = f"{a}**{b}"  # "2**3"

print(eval(expr))    # 8

```

  

• **Access to current environment:** variables, functions, etc.

  

### 🔹 Dangerous Example

  

```python

user_input = "os.system('rm -rf /')"

eval(user_input)  # ❌ Will execute dangerous code

```

  

• This is why never use eval() on untrusted input.

  

### 🔹 Safe Alternative

Use ast.literal_eval() for parsing strings containing literals only:

  

```python

import ast

s = "[1, 2, 3]"

lst = ast.literal_eval(s)  # Safe

print(lst)  # [1, 2, 3]

```

  

• Works with strings, numbers, lists, dicts, tuples, booleans, None.

• ❌ Cannot run expressions like x + 5 — only static data.

  

### 🔹 eval()

### ✅ Definition

  

**`eval(expression, globals=None, locals=None)`**

• Evaluates a string as a Python expression and returns the result.

• Can optionally use globals and locals dictionaries to control the environment.

  

### 1. **Basic Usage**

  

```python

x = 10

expr = "x + 5"

result = eval(expr)

print(result)  # 15

```

  

### 2. **Arithmetic Expressions**

  

```python

expr = "2 + 3 * 4"

print(eval(expr))  # 14

```

  

### 3. **Using Variables**

  

```python

a = 5

b = 7

expr = "a * b"

print(eval(expr))  # 35

```

  

### 4. **Using Functions**

  

```python

def square(x):

    return x**2

expr = "square(6)"

print(eval(expr))  # 36

```

  

### 5. **With globals / locals**

  

```python

x = 10

expr = "x + y"

print(eval(expr, {"y":5}, {}))  # 15 → only `y` is passed

```

  

### 6. **Security Warning ⚠️**

• Never use eval() on untrusted input — it can execute arbitrary code.

  

```python

# Dangerous:

# eval("__import__('os').system('rm -rf /')")  # ❌

```

  

• Safe alternatives: ast.literal_eval() (only evaluates literals like numbers, strings, lists, dicts).

  

### 7. **With Literals**

  

```python

import ast

s = "[1,2,3]"

lst = ast.literal_eval(s)

print(lst)  # [1, 2, 3]

```

  

### ⚡ Key Notes

• Returns the result of evaluated expression.

• Only works for single expressions, not statements like loops or if.

• Can pass globals / locals for controlled execution.

• Dangerous with untrusted input — use ast.literal_eval() if possible



---

  

## Tricky / Important Points About `append()` and `extend()`

  

### 1. **`append()` always adds the object as-is**

  

```python

lst = [1, 2]

lst.append([3,4])

print(lst)  # [1, 2, [3, 4]]

```

• Many expect it to "add elements individually," but it adds the list itself.

  

### 2. **`extend()` iterates over any iterable**

  

```python

lst = [1,2]

lst.extend("abc")

print(lst)  # [1, 2, 'a', 'b', 'c']

```

• Strings, tuples, sets all work.

• But non-iterables raise TypeError:

  

```python

lst.extend(5)  # ❌ TypeError

```

  

### 3. **Nested Lists Confusion**

  

```python

lst = [[1,2], [3,4]]

lst.append([5,6])

print(lst)  # [[1,2],[3,4],[5,6]] → nested one level deeper

lst.extend([5,6])

print(lst)  # [[1,2],[3,4],5,6] → elements added individually

```

  

### 4. **Difference in length change**

• **append()** → +1 length regardless of what you append.

  

```python

lst = [1,2]

lst.append([3,4])

print(len(lst))  # 3

```

• **extend()** → +len(iterable)

  

```python

lst = [1,2]

lst.extend([3,4])

print(len(lst))  # 4

```

  

### 5. **Extending with a set → unordered addition**

  

```python

lst = [1,2]

lst.extend({5,4})

print(lst)  # [1,2,4,5] → order not guaranteed

```

• Sets are iterables, but no order is preserved.

  

### 6. **Appending or extending with mutable objects**

  

```python

lst = []

lst.append([1,2])

lst[0].append(3)

print(lst)  # [[1,2,3]] → changes inside the nested list reflect

```

• Mutables are added by reference in append/extend.

  

### 7. **Chaining ❌**

  

```python

lst = [1,2]

lst.append([3,4]).append(5)  # ❌ AttributeError

```

• append() and extend() return None, cannot chain.

  

### 8. **Extending with an empty iterable**

  

```python

lst = [1,2]

lst.extend([])

print(lst)  # [1,2] → no change

```

• append([]) would add an empty list → [1,2,[]]

  

### 9. **Strings vs Lists — subtle gotcha**

  

```python

lst = [1,2]

lst.append("abc")  # [1,2,'abc']

lst.extend("abc")  # [1,2,'abc','a','b','c']

```

• If you expect characters to merge into the list, you need extend().

  

### 10. **Common interview trick question**

• **Question:** What's the difference between lst.append([1,2,3]) and lst.extend([1,2,3])?

• **Answer:** append → one element (the list) added; extend → each element added individually.

• People often forget this when the element is itself a list.

  

### 💡 Summary / Memory Tricks

• **append()** → "add one object at the end"

• **extend()** → "unpack the iterable and add each element"

• Returns None → cannot chain

• Mutables are added by reference → modifying them later changes the list

• Strings are iterables → extend() breaks them into chars, append() adds whole string

  

---

  

## Python List Method: `insert()`

  

• **`l.insert(item,index)`** : it inserts the element at the given specific index in the list , none error , it doesn't raise index out of range error if given index is less than zero it will add at first else at last , returns none modifies list in place

  

### ✅ Definition

  

**`list.insert(index, element)`**

• Inserts an element at a specific position in the list.

• Shifts elements to the right to make space.

• Modifies the original list in place.

• Returns None.

  

### 1. **Basic Usage**

  

```python

lst = [1, 2, 3]

lst.insert(1, 10)  

print(lst)  # [1, 10, 2, 3]

```

• index = 1 → insert before element at index 1.

  

### 2. **Insert at beginning**

  

```python

lst = [1, 2, 3]

lst.insert(0, 100)

print(lst)  # [100, 1, 2, 3]

```

  

### 3. **Insert at end**

  

```python

lst = [1, 2, 3]

lst.insert(len(lst), 200)

print(lst)  # [1, 2, 3, 200]

```

• ❌ Using append() is faster for end, but insert() works.

  

### 4. **Negative index**

  

```python

lst = [1, 2, 3]

lst.insert(-1, 99)

print(lst)  # [1, 2, 99, 3]

```

• Negative index counts from the end.

• If index < -len(lst) → inserts at beginning.

• If index > len(lst) → inserts at end.

  

### 5. **Insert with mutable objects**

  

```python

lst = [[1], [2]]

lst.insert(1, [0])

print(lst)  # [[1], [0], [2]]

lst[1].append(5)

print(lst)  # [[1], [0,5], [2]] → mutable reference

```

  

### 6. **Inserting a list vs extend**

  

```python

lst = [1, 2]

lst.insert(1, [3, 4])

print(lst)  # [1, [3,4], 2] → inserted as **single element**

```

• ❌ If you want to add elements individually, use extend() instead.

  

### 7. **Edge Cases**

• **Empty list:**

  

```python

lst = []

lst.insert(0, 10)

print(lst)  # [10]

```

• **Index out of bounds:**

  

```python

lst = [1, 2]

lst.insert(100, 99)

print(lst)  # [1, 2, 99] → adds at **end**

  

lst.insert(-100, 0)

print(lst)  # [0, 1, 2, 99] → adds at **start**

```

  

### 8. **Key Notes / Tricky Points**

1. insert() shifts elements to the right → slow for large lists.

2. Works with any object: number, string, list, tuple, dict, etc.

3. Returns None → cannot chain.

4. Negative indices start from the end, but indices beyond range are handled gracefully.

5. Do not confuse with append/extend: insert() can place element anywhere, not just end.

  

### 💡 TL;DR Memory Trick

• **append()** → add at end

• **extend()** → add elements individually at end

• **insert()** → add anywhere by index

  

### Additional Notes

If you want, I can make a mega table comparing append(), extend(), and insert() with tricky cases & examples, so it's super easy to memorize.

Do you want me to make that table?

You said:

is it give index out of range error

ChatGPT said:

No — insert() does not raise IndexError for out-of-range indices. Python handles it gracefully:

  

### 1. **Index larger than list**

  

```python

lst = [1, 2, 3]

lst.insert(100, 99)  # index > len(lst)

print(lst)  # [1, 2, 3, 99] → added at end

```

  

### 2. **Index smaller than negative length**

  

```python

lst = [1, 2, 3]

lst.insert(-100, 0)  # index < -len(lst)

print(lst)  # [0, 1, 2, 3] → added at start

```

  

### ✅ Key Notes

• Python caps the index:

  ○ index > len(lst) → inserts at end

  ○ index < -len(lst) → inserts at start

• No IndexError is raised, unlike direct assignment (lst[100] = 5 would fail).

  

---

  

## Python List Method: `remove()`

  

• **`l.remove(element)`** : it will remove the first occurrence of element , returns none, Value Error if not found , removing from empty list also give value error

  

### ✅ Definition

  

**`list.remove(element)`**

• Removes the first occurrence of the specified element from the list.

• Modifies the list in place.

• Returns None.

  

### 1. **Basic Usage**

  

```python

lst = [1, 2, 3, 2]

lst.remove(2)

print(lst)  # [1, 3, 2] → removes **first 2 only**

```

  

### 2. **Removing an element not present → ❌ ValueError**

  

```python

lst = [1, 2, 3]

lst.remove(5)  # ❌ ValueError: list.remove(x): x not in list

```

• **Tip:** check if element exists first:

  

```python

if 5 in lst:    

    lst.remove(5)

```

  

### 3. **Works with any object**

  

```python

lst = ["a", "b", "c", "b"]

lst.remove("b")

print(lst)  # ['a', 'c', 'b'] → removes **first occurrence**

```

• Works with numbers, strings, tuples, objects, etc.

  

### 4. **Only removes first occurrence**

  

```python

lst = [1, 2, 2, 2, 3]

lst.remove(2)

print(lst)  # [1, 2, 2, 3] → only first 2 removed

```

• To remove all occurrences → use a loop or list comprehension:

  

```python

lst = [1, 2, 2, 3]

lst = [x for x in lst if x != 2]

print(lst)  # [1, 3]

```

  

### 5. **Works with mutable objects**

  

```python

lst = [[1], [2], [1]]

lst.remove([1])

print(lst)  # [[2], [1]] → removes **first matching list**

```

• Matches by equality (==), not by reference (is)

  

```python

a = [1]

b = [1]

lst = [a, b]

lst.remove([1])  # removes a (first one) → equality used

```

  

### 6. **Removing from empty list → ❌ ValueError**

  

```python

lst = []

lst.remove(1)  # ❌ ValueError

```

  

### 7. **Return value**

  

```python

lst = [1, 2, 3]

result = lst.remove(2)

print(result)  # None → in-place operation

```

• Cannot chain remove() calls.

  

### 8. **Common interview tricky points**

1. Only first occurrence is removed.

2. Raises ValueError if element doesn't exist.

3. Works on mutable and immutable objects.

4. Cannot remove by index — that's what pop() is for.

  

### 💡 TL;DR / Memory Tricks

• **remove(x)** → remove first x in list

• Not found → ValueError

• Only first → use list comprehension to remove all

• Returns None → cannot chain

  

---

  

## Python List Method: `pop()`

  

• **`l.pop()`** : by default it remove the last element , if index is passed it will remove the element at that index, returns the deleted element , IndexError if index is > len(a) and if the list is empty

  

### ✅ Definition

  

**`list.pop(index=-1)`**

• Removes and returns an element at the given index.

• Default index = -1 → removes the last element.

• Modifies the list in place.

  

### 1. **Basic Usage (pop last)**

  

```python

lst = [1, 2, 3]

x = lst.pop()

print(x)   # 3 → popped element

print(lst) # [1, 2]

```

  

### 2. **Pop specific index**

  

```python

lst = [10, 20, 30]

y = lst.pop(1)

print(y)   # 20

print(lst) # [10, 30]

```

  

### 3. **Negative index**

  

```python

lst = [1, 2, 3]

x = lst.pop(-2)

print(x)   # 2

print(lst) # [1, 3]

```

• Works like normal list indexing.

  

### 4. **Empty list → ❌ IndexError**

  

```python

lst = []

lst.pop()  # ❌ IndexError: pop from empty list

```

• Cannot pop if list is empty.

  

### 5. **Return value**

• pop() returns the removed element (unlike remove() which returns None).

  

```python

lst = [1,2,3]

removed = lst.pop()

print(removed)  # 3

```

• Useful in stack (LIFO) operations.

  

### 6. **Pop in a loop**

  

```python

stack = [1,2,3,4]

while stack:    

    print(stack.pop())

# Output: 4 3 2 1 → last-in-first-out

```

  

### 7. **Pop vs remove**

  

| Feature | **pop()** | **remove()** |

|---------|-----------|--------------|

| Removes | by index | by value |

| Returns | removed element | None |

| Default | last element (-1) | must specify value |

| Raises error | IndexError if invalid | ValueError if not found |

  

### 8. **Tricky / important points**

1. pop() returns the removed element, unlike remove() (returns None).

2. Negative index works the same as normal indexing.

3. Default behavior pops last element → useful for stacks.

4. Index out of range → IndexError, cannot handle gracefully.

5. Can be used in LIFO operations.

6. Does not remove all occurrences → use remove() for that.







# Python List Methods — clear(), index(), count(), sort(), reverse(), copy()

---

  

## list.clear()

  

l.clear() : it will wmpty the list , outpot none, error none ,

🔹 Python List Method: clear()

✅ Definition

list.clear()

Removes all elements from the list.

Modifies the list in place.

Returns None.

  

1. Basic Usage

  

```python

lst = [1, 2, 3]

lst.clear()

print(lst)  # []

```

The list becomes empty, but the list object still exists.

  

2. Return Value

  

```python

lst = [1, 2, 3]

res = lst.clear()

print(res)  # None

```

Important: clear() does not return the cleared list — it modifies in place.

  

3. On Empty List

  

```python

lst = []

lst.clear()

print(lst)  # [] → no error

```

Works safely even if the list is already empty.

  

4. Effect on References

  

```python

lst1 = [1, 2, 3]

lst2 = lst1  # another reference

lst1.clear()

print(lst2)  # [] → also cleared!

```

Tricky point: clear() affects all references to the list because it modifies the original object in place.

  

5. Difference from Reassignment

  

```python

lst1 = [1,2,3]

lst2 = lst1

lst1 = []       # reassigns lst1, lst2 unchanged

lst1.clear()    # clears lst1 in place, lst2 also affected

```

lst = [] → creates a new list object

lst.clear() → empties existing list object

  

6. Tricky / Interview Points

Returns None → cannot chain: lst.clear().append(1) ❌

Works with any list — empty or filled.

Modifies in place → references to the list are affected.

Cannot use with non-list objects → dict.clear(), set.clear() exist separately.

  

💡 TL;DR Memory Tricks

lst.clear() → empty the list in place

Existing references → also empty

Safe on empty list, returns None

  

---

  

## list.index()

  

l.index(value, start , end ) : it will give the index of first occurance of value , if not found ValueError, output is int

  

🔹 Python List Method: index()

✅ Definition

list.index(element, start=0, end=len(list))

Returns the index of the first occurrence of the element in the list.

Optional start and end arguments restrict the search to a subsection of the list.

Raises ValueError if the element is not found.

  

1. Basic Usage

  

```python

lst = [10, 20, 30, 20]

print(lst.index(20))  # 1 → first occurrence

```

  

2. Using start and end

  

```python

lst = [10, 20, 30, 20, 40]

print(lst.index(20, 2))    # 3 → start searching from index 2

print(lst.index(20, 0, 2)) # 1 → search in index 0 to 1

```

start is inclusive, end is exclusive.

  

3. Element not in list → ❌ ValueError

  

```python

lst = [1,2,3]

lst.index(5)  # ❌ ValueError: 5 is not in list

```

Tip: use if x in lst before calling index() to avoid errors.

  

4. Works with any object

  

```python

lst = ["a", "b", "c", "b"]

print(lst.index("b"))  # 1 → first occurrence

```

Works with numbers, strings, tuples, objects, etc.

  

5. Tricky Points

First occurrence only

  

```python

lst = [1,2,3,2]

lst.index(2)  # 1 → not 3

```

IndexError confusion → People often think it raises IndexError if not found, but it’s ValueError.

Slicing with start/end

start and end are indices relative to the full list, not the sliced list.

Mutable objects

  

```python

lst = [[1,2], [3,4], [1,2]]

print(lst.index([1,2]))  # 0 → equality used, not reference

```

  

6. Quick Tips / Tricky Scenarios

Check before calling:

  

```python

if 5 in lst:

    print(lst.index(5))

```

With tuples or other objects:

  

```python

lst = [(1,2), (3,4)]

print(lst.index((3,4)))  # 1

```

Cannot use negative indices for index() start/end in confusing ways; they are interpreted as usual Python indices (start from end).

  

💡 TL;DR Memory Tricks

lst.index(x) → first index of x

Optional start/end restricts search

Raises ValueError if not found

First occurrence only

Equality (==) used, not identity

  

---

  

## list.count()

  

l.count(value) : give how much time the value is present , Output int , Error none ,

  

🔹 Python List Method: count()

✅ Definition

list.count(element)

Returns the number of occurrences of the specified element in the list.

Does not modify the list.

Works with any object.

  

1. Basic Usage

  

```python

lst = [1, 2, 2, 3, 2]

print(lst.count(2))  # 3 → number of times 2 appears

```

  

2. Works with strings in a list

  

```python

lst = ["a", "b", "a", "c"]

print(lst.count("a"))  # 2

```

  

3. Works with mutable objects

  

```python

lst = [[1], [2], [1]]

print(lst.count([1]))  # 2 → equality (`==`) is used

```

Tricky point: count() uses equality comparison, not object identity.

  

4. Element not present

  

```python

lst = [1,2,3]

print(lst.count(5))  # 0 → returns 0, no error

```

Unlike index() or remove(), does not raise an error if element is absent.

  

5. Nested lists / complex objects

  

```python

lst = [[1,2], [3,4], [1,2]]

print(lst.count([1,2]))  # 2 → matches equal lists

```

Works similarly for tuples, strings, or other objects.

  

6. Tricky / important points

Does not modify the list → safe for checks.

Equality comparison used, not reference.

Returns 0 if element not found.

Works with any object type, including numbers, strings, tuples, lists, etc.

Can be used in conditionals:

  

```python

if lst.count(2) > 1:

    print("2 occurs more than once")

```

  

💡 TL;DR Memory Tricks

lst.count(x) → how many times x appears

Equality (==) used, not identity

Returns 0 if not found

Does not modify the list

  

---

  

## list.sort()

  

l.sort() : modifies the original list , TypeError if of mixed datatypes, output none , can use key , can use reverse to make dec to asc

  

🔹 Python list.sort() — Important & Expected Points

1. Sorts the list in place

  

```python

lst = [3, 1, 2]

lst.sort()

print(lst)  # [1, 2, 3]

```

✅ Important: modifies the original list, does not return a new list.

  

2. Default behavior

Sorts in ascending order for numbers or lexicographically for strings.

  

```python

lst = ["banana", "apple", "cherry"]

lst.sort()

print(lst)  # ['apple', 'banana', 'cherry']

```

  

3. Using reverse=True

  

```python

lst = [3, 1, 2]

lst.sort(reverse=True)

print(lst)  # [3, 2, 1]

```

Sorts in descending order.

  

4. Using key argument

Provides a function that computes a value to sort by.

  

```python

words = ["apple", "banana", "cherry"]

words.sort(key=len)

print(words)  # ['apple', 'cherry', 'banana'] → sorted by length

```

  

5. Sorting by last character

  

```python

words = ["dog", "cat", "elephant"]

words.sort(key=lambda x: x[-1])

print(words)  # ['elephant', 'dog', 'cat']

```

✅ Subtle point: when keys are equal, Python preserves original order (stable sort).

  

6. Sorting lists of tuples/dicts

  

```python

data = [("Alice", 25), ("Bob", 20)]

data.sort(key=lambda x: x[1])  # sort by age

print(data)  # [('Bob', 20), ('Alice', 25)]

```

Works for lists of any objects, as long as the key function returns a comparable value.

  

7. Mixed types

  

```python

lst = [1, "a", 2]

lst.sort()  # ❌ TypeError: '<' not supported between instances of 'str' and 'int'

```

Cannot sort a list with incompatible types without a custom key function.

  

8. Stable sorting

Python’s sort is stable → preserves the relative order of elements with equal keys.

  

```python

lst = [(1, 'b'), (2, 'a'), (1, 'a')]

lst.sort(key=lambda x: x[0])

print(lst)  # [(1,'b'), (1,'a'), (2,'a')]

```

✅ Important for multi-level sorting.

  

9. Tricky / subtle points

Modifies the list in place, returns None → cannot chain calls.

key function is called once per element → efficient.

reverse=True does not reverse keys, only final order.

Works on numbers, strings, tuples, objects as long as elements are comparable.

Raises TypeError if elements are not comparable.

  

✅ TL;DR / Expected Uses

Sort a list in ascending or descending order.

Use key to sort by length, last character, dictionary values, object attributes.

Stable → preserves original order when keys are equal.

Use reverse=True for descending order.

Modifies the list in place → returns None.

  

---

  

## list.reverse()

  

l.reveerse() : it reverses the lsit , output nonr , s=reverse in place , none Error

  

🔹 Python list.reverse() — Important & Expected Points

1. Reverses the list in place

  

```python

lst = [1, 2, 3]

lst.reverse()

print(lst)  # [3, 2, 1]

```

✅ Important: modifies the original list, does not return a new list.

  

2. Return value

  

```python

lst = [1, 2, 3]

res = lst.reverse()

print(res)  # None

```

Tricky point: returns None, so cannot chain calls.

  

3. Works with any type

  

```python

lst = ["a", "b", "c"]

lst.reverse()

print(lst)  # ['c', 'b', 'a']

```

Works with numbers, strings, tuples, objects — just reverses the order.

  

4. Difference from slicing

  

```python

lst = [1, 2, 3]

rev = lst[::-1]

print(rev)  # [3, 2, 1] → new list

print(lst)  # [1, 2, 3] → original list unchanged

```

reverse() → in-place, no new list.

[::-1] → returns a new reversed list, original unchanged.

  

5. Reversing after sorting

  

```python

lst = [3, 1, 2]

lst.sort()

lst.reverse()

print(lst)  # [3, 2, 1]

```

✅ Expected use: combine with sort() for descending order.

  

6. Empty list

  

```python

lst = []

lst.reverse()

print(lst)  # [] → safe, no error

```

  

- Tricky / subtle points
- Modifies the list in place → all references to the list see the change.
- Returns None → cannot chain.
- Works for any object type.
- Safe on empty lists.
- Often used after sorting, or to implement stack reversal.

  

✅ TL;DR / Expected Uses

- Reverse the order of elements in a list in place.
- Works with numbers, strings, tuples, lists, or objects.
- Use after sorting to get descending order.
- Returns None, modifies original list.
- Safe for empty lists.

  

---

  

## list.copy()

  

l.copy() : it give a list  , creates the copy of list , error none

🔹 Python list.copy() — Important & Expected Points
1. Creates a shallow copy of the list

  

```python

lst = [1, 2, 3]

lst_copy = lst.copy()

print(lst_copy)  # [1, 2, 3]

```

✅ Important: new list object, but elements are the same references (shallow copy).

  

2. Original list unaffected

  

```python

lst = [1, 2, 3]

lst_copy = lst.copy()

lst_copy.append(4)

print(lst)      # [1, 2, 3]

print(lst_copy) # [1, 2, 3, 4]

```

Changes to the copy do not affect the original list.


3. Shallow copy behavior with mutable elements

  

```python

lst = [[1,2], [3,4]]

lst_copy = lst.copy()

lst_copy[0].append(5)

print(lst)      # [[1,2,5], [3,4]] → inner list modified

print(lst_copy) # [[1,2,5], [3,4]]

```

✅ Subtle point: copy() is shallow, so inner mutable objects are shared.
For a deep copy, use copy.deepcopy() from the copy module.

  

4. Works on empty list


```python

lst = []

lst_copy = lst.copy()

print(lst_copy)  # []

```
Safe even if the list is empty.
  

5. Return value

```python

lst = [1, 2, 3]

res = lst.copy()

print(res)  # [1, 2, 3] → returns the new list

```

Unlike append(), extend(), or reverse(), copy() returns a new list.

  

6. Tricky / subtle points
- Shallow copy → inner mutable elements are still shared.
- Modifies nothing, just returns a new list.
- Useful for preserving the original list before modifications.
- Can be combined with operations like sort() or reverse() without affecting the original list.
- Safer than slicing (lst[:]) when you want explicit copy semantics.

  

✅ TL;DR / Expected Uses

- Create a shallow copy of a list.
- Changes to the copy do not affect the original list (except inner mutables).
- Safe for empty lists.
- Returns new list object.
- Use when you want to preserve the original list before modifying it.