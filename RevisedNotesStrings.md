# RevisedNotesStrings 

--- 

## Metadata

- **Day :** Sunday
- **Date :** 2025-09-07
- **Time :** 16:05
- **Tags :** #python #revised #strings   
- **References :** [[RevisedNotes]] , [[FunctionsStrings]] , [[ImportantQuestionsSrtings1]]
- **Branch of :** Python > RevisedNotes > RevisedNotesStrings  
- **Author :**  dx

---

# Notes

# Strings

- **len()** : length, iterable must, else `TypeError`
    
- `l.upper()`, `l.lower()` : return new `str`, none Error
    
- `l.capatlize()` : first letter of first word , None
    
- `l.title()` : First letter of each word ,None
    
- `l.strip()`, `l.rstrip()`, `l.lstrip()` : it will by default remove space `\n` `\t` `\r` `\f` `\v` padding, or specified padding even `!@` can remove `!!!!!!!!!!@@@@@@@` , None Error
    
- `l.replace(oldsubstr,newstr,count)` : it will give a new str by repalacing that , `TypeError` if not string, or not at least 2 arg, no error if sub str not found
    
- `l.find(substr, start, end)` or `l.rfind()` : it will give the index of 1sst occuracnce , from left or , right , Give `-1` if not found , NO error
    
- `l.index(substr, start, end)`, `l.rfind()`: it will give the first occurance of str , from left/right , `ValueError` if not found
    
- `l.count(str, start, end)` : it will count the occurance of str , no error , even not index out of range error
    
- `l.split("SEPERAROR", MAXsplits)` / `l.rsplit()` : it will split the str into parts acc to substring passed, it doesn’t give separator in splitted list , None , GIVES LIST , Gives full str if separator not present
    
- `l.partition("SEPERATOOR")` : it will give a TUPLE of first split of str with the seperator , `ValueError` if not present
    
- `"SEPERATOR".join(iterable)` : Join the iterable with the seperator, `TypeError` if not iterable or not `str`
    
- `l.startswith(substr, start, end)` / `l.endswith()` : Return true if condition True, Output Type `bool`, no Error
    
- `str.isalpha()` / `str.isdigit()` / `str.isalnum()` / `str.isspace()` / `str.islower()` / `str.isupper()` / `str.istitle()` : Return `True` or `False` if the condition satisfy, NO arg required
    
- `l.zfill(TOTALLENGTH)` : it will pad the str left with zeroes and preserve sign , Pad as total length
    
- **`str.encode()`**
    
    - Syntax: `string.encode(encoding='utf-8')`
        
    - Input: `str`
        
    - Output: `bytes`
        
    - Error: `UnicodeEncodeError` if characters can’t be encoded.
        
    - Example: `"hello".encode()` → `b'hello'`
        
    
    ```python
    "hello".encode()  # b'hello'   (5 bytes: 68 65 6c 6c 6f in hex)
    
    "♥".encode("utf-8")  # b'\xe2\x99\xa5'  (3 bytes in UTF-8)
    ```
    
    `b` is byte literal
    
- **`str.format()` / `str.format_map()`**
    
    - Syntax: `string.format(*args, **kwargs)` / `string.format_map(mapping)`
        
    - Input: `str` with placeholders
        
    - Output: `str`
        
    - Error: `KeyError` / `IndexError` if placeholders missing.
        
    - Example: `"Hello {}".format("World")` → `"Hello World"`
        
- **`str.casefold()`**
    
    - Syntax: `string.casefold()`
        
    - Input: `str`
        
    - Output: `str`
        
    - Error: None
        
    - Example: `"Straße".casefold()` → `"strasse"`
        
    - Use: For aggressive lowercasing → best for case-insensitive comparison, especially with non-English text.
        

---

