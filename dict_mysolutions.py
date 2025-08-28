#1
def que1():
    return {}
# print(que1())

#2
def que2():
    d={'name':'Alice','age':25,'city':'Boston'}
    return d
# print(que2())

#3
def que3():
    d={'name': 'Bob', 'age': 30}
    return d['name']
# print(que3())

#4
def que4():
    d={'name': 'Carol', 'age': 28}
    d['country']="USA"
    return d
# print(que4())

#5
def que5():
    d={'name': 'David', 'age': 35, 'city': 'NYC'}
    del d['age']
    return d
# print(que5())

#6
def que6():
    d={'a': 1, 'b': 2, 'c': 3}
    return list(d.keys())
# print(que6())

#7
def que7():
    d={'x': 10, 'y': 20, 'z': 30}
    return list(d.values())
# print(que7())

#8
def que8():
    d={'p': 5, 'q': 6}
    return list(d.items())
# print(que8())

#9
def que9():
    d={'name': 'Eve', 'age': 22}
    return 'name' in d
# print(que9())

#10
def que10():
    # get syntax is d.get("key",default_value) no keywork like default=0
    d={'name': 'Frank'}
    return d.get("name",0)
# print(que10())



#11
def que11():
    d={'a': 1, 'b': 2}
    d2={'c': 3, 'd': 4}
    d.update(d2)#it will update d value as per d2 if they have a value of same key then d2 will overwrite that one
    return d
# print(que11())

#12
def que12():
    d={'x': 100, 'y': 200}
    d.clear()
    return d
# print(que12())

#13
def que13():#create a new dict with new id
    d={'name': 'Grace', 'score': 95}
    print(id(d))
    d2=d.copy()
    print(id(d2))
    return d2
# print(que13())

#14
def que14():#pop must take one arg as a KEY otherwise error and it will give the poped value
    d={'name': 'Helen', 'age': 29}
    return d.pop('age')
# print(que14())

#15
def que15():#popitem doesnt require agr it wll pop out the last value ang return last (key:value)
    d={'a': 1, 'b': 2, 'c': 3}
    return d.popitem()
# print(que15())

#16
def que16():
    d={'name': 'Ivan'}# it only takes 1 key and set its default value for further change
    d.setdefault('phone',"n/a")
    return d["phone"]
# print(que16())

#17
def que17():
    keys=['a', 'b', 'c']
    values=[1, 2, 3]
    return dict(zip(keys,values))
# print(que17())

#18
def que18():
    d={'math': 90, 'science': 85, 'english': 88}
    return len(d)
# print(que18())

#19
def que19():
    d={'red': 1, 'blue': 2}
    return "\n".join(tuple((k for k in d)))#to return a valur that has \n to print in new line
# print(que19())



#20
def que20():
    d={'cat': 'meow', 'dog': 'bark'}
    return "\n".join((d[k] for k in d))
# print(que20())

#21
def que21():
    d={'apple': 5, 'banana': 3}
    return tuple(((k,d[k]) for k in d))
# print(que21())

#22
def que22():
    d={'name': 'John'}
    #or
    print(bool(d))#to check whether something is empty or not
    return True if d=={} else False
# print(que22())

#23
def que23():
    d={'x': 1, 'y': 2}
    return list(d.items())
# print(que23())

#24
def que24():
    a=[('a', 1), ('b', 2)]
    return dict(a)
# print(que24())

#25
def que25():
    d=dict()
    return d.fromkeys(['p', 'q', 'r'],0)
# print(que25())

#26
def que26():
    d={'name': 'Kate', 'score': 75}
    d['score']=85
    return d
# print(que26())

#27
def que27():
    d={'a': 50, 'b': 100, 'c': 75}
    #return 100 in d       checks the keys by default
    #or any(val == 100 for val in d.values())
    return 100 in d.values()
# print(que27())

#28
def que28():
    d={'x': 10, 'y': 25, 'z': 15}
    return max(d.values()) if d else "EMPTY"
# print(que28())

#29
def que29():
    d={'p': 8, 'q': 3, 'r': 12}
    return min(d.values()) if d else "EMPTY"
# print(que29())

#30
def que30():
    d={'a': 1, 'b': 2, 'c': 3, 'd': 4}
    return len(d.items())
# print(que30())

#31'
def que31():
    return {1: 'one', 2: 'two', 3: 'three'}

#32
def que32():
    d={'name': 'Leo', 'age': 24, 'city': 'LA'}
    k=['name','city']
    return [d[i] for i in k]
# print(que32())

#33
def que33():
    d={'name': 'Max', 'email': 'max@email.com'}
    return 'phone' not in d
# print(que33())

#34
def que34():
    d={'a': 10, 'b': 20, 'c': 30}
    return sum(d.values())
# print(que34())

#35
def que35():
    return {(1, 2): 'coordinates', (3, 4): 'point'}

#36
def que36():
    d={'name': 'Nina', 'temp': 'delete'}
    del d['temp']
    return d
# print(que36())

#37
def que37():
    a={'a': 1, 'b': 2}
    b={'b': 2, 'a': 1}
    print(a is b)##flase
    return a==b
# print(que37())

#38
def que38():
    a='hello'
    # return dict(enumerate(list(a)[::-1])) it was giving index as a key  
    return {ch: i for i, ch in enumerate(a)}
# print(que38())

#39
def que39():
    d={'name': 'Oscar', 'age': 31}
    return {k.upper(): v for k, v in d.items()}
# print(que39()) 

#40
def que40():
    d={'first': 1, 'second': 2, 'third': 3}
    return list(d.items())[0]
# print(que40())

#41
def que41():
    d={'person': {'name': 'Alice', 'details': {'age': 25, 'city': 'Boston'}}}
    return d

#42
def que42():
    d={'student': {'info': {'name': 'Bob', 'age': 20}}}
    return d['student']['info']['age']
# print(que42())

#43
def que43():
    return {x:x**2 for x in range(1,6)}
# print(que43())

#44
def que44():
    a='hello world'
    return {i:a.count(i) for i in a}
# print(que44())

#45
def que45():
    d={'a': 1, 'b': 2}
    d2={'c': 3, 'd': 4} 
    # d.update(d2)
    return {**d,**d2}#unpacking the dictionanries
  
# print(que45())


#46
def que46():
    a={'b': 2, 'a': 1, 'c': 3}
    return dict(sorted(a.items()))
# print(que46())



#47
def que47():
    a={'alice': 85, 'bob': 90, 'charlie': 75}
    return dict(sorted(a.items(), key=lambda x: x[1]))
# print(que47())

#48
def que48():
    d={'x': 10, 'y': 25, 'z': 15}
    return max(d.items(),key=lambda x: x[1])[0]
# print(que48())

#49
def que49():
    d={'p': 8, 'q': 3, 'r': 12}
    return min(d.items(),key=lambda x: x[1])[0]
# print(que49())

#50
def que50():
    d=['apple', 'banana', 'cherry', 'apricot']
    d2=dict()
    for i in d:
        x=[]
        for j in d:
            if i[0].lower()==j[0].lower():
                x.append(j)
        d2[i[0]]=x
    return d2
# print(que50())

#51
def que51():
    d={'a': 1, 'b': 2, 'c': 3}
    return {j:i for i,j in d.items()}
# print(que51())


#52
def que52():
    d={'a': 10, 'b': 5, 'c': 15, 'd': 8}
    return dict(filter(lambda x: x[1]>7,d.items()))
# print(que52())

#53
def que53():
    d=['cat', 'elephant', 'dog']
    return {x:len(x) for x in d}
# print(que53())

#54
def que54():
    d={'a': [1, 2]}
    d2={'a': [3, 4], 'b': [5]}
    d3=dict()
    # for i in d:
    #     a=[]
    #     for j in d2:
    #         if i== j:
    #             a+=d[i]+d2[j]
    #         elif i!=j and i not in d3:
    #             d3[j]=d2[j]
    #     d3[i]=a
    # return d3
    for k in set(d) | set(d2):  # union of keys
        d3[k] = d.get(k, []) + d2.get(k, [])
    return d3
# print(que54())

#55
def que55():
    a={'outer': {'inner1': 1, 'inner2': 2}}
    l=[]
    for i,j in a.items():
        l.append(i)
        if isinstance(j,dict):
            l.extend(j.keys())

    # #recurrsive version
    # def get_all_keys(d):
    # keys = []
    # for k, v in d.items():
    #     keys.append(k)
    #     if isinstance(v, dict):
    #         keys.extend(get_all_keys(v))
    # return keys
            
    return l
# print(que55())

#56
def que56():
    a='programming'
    v=0
    c=0
    d={}
    for i in a:
        if i in "AEIOaeiou":#or use lower ()
            v+=1
        elif i not in "AEIOUaeiou":
            c+=1
    d["vowel"]=v
    d["consonant"]=c
    return d
# print(que56())

#57
def que57():
    a= {'alice': 85, 'bob': 92, 'charlie': 78}
    return sum(a.values())/len(a)
# print(que57())

#58
def que58():
    a={'a': 1, 'b': None, 'c': 3, 'd': None}
    # for i,j in a.items():         it will give Runtime error so it is advised to make copy 
        # if j==None:
            # del a[i]
    
    for i ,j in list(a.items()):
        if j==None:
            del a[i]
    # return a

    # or 
    a={'a': 1, 'b': None, 'c': 3, 'd': None}
    for i in list(a.keys()):
        if a[i]==None:
            del a[i]
    # return a


    #or create a a new dict 
    a={'a': 1, 'b': None, 'c': 3, 'd': None}
    return {i:j for i, j in a.items( ) if j!=None}


# print(que58())

#59
def que59():
    return {i:"even" for i in range(10) if i%2==0 }
# print(que59())

#60
def que60():
    a={'a': 'hello', 'b': 'world'} 
    return {i:j.upper() for i,j in a.items()}
# print(que60())

#61
def que61():
    a={'a': 1, 'b': 2, 'c': 3} 
    b={'b': 4, 'c': 5, 'd': 6}
    return list(set(a)&set(b))
# print(que61())

#62
def que62():
    a=[1, 2, 2, 3, 3, 3]
    return {i:a.count(i) for i in set (a)}
# print(que62())

#63
def que63():
    a=[{'a': 1}, {'b': 2}, {'c': 3}]
    return {k:n for i in a for k,n in i.items()}
# print(que63())

#64
def que64():
    d={'name': 'John', 'age': 30, 'city': 'NYC'}
    k=['name', 'city',]
    # return {i:d[i] for i in k} #can raise keyerror if nt preent
    return {i:d[i] for i in k if i in d}
# print(que64())

#65
def que65():
    d={'a.b': 1, 'a.c': 2, 'b.d': 3}
    # return {i[0]:{i[-1]:d.get(i)}for i in d if len(i)>=2}       had to split at "."
    # d2={}
    # for i in list(d.keys()):
        
    #     if len(i)>=1:
    #         a=i.split(".")
    #         for j in     
    # return d2

    d = {'a.b': 1, 'a.c': 2, 'b.d': 3}
    out = {}
    for k, v in d.items():
        cur = out
        parts = k.split('.')
        for p in parts[:-1]:
            cur = cur.setdefault(p, {})
        cur[parts[-1]] = v
    return out

# print(que65())

#66
def que66():
    L = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]
    out = {}
    for d in L:
        for k, v in d.items():
            out[k] = out.get(k, 0) + v
    return out

# print(que66())

#67
def que67():
    a={'x': 10, 'y': 30, 'z': 20}
    return dict(list(sorted(a.items(),key=lambda x:x[1] )))
# print(que67())

#68
def que68():
    a=[1, 2, 2, 3]
    b=['a', 'b', 'c', 'd']
    return dict(zip(a,b)) #what it wil do is add 2:b but when it add 2:c it will overwrite first occurace
# print(que68())

#69
def que69():
    d={'a': 10, 'b': 5, 'c': 15}
    return [i for i,j in d.items() if j>7]
# print(que69())

#70
def que70():
    d={'person': {'name': 'Alice', 'age': 25}}
    d['person']['phone']='123-456'
    return d

#71
def que71():
    a='the cat and the dog' 
    b=a.split()
    d={}
    for i in b:
        d[i]=b.count(i)
    return d
# print(que71())

#72
def que72():
    {1: {1: 1, 2: 2, 3: 3}, 2: {1: 2, 2: 4, 3: 6}, 3: {1: 3, 2: 6, 3: 9}}
    a=range(1,4)
    return {i: {j: i*j for j in range(1, 4)}for i in range(1, 4)}
# print(que72())

#73
def que73():
    d={'name': 'John', 'age': '30'}
    return {j:i for i,j in list(d.items())}
# print(que73())

# #74
# def que74():
#     d=[{'name': 'A', 'grade': 'B'}, {'name': 'C', 'grade': 'A'}, {'name': 'D', 'grade': 'B'}]
#     for i in d: