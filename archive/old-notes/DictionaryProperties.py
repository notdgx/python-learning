#MUTABLE
d={"a":23 ,"B":3323 , "c" : 233 ,"d3": 334}
print(d)
d["a"]="YOOOOOOOOO"
print(d)

#MEMBERSHIP checks the key only not the value
print("a" in d)#TRUE
print(233 in d)#FALSE


#ITERATION
for i in d:
    print(i)#prints key

for i in d:
    print(d[i])#print VALUE


#COMPARISON oredr doesn,t count as it isunordered datatype
a={1:"A",2:"B",3:"C"}
b={1:"A",3:"C",2:"B"}
f={"a":23 ,"B":3323 , "c" : 233 ,"d3": 334}
print(a==b)#TRUE
print(a==d)#at first keys doesn't match

#IDENTITY
a={1:"A",2:"B",3:"C"}
b={1:"A",3:"C",2:"B"}
c={1:"A",2:"B",3:"C"}
print(a is b)#FALSE
print(a is c)#FAlse

print(a==b)#true
print(a==c)#true

#ACCESS BY KEYS
a={1:"A",2:"B",3:"C"}
print(a[1])#A
print(a[2])#B

for i,j in a.items():
    print(i,j)#give key value