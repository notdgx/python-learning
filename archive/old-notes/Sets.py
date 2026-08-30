def function_len():
    a = {1,2,3,4,5,6,7}# set 
    b = {1,2,3,3,3,4,5,5,5,5,6,6,6,7}

    print(len(a))#7
    print(len(b))# 7 because all elements are uniquee
    print(len(12))# typeerror non iterable

def function_min_max():
    a = {1,2,3,4,5,6,7}# set 
    b = {1,2,3,3,3,4,5,5,5,5,6,6,6,7}
    c={1,2,3,4,"a",(3,4,5)}
    d={"A","a","b","c"}
    e={(1,),(2,),(0,1,)}
    f={"abc","aef","alm"}
    g={(1,2,3),(2,3,4),(1,2,4),(1,1,9)}

    print(type(min(a)))
    print(min(a))#1
    print(min(b))#1
    #print(min(c))#TypeError  as it can only comapare same datatype
    print(min(d))# A as ASCII value is 65 lowest
    print(min(e))# cmmpares lowest len no as lowest length no i 1 only compare 1st value of each and as 0 is smallest
    print(min(f))# as ist letter is same as a then jump to 2nd and b<e<f
    print(min(g))# 1st value is smallest as 1 compare the three with value 1 and then move to second value of three


    print(type(max(a)))
    print(max(a))#7
    print(max(b))#7
    #print(max(c))#TypeError  as it can only comapare same datatype
    print(max(d))# c as ASCII value is 99 largest
    print(max(e))# cmmpares lowest len no as lowest length no i 1 only compare 1st value of each and as 2 is largest
    print(max(f))# as ist letter is same as a then jump to 2nd and b<e<f
    print(max(g))# ist value out of four the maximum is 2

def functions_sorted():
    a = {1,2,3,4,5,6,7}# set 
    b = {1,2,3,3,3,4,5,5,5,5,6,6,6,7}
    c={1,2,3,4,"a",(3,4,5)}
    d={"A","a","b","c"}
    e={(1,),(2,),(0,1,)}
    f={"abc","aef","alm"}
    g={(1,2,3),(2,3,4),(1,2,4),(1,1,9)}

    print(type(sorted(a)))# as set is unoreded datatype sorted () returns a list which is ordered datatype
    print(sorted(a))
    print(sorted(b))
    #print(sorted(c))# Typeerror
    print(sorted(d))# use ascii pattern
    print(sorted(e))# work as min and max function logic
    print(sorted(f))
    print(sorted(g))

def function_sum():
    a={1,2,3,4,5,6}
    b={5,7,9,3,5,6,4,3,4,33,}
    c={1.2222,4.5454,8.9876,34343,45,4}
    d={2,2,32,32,"dfds"}
    print(type(sum(a)))#integer
    print(sum(a))
    print(sum(b))
    print(type(sum(c)))#float
    print(sum(c))
    print(sum(d))#typerror


def function_all_any():
    a={1,2,3,4,5,6,7,7,8}
    b={13.3,6564,445,0, 43,}
    c={"a","b","c","",""}
    d={"",""}
    e={(1,2),(3,34,332),(43,3,3,),(0,)}
    s = {(1, 2), (), (3, 4)}
    f={}

    #0, None, False, '', [], {} → falsy
    #Everything else → truthy
    print(all(a))#True
    print(all(b))#false
    print(all(c))#false
    print(all(d))#false
    print(all(e))#true because alll non empty
    print(all(s))#false
    print(all(f))#all() returns True only if all elements are truthy — and that includes the case where there are no elements at all.

    print("_____")

    print(any(a))#true
    print(any(b))#true
    print(any(c))#true
    print(any(d))#false
    print(any(e))#true
    print(any(s))#true 
    print(any(f))#flase as any (a) where a= {},[],""

def function_add():
    a={1,2,3,4,5,6,7,7,8}
    print(id(a))

    print(a.add("a"))# return none and only able to add only one element 
    print(a,id(a))#id same as previous mutable datatype
    a.add([2,4,5,6])# as list is immutable and unhashablr it give Typeerrr
    a.add(1,2,3)# typer errror as only takes one argunment
    a.add(1).add(8)# None Type error as uncaninable retiurns none

def function_update():
    a={1,2,3,4,5,6,7,7,8}
    print(id(a))

    b=["ds",3,3,434,43]
    c={"ffff":"sdfd",3:55,"ddd":65}# only keys will be added as it is immutable values can be either but sets allows only immutable values
    d=(1,34,("w",2),7)

    #Work like Bulk Union

    print(a.update())#nonetype
    print(a)
    a.update(b)
    print(a)
    a.update(c)
    print(a)
    a.update(d)
    print(a)
    a.update(b,c,d)#will add the elements opny in one go
    print(a)
    a.update(range(78,99))# by range()
    print(a)

def function_removwe():
    a={1,2,3,4,5,6,7,7,8}
    print(id(a))

    #remove a present element from the set Returns none Unchainable
    a.remove(1)#removes 1
    print(a)
    #a.remove(66)#Key error not present
    #a.remove([1,2])# typeerror unhashable
    #a.remove() #TypeError as reqire at least one argunment


    #to safley remove element by remove()
    x=6
    if x in a:
        a.remove(x)
        print(a)


def function_discard():
    a={1,2,3,4,5,6,7,7,8}
    print(id(a))

    #discards a present element if not present didnt give error ,Returns none ,Unchainable
    a.discard(1)#removes 1
    print(a)
    a.discard(66)#Key not present give nom error
    print(a)
    #a.discard([1,2])# typeerror unhashable
    # a.discard() #TypeError as reqire at least one argunmemt in discard

def function_pop():
    a={1,2,3,4,5,6,7,7,8}
    print(id(a))

    # removes any random value no specific pattern #returns the value

    print(a.pop())# Ranodomly removed 1
    print(a.pop(3))# Typerror as it takes no argunment
    print(set().pop())# KeyError as set must not be empty


    #The element removed is not truly random — it’s based on the internal hash table order.
    # In small sets, it might look like the first inserted one goes
    # But don’t rely on order — it’s unpredictable and implementation-dependent

    #forsafley with no key error
    a=set()
    #a.update([1,2,3,4,])
    if a == set():
        print("empty")
    else:
        print(a.pop())

def function_clear():
    a={1,2,3,4,5,6,7,7,8}
    print(id(a))

    # removes alll the elements from the set returns none, Type error when an argunment is passed
    print(a.clear())# None
    print(a)# empty
    a.clear(42)# TypeError

def function_copy():
    a={1,2,3,4,5,6,7,7,8}
    print(id(a))

    # safe copy from one set, have same elements, have diffrent ids, 
    b=a.copy()
    print(b,id(b))
    b.add(0)
    print(b,id(b))

    #TypeError takes no argunment
    c=b.copy(3)

def function_union():
    a={1,2,3,4,5,6,7,7,8}
    b={23,43,54,767,89,67,45,34,34}

    #Union or | Returns a new set, Dont modify the original
    print(a.union(b))
    print(a,b)#Unchanged
    #print(a.union(3))#TypeError as non iterable
    print(a.union(["e","e","y","b"]))# add lists elements to a
    print(a.union(["w","f","n","x"],(99,65,54,33,4),"dfffffgdfghtrthhyjyjasxcvbnmlkui",range(39,69)))# allows multiple iteranles\

def function_intersection():
    a={1,2,3,4,5,6,7,7,8}


    b={23,43,54,767,89,67,45,34,34}

    #Interrsection or & returns a new set , Old unchanged , TypeError if uniterable
    print(a.intersection(b))
    #print(a.intersection(21))# Typeerror
    print(a.intersection([12,3,4,5,"a","j"]))
    print(a.intersection([12,4,5,66,5,3],(0,53,5,7,),range(0,10000),"sdfgfsdfgf"))#multiple itrables

def function_difference():
    a={1,2,3,4,5,6,23,43,54,767,89,67,45,35,34,45,34,34,"1","g",'l',"vc"}
    b={23,43,54,767,89,67,45,34,34}

    #Give the diffrence , return a new set , Give TpeError if uniterable , 
    print(a.difference(b))#returmns diffrence
    #print(a.difference(332))#TypeError non iterable
    print(a.difference([2,"1",45,35]))#iterable
    print(a.difference([1,3,5,6],("1",4,),range(1,66),"vc"))

def function_symmetric_differernce():
    a={1,2,3,4,5,6,23,43,54,767,89,67,45,35,34,45,34,34,"1","g",'l',"vc"}
    b={23,43,54,767,89,67,45,34,34}

    # Tale only one arunment returns a newset, TypeError if un iterable
    print(a.symmetric_difference(b))
    #print(a.symmetric_difference(32))#TypeError unityerable
    print(a.symmetric_difference([1,3,54],("dsd"),"sdsdfs",range(21,54)))# TypeError take sOnly Argunment


def function_intersection_update():
    a={1,2,3,4,5,6,23,43,54,767,89,67,45,35,34,45,34,34,"1","g",'l',"vc"}
    b={23,43,54,767,89,67,45,34,34}

    # Modifies the Original set , Returmns None , Can Take multiple ardunmets only iterable 

    #print(a.intersection_update(b))#none
    print(a)# Updated in the original set
    #print(a.intersection_update(23))#TypeError only takes iterable
    print(a.intersection_update([1,3,4,3,43,54,"1"],("1",),"1"))# can take multiple argunment , gives None as update original
    print(a)

def difference_update():
    a={1,2,3,4,5,6,23,43,54,767,89,67,45,35,34,45,34,34,"1","g",'l',"vc"}
    b={23,43,54,767,89,67,45,34,34}

    # Modifies the Original set , Returmns None , Can Take multiple ardunmets only iterable 

    print(a.difference_update(b))#none
    print(a)# Updated in the original set
    #print(a.difference_update(23))#TypeError only takes iterable
    print(a.difference_update([1,3,4,3,43,54,"1"],("1",),"1"))# can take multiple argunment , gives None as update original
    print(a)


def function_symmetric_diffrence_update():
    a={1,2,3,4,5,6,23,43,54,767,89,67,45,35,34,45,34,34,"1","g",'l',"vc"}
    b={23,43,54,767,89,67,45,34,34}

    # Modifies the Original set , Returmns None , Cannot  Take multiple ardunmets,  

    print(a.symmetric_difference_update(b))#none
    print(a)# Updated in the original set
    #print(a.symmetric_difference_update(23))#TypeError only takes iterable
    print(a.symmetric_difference_update([1,3,4,3,43,54,"1"],("1",),"1"))# cannot take multiple argunment , gives TypeError
    print(a)

def function_isdisjoint():
    a={1,2,3,4,5,6,23,43,54,767,89,67,45,35,34,45,34,34,"1","g",'l',"vc"}
    b={23,43,54,767,89,67,45,34,34}

    # Deosnt Modifies the Original set , Returmns True /False , Cannot  Take multiple argunmets,  

    print(a.isdisjoint(b))#False ass some elements are common
    # print(a.isdisjoint(23))#TypeError only takes iterable
    # print(a.isdisjoint([1,3,4,3,43,54,"1"],("1",),"1"))# cannot take multiple argunment , gives TypeError
    print(a.isdisjoint(["assasa"]))#True

def function_issubset():
    a={1,2,3,4,5,6,23,43,54,767,89,67,45,35,34,45,34,34,"1","g",'l',"vc"}
    b={23,43,54,767,89,67,45,34,34}

    # Deosnt Modifies the Original set , Returmns True /False , Cannot  Take multiple argunmets,  Check whethe a is subset of b

    print(a.issubset(b))#False 
    # print(a.issubset(23))#TypeError only takes iterable
    # print(a.issubset([1,3,4,3,43,54,"1"],("1",),"1"))# cannot take multiple argunment , gives TypeError
    print(a.issubset({1,2,3,4,5,6,23,43,54,767,89,67,45,35,34,45,34,34,"1","g",'l',"vc","dcd","bbb"}))#True

def function_issuperset():
    a={1,2,3,4,5,6,23,43,54,767,89,67,45,35,34,45,34,34,"1","g",'l',"vc"}
    b={23,43,54,767,89,67,45,34,34}

    # Deosnt Modifies the Original set , Returmns True /False , Cannot  Take multiple argunmets,  Check whethe a is superset 

    print(a.issuperset(b))#True
    # print(a.issuperset(23))#TypeError only takes iterable
    # print(a.issuperset([1,3,4,3,43,54,"1"],("1",),"1"))# cannot take multiple argunment , gives TypeError
    print(a.issuperset({1,2,3,4,5,6,23,43,54,767,}))#True

