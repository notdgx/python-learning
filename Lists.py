def function_len():
    t=(2,3,44,6,5,6,7,8,9,10)
    a="listconversion"
    print(list(t))# This will convert tuple to list
    print(list(a))# This will convert string to list of characters
    print(list(range(5)))  # This will convert range to list [0,1,2,3,4]
    print(list(2323))  # This will raise an error since int cannot be converted to list


def function_list():
    t=(2,3,44,6,5,6,7,8,9,10)
    a="listconversion"
    print(list(t))# This will convert tuple to list
    print(list(a))# This will convert string to list of characters
    print(list(range(5)))  # This will convert range to list [0,1,2,3,4]
    print(list(2323))  # This will raise an error since int cannot be converted to list

def function_sorted():
    l1=[32,55,4,4,554,5,45,45,4,5,45,5,55,4,52,8,8,78,32,12,2,5,4,2,4,5,5,4,84,4,4.22]
    print(id(l1))
    a=sorted(l1)
    print(id(a))

def function_sum(): 
    l1=[32,55,4,4,554,5,45,45,4,5,45,5,55,4,52,8,8,78,32,12,2,5,4,2,4,5,5,4,84,4,4.92]
    a=sum(l1) #1175.92
    print(a) #1175 explicit type conversion
    print(int(a))

def function_minmax():
    l1=[32,55,4,4,554,5,45,45,4,5,45,5,55,4,52,8,8,78,32,12,2,5,4,1.999999,4,5,5,4,84,4,4.92]
    a=min(l1)
    b=max(l1)
    print(a)
    print(b)  

def function_reversed():
    l1=[32,55,4,4,554,5,45,45,4,5,45,5,55,4,52,8,8,78,32,12,2,5,4,1.999999,4,5,5,4,84,4,4.92]
    a=reversed(l1)  
    print(a) #<list_reverseiterator object at 0x00000124A941BFA0>
    print(list(a))  #[4.92, 84, 4, 5, 5, 4, 1.999999, 4, 5, 4, 2, 5, 12, 32, 78, 8, 8, 52, 4, 55, 5, 45, 4, 5, 45, 5, 55, 4, 554, 4, 4, 55, 32]
    print(id(l1))  # Prints the id of the original list
    print(id(a))   # Prints the id of the reversed iterator
    print(list(a)) 

def function_append():
    l1=[32,55,4,4,554,6,7,8,9]
    print(id(l1)) #print the id of the list l1
    a=223
    b=[2,4,5,6,7,8,9]
    print(id(l1.append(a))) #print the id of the list l1 after appending a as the output is none it will give the id of none object
    print(id(l1.append(b))) #print the id of the list l1 after appending b as the output is none it will give the id of none object
    # it does not modify the id

def function_extend():
    l1=[32,55,4,4,554,6,7,8,9]
    l2=[2,45,67,64,34,2,32,23,323,23,23,2,3,2,3,2,3,2,3,2,3]
    print(id(l1)) #print the id of the list l1
    print(id(l2)) #print the id of the list l2
    print(l1.extend(l2))# extend l1 with l2
    # The extend method modifies l1 in place and returns None
    print(l1) 
    print(id(l1))#same id as before extending 
    print(id(l2))#same id as before extending

def function_insert():
    l1=[1,2,3,4,5,6,7,8,9]
    a=2
    print(id(l1))#original id of l1
    print(l1.insert(2, a))#None  ALWAYS NEED TWO ARGUMENTS: index and value to insert
    # Inserting 'a' at index 2 in l1
    print(l1)#[1, 2, 2, 3, 4, 5, 6, 7, 8, 9]
    print(id(l1))#id of l1 after insertion SAME

def function_pop():
    l1=[1,2,3,4,5,6,7,8,9]
    print(id(l1))#gives the id of the list l1
    print(l1.pop())#removes the last element of the list l1 and returns it
    print(id(l1))#gives the id of the list l1 after the pop operation SAME
    print(l1.pop(3))#removes the 4th element of the list l1 and returns it
    print(l1)
    print(id(l1))#gives the id of the list l1 after the pop operation SAME
    print(l1.pop(23))# This will raise an IndexError because the index is out of range
    print([].pop())# This will raise an IndexError because the list is empty

def function_remove():
    l1=[1,2,3,4,5,6,7,8,9]
    a=2
    print(id(l1))#gives the id of the list l1
    print(l1.remove(a))# This will remove the first occurrence of 'a' from the list l1 also give NONE
    print(l1) # This will print the modified list after removing 'a'
    print(id(l1))# This will print the id of the list l1 after removing 'a' SAME

def function_clear():
    l1=[1,2,3,4,5,6,7,8,9]
    print(id(l1))#gives the id of the list l1
    print(l1.clear())#clears the list l1 RETURNS NONE
    print(l1)#prints the empty list after clearing
    print(id(l1))#gives the id of the list l1 after clearing SAME
    print([].clear())#clears the empty list RETURNS NONE no erroe

def function_count():
    l1=[1,2,3,2,2,2,2,2,4,5,6,7,8,9,"a","a","A","A","b","c","d","e","f","g","h","i","j"]
    print(id(l1))#gives the id of the list l1
    print(l1.count(2))#counts the number of occurrences of 2 in the list l1
    print(l1.count("a"))#counts the number of occurrences of "a" in the list l1
    print(l1.count())#type error, count() requires ONE  argument

def function_index():
    l1=[1,2,3,4,5,6,7,8,9]
    a=2
    print(id(l1))#gives the id of the list l1
    print(l1.index(a))#gives the index of the element a in the list l1 searches all list elements
    print(id(l1.index(a)))#gives the id of the index of the element a in the list l1 searches all list elements if it find the value it give its default id
    print(l1.index(a, 0, 5))#gives the index of the element a in the list l1 searches from index 0 to index 5 
    print(l1.index(a, 5))#gives the index of the element a in the list l1 searches from index 5 to the end of the list VALUEERROR

def function_reverse():
    l1=[1,2,3,2,2,2,2,2,4,5,6,7,8,9,"a","a","A","A","b","c","d","e","f","g","h","i","j"]
    print(id(l1))#gives the id of the list l1
    print(l1.reverse())#reverses the list l1
    print(l1)#prints the reversed list
    print(id(l1))#gives the id of the list l1 after reversing SAME

def function_sort():
    l1=[32,55,4,4,554,5,45,45,4,5,45,5,55,4,52,8,8,78,2.22,32,12,2,5,4,2,4,5,5,4,84,4,"ds"]
    a=l1.sort(reverse=True)
    #
    l1=[32,55,4,4,554,5,45,45,4,5,45,5,55,4,52,8,8,78,32,12,2,5,4,1.999999,4,5,5,4,84,4,4.92]
    a=l1.sort()
    print(a)

def function_copy():
    l1=[1,2,3,2,2,2,2,2,4,5,6,7,8,9,"a","a","A","A","b","c","d","e","f","g","h","i","j"]
    print(id(l1))#gives the id of the list l1
    a=l1.copy()#copying the list l1 to a
    print(id(a))#gives the id of the list a
    print(a is l1)#checks if a and l1 are the same object, returns False it checks the identity, not the content
    print(a==l1)#checks if a and l1 have the same content, returns True it checks the equality of the content, not the identity

    a.append(2)#appending 2 to the list a
    print(a==l1)#checks if a and l1 have the same content, returns True it checks the equality of the content, not the identity FALSE because a has been modified

def function_enumerate():
    l1=[1,2,3,2,2,2,2,2,4,5,6,7,8,9,"a","a","A","A","b","c","d","e","f","g","h","i","j"]
    a=enumerate(l1)
    print(a)#gives the enumerate object
    print(list(a))#converts the enumerate object to a list of tuples

    for i,j in enumerate(l1):
        print(i,j)#prints the index and value of each element in the list l1
    print("LENGTH IS",len(l1))#prints the length of the list l1

def function_zip():
    l1=["a","b","c","d","e","f"]
    l2=[1,2,3,4,5]
    l3=["A","B","C","D","E","F"]
    a=zip(l1,l2,l3,range(4))#it will zip the elements of l1 and l2 together
    #and if length of l1 and l2 is not same it will zip till the shortest length it makes zip object
    print(a)
    print(id(a))#gives the id of the zip object a
    print(list(a))

def function_map():
    l1=[1,2,3,4,5,6,]# input list
    def cuber(x):# function to cube the elements it can be lambda function also
        return x**3 #returning cube of x
    # using map function to apply cuber function to each element of l1
    print(map(cuber,l1)) # this will return a map object
    l2=list(map(cuber,l1))#this will convert the map object to a list
    print(l2)

def function_filter():
    l1=[1,2,3,4,5,6]# input list
    def filter_even_numbers(x):#condition to filter even numbers
        if x % 2 == 0:
            return True

    a=print(filter(filter_even_numbers, l1))  # this will return a filter object
    b=list(filter(filter_even_numbers, l1))  # this will convert the filter object to a list
    print(b)  # prints the list of even numbers

def funxtion_all():
    l1=[0,1,0,11,11,1,1,1,1,1]
    l2=[0,0,0,0,0,0,0,0,0,0]
    l3=[1,2,3,4,5,6,7,8,9,10]
    l4=["aaa","bbb","ccc","ddd","eee","fff","ggg","hhh","iii","jjj","","",""]
    l5=[True,False]
    l6=[True,True,True,True,True,True,True,True,True,False]
    l7=[False,False,False,False,False,False,False,False,False,False]
    print(all(l1))  # False, because of the zeros
    print(all(l2))  # False, all elements are zero
    print(all(l3))  # True, all elements are non-zero
    print(all(l4))  # False, because of the empty strings
    print(all(l5))  # False, because of the False
    print(all(l6))  # False, because of the False
    print(all(l7))  # False, all elements are False
    print(all([]))  # True, because the list is empty


def function_any():
    l1=[0,1,0,11,11,1,1,1,1,1]
    l2=[0,0,0,0,0,0,0,0,0,0]
    l3=[1,2,3,4,5,6,7,8,9,10,"A"]
    l4=["aaa","bbb","ccc","ddd","eee","fff","ggg","hhh","iii","jjj","","",""]
    l5=[True,False]
    l6=[True,True,True,True,True,True,True,True,True,False]
    l7=[False,False,False,False,False,False,False,False,False,False]
    print(any(l1))  # True, because of the 1s
    print(any(l2))  # False, all elements are zero
    print(any(l3))  # True, all elements are non-zero
    print(any(l4))  # True, because of the non-empty strings
    print(any(l5))  # True, because of the True
    print(any(l6))  # True, because of the True
    print(any(l7))  # False, all elements are False
    print(any([]))  # False, because the list is empty



def function_type():
    l1=[11,12,13,14,15,16,17,18,19,20]
    l2=[0,0,0,0,0,0,0,0,0,0]
    l3=[1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0]
    l4=["aaa","bbb","ccc","ddd","eee","fff","ggg","hhh","iii","jjj","","",""]
    l5=[True,False]

    print(type(l1))
    print(type(l2))
    print(type(l3))
    print(type(l4))
    print(type(l5))
    #this will print the type of each list which is <class 'list'> for all of them


def function_eval():
    l1="[11,12,13,14,15,16,17,18,19,20]"
    l2="[0,0,0,0,0,0,0,0,0,0]"
    l3="[1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0]"
    l4='["aaa","bbb","ccc","ddd","eee","fff","ggg","hhh","iii","jjj","","",""]'
    l5="[True,False]"
    l6=[1,2,3,4,5,6,7,8,9,10]

    print(eval(l1))# This will convert the string representation of the list into an actual list
    print(eval(l2))# This will convert the string representation of the list into an actual list
    print(eval(l3))# This will convert the string representation of the list into an actual list
    print(eval(l4))# This will convert the string representation of the list into an actual list
    print(eval(l5))# This will convert the string representation of the list into an actual list
    print(eval(l6))# this will give an error because l6 is already a list, not a string representation

# function_len()
# function_list()
# function_sorted()
# function_sum()
# function_minmax()
# function_reversed()
# function_append()
# function_extend()
# function_insert()
# function_pop()
# function_remove()
# function_clear()
# function_count()
# function_index()
# function_reverse()
# function_sort()
# function_copy()
# function_enumerate()
# function_zip()
# function_map()
# function_filter()
# funxtion_all()
# function_any()
# function_type()
# function_eval()

# The above functions demonstrate various list operations in Python.
# Each function performs a specific operation and prints the results.
# You can call these functions to see how they work and what outputs they produce.
# Note: Some functions may raise errors because of it the remaining functions will not work properly
# if an error occurred then another line of code will not be executed
















