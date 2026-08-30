# Topics 

- List , Dict , Tuples , Sets, FSets

# PyObjects

### Common Fields of All DataTypes

#### ob_refcnt

```
Simple meaning: how many things are pointing at this object right now
```
```python
x = 10        # ob_refcnt = 1  (x points to it)
y = x         # ob_refcnt = 2  (x and y both point to it)
del x         # ob_refcnt = 1  (only y points now)
del y         # ob_refcnt = 0  -> IMMEDIATELY FREED from memory
```

- When this hits zero, Python says "nobody needs this anymore" and f==rees the memory==. That is the entire garbage collection mechanism for most cases. Just a counter.

---

#### ob_type

```
Simple meaning: what TYPE is this object -- int? str? list? your custom class?
```
```python
x = 10
# ob_type points to the int class
# this is how Python knows x is an int at runtime
# this is how x.bit_length() works -- look up bit_length in ob_type
# this is how x + y works -- look up __add__ in ob_type
```

- Every single operation Python does on an object starts here. It checks ob_type first. Always. Without ob_type there is no dynamic typing. It is the backbone of everything.


## Pythonlist -- PyListObject


```c
// Include/listobject.h
typedef struct {
    PyObject_VAR_HEAD        // refcnt + ob_type + ob_size (current length)
    PyObject **ob_item;      // pointer to array of PyObject pointers
    Py_ssize_t allocated;    // total slots allocated (capacity)
} PyListObject;
```

Expanded:

```c
typedef struct {
    Py_ssize_t    ob_refcnt;    // 8 bytes
    PyTypeObject *ob_type;      // 8 bytes  points to PyList_Type
    Py_ssize_t    ob_size;      // 8 bytes  current number of items
    PyObject    **ob_item;      // 8 bytes  pointer to the array
    Py_ssize_t    allocated;    // 8 bytes  allocated capacity
} PyListObject;
// Total: 40 bytes for the struct itself
// PLUS separate heap allocation for the ob_item array
```

The actual items are NOT inside this struct. `ob_item` is a pointer to a separate heap-allocated array of PyObject pointers:

```
PyListObject (40 bytes on heap)
+------------------+
| ob_refcnt = 1    |
| ob_type = list   |
| ob_size = 3      |  <- 3 items currently
| ob_item ---------|----> [ptr][ptr][ptr][...empty slots...]
| allocated = 4    |         |     |     |
+------------------+         v     v     v
                          PyObj PyObj PyObj
                          (1)   (2)   (3)
```

- `ob_size` is current length. `allocated` is total capacity. When you `append` and `ob_size == allocated`, Python allocates a bigger array and copies pointers over. This is the same as `std::vector` growth in C++.

### ob_size

```
Simple meaning: how many items are currently in the list RIGHT NOW
```

```python
lst = [1, 2, 3]    # ob_size = 3
lst.append(4)      # ob_size = 4
lst.pop()          # ob_size = 3
print(len(lst))    # len() just reads ob_size directly, instant
```

`len()` on a list is instant because it just reads this field. It does not count anything.

---

### ob_item

```
Simple meaning: the actual array where the list items live
               but it stores POINTERS to items, not the items themselves
```

```python
lst = [1, "hello", 3.14]
# ob_item[0] -> points to PyObject(int 1)
# ob_item[1] -> points to PyObject(str "hello")
# ob_item[2] -> points to PyObject(float 3.14)
```

Because it stores pointers not values, a list can hold mixed types. Each slot is just an address pointing somewhere else in the heap. Does not matter what type lives there.

---

### allocated

```
Simple meaning: how many slots are reserved in memory total
               even if some are empty and not used yet
```

```python
lst = []           # ob_size=0, allocated=0
lst.append(1)      # ob_size=1, allocated=4   <- grabbed 4 slots upfront
lst.append(2)      # ob_size=2, allocated=4   <- used existing slot, no resize
lst.append(3)      # ob_size=3, allocated=4   <- same
lst.append(4)      # ob_size=4, allocated=4   <- same
lst.append(5)      # ob_size=5, allocated=8   <- ran out, grabbed 8 slots
```

- Python grabs extra empty slots in advance so it does not resize every single append. Resizing means allocating new memory and copying everything over which is slow. By grabbing extra slots upfront, most appends are instant. This is the same trick C++ std::vector uses.

---

## Python dict -- PyDictObject


```c
// Simplified from Include/cpython/dictobject.h
typedef struct {
    PyObject_HEAD              // refcnt + ob_type
    Py_ssize_t ma_used;        // number of key-value pairs
    PyDictKeysObject *ma_keys; // pointer to keys structure (hash table)
    PyObject **ma_values;      // pointer to values array
} PyDictObject;
```

The hash table inside `ma_keys` uses open addressing with a compact index array:

```
dict {"a": 1, "b": 2}

PyDictObject
+------------------+
| ob_refcnt        |
| ob_type = dict   |
| ma_used = 2      |
| ma_keys ---------|----> hash table
| ma_values -------|----> [PyObj(1), PyObj(2)]
+------------------+

hash table:
index array:  [-, 0, -, 1, -, -, -, -]
                   |        |
entries:      [hash,"a",ptr][hash,"b",ptr]
```

### ma_used

```
Simple meaning: how many key-value pairs are in the dict right now
```


```python
d = {"a": 1, "b": 2}    # ma_used = 2
d["c"] = 3               # ma_used = 3
del d["a"]               # ma_used = 2
print(len(d))            # reads ma_used directly, instant
```

Same idea as ob_size in list. len() just reads this, does not count.

---

### ma_keys

```
Simple meaning: the hash table that stores keys and lets Python find them fast
```
```python
d = {"name": "alice", "age": 30}
d["name"]    # Python hashes "name" -> gets a number
             # uses that number to find the slot instantly
             # no searching through all keys
             # O(1) lookup
```

Without this, finding a key would mean checking every key one by one. With the hash table, Python jumps directly to the right slot. This is why dict lookup is fast regardless of size.

---

### ma_values

```
Simple meaning: the array that stores the VALUES corresponding to each key
```
```python
d = {"a": 1, "b": 2}
# ma_keys  has "a" and "b" with their hash positions
# ma_values has PyObject(1) and PyObject(2)
# when you look up d["a"]:
#   hash "a" -> find position in ma_keys -> get index -> read ma_values[index]
```

Keys and values are stored separately. Keys in the hash table structure. Values in a plain array. Finding the key tells you the index. That index reads the value from ma_values.
_______
_______

# Summary Table

```
Field          Lives in     Controls
-----          --------     --------
ob_refcnt      every object  memory lifetime, freed when hits 0
ob_type        every object  what type it is, how operations work
ob_size        int/list      int: how many digit slots used
                             list: how many items currently in it
ob_digit[]     int           the actual number data, split into chunks
ob_fval        float         the actual decimal number
length         str           how many characters
hash           str           cached fingerprint for dict lookups
kind           str           bytes per character (1, 2, or 4)
interned       str           is this string a shared global copy
ob_item        list          pointer to the array of item pointers
allocated      list          total reserved slots including empty ones
ma_used        dict          how many key-value pairs currently
ma_keys        dict          hash table for fast key lookup
ma_values      dict          array of value pointers
```


```
ob_refcnt   -> is anyone using this? if no, delete it
ob_type     -> what am I? how do I behave?
ob_size     -> how big am I right now?
ob_digit    -> my actual number data
ob_fval     -> my actual float data
length      -> how long am I (string)
hash        -> my fingerprint, pre-calculated
kind        -> how compact can I store my characters
ob_item     -> where my list items actually live
allocated   -> how much room did I grab in advance
ma_used     -> how many pairs do I have
ma_keys     -> my fast lookup table
ma_values   -> where my values actually live
```