def function_len():
    t1=(1,2,3,4,5,6)
    t2=(2,)
    t3=(2)
    print(len(t1))# Output: 6 as t1 is a tuple with 6 elements
    print(len(t2))# Output: 1 as t2 is a tuple with 1 element
    print(len(t3))# TypeError: t3 is not a tuple, it is an integer for it be a tuple it should be (2,)

def function_count():
    t1=("A","b","a","A",1,2,3,3,3,3,(1,2,3),(3),[1,2,3],{1,2,3},True,False)# tuple with mixed types

    print(t1.count("A")) # Output: 2, counts occurrences of "A"
    print(t1.count(3)) # output is 5 it will still count (3) as 1 occurrence
    print(t1.count((1,2,3))) # Output: 1, counts occurrences of the tuple (1,2,3)
    print(t1.count((1,2)))# Output: 0, counts occurrences of the tuple (1,2)
    print(t1.count())# type error as count() requires an argument
    print(t1.count(2,3))# TypeError: count() takes exactly one argument, but two were given

def function_index():
    t1=("A","b","a","A",1,2,3,3,3,3,(1,2,3),(3),[1,2,3],{1,2,3},True,False)# tuple with mixed types

    print(t1.index("A")) # Output: 0, first occurrence of "A" is at index 0
    print(t1.index("A",1))#searches for "A" starting from index 1, Output: 3
    print(t1.index(3,9,len(t1)))# searches for 3 starting from index 9 to the end, Output: 9
    print(t1.index())# TypeError: index() takes at least 1 argument (0 given)
    print(t1.index("AAA"))# ValueError: "AAA" is not in tuple t1

def function_in():
    t1=("A","b","a","A",1,2,3,3,3,3,(1,2,3),(3),[1,2,3],{1,2,3},True,False)# tuple with mixed types

    print("A"in t1) # Output: True, "A" is in the tuple
    print("X"in t1) # Output: False, "X" is not in the tuple
    print((1)in t1) # Output: True, 1 is in the tuple (1) is same as 1
    print((1,2,3)in t1) # Output: True, (1,2,3) is in the tuple

def function_tuplepacking():
    t1=1,2,3,5
    t2=(1,)
    t3=(1)
    a,b,c=1,2,3


    print(type(t1)) # Output: <class 'tuple'>, t1 is a tuple
    print(type(t2)) # Output: <class 'tuple'>, t2 is a tuple
    print(type(t3)) # Output: <class 'int'>, t3 is not a tuple, it is an integer
    d=a,b,c # d is a tuple (1, 2, 3)
    print(type(d)) # Output: <class 'tuple'>

def function_unpacking():
    t1=1,2,3,5
    a,b,c,d=t1
    print(a, b, c, d)  # Output: 1 2 3 5, unpacking the tuple t1

    x,y,z=t1  # Unpacking t1 into x, y, z
    print(x, y, z)  # Value Error: not enough values to unpack (expected 3, got 4)

    print(type(a))  # Output: <class 'int'>, a is an integer


def function_tuples():
    a="Tuple"
    b=[1,2,3,5]
    c=(1,2,3,5)
    d=25
    e=True
    f=25,

    print(tuple(a))  # Output: ('T', 'u', 'p', 'l', 'e'), converts string to tuple
    print(tuple(b))  # Output: (1, 2, 3, 5), converts list to tuple
    print(tuple(c))  # Output: (1, 2, 3, 5), c is already a tuple
    print(tuple(d))  # Output: TypeError: cannot convert 'int' object to tuple
    print(tuple(e))  # Output: TypeError: cannot convert 'bool' object to tuple
    print(tuple(f))  # Output: (25,), converts single-element tuple to 
    

def function_min_max():
    t1=(21,22,23,24,25,26,27,28,29,30,1,2,3,4,5,6,7,8,9,10)
    t2=(1,2,3,4,5,6,7,8,9,10,"a","b","c","d","e","f","g","h","i","j")
    print(min(t1))  # Output: 1, minimum value in t1
    print(max(t1))  # Output: 1, minimum value in t2


    print(min(t2))  # Type ERROR: min() not supported between instances of 'int' and 'str'
    print(max(t2))  # Type ERROR: max() not supported between instances of 'int' and 'str'

    print(min(()))# ValueError: min() arg is an empty 


def function_sum():
    t1=(21,22,23,24,25,26,27,28,29,30,1,2,3,4,5,6,7,8,9,10)
    t2=(1,2,3,4,5,6,7,8,9,10,"a","b","c","d","e","f","g","h","i","j")

    print(sum(t1))  # Output: 255, sum of all elements in t1
    print(sum(t2))  # Type ERROR: sum() not supported between instances of 'int' and 'str'\


def function_sorted():
    t1=(21,22,23,24,25,26,27,28,29,30,1,2,3,4,5,6,7,8,9,10)# tuple of numbers
    print(id(t1))  # Print the memory address of the tuple

    a=sorted(t1,reverse=True)  # Sort the tuple
    print(a)  # Print the sorted tuple
    print(id(a))  # Print the memory address of the sorted tuple
    #here we can see that the memory address of the sorted tuple is different from the original tuple 
    #because tuple is immutable and sorted() returns a new list of tuple elements in sorted order
    #so the original tuple remains unchanged
            
def function_reversed():
    t1=(2,3,4,5,"A","B",True,False,[1,2,3],{1,2,3},(1,2,3),{1,2,3},(1,2),{1:2},(1,2,3,4))
    print(id(t1))  # Output: Memory address of t1

    a=reversed(t1)
    print(id(a))  # Output: Memory address of the reversed object
    print(a)  # Output: <reversed object at ...>

    #can be converted to a listor tuple as we got a as a reversed object

    print(list(a))  # Output: [(1, 2, 3, 4), {1: 2}, (1, 2), {1, 2, 3}, (1, 2, 3), {1, 2, 3}, [1, 2, 3], False, True, 'B', 'A', 5, 4, 3, 2]
    print(tuple(a)) # () because a is already exhausted after the first conversion

    t2=(1,2,3,4,5)
    print(tuple(reversed(t2)))  # Output: (5, 4, 3, 2, 1), reverses the tuple t2

def function_all():
    t1=(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
    t2=(1,0,1,0,1,0,1,0,1,0,1,0,1,0,1)
    t3=(1,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
    t4=("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O")
    t5=(True,True)
    t6=(True,False,True,False,True,False,True,False,True,False,True,False,True,False,True)
    t7=("a","","")

    print(all(t1))  # Output: False, as all elements are 0
    print(all(t2))  # Output: False, as not all elements are True
    print(all(t3))  # Output: False, as not all elements are True
    print(all(t4))  # Output: True, as all elements are non-empty strings
    print(all(t5))  # Output: True, as all elements are True
    print(all(t6))  # Output: False, as not all elements are True
    print(all(t7))  # Output: False, as not all elements are non-empty strings

def function_any():
    t1=(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
    t2=(1,0,1,0,1,0,1,0,1,0,1,0,1,0,1)
    t3=(1,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
    t4=("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O")
    t5=(True,True)
    t6=(True,False,True,False,True,False,True,False,True,False,True,False,True,False,True)
    t7=("a","","")
    print(any(t1))  # Output: False, as all elements are 0
    print(any(t2))  # Output: True, as at least one element is non-zero
    print(any(t3))  # Output: True, as at least one element is True
    print(any(t4))  # Output: True, as all elements are non-empty strings
    print(any(t5))  # Output: True, as all elements are True
    print(any(t6))  # Output: True, as at least one element is True
    print(any(t7))  # Output: True, as at least one element is non-empty string


# function_len()
# function_count()
# function_index()
# function_in()
# function_tuplepacking()
# function_unpacking()
# function_tuples()
# function_min_max()
# function_sum()
# function_sorted()
# function_reversed()
# function_all()
# function_any()


# The code above defines various functions to demonstrate tuple operations in Python.
# Each function showcases different tuple methods and properties, such as length, counting elements, indexing, membership testing, packing and unpacking, conversion to tuples, finding minimum and maximum values, summing elements, sorting, reversing, and checking conditions with `all` and `any`.

