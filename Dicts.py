def function_len():
    d1={1:"A",2:"B",3:"C",4:"D",5:"E"} #dictionary
    print(id(d1)) #prints the id of the dictionary

    print(len(d1)) #prints the length of the dictionary
    print(len({})) #prints the length of an empty dictionary
    print(len(123)) #raises TypeError because 123 is not a dictionary

def function_clear():
    d1={1:"A",2:"B",3:"C",4:"D",5:"E"} #dictionary
    print(id(d1)) #prints the id of the dictionary


    d1.clear() #clears the dictionary
    print(len(d1)) #prints the length of the cleared dictionary
    print(d1) #prints the cleared dictionary
    print(id(d1)) #prints the id of the cleared dictionary SAME as before
    d1.clear(2)# will raise TypeError because clear() does not take any arguments



def function_copy():
    d1={1:"A",2:"B",3:"C",4:"D",5:"E"} #dictionary
    print(id(d1)) #prints the id of the dictionary

    d2=d1.copy() #copying the dictionary
    print(id(d2)) #prints the id of the copied dictionary

    if d1 is d2: #checks if both variables point to the same dictionary
        print("TRUE")
    else:
        print("FALSE") #prints FALSE if they are not the same

    #Both d1 and d2 are different dictionaries


def function_fromkeys():
    d1={1:"A",2:"B",3:"C",4:"D",5:"E"} #dictionary
    l1=[1,2,3,4,5,6,6,7,8,9] #list
    t1=(1,2,3,4,56,67,889,89,) #tuple
    a=range(1,10) #range object
    b="HAPPYHAPPYHAPPY"
    c="HAPPYhappy"

    #dict1={}.fromkeys()# TypeError because fromkeys() requires at least one argument
    print(dict.fromkeys(l1)) #creates a dictionary with keys from l1 and values set to None
    print(dict.fromkeys(t1, "value")) #creates a dictionary with keys from t1 and all values set to "value"
    print(dict.fromkeys(a, 0)) #creates a dictionary with keys from range object a and all values set to 0
    print(dict.fromkeys(a,"VALUEE"))#creates a dictionary with keys range 1,10 and value"VALUEE"
    print(dict.fromkeys(b,2))# here we got only 5 letters because keys are immutable and unique
    print(dict.fromkeys(c,"YOO"))# we will get 10 keys because python is case senstive
    print(dict.fromkeys(123,2))# Type ERROR

def function_get():
    d1={1:"A",2:"B",3:"C",4:"D",5:"E"} #dictionary

    print(d1.get(1))# it will print the value AT key 1
    print(d1.get(10))# now the key is not presenrt it will return none as default is set at none
    print(d1.get(10,"NOT PRESENT SYBAU"))# now the default value is changed
    print(d1.get(3))# this will print the value corresponding to key 3

def function_items():
    d1={1:"A",2:"B",3:"C",4:"D",5:"E"} #dictionary

    print(d1.items())#it will print the dict_items object of key value pairs present in d1
    print(type(d1.items()))# <class 'dict_items'>
    print(list(d1.items()))#it will convert it into list
    print(tuple(d1.items()))# it will convert it into tuple
    print(d1.items(1))# it will raise TypeError as it takes no argunments

def function_keys():
    d1={1:"A",2:"B",3:"C",4:"D",5:"E"} #dictionary

    print(d1.keys())#it will print the dict_keys object of keys present in d1
    print(type(d1.keys()))# <class 'dict_keys'>
    print(list(d1.keys()))#it will convert it into list
    print(tuple(d1.keys()))# it will convert it into tuple
    print(d1.keys(1))# it will raise TypeError as it takes no argunments

def functions_pop():
    d1={1:"A",2:"B",3:"C",4:"D",5:"E"} #dictionary

    print(d1.pop())#TtypeError as it rrrequire at least 1 argunment 
    print(d1.pop(1))# it will remove the key value pair of key 1 from the dictionary and returns it
    print(d1.pop(7))#it will raise KeyError as not present
    print(d1.pop(7,"NOT PRESENT"))# to avoid keyeerrror we can add default valure that will be given when key not present


def function_popitem():
    d1={1:"A",2:"B",3:"C",4:"D",5:"E"} #dictionary

    print(d1.popitem())#it will remove the last key value pair and return it as a tuple
    print(d1.popitem(1))#it will give error as it take no argunments
    print({}.popitem())#it will give the key error as dictionary is empty
    print(d1)


def function_setdefault():
    d1={1:"A",2:"B",3:"C",4:"D",5:"E"} #dictionary

    print(d1.setdefault(1))#it will return the value of key if present otherwise assign the key with default value by default it is None
    print(d1.setdefault(7))#here 7 is not present it will make it key with value None
    print(d1.setdefault(8,"YOOOO"))# it will creaye a key 8 with value "YOOOO"
    print(d1.setdefault())#Type Error as it takes at least one argunment
    print(d1)

def function_values():
    d1={1:"A",2:"B",3:"C",4:"D",5:"E"} #dictionary

    print(d1.values())#give the value object contains the list of values present in d1
    print(type(d1.values()))#<class dict_values>
    print(d1.values(1))# type error as it takes no argunments


def function_update():
    d1={1:"A",2:"B",3:"C",4:"D",5:"E"} #dictionary
    d2={4:"M",5:"N",6:"K"}

    d3={1:"A",2:"B",3:"C",4:"D",5:"E"}
    d4={1:"A",2:"B",3:"C",4:"D",5:"E"}
    l1=[[1,"X"],[2,"Y"],[3,"Z"]]
    t1=((0,"K"),(9,"J"),(8,"L"))

    d1.update(d2)# it updated the exsisting key value as per d2
    print(d1,d2)

    d3.update(t1)# it will update the key value pairs in d3 as per t1
    print(d3,t1)

    d4.update(l1)# it updated the key value pairs as per l1
    print(d4,l1)

    d4.update(12)# typeerror as int is not iterable



# function_clear()
# function_copy()
# function_fromkeys()
# function_get()
# function_items()
# function_keys()
# function_len()
# function_popitem()
# function_setdefault()
# functions_pop()
# function_update()
# function_values()


# The above functions demonstrate various dictinaries operations in Python.
# Each function performs a specific operation and prints the results.
# You can call these functions to see how they work and what outputs they produce.
# Note: Some functions may raise errors because of it the remaining functions will not work properly
# if an error occurred then another line of code will not be executed











