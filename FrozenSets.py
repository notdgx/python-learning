def function_len():
    a = frozenset({1,2,3,4,5,6,7})# frozenset 
    b = frozenset({1,2,3,3,3,4,5,5,5,5,6,6,6,7})
    # LENGTH CANT BE CHANGED IMMUTABLE
    print(len(a))#7
    print(len(b))# 7 because all elements are uniquee
    print(len(12))# typeerror non iterable

def function_sorted():
    a = frozenset({1,2,3,4,5,6,7})
    b = frozenset({1,2,3,3,3,4,5,5,5,5,6,6,6,7,"a"})

    print(id(a),id(b))
    print(id(sorted(a)),sorted(a))# by default creayte a list in new Ascending


    #print(sorted(b))#Typeerror cant compat mixed dstatypes
    print(sorted(a,reverse=True))#to get in descending
    print(sorted(3))#TypeError


def function_copy():
    a = frozenset({1,2,3,4,5,6,7})

    b=a.copy()
    print(b)
    print(id(a),id(b))#refers to same id as it is immutable and hashable
    print(a is b)#True

def function_union():
    a = frozenset({1,2,3,4,5,6,7})
    b=frozenset({1,4,6,7,98,9})


    print(id(a),id(b))
    print(a.union(b),a|b,id(a.union(b)),id(a|b))#unoin can be done by fun ction or|
    print(a.union(b,[1,5,68,6,7876,788990,"sda","ddds"],("dsjs"),"asdfghjkl",range(99,999)))#can support multiple iterators
    #print(a.union(232))#uniterable

def function_intersection():
    a=frozenset({1,2,3,4,5,6,7,7,8})


    b=frozenset({23,43,54,767,89,67,45,34,34}) # Interrsection or & ,returns a new frozenfrozensetset , Old unchanged , TypeError if uniterable
    print(a.intersection(b))
    #print(a.intersection(21))# Typeerror
    print(a.intersection([12,3,4,5,"a","j"]))
    print(a.intersection([12,4,5,66,5,3],(0,53,5,7,),range(0,10000),"sdfgfsdfgf"))#multiple itrables
    print(type(a.intersection([12,4,5,66,5,3],(0,53,5,7,),range(0,10000),"sdfgfsdfgf")))#type is frozenset

def function_difference():
    a=frozenset({1,2,3,4,5,6,23,43,54,767,89,67,45,35,34,45,34,34,"1","g",'l',"vc"})
    b=frozenset({23,43,54,767,89,67,45,34,34})

    #Give the diffrence , return a new frozenset , Give TpeError if uniterable , 
    print(a.difference(b))#returns diffrence
    #print(a.difference(332))#TypeError non iterable
    print(a.difference([2,"1",45,35]))#iterable
    print(a.difference([1,3,5,6],("1",4,),range(1,66),"vc"))

def function_symmetric_difference():
    a=frozenset({1,2,3,4,5,6,23,43,54,767,89,67,45,35,34,45,34,34,"1","g",'l',"vc"})
    b=frozenset({23,43,54,767,89,67,45,34,34})

    # Tale only one arunment returns a newset, TypeError if un iterable
    print(a.symmetric_difference(b))
    #print(a.symmetric_difference(32))#TypeError uniterable
    print(a.symmetric_difference([1,3,54],("dsd"),"sdsdfs",range(21,54)))# TypeError take sOnly Argunment


def function_isdisjoint():
    a=frozenset({1,2,3,4,5,6,23,43,54,767,89,67,45,35,34,45,34,34,"1","g",'l',"vc"})
    b=frozenset({23,43,54,767,89,67,45,34,34})

    # Deosnt Modifies the Original frozenset , Returmns True /False , Cannot  Take multiple argunmets,  

    print(a.isdisjoint(b))#False ass some elements are common
    # print(a.isdisjoint(23))#TypeError only takes iterable
    # print(a.isdisjoint([1,3,4,3,43,54,"1"],("1",),"1"))# cannot take multiple argunment , gives TypeError
    print(a.isdisjoint(["assasa"]))#True

def function_issubset():
    a=frozenset({1,2,3,4,5,6,23,43,54,767,89,67,45,35,34,45,34,34,"1","g",'l',"vc"})
    b=frozenset({23,43,54,767,89,67,45,34,34})

    # Deosnt Modifies the Original frozenset , Returmns True /False , Cannot  Take multiple argunmets,  Check whethe a is subset of b

    print(a.issubset(b))#False 
    # print(a.issubset(23))#TypeError only takes iterable
    # print(a.issubset([1,3,4,3,43,54,"1"],("1",),"1"))# cannot take multiple argunment , gives TypeError
    print(a.issubset({1,2,3,4,5,6,23,43,54,767,89,67,45,35,34,45,34,34,"1","g",'l',"vc","dcd","bbb"}))#True

def function_issuperset():
    a=frozenset({1,2,3,4,5,6,23,43,54,767,89,67,45,35,34,45,34,34,"1","g",'l',"vc"})
    b=frozenset({23,43,54,767,89,67,45,34,34})

    # Deosnt Modifies the Original frozesnet , Returmns True /False , Cannot  Take multiple argunmets,  Check whethe a is superset 

    print(a.issuperset(b))#True
    # print(a.issuperset(23))#TypeError only takes iterable
    # print(a.issuperset([1,3,4,3,43,54,"1"],("1",),"1"))# cannot take multiple argunment , gives TypeError
    print(a.issuperset({1,2,3,4,5,6,23,43,54,767,}))#True