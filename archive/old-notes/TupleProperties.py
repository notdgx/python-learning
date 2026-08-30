# IMMUTABLE values can't be changed after initialization 


t1=(1,2,3,4,5,6,6,8,9)
t2=1,2,3,4,5,6,7,8
print(id(t1))# id of t1
print(t1)# prints t1
#t1[3]="23"#ERROOR Immutable


#MEMBERSHIP 
print(5 in t1) # RETURN TRUE AS present at 4th index

#ITERABLE
for i in t1:
    print(i)

#RELATIONAL
print(t1==t2)
print(t1!=t2)

t3=(1,2,3,4)
t4=(1,2,3)
t5=(1,2,3,567)
t6=(1,2,3,"Aadads")

print(t3>t4)
print(t4<t5)# True
print(t4==t5) # 1=1 2=2 3=3 but len(l4) != len(l5)
print(t5==t6)#Type error as str and int not commparable
print(t3==t5)# 1=1 2=2 3=3 4>0
print(t3>=t4)#true as l3>l4


#CONCATINATE REPLICATE  - IMMUTABLE CHANGES ID AFTER +,* creates new oject delete previous

print(t1)
print(t1*23)# replicate
print(t1+t2+t3+t4)

#IDENTITY

l=(1,2,3,4,5)
m=(1,2,3,4,5)
b=l
print(id(l),id(m))
print(b==l)#check content False
print(l is b)#check id True 

print(l==m)#check conttent True
print(l is m)#ceck id False ####may vary due to caching

a =(1,)
b = a
b=b+(2,)

print(a)       # (1,)
print(b)       # (1, 2)
print(a is b)  # False


#INDEXING
l=(1,2,3,4,5,6,6,6,7,7,89,90)
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
