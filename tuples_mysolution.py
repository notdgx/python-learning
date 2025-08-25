#1
def que1():
    t=1,2,3,4,5
    return len(t)
#print(que1())

#2
def que2():
    tuple = (10, 20, 30, 40, 50)
    return tuple[2]

#print(que2())

#3 
def que3():
    element=42,
    return type(element)

#print(que3())

#4 
def que4():
    tuple = (15, 25, 35, 45)
    element = 25
    return element in tuple

# print(que4())

#5
def que5():
    t1=(1,2)
    t2=(3,4)
    return t1+t2

#6
def que6():
    t=("a","b")
    times=3
    return t*3

#7 
def que7():
    t=(1,2,3,4,5,6)
    return t[2:5]
# print(que7())

#8
def que8():
    tuple = ('apple', 'banana', 'cherry')
    return tuple[-1]
# print(que8())

#9
def que9():
    list = [1, 2, 3]
    return tuple(list)

#10 
def que10():
    tuple = (100, 200, 300)
    a,b,c=tuple
    return a,b,c
# print(que10())

#11
def que11():
    t=tuple()
    return type(t)
# print(que11())

#12
def que12():
    tuple = (45, 12, 78, 23, 56)
    return max(tuple) if tuple else None
# print(que12())

#13
def que13():
    tuple = (45, 12, 78, 23, 56)
    return min(tuple) if tuple else None

#14
def que14():
    tuple = (1, 2, 3, 4, 5)
    return sum(tuple)

#15
def que15():
    tuple = (1, 2, 3)
    return list(tuple)

#16
def que16():
    tuple = (10, 20, 30, 40)
    return tuple[:2]

#17
def que17():
    tuple = (1, 2, 3, 4, 5, 6)
    return tuple[0:len(tuple):2]

#18
def que18():
    tuple = (1, 2, 3, 4, 5)
    return tuple[::-1]

#19
def que19():
    tuple1 = (1, 2, 3)
    tuple2 = (1, 2, 3)
    return tuple1==tuple2

#20
def que20():
    int1=10
    string1='hello'
    float1=3.14
    return tuple([int1, string1 ,float1])

#21
def que21():
    tuple = (10, 20, 30, 40, 50)
    return tuple[-2]

#22
def que22():
    string = 'python'
    return tuple(string)

#23
def que23():
    tuple = ()
    return tuple==()

#24()
def que24():
    tuple1 = (1, 2)
    tuple2 = (1, 3)
    return tuple1<tuple2

#25
def que25():
    t=(1, 2, 2, 3, 3, 3)
    t1=t
    return t1



#26
def que26():
    tuple1 = (1, 2, 3, 4, 5)
    return  tuple1[(len(tuple1)//2)] if tuple1 else None
# print(que26())

#27
def que27():
    tuple1 = ((1, 2), (3, 4))
    return len(tuple1)

#28
def que28():
    a=range(1,6)
    return tuple(a)

#29
def que29():
    tuple1 = (10, 20, 30, 40, 50)
    return tuple1[1:]
# print(que29())

#30
def que30():
    tuple1 = (10, 20, 30, 40, 50)
    return tuple1[:len(tuple1)-1] #or tuple1[:-1]
# print(que30())

#31
def que31():
    tuple1 = (2, 3, 4)
    x=1
    for i in tuple1:
        x=x*i
    return x

# print(que31())

#32
def que32():
    t=(1,2,3)
    return all(isinstance(i, int) for i in t)
# print(que32())

#33
def que33():
    n = [1, 2, 3, 4]
    return tuple((i**2 for i in n))
# print(que33())

#34
def que34():
    t = (10, 20, 30, 40, 50)
    return tuple((t[i] for i in range(len(t)) if i%2==0))
# print(que34())

#35
def que35():
    t= ('a', 'b', 'c')
    return "".join(t)
# print(que35())

#36
def que36():
    t = (1, None, 3)
    return True if None in t else "not present"
# print(que36)

#37
def que37():
    s = [True, False, True]
    return tuple(s)
# print(que37()

#38
def que38():
    t = (1, 'hello', 3.14)
    return type(t[0])
# print(que38())

#39'
def que39():
    st= 'ABC'
    return tuple(st)

#40
def que40():
    t = (1, 2, 3, 4, 5)
    #the leading + after t[-1], is actually applying unary plus to a tuple, which is not valid.
    #    t2=t[-1], + t[1:len(t)-1] + t[0],
    return (t[-1],) + t[1:len(t)-1] + (t[0],)
# print(que40())

#41
def que41():
    t = (1, 2, 3, 3, 3, 4)
    e=3
    return t.count(e)
# print(que41())

#42
def que42():
    t= ('banana', 'apple', 'cherry', 'apple')
    a='apple'
    try:
        return t.index(a)  # returns the first occurrence index
    except ValueError:
        return None  # if not found
# print(que42())

#43
def que43():
    tuple1 = (1, 2, 3)
    tuple2 = ('a', 'b', 'c')
    return list(zip(tuple1,tuple2))
# print(que43())

#44
def que44():
    t = ('x', 'y', 'z')
    return list(enumerate(t))
# print(que44())

#45
def que45():
    t = (5, 2, 8, 1, 9)
    return sorted(t)
#sort syntax for list a.sort() 
#for sorted sorted(t)
# print(que45())

#46
def que46():
    t = ('banana', 'apple', 'cherry')
    #sorted can do the work even with str
    return sorted(t)
# print(que46())

#47
def que47():
    t= (1, 2, 3, 2, 4, 2)
    return tuple((i for  i in range(len(t)) if t[i]==2))
# print(que47())


#48
def que48():
    t = (1, 2, 2, 3, 3, 3, 4)
    seen=set()
    t2=tuple()
    for i in t:
        if i not in seen :
            t2=t2+(i,)
            seen.add(i)

    return t2

    #or the fastest with dict
    #return tuple(dict.fromkeys(t))

#49
def que49():
    t = (1, 2, 3, 4, 5, 6, 7, 8)
    return tuple((filter(lambda x:x%2==0, t)))

#or without filr=ter fastest
#return tuple(x for x in t if x % 2 == 0)
# print(que49())

#50
def que50():
    coordinates = [(0, 0), (1, 1), (2, 2)]
    #dictionary comprehension
    return {coord: f'point{i}' if i else 'origin' for i, coord in enumerate(coordinates)}

#51
def que51():
    t = ('a', 'b', 'c')
    for i in t:
        print(i)

#52
def que52():
    t= (1, 2, 3, 4, 5)
    first , *rest =t
    return f"first = {first}, rest = {rest}"
# print(que52())

#53
def que53():
    t= (1, 2, 3, 2, 2, 4, 5)
    maxcount=0
    element=None
    for i in t:
        c=t.count(i)
        if c>maxcount:
            maxcount=c
            element=i
    return element
# print(que53())

#54
def que54():
    names = ['Alice', 'Bob']
    ages = [25, 30]
    return list (zip(names,ages))
# print(que54())

#55
def que55(t=((1, 2), (3, 4), (5, 6))):
    t2=tuple()
    for i in t:
        if isinstance(i,tuple):
            t2=t2+que55(i)
        else:
            t2=t2+(i,)
    return t2
# print(que55())

#56
def que56():
    t = (1, 2, 3, 2, 4, 3, 5)
    seen=set()
    t2=list()#for best efficiency as tuple will be created and deleted every time
    for i in t:
        if i not in seen:
            seen.add(i)
        else:
            t2+=(i,)
    return tuple(t2)
# print(que56())

#57
def que57():
    n = [1, 2, 3, 4]
    return tuple((i**2 for i in n))
# print(que57())

#58
def que58():
    t = (1, 2, 3, 4, 5, 6)
    pairs = list(zip(t[::2], t[1::2]))
    return pairs
# print(que58())

#59
def que59():
    tuple1 = (1, 2, 3, 4)
    tuple2 = (3, 4, 5, 6)
    return tuple(set(tuple1)&set(tuple2))
# print(que59())

#60
def que60():
    d = {'a': 1, 'b': 2, 'c': 3}
    return tuple(d.keys())
# print(que60())

#61
def que61():
    d = {'a': 1, 'b': 2, 'c': 3}
    return tuple(d.values())
# print(que61())

#62
def que62():
    keys = ('name', 'age')
    values = ('John', 25)
    return dict(zip(keys, values))
# print(que62())


#63
def que63():
    t = (10, 20, 30, 40, 50)
    return sum(t)/len(t)
# print(que63())

#64
def que64():
    t= (5, 2, 8, 1, 9, 3)
    return sorted(set(t))[-2]
# print(que64())

#65
def que65():
    t = (1, 2, 3, 2, 4)
    old=2
    new=9
    return tuple(new if x == old else x for x in t)
# print(que65())

#66
def que66():
    t=(1, 3, 6, 10, 15)
    sumn=0
    t2=list()
    for i in t:
        sumn+=i
        t2.append(i)
    return tuple(t2)
# print(que66())

#67
def que67():
    t = (1, 2, 3, 4, 5)
    return t==tuple(sorted(t))
# print(que67())

#68
def que68():
    t = (1, 2, 3, 4, 5)
    n = 2
    return t[n:]+t[:n]
# print(que68())

#69
def que69():
    t = (1, 2, 3, 4, 5, 6)
    return tuple((filter((lambda x: x>3),t)))
# print(que69())

#70
def que70():
    t= ('1', '2', '3', '4')
    return tuple((int(i) for i in t))
# print(que70())

#71
def  que71():
    t= ('a', 'b', 'c')
    start = 1
    #return tuple((zip (range(start,len(t)+start),t)))
    #enumerate can have start attribute so i=use enamurate instead
    return tuple((enumerate(t,start=start)))
# print(que71())

#72
def que72():
    tuple1 = (1, 3, 5)
    tuple2 = (2, 4, 6)
    return tuple((x for i in zip(tuple1,tuple2) for x in i))
# print(que72())

#73
def que73():
    t = (1, 2, 4, 5, 6)
    fullt=set(range(1,len(t)+1))
    missing=fullt-set(t)
    return missing.pop() if missing else None
# print(que73())

#que74
def que74():
    t = (1, 2, 3, 4, 5)
    return len(t)==len(tuple(set(t)))
# print(que74())

#75
def que75(t=[(1, 2), (3, 4), (5, 6)]):
    
    t2=tuple()
    for i in t:
        if isinstance(i,tuple):
            t2+=que75(i)
        else:
            t2+=(i,)
    return t2
# print(que75())

#76
def que76():
    t = (10, 15, 12, 20, 25)
    return tuple((t[i+1]-t[i] for i in range(len(t)-1)))
# print(que76())

#77
def que77():
    t= (1, 2, 3, 4)
    fx=lambda x:x**2
    return tuple((map(fx,t)))
# print(que77())

#78
def que78():
    t = ('cat', 'elephant', 'dog', 'butterfly')
    return max(t,key=len)
# print(que78())

#79
def que79():
    t= (1, 2, 3, 4, 5, 6)
    # e=list()
    # o=list()
    # for i in t:
    #     if i%2==0:
    #         e.append(i)
    #     else:
    #         o.append(i)
    # return f"EVENS = {tuple(e)} , ODD = {tuple(o)}"

    ##mempory efficent
    evens = tuple(x for x in t if x % 2 == 0)
    odds = tuple(x for x in t if x % 2 != 0)
    return f"EVENS = {evens} , ODDS = {odds}"

# print(que79())

def que80():
    t = (1, 2, 3, 4, 5)
    return list((zip(t,t[1:])))
# print(que80())

#81
def que81():
    t= (((1, 2), (3, 4)), ((5, 6), (7, 8)))
    return t[1][0][1]

#82
def que82():
    t = ((1, 2), (3, (4, 5)))
    (a, b), (c, (d, e)) = t
    return a, b, c, d, e
# print(que82())

#83
def que83():
    t=[((1, 2), 'A'), ((2, 3), 'B')]
    return dict(t)
# print(que83())

#84 
def que84():
    t = (1, [2, 3], 4)
    t[1].append(5)
    return t
# print(que84())


#85
def que85(t=(1, (2, (3, 4)), 5)):
    
    t2=tuple()
    for i in t:
        if isinstance(i,tuple):
            t2+=que85(i)
        else:
            t2+=(i,)
    return t2
# print(que85())

#86
def que86(p1,p2):
    (x1,y1),(x2,y2)=p1,p2
    return ((x2-x1)**2 +(y2-y1)**2 )**0.5
# print(que86((1, 2), (3, 4)))

#87
def que87():
    m=((1, 2, 3), 
       (4, 5, 6),
        (7, 8, 9))
    colm=1
    return tuple((i[colm-1] for i in m))
# print(que87())

#88
# def que88():


#89
def que89():
    t = [(2, 1), (1, 3), (1, 2)]
    
    return sorted(t,key= lambda x: (sum(x),x[0]))

# #| Original tuple | Key function output `(sum(x), x[0])` |
# | -------------- | ------------------------------------ |
# | (2, 1)         | (3, 2)                               |
# | (1, 3)         | (4, 1)                               |
# | (1, 2)         | (3, 1)                               |

# print(que89())

#90
def que90():
    pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
    l=[]
    for num,letter in pairs:
        l.append((num,letter))
    return l
# print(que90())

#91
# def que91():


#92
def que92():
    t = (1, 2, 3)
    return tuple(((t[i],t[j]) for i in range(len(t)) for j in range(i+1,len(t))))
# print(que92())

#93
def que93(*n):
    return sum(n)
# print(que93(*(24,546,6676,5,42)))

#94
# def que94():
    # points = [(0, 0), (1, 1), (2, 2)]