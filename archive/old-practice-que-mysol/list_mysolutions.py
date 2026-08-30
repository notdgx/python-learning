############# I TRIED UPTO 91 QUESTIONS AND I DIDNT DO THE 58,66,76,82,88 AND 91-100
# BECAUSE THEY SEEMS TOO DIFFICULT AWY FROM MY UNDERSTANDING 
# AS I MATCHED MT RESULTS TO SOLUTIONS I FOUND THAT I CAN MAKE THEM SHORT AND WITH RETURN STATEMENT
# AND PASS DIIF AGRUNMENTS 
# IT WAS MY FIRST TIME DOING IT SOOOOOO 
# BUT I AM SATISFIED AND WILL DO OTHER AT MY LEVEL UP I LEARNED A LOT NEW :)


# 1 
def que1():
    a=list((1,2,3,4,5))
    print(a)
#que1()

#2◍
def que2():
    a=[10, 20, 30, 40, 50]#given
    print(a[2])#for third element

#que2()

#3
def que3():
    a=['apple', 'banana', 'cherry', 'date']
    print(len(a))#prints length of a

# que3()

#4 
def que4():
    a=['apple', 'banana', 'cherry']
    b="grape"
    a.append(b)
    print(a)

# que4()

#5 
def que5():
    a=[10, 20, 30, 40]
    b=25
    a.insert(2,b)
    print(a)
# que5()

#6 ◍
def que6():
    a=['apple', 'banana', 'cherry', 'banana']
    a.remove("banana")
    print(a)
# que6()

#7 ◍
def que7():
    a=[5, 10, 15, 20]
    a.pop(1)
    print(a)
    #removes element by index
# que7()

#8 
def que8():
    a=['apple', 'banana', 'cherry']
    print('orange' in a)

# que8()

#9◍ can give value error if not present
def que9():
    a=['apple', 'banana', 'cherry', 'date']
    print(a.index("cherry"))
#que9()

#10
def que10():
    a=['apple', 'banana', 'apple', 'cherry']
    c=0
    for i in a:
        if i=="apple":
            c+=1
    print(c)

    #or
    print(a.count("apple"))
# que10()

#11
def que11():
    a=[0, 1, 2, 3, 4, 5]
    print(a[1:4])
# que11()

#12◍ can give indexerror if l=[]
def que12():
    a=[10, 20, 30, 40, 50]
    print(a[-1])
# que12()

#13◍ can give indexerror if not valid
def que13():
    a=['a', 'b', 'c', 'd']
    a[2]="NEW"
    print(a)
# que13()

#14
def que14():
    a=[1, 2, 3] 
    b=[4,5,6]
    a.extend(b)
    print(a)

# que14()

#15
def que15():
    a=[1, 2, 3, 4, 5]
    a.clear()
    print(a)
# que15()

#16
def que16():
    a=[1, 2, 3, 4]
    b=a.copy()
    print(b)
    print(id(a),id(b))
# que16()

#17
def que17():
    a=[1,2]
    b=[3,4]
    print(a+b)
# que17()

#18(
def que18():
    a=[1,2]
    print(a*3)
# que18()

#19◍ or can do l==0
def que19():
    a=[]
    b=[1,3]
    print(a == [])
    print(b == [])

# que19()

#20◍
def que20():
    a=[45, 12, 78, 23, 67]
    b=[]
    print(min(a))
    print(min(b))#ValueError as b is empty
#return min(lst) if lst else None
# this condition will check whether l is empty then
#return none
# que20()

#21
def que21():
    a=[45, 12, 78, 23, 67]
    b=[]
    print(max(a))
    print(max(b))#ValueError

# que21()

#22
def que22():
    a=[1, 2, 3, 4, 5]
    print(sum(a))#no errors except when non iterable 
# que22()

#◍my map version is fast for big data
#23
def que23():
    l=[1,2,3,4,5]
    a=map(lambda x:x**2,l)
    print(list(a))
# que23()

#24
def que24():
    a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    b=[]
    for i in a:
        if i%2==0:
            b.append(i)

    print(b)

# que24()

#25
def que25():
    a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    b=[]
    for i in a:
        if i%2!=0:
            b.append(i)

    print(b)
# que25()

#26
def que26():
    a=['red', 'green', 'blue']
    for i in a:
        print(i)

# que26()

#27
def que27():
    a=['hello', 'world', 'python']
    b=[]
    c=[]
    for i in a:
        b.append(len(i))
    print(b)

    #OR 
    print(list(map(lambda x:len(x),a)))

# que27()

#28◍i should take in account the error possibility
def que28():
    a=[10, 20, 30, 40, 50]
    b=[]
    b.append(a[0])
    b.append(a[-1])
    print(b)
# que28()

#29◍ i can check whether a list is empty or not by- if l:
def que29():
    a=[1, 2, 3, 4, 5]
    print(a.pop(),",",a)
# que29()


#30
def que30():
    a=[0, 1, 2, 3, 4, 5]
    print(a[3:0:-1])
# que30()

#31
def que31():
    a=[2, 4, 6, 8]
    print(all(i%2==0 for i in a))#all check here a condition it has a generator condition that is useful like lambda 
# que31()


#32
def que32():
    a=[1, 3, 5, 8] 
    print(any(i%2==0 for i in a))

# que32()


#33
def que33():
    a=['old', 'car', 'old', 'house']
    for i in range(len(a)):
        if a[i]=="old":
            a[i]="new"

    print(a)
# que33()

#34◍
def que34():
    a=[]
    for i in range(1,6):
        a.append(i*3)
    print(a)

# que34()

#35◍
def que35():
    a=[10, 20, 30, 40, 50]
    print(sum(a)/len(a))

# que35()

#36
def que36():
    a=[1, 2, 3, 4, 5]
    b=[]
    for i in a:
        b.append(str(i))
    print(b)

# que36()

#37
def que37():
    a='hello'
    print(list(a))

# que37()

#38
def que38():
    a=['apple', 'banana', 'cherry']
    #using th e join() as syntax "".join(iterable)
    print(",".join(a))# give output as str

# que38()


#39
def que39():
    a="one,two,three,four"
    b=a.split(",")
    print(b)
# que39()


#40
def que40():
    a= [1, 2, 3, 4, 5]
    ###################### Instance use i dont studied yet 
    if all(isinstance(x, int) for x in a):
        print("TRUE")

    #bool is a subclasss of int
# que40()

#41
def que41():
    a=[64, 34, 25, 12, 22, 11, 90]
    print(a.sort())#returns none sort tht list in place
    print(a)
# que41()

#42
def que42():
    a=[64, 34, 25, 12, 22, 11, 90]
    print(a.sort(reverse=True))#returns none
    print(a)
# que42()


#43
def que43():
    a=[1, 2, 3, 4, 5]
    print(a.reverse())#returns none
    print(a)
    #reverse in place

#que43()

#44
def que44():
    print(list(i**2 for i in range(1,11)))
# que44()

#45
def que45():
    n=10
    print(list(i**2 for i in range(1, n+1) if i % 2 == 0))#new topic syntax as ( <to print or output>  for loop <condition> )
# que45()

#46
def que46():
    a=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    b=a[1][2]
    print(b)
# que46()


#47
def que47():
    a=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    a[1][1]=50
    print(a)
# que47()


#48
def que48():
    a=[1, 2, 2, 3, 4, 4, 5]
    print(a)
    b=set(a)
    print(list(b))
# que48/


#49 should put condition for indexerror
def que49():
    a=[45, 12, 78, 23, 67, 89, 34]
    a.sort()
    print(a[-2])
# que49/

#50
def que50():
    a=[45, 12, 78, 23, 67, 89, 34]
    a.sort()
    print(a[-2])
# que50/

#51
def que51():
    a=[1, 2, 3, 4]
    b=[3, 4, 5, 6]
    print(list(set(a)&set(b)))#first convert list to set aand thenconvert them back
# que51()


#52
def que52():
    a=[1, 2, 3, 4, 5] 
    b=[3, 4, 5, 6, 7]
    print(list(set(a)-set(b)))#first convert list to set aand thenconvert them back
#que52()

#53
def que53():
    l=[1,2,3,4,5]
    position=2
    position=position%len(l)
    print(l[position:]+l[:position])
#que53()


#54
def que54():
    l=[1,2,3,4,5]
    n=2
    position=len(l)-n
    position=position%len(l)
    print(l[position:]+l[:position])
#que54()



#55
def que55():
    l=[1,2,3,4, 5,6,7,8,9,10]
    n=3
    a=[]
    for i  in range(0,len(l),n):
        a.append(l[i:i+n])
    print(a)
#que55()

#56
def que56():
    a=['cat', 'elephant', 'dog', 'python', 'ai']
    b=[]
    for i in a:
        if len(i)>4:
            b.append(i)
    print(b)
    
#or filter
    print(list((filter(lambda x:len(x)>4,a))))
#que56()



#57◍
def que57():
    a=[]
    for i in range(1,21):
        if i%2==0 and i%3==0:
            a.append(i)
    print(a)
#que57/

#58
def que58():
    a=["a","b","c","d"]
    b=[]
    for i in enumerate(a):
        b.append(i)
    print(b)
#que58/

#59
def que59():
    a=['name', 'age', 'city']
    b=['John', 25, 'NYC']
    print(zip(a,b))#give zip object
    print(list(zip(a,b)))
#que59/

#60
def que60():#
    a = ['name', 'age']
    b = [['John', 25], ['Jane', 30]]
    c = []
    for i in b:
        d={}
        for j in range(len(a)):
            d[a[j]]=i[j]
        c.append(d)    
    print(c)

    #or by zip
    d=[]
    for i in b:
        d.append(dict(zip(a,i)))
    print(d)
        
    # or list Comprehension
    d = [dict(zip(a, i)) for i in b]
    print(d)


    # or generator obj
    d = (dict(zip(a, i)) for i in b)  # This is a generator, NOT a list
    print(list(d))  # You must convert to list if you want to print all at once ,doesnt store all value at once it just genreate vxalue on call,
    #but converted into list so then work same as above


# que60()


#61
def que61():# took me over 15 min and 5 min chatgpt session  
    a=['apple', 'banana', 'cherry', 'apricot',]
    b={}
    for i in range(len(a)):
        g=[]
        for j in a:
            if a[i][0].lower()==j[0].lower():
                g.append(j)
        b[a[i][0]]=g
    print(b)

    # what i was doing previously was resetiing g evertime
    # a = ['apple', 'banana', 'cherry', 'apricot']
    # b = {}
    # for i in range(len(a)):
    #     for j in a:
    #         g = []
    #         if a[i][0].lower() == j[0].lower():
    #             g.append(j)
    #         b[a[i][0]] = g


# que61()

#62 enamurate can also be used
def que62():
    a=['a', 'b', 'a', 'c', 'a']
    b=[]
    for i in range(len(a)):
        if a[i]=='a':
            b.append(i)
    print(b)

    # with generator
    d=(i for i in range(len(a)) if a[i]=='a')#give the generator obj
    # <...> for loop <condition>  
    #... will be saved in d
    print(list(d))

    #with list Comprehension
    print([i for i in range(len(a)) if a[i]=='a']) # no need to cone=vert ass it returns a list
# que62()

#63
def que63():
    a=[1,3]
    b=['a', 'b', 'c', 'd', 'e']
    c="X"
    for i in a:
        b[i]=c
    print(b)

    # in generator
    #print(list(()))
    # generator or list compression caant do becatuse <...> creates new object not bring change in old one
# que63()

#64
def que64():
    a=[1, 2, 3, 2, 1]
    # print(a==a.reverse())
    #wrong as it returns none it modifies it in place what i was doing use reversed instead but slicing preffered
    print(a==list(reversed(a)))
    #or 
    print(a==a[::-1])
# que64()

#65
def que65():
    a=[[1, 2, 3], [4, 5, 6]]
    b=list(zip(a[0],a[1]))
    print(b)

    #* is a unpacking operator
   # list(zip(*matrix))
#[[1, 2, 3],  
# [4, 5, 6]]

# to    

# [[1, 4],  
#  [2, 5],  
#  [3, 6]]

# is transpose


# que65()

#66
def que66():
    a=[1,2,3,]
    b=[4,5,6,]
    #1st

    print(sorted(a+b))

    #2nd  

    a.extend(b)
    a.sort()
    print(a)

    #3rd
# its  pretty complcated under the hood version **SKIPs
# que66()  

#67
def que67():
    a= [1, 2, 3, 4, 5]
    b=[]
    sum=0
    for i in a:
        sum+=i
        b.append(sum)
    print(b)

# que67()

#68
def que68():#from chatgpt
    a = [3, 1, 4, 1, 5, 9, 2]
    c = []
    max_val = float('-inf')  # Initialize with the lowest possible value

    for i in a:
        max_val = max(max_val, i)  # update max
        c.append(max_val)

    print(c)
# que68()

#69
def que69():
    a=[1, 2, 2, 3, 3, 3, 4]
    b={}
    for i in a:
        b[i]= a.count(i)
    print(b)

    #with generator
    print(dict(((i,a.count(i)) for i in a )))
# que69()

#70
def que70():
    a=[1, 6, 2, 8, 3, 9, 4]
    for i in a:
        if i>5:
            a.remove(i)
    print(a)
    
    #filte()
    a=[1, 6, 2, 8, 3, 9, 4]
    print(list((filter(lambda x : x<5 , a))))
    
    #generator
    
    a=[1, 6, 2, 8, 3, 9, 4]
    print(list((i for i in a if i<5)))

    #list compression
    print([i for i in a if i<5])


# que70()

#71
def que71():
    a=[1, 2, 3, 4, 5, 6, 7]
    n=3
    b=[]

    for i in range(len(a) - n + 1):# 5 combination to get 3 window
        x=0
        for j in range(i,i+n):
            x+=a[j]
        b.append(x/3)
    print(b)
# que71()

#72
def que72():
    #it means Take one element from a, then one from b, then the next from a, then next from b, and so on...
    a=[1,3,5]
    b=[2,4,6]
    c=[]
    for i,j in zip(a,b):
        c.extend([i,j])
    print(c)
# que72()

#73
def que73():
    a=[1, 2, 3, 4, 5, 6]
    e=[]
    o=[]
    for i in a:
        if i%2==0:
            e.append(i)
        else:
            o.append(i)
    print((e,o))
# que73()

#74
def que74():
    a = [1, 2, 4, 5, 6]
    for i in range(a[0], a[-1] + 1):
            if i not in a:
                print(i)
    #or use sum method
#que74()

#75
def que75():
    #not the actual method slow for big list  , binary ia fast but only works on sorted lists ascending or descending
    a=[1,3,5,7,9,11]
    n=7
    for i in range(len(a)):
        if a[i]==n:
            print(i)
            
            
      #actual binary method
    a=[1,3,5,7,9,11]
    n=7
    low=0
    high=len(a)-1
    is_asc=a[low]<a[high]
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == n:
            print(mid)
            break
        if is_asc:
            if a[mid] < n:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if a[mid] > n:
                low = mid + 1
            else:
                high = mid - 1
            
# que75()

#76
# def que76():
#     a=[10, 9, 2, 5, 3, 7, 101, 18]
    # dont know out off brain

#77
def que77():
    #not recommended as it will create a bug as list is continously changing it
    # #if more than 2 the 2s wiill not be removed 
    a=[1, 2, 3, 4, 5, 2, 4, 6]
    b=[2,4]
    for i in b:
        for j in a:
            if i==j:
                a.remove(i)
    print(a)

    #list comresion , creating another one
    a = [1, 2, 3, 4, 5, 2, 4, 6]
    b = [2, 4]
    a = [x for x in a if x not in b]
    print(a)

    #filter()
    a = [1, 2, 3, 4, 5, 2, 4, 6]
    b = [2, 4]
    result = list(filter(lambda x: x not in b, a))
    print(result)

    #if b is large for speeding it up 
    a = [1, 2, 3, 4, 5, 2, 4, 6]
    b = set([2, 4])
    a = [x for x in a if x not in b]
    print(a)
#set is faster than list for lookups using in because it's an unindexed, unordered data type that uses a hash table for constant-time access.
#Python doesn't search through each item like list It hashes <whatever> and jumps straight to the memory slot where it should be
# que77()


#78
def que78():
    a=[1, 3, -1, -3, 5, 3, 6, 7]
    n=3
    b=[]
    for i in range(len(a)-n+1):
        e=[]
        for j in range(i,i+n):
            e.append(a[j])
        b.append(max(e))

    #b.append(max(a[i:i+n])) 
    #for directly slice

    print(b)
# que78()

#79
def que79():
    a=[1, 2, 3, 4]
    b=[1, 3, 3, 5]
    c=[]
    for i,j in zip(a,b):
        c.append(i == j)
    print(c)

    # othr
    print(list((x==y for x,y in zip(a,b))))
    print([x==y for x,y in zip(a,b)])
    
# que79()

#80
def que80():
    a=[1, 2, 3]
    b=[3, 1, 2]
    # the both has same datatype 
    a.sort()
    b.sort()
    print(a==b)

# que80()

#81
def que81():
    a=[[1, 2], [3, 4, 5], [6]]
    b=[]
    for i in a:
        for j in i:
            b.append(j)
    print(b)
# que81()

#82◍
# def que82():
#     a= [1, [2, 3, [4, 5]], 6]

#83
def que83():

    #for small lists
    a=[3, 1, 4, 1, 5, 9, 2, 6, 5]
    b=[]
    for i in a:
        if i not in b:
            b.append(i)
    print(b)

    # if large data for faster 

    a = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    seen = set()
    b = []
    for i in a:
        if i not in seen:     # O(1) check
            b.append(i)
            seen.add(i)
    print(b)

# que83()

#84
def que84():
    a=[1, 2]
    b=['a', 'b']
    c=[]
    for i in a:
        for j in b:
            c.append((i,j))

    print(c)

    #list compression
    d = [(i, j) for i in a for j in b]
    print(d)

# que84()

#85
def que85():
    #all cartesian pairs
    a=[1, 2, 3, 4]
    r=2
    c=[]
    for i in a:
        for j in a:
            c.append((i,j))
    print(c)

    #all cartesian pairs excluding (i,i) permmutation
    a=[1, 2, 3, 4]
    r=2
    c=[]
    for i in a:
        for j in a:
            if i!=j:
                c.append((i,j))
    print(c)

    # # cartesian product combination
    a = [1, 2, 3, 4]
    c = []
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            c.append((a[i], a[j]))
    print(c)
# que85()

# #86
# def que86():
#     def permutations(lst):
#     def helper(path, used):
#         if len(path) == len(lst):
#             result.append(tuple(path))
#             return
#         for i in lst:
#             if i not in used:
#                 helper(path + [i], used | {i})
    
#     result = []
#     helper([], set())
#     return result

# # Test
# print(permutations([1, 2, 3]))



#87
def que87():
    #not > and > or
# if multiple L to R
    a,b=2,3
    n=20
    c=[]
    for i in range(1,n+1):
        if (i%2==0 or i%3==0) and i>5:
            c.append(i)

    print(c)
# que87()

#88
# def que88():
    

#89
def que89():
    a=[1, 2, 3, 2, 4, 5, 1, 6, 7, 3] 
    seen=set()
    duplicate=set()
    for i in a:
        if i in seen:
            duplicate.add(i)
        else:
            seen.add(i)
    print(list(duplicate))

#que89()

#90
def que90():
    a=[1, 2, 3]
    b=[4, 5]
    c=[6, 7, 8, 9]
    print(list(zip(a,b,c)))
    #or it can be replaced by args for unkm=nown multiple inputs
# que90()

#91◍
# def que91():


#92
# def que92():