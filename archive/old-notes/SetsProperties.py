#PROPERTIES 
 
s1={1,2,3,45,5}# a set is unordered,unique, mutable , non duplicate values(ignore if any), contains immutable values only(hashable)
print(type(s1))#<class 'set'>
print(s1)# prints values oof set but no specific order

s2={1,2,3,4,4,4,4,4,5,5,5,5}#no duplicate allowed here  actually only unique values are stored in id
print(s2)

#NO ORDER 
s1={1,2,3,4,5,5,65,6,5,}
#print(s1[3])#typeerror as no indexing unorderd 

#iterable
s={1,3,2,4,5,6,6,6,6,"j","o","n",'h'}
for i in s:
    print(i,end=" ")#may change the order 
    

#Only Immutable (hashable) data allowed
#a={1,2,3,(1,2),"a",[1,2,3]}# Type Error as list is mutable datattype

#Initilazing empty set
a={}
print(type(a))# <classs 'dict'>

# to initilaze a empty set
a=set()
print(a,type(a)) 

#Set operations union , intersection , diffrence , symmetric diffrence

a={1,2,3,4,5}
b={1,2,3,7,8,9}
print(id(a),id(b))
#union
print(id(a|b),a|b)#union
#intersection
print(id(a&b),a&b)#intersection
#diffrence
print(id(a-b),a-b)
print(id(b-a),b-a)
#symmetric diffrence
print(a^b)
print(b^a)
print(id(a^b))
