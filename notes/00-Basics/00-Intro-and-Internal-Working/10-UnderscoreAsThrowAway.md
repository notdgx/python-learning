---
date: 2026-08-30
time: "19:34:11+05:30"
---
# THROWAWAY _ AND DUNDER METHODS

---

# _ AS THROWAWAY

---

## Idea

When Python unpacks or iterates, every position needs a name. Sometimes you genuinely do not care about certain values. Instead of making up a fake name like `unused` or `temp`, Python convention is to use `_` as a signal that says "I am explicitly ignoring this value".

It is not special syntax. `_` is a completely normal variable name that just happens to be a single underscore. The convention gives it meaning, not the language.

---

## In Loops

```python
# you want to do something 5 times
# you do not care about the loop counter

for _ in range(5):
    print("hello")

# output:
# hello
# hello
# hello
# hello
# hello
```

Compare with using a real name:

```python
for i in range(5):       # i exists but is never used
    print("hello")       # linters will warn: variable i unused
```

Using `_` silences the linter warning and communicates intent clearly -- "I know I am not using this value, that is deliberate."

What actually happens internally:

```python
for _ in range(5):
    print("hello")

# bytecode does this:
# LOAD iteration value
# STORE_FAST _         <- _ gets assigned each iteration
# body executes
# repeat
# _ gets overwritten each loop with new value
# after loop _ holds the last value (4 in this case)

print(_)    # 4 -- _ is a real variable, holds last value
```

`_` is a real name. It gets assigned. It just signals to humans "ignore this".

---

## In Unpacking

When you unpack a tuple or list but only need some positions:

```python
# function returns three values, you only need first and last
def get_data():
    return "alice", 30, "engineer"

name, _, job = get_data()
print(name)    # alice
print(job)     # engineer
print(_)       # 30 -- still assigned, just ignored by convention
```

```python
# database row -- you only need name and salary
row = (1, "alice", "engineering", 95000, "2020-01-15")

id_, name, _, salary, _ = row
print(name)     # alice
print(salary)   # 95000
```

Note: when you use `_` multiple times in the same unpacking, each one overwrites the previous. Only the last value is held:

```python
_, name, _, salary, _ = (1, "alice", "eng", 95000, "2020")
print(_)    # "2020" -- last assignment wins
```

---

## Extended Unpacking With *_

```python
# grab first and last, ignore everything in middle
first, *_, last = [1, 2, 3, 4, 5, 6, 7]
print(first)    # 1
print(last)     # 7
print(_)        # [2, 3, 4, 5, 6] -- middle collected as list

# grab just first, ignore rest
first, *_ = [1, 2, 3, 4, 5]
print(first)    # 1
print(_)        # [2, 3, 4, 5]

# grab just last, ignore rest
*_, last = [1, 2, 3, 4, 5]
print(last)     # 5
print(_)        # [1, 2, 3, 4]
```

---

## In Nested Unpacking

```python
# list of (name, (age, city)) tuples
people = [
    ("alice", (30, "delhi")),
    ("bob",   (25, "mumbai")),
]

for name, (_, city) in people:
    print(name, city)
# alice delhi
# bob mumbai
# age is ignored via _ in nested unpack
```

---

## Multiple _ In Same Line 

```python
# this looks like ignoring two things
# but _ is ONE variable assigned twice
a, _, b, _ = (1, 2, 3, 4)
print(_)    # 4 -- only last assignment kept
            # 2 was assigned then overwritten by 4
```

If you want to ignore multiple truly separate values and not have them collide, some people use `_1`, `_2` etc though this is not standard:

```python
a, _1, b, _2 = (1, 2, 3, 4)    # non-standard but avoids collision
```

---

## In REPL -- Special Behavior

In the interactive Python shell, `_` has an additional automatic behavior:

```python
>>> 5 + 3
8
>>> _
8              # _ automatically holds last expression result

>>> "hello".upper()
'HELLO'
>>> _
'HELLO'

>>> x = 10     # assignment does NOT update _
>>> _
'HELLO'        # still previous result, assignment skipped
```

This is built into the REPL itself. Not available in scripts. In scripts `_` is just a normal variable.

---

## In Internationalisation (i18n)

One legitimate non-throwaway use of `_` as a name:

```python
import gettext
_ = gettext.gettext    # _ bound to translation function

# now all strings wrapped in _() get translated
print(_("Hello"))      # looks up translation for "Hello"
print(_("Welcome"))    # looks up translation for "Welcome"
```

This convention comes from C's gettext library. Django and many frameworks use it. When you see `_("some string")` in code it means "translate this string", not a throwaway.

---
