# MUTABLE values can be changed after initialization

l1=[1,2,34,"a","b","b","2","#@@"]
l2=["2",3,32,"SDSS",434]
print(id(l1))
print(l1)
l1[3]=323232 # changes value at 3rd index to 323232
print(id(l1))# SAME as before
print(l1)

#MEMBERSHIP 
print("b" in l1) # RETURN TRUE AS present at 4th index

#ITERABLE
for i in l1:
    print(i)

#RELATIONAL
print(l1==l2)
print(l1!=l2)

l3=[1,2,3,4]
l4=[1,2,3]
l5=[1,2,3,567]
l6=[1,2,3,"Aadads"]

print(l3>l4)
print(l4<l5)# True
print(l4==l5) # 1=1 2=2 3=3 but len(l4) != len(l5)
print(l5==l6)#Type error as str and int not commparable
print(l3==l5)# 1=1 2=2 3=3 4>0
print(l3>=l4)#true as l3>l4


#CONCATINATE REPLICATE if used l+=[3] or extend append then same id but l=l+[3] it make new SAME WITH +

print(l1)
print(l1*23)# replicate
print(l1+l2+l3+l4)

#IDENTITY

l=[1,2,3,4,5]
m=[1,2,3,4,5]
b=l
print(b==l)#check content False
print(l is b)#check id True 

print(l==m)#check conttent True
print(l is m)#ceck id False

a = [1]
b = a
b.append(2)

print(a)       # [1, 2]
print(b)       # [1, 2]
print(a is b)  # True


#INDEXING
l=[1,2,3,4,5,6,6,6,7,7,89,90]
print(l[4])
print(l[-3])
print(l[6])
#print(l[65])#INdexERROr

#SLICING

print(l[1:])
print(l[1:5])
print(l[2:9:3])
print(l[::-1])#reverse
print(l[-len(l):-4])
