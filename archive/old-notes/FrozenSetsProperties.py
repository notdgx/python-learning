## INITILAZING
a=frozenset([1,2,3,45,55,56,])
print(a)
print(type(a))
b=frozenset({1,2,4,5,6})
print(b,type(b))
print(frozenset((2,324.45,767775)))
print(frozenset("HELLOOOOOOOO"))
print(frozenset(range(1,9)))
#print(frozenset(1221))#TypeError as int is not a itrable


# MEMBERSHIP TEST
a=frozenset([1,2,3,45,55,56,])
print(1 in a )#TRUE
print("A" not in a)#TRUE
print("a" in a)#FALSE


# SET ARTHIMETIC
a=frozenset([1,2,3,45,55,56,])
b=frozenset([1,2,3])
print(id(a),id(b))
print(a|b,type(a|b),id(a|b)) # creates a new frozenset as for union 

print(id(a),id(b))
print(a&b,type(a&b),id(a&b)) # creates a new frozenset as fro intersection

print(id(a),id(b))
print(a^b,type(a^b),id(a^b)) # creates a new frozenset as for symmetricdifference

print(id(a),id(b))
print(a-b,type(a-b),id(a-b)) # creates a new frozenset as for difference

# COMPAERISON

a=frozenset((1,2,3,4))
b=frozenset((1,2,3,4,))
c=frozenset((2,3,5,6,7))
d=frozenset((1,2,3))

print(a==b)#FALSE
print(a==c)#TRUE
print(a is c)#FALSE


#CAN BE USED AS A PAIR OF KEYS FOR DICTIONARIES
d = {frozenset([1, 2]): "value"}
print(d[frozenset([2, 1])])  # "value"

#Operation	Error Type	Reason
# .add()	AttributeError	Immutable
# .remove()	AttributeError	Immutable
# .update()	AttributeError	Immutable
# .pop()	AttributeError	Immutable
# .clear()	AttributeError	Immutable
# .intersection_update()	AttributeError	Immutable


