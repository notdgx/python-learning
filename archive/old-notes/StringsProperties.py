# IMMUTABLE
a="Hello Buddy get a job"
print(id(a))
#a[5]="e"#ERROR TYPE ERROR

#MEMBERSHIP

print("e" in a)
print("H" not in a)

#ITERATION

for i in a:
    print(i,end="")
for i in range(len(a)):
    print(a[i],end="")

#RELATIONAL


a="HELLO"
b="HELLO"
c="Hello"
print(id(a),id(b),id(c))# for small str a,b has same id 
print(a==b)#true
print(a!=b)#false
print(a>=c)#False based on ASCII values
print(a<=b)#True

#CONCATINATE AND REPLICATE

a="HELLO"
b="Hello"
print(id(a),id(b))

print(id(a+b))
print(id(a*5))

#IDENTITY
a="HELLO"
b=a
print(b is a)#TRUE
b+="a"
print(b)
print(b is a)#false

#INDEXING
a="HELLO BUDDY YOU UNEMPLOYED"
print(a[3])#L
print(a[-4])#O
print(a[1:6])#ELLO 
print(a[:8:2])#HLOB
print(a[-4:-len(a):-2])

