#1
def que1():
    a = [1, 2, 2, 3, 4, 4, 5]
    return set(a)
# print(que1())

#2
def que2():
    my_set = {1, 2, 3}
    element = 2
    return element in my_set
# print(que2())

#3
def que3():
    a =  {1, 2, 3}
    element = 4
    a.add(element)
    return a
# print(que3())

#4
def que4():
    my_set = {1, 2, 3}
    a=2
    my_set.remove(a) if a in my_set else None
    return my_set
# print(que4())

#5
def que5():
    my_set = {1, 2, 3}
    element = 5
    my_set.discard(element)
    return my_set
# print(que5())

#6
def que6():
    my_set = {1, 2, 3, 4, 5}
    return len(my_set)
# print(que6())

#7
def que7():
    my_set = set()
    return True if my_set==set() else False
#or return not my_set True if empty, False otherwise
# print(que7())

#8
def que8():
    a = set()
    return a
# print(que8())

#9
def que9():
    a = "hello"
    return set(a)
# print(que9())

#10
def que10():
    t = {1, 2, 3}
    n=5
    return n not in t
# print(que10())

#11
def que11():
    t = {1, 2, 3}
    t.clear()
    return t
# print(que11())

#12
def que12():
    a = (1, 2, 3, 2, 4)
    return set(a)
# print(que12())

#13
def que13():
    a = {1, 2, 3}
    return a.pop() #deletes a randomn element
# print(que13())

#14
def que14():
    a = [1, 'hello', 3.14, True]
    return set(a)# as  True is consedered as 1 whivh is also persent so removed duplicated items
# print(que14())

#15
def que15():
    a = "the cat sat on the mat"
    return set(a.split())
# print(que15())

#16
def que16():
    set1 = {1, 2, 3}
    set2 = {4, 5, 6}
    return len(set1)==len(set2)
# print(que16())

#17
def que17():
    a = 5
    return set(range(1,a+1))
# print(que17())

#18
def que18():
    a = ['user@email.com', 'admin@email.com', 'user@email.com']
    return set(a)
# print(que18())

#19
def que19():
    return set((i for i in range(1,11) if i %2==0))
# print(que19())

#20
def que20():
    a = my_set = {1, 2, 3, 4}
    return all(i for i in a if i>0)
# print(que20())

#21
def que21():
    return set("aeiou")
# print(que21())

#22
def que22():
    str1 = 'hello'
    str2 = 'world'
    return set(str1) | set(str2)
# print(que22())

#23
def que23():
    return set((x**2 for x in range(1,6)))
# print(que23())

#24
def que24():
    a = "hello"
    seen=set()
    for i in a:
        if i in seen:
            return True
        seen.add(i)
    return False
# print(que24())

#25
def que25():
    a = {'a': 1, 'b': 2, 'c': 3}
    return set(a.keys())
# print(que25())

#26
def que26():
    a = {'a', 'b', 'c', 'e', 'f'}
    return set((i for i in a if i.lower() not in "aeiou"))
# print(que26())

#27
def que27():
    a = {42}
    return len(a)==1
#print(que27())

#28
def que28():
    a = ['file1.txt', 'file2.pdf', 'file3.txt', 'file4.jpg']
    return set(("."+i.split(".")[-1] for i in a))
# print(que28())

#29
def que29():
    a = "john"
    b="python"
    return set(a) & set(b)
# print(que29())

# 30. Create a set of prime numbers less than 20
def que30():
    a = range(2, 20)
    primes = set()
    
    for i in a:
        is_prime = True
        for j in range(2, int(i**0.5) + 1):  # check divisibility up to sqrt(i)
            if i % j == 0:#if a number has a divisor, at least one of them must be ≤ √i.
                is_prime = False
                break
        if is_prime:
            primes.add(i)
    
    return primes

# print(que30())  # Output: {2, 3, 5, 7, 11, 13, 17, 19}

#31
def que31():
    a = {1, 2}
    elements = [3, 4, 5]
    a.update(elements) #must me a iterble
    return a
# print(que31())

#32
def que32():
    a = {1, 2, 3}
    return a.copy()
# print(que32())

#33
def que33():
    a = [1, 2, 3, 4, 5]
    return len(set(a))==len(a)
#print(que33())

#34
def que34():
    a = {1, 2, 3, 4, 5} 
    # return {i for i in a if i % 2 != 0}

# by filter
    return set(filter(lambda x:x%2==0,a))
# print(que34())

#35
def que35():
    a = ['cat', 'dog', 'elephant', 'fox']

    return {len(i) for i in a} #it is a set generator obj
# print(que35())

#36
def que36():
    a = {1, -2, 3, 4}
    return any(i for i in a if i>0)
# print(que36())

#37
def que37():
    a = 12321
    return set(str(a))
# print(que37())

#38
def que38():
    a = {3, 7, 1, 9, 5}
    return f"max {max(a)} , min {min(a)}" 
# print(que38())

#39
def que39():
    a = ['apple', 'banana', 'cherry', 'avocado']
    return {i[0] for i in a}
# print(que39())

#40
def que40():
    a = {'hello', 'world', 'python'}
    return all(i.isalpha( ) for i in a)
# print(que40())

#41
def que41():
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    return set1 | set2
# print(que41())

#42
def que42():
    set1 = {1, 2, 3}
    set2 = {2, 3, 4}
    return set1 & set2
# print(que42())

#43
def que43():
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5}
    return set1 -set2
# print(que43())

#44
def que44():
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    print(set1.symmetric_difference(set2))#or
    return set1 ^ set2
# print(que44())

#45
def que45():
    set1 = {1, 2}
    set2 = {1, 2, 3, 4}
    print(set1.issubset(set1))
    return set1 <= set2
# print(que45())

#46
def que46():
    set1 = {1, 2, 3, 4}
    set2 = {2, 3}
    print(set1.issuperset(set2))#or
    return set1 >= set2
# print(que46())

#47
def que47():
    set1 = {1, 2, 3}
    set2 = {4, 5, 6}
    return set1.isdisjoint(set2)# does nt work with multiple 2 each time
# print(que47())

#48
def que48():
    set1 = {1, 2,}
    set2 = {3, 4}
    set1.update(set2) # it is like a union + update or use |=
    return set1
# print(que48())

#49
def que49():
    set1 = {1, 2, 3}
    set2 = {2, 3, 4}    
    set1 &= set2       #intersection_update() or &= 
    return set1.intersection_update(set2) #it will give none as it will modify in plase same as &=
# print(que49())

#50
def que50():
    set1 = {1, 2, 3, 4}
    set2 = {3, 4}
    set1-=set2
    return set1.difference_update(set2)
#print(que50())

#51
def que51():
    sets = [{1,2,3}, {2,3,4}, {2,3,5}]

    return set.intersection(*sets)# npacking sets
# print(que51())

#52
def que52():
    numbers = {1, 2, 3, 4, 5, 6}

    return {i for i in numbers if i%2==0}
# print(que52())

#53
def que53():
    return {i**2 for i in range(1,11) if i % 2 ==0 }
#print(que53())

#54
def que54():
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    set1 ^= set2
    return set1
# print(que54())

#55
def que55():
    set1 = {1, 2}
    set2 = {1, 2, 3}
    return set1 < set2
# print(que55())

#56
def que56(a = [[1, 2], [2, 3], [3, 4, 1]]):
    l=[]
    for i in a :
        if isinstance(i,list ):
            l.extend(que56(i))
        else:
            l.append(i)

    return set(l)
# print(que56())

#57
def que57():
    sets = [{1, 2}, {2, 3}, {3, 4}]
    return set.union(*sets)
# print(que57())

#58
def que58():
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    a=set1&set2
    set1-=a
    set2-=a
    return set1,set2
# print(que58())

#59
def que59():
    sets = [{1}, {1, 2}, {1, 2, 3}]
    return all(s1 < s2 for s1, s2 in zip(sets, sets[1:]))
# print(que59())

#60
def que60():
    a =[{1, 2}, {2, 3}, {4, 5}]
    return set.union(*a)
# print(que60())

#61
def que61():
    data = {1, 2, 3, 4, 5}
    blacklist = {2, 4}
    return data-blacklist
# print(que61())

#62
def que62():
    set1 = {1, 2, 3, 4}
    others = [{2, 3}, {3, 5}]
    return set1.difference(*others)
# print(que62())

#63
def que63():
    a = {1, 2, 3}
    set2 = {2, 3, 4}
    return f"only in set 1 {a-set2} common {a& set2} only in set2 {set2-a}"
# print(que63())

#64
def que64():
    sets = [{1, 2}, set(), {3, 4}]
    return not all(sets)#or return any(not s for s in sets)
    
# print(que64())

#65
def que65():
    a = [{1}, {1, 2, 3}, {1, 2}]
    return max(a,key=len)
# print(que65())

#66
def que66():
    dir1 = {'file1.txt', 'file2.pdf'}
    dir2 = {'file3.txt', 'file4.jpg'}
    ex={"."+i.split(".")[-1] for i in dir1 if "." in i}
    ex2={"."+i.split(".")[-1] for i in dir2 if "." in i}
    return set.intersection(ex,ex2)
# print(que66())

#67
def que67():
    emails = {'user@gmail.com', 'admin@yahoo.com'}
    valid = {'gmail.com', 'outlook.com'}
    return {e for e in emails if e.split("@")[-1] in valid}
# print(que67())

#68
def que68():
    post1_tags = {'python', 'coding', 'tutorial'}
    post2_tags = {'python', 'programming', 'tutorial'}
    return post1_tags & post2_tags
# print(que68())

#69
def que69():
    role1 = {'read', 'write'}
    role2 = {'read', 'execute'}
    return role1 & role2
# print(que69())

#70
def que70():
    user_permissions = {'read', 'write', 'execute'}
    required = {'read', 'write'}
    # return True if user_permissions & required == required else False
    #or can be done with is subbset or superset 
    return required <user_permissions
# print(que70())

#71
def que71():
    user1_friends = {'Alice', 'Bob', 'Charlie'}
    user2_friends = {'Bob', 'Charlie', 'David'}
    return user1_friends & user2_friends
# print(que71())

#72
def que72():
    job1 = {'Python', 'SQL'}
    job2 = {'Python', 'JavaScript', 'SQL'}
    return job1 | job2
# print(que72())

#73
def que73():
    store1 = {'laptop', 'mouse'}
    store2 = {'laptop', 'keyboard'}
    return f" available everywhere {store1 & store2}"
# print(que73())

#74
def que74():
    recipe1 = {'flour', 'eggs', 'milk'}
    recipe2 = {'flour', 'sugar'}
    return f"all_ ingredients {recipe1 & recipe2}"
# print(que74())

#75
def que75():
    votes_for = {'Alice', 'Bob'}
    votes_against = {'Charlie'}
    all_members = {'Alice', 'Bob', 'Charlie', 'David'}
    return f"abstained {all_members - (votes_for | votes_against)}"# witthhout function it is faster

#print(que75())

#76
def que76():
    enrolled = {'Math101', 'Physics101'}
    conflicts = [{'Math101', 'Math102'}, {'Physics101', 'Chemistry101'}] 
    return any(enrolled & c for c in conflicts)

# print(que76())

#77
def que77():
    completed = {'Math101', 'Physics101'}
    course_prereqs = {'Math201': {'Math101'}, 'Physics201': {'Physics101', 'Math101'}}
    
    # it mean s that for key subject a person require to have the values subjects
    available = {i for i in course_prereqs if course_prereqs[i] <= completed}
    return f"course available {available}"
# print(que77())

#78
def que78():
    content_keywords = {'python', 'programming', 'tutorial'}
    user_interests = {'python', 'data science'}
    return f" relevence score = {len(content_keywords & user_interests)}"
# print(que78())

#79
def que79():
    available_features = {'age', 'income', 'education'}
    important_features = {'age', 'income'}
    # return f"selected_features = { available_features & important_features}" if important_features <= available_features  else None
    # or the best way 
    selected = available_features & important_features
    return f"selected_features = {selected}" if selected else None
    
# print(que79())

#80
def que80():
    user1 = {'movie1', 'movie2'}
    user2 = {'movie2', 'movie3'}
    # Jaccard similarity=∣A∪B∣/∣A∩B∣​
    p = len(user1 &  user2) / len(user1 | user2)
    return f" similarity = {p :.2f}"#:.2f formatting specifier
# print(que80())

#81
def que81():
    a = [1, 2, 3]
    return { frozenset(a) : "value"}# to use list as key for dixct
# print(que81())

#82
def que82():
    sets = [frozenset({1, 2}) , frozenset({2, 3})]

    return set.intersection(*map(set, sets))
# print(que82())

#83
def que83():
    s = {1, 2, 3}
    # start with empty set in a set
    pset = {frozenset()}  
    for elem in s:
        pset |= {subset | {elem} for subset in pset}  # add elem to each existing subset
    return pset

# print(que83())


#84
def que84():
    a = 0
    return 0
#print(que84())

#85
def que85():
    a = {1,2,3,4,5}
    sets = [{1,2,3}, {2,4}, {3,4}, {4,5}]
    return 0
#print(que85())

#86
def que86():
    a = 0
    return 0
#print(que86())

#87
def que87():
    a = 0
    return 0
#print(que87())

#88
def que88():
    a = 0
    return 0
#print(que88())

#89
def que89():
    a = 0
    return 0
#print(que89())

#90
def que90():
    a = 0
    return 0
#print(que90())

#91
def que91():
    a = 0
    return 0
#print(que91())

#92
def que92():
    a = 0
    return 0
#print(que92())

#93
def que93():
    a = 0
    return 0
#print(que93())

#94
def que94():
    a = 0
    return 0
#print(que94())

#95
def que95():
    a = 0
    return 0
#print(que95())

#96
def que96():
    a = 0
    return 0
#print(que96())

#97
def que97():
    a = 0
    return 0
#print(que97())

#98
def que98():
    a = 0
    return 0
#print(que98())

#99
def que99():
    a = 0
    return 0
#print(que99())

#100
def que100():
    a = 0
    return 0
#print(que100())
