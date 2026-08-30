#1
def que1():
    a="hello"
    return a[::-1]

# print(que1())

#2
def que2():
    a="hello world"
    return len(a)-a.count(" ")
# print(que2())


# 3
def que3():
    a = "python"
    return a[0]+a[-1]
# print(que3())

# 4
def que4():
    a = "coding"
    l=0
    for i in a:
        l+=1
    return l
# print(que4())

# 5
def que5():
    a = "12345"
    return a.isdigit()
# print(que5())

# 6
def que6():
    a = "Hello World"
    return a.upper()
# print(que6())

# 7
def que7():
    a ="programming"
    return len([1 for i in a if i.lower() in "aeiou"])
    # return sum(1 for i in a if i.lower() in "aeiou")
# print(que7())

# 8
def que8():
    a = "hello world python"
    # return "".join(a.split(" "))
    return a.replace(" ","")
# print(que8())

# 9
def que9():
    a = "   "
    return a.isspace()
# print(que9())

# 10
def que10():
    a = "abcdef"
    return a[::2]
# print(que10())

# 11
def que11():
    a = "hello"
    character="l"
    return a.count("l")
# print(que11())

# 12
def que12():
    a = "Hello"
    b="HELLO"
    return a.lower()==b.lower()
# print(que12())

# 13
def que13():
    a = "abc123def456"
    return "".join((i for i in a if i.isdigit()))# can directly join with obj
# print(que13())

# 14
def que14():
    a = "HelloWorld"
    return a.isalpha()
# print(que14())

# 15
def que15():
    a = "hi"
    n=3
    separator="-"
    # return "-".join((a for i in range(n) ))
    return "-".join([a]*n)#["hi"] * 3  -> ["hi", "hi", "hi"]
# print(que15())

# 16
def que16():
    a = "python"
    index=2
    return a[index] if -len(a) <= index < len(a) else None
#for handeling negative index
# print(que16())

# 17
def que17():
    a = "hello world"
    prefix="hello"
    return a.startswith(prefix)
# print(que17())

# 18
def que18():
    a = "python.py"
    suffix=".py"
    return a.endswith(suffix)
# print(que18())

# 19
def que19():
    a = "hello_world_python"
    #Snake case is a way of writing identifiers (like variable names, function names, or file names) in programming where:
    # All letters are lowercase.
    # Words are separated by underscores _ instead of spaces or capitalization.

    #| Style       | Example            |
# | ----------- | ------------------ |
# | Snake case  | `my_variable_name` |
# | Camel case  | `myVariableName`   |
# | Pascal case | `MyVariableName`   |
# | Kebab case  | `my-variable-name` |



    return " ".join(a.split("_")).title()
# print(que19())

# 20
def que20():
    a = "hello world python"
    return len(a.split())
# print(que20())

# 21
def que21():
    a = "racecar"
    return a==a[::-1]
# print(que21())

# 22
def que22():
    a = "hello world"
    character="l"
    # return "".join(a.split(character))
    return a.replace(character,"")
# print(que22())



# 23
def que23():
    a = "abc"
    return list(a)
# print(que23())

# 24
def que24():
    a = ['a', 'b', 'c']
    delimiter="-"
    return delimiter.join(a)
# print(que24())

# 25
def que25():
    a = "aaaa"
    #return len(set(a))==1
    return all(i==a[0] for i in a)#memory efficient
# print(que25())

# 26
def que26():
    a = "python"
    return a[(len(a)//2)-1:(len(a)//2)+1] if len(a)%2==0 else a[len(a)//2-1]
# print(que26())

# 27
def que27():
    a = "hello world"
    return a.capitalize()
# print(que27())

# 28
def que28():
    a = "hello world"
    substring="wor"
    return substring in a
# print(que28())

# 29
def que29():
    s1 = "abcde"
    s2 = "cdeab"
    return len(s1) == len(s2) and s2 in s1 + s1
# print(que29())


# 30##
def que30():
    a = "aabbcc"
    seen=set()
    return "".join((i for i in a if  not (i in seen or seen.add(i) )))
# print(que30())

# 31
def que31():
    a = "hello"
    return len([i for i in a if i.isalpha() and i.lower() not in "aeiou"])# is alpha to ignore other char
# print(que31())

# 32
def que32():
    a = "Hello World"
    return a.swapcase()
# print(que32())

# 33
def que33():
    a = "abccba"
    # for i in a:
    #     if a.count(i)==1:
    #         return i
            #not memort efficient

    #use dictionary
    d={}
    for i in a:
        d[i]=d.get(i,0)+1
    for i in d:
        if d[i]==1:
            return i
        return None

    
# print(que33())

# 34
def que34():
    s= "hello"
    le=10 
    ch="*"
    n = max(le - len(s), 0)
    left = n // 2 + (n % 2)  # put extra on the left to match "***hello**"
    right = n - left
    return ch * left + s + ch * right
# print(que34())

# 35
def que35():
    a="1234.5"
    try:
        return True if float(a) else None
    except ValueError:
        return None
# print(que35())

# 36
def que36():
    a = "abc123def456"
    return "".join((i for i in a if i.isalpha()))
# print(que36())

# 37
def que37():
    a = "line1\nline2\nline3"
    return 0 if not a else a.count("\n")+1
# print(que37())

# 38
def que38():
    a = "abc"
    b= "bca"
    return sorted(a)==sorted(b)#preserve duplicates
# print(que38())

# 39
def que39():
    a= "The quick brown fox"
    words = a.split()
    return max(words, key=len) if words else "" 
# print(que39())

# 40
def que40():
    a  ="hello"
    index=1
    new_char="a"
    # return a.replace(a[index],new_char) wrong as it rplace all occureance
    return a[:index]+new_char+a[index+1:] if (0 <= index < len(a)) and len(new_char)!=0 else None

# print(que40())

# 41
def que41():
    a="aaabbcc"


    # seen=set()
    # output=""
    # for i in a:
    #     if i not in seen:
    #         output=output+i+str(a.count(i))
    #         seen.add(i)
    # return output                fails when aaabbbaba


    if not a:
        return ""

    output = []
    count = 1

    for i in range(1, len(a) +1):
        if i < len(a) and a[i] == a[i - 1]:
            count += 1
        else:
            output.append(a[i - 1] + str(count))
            count = 1

    return "".join(output)

# print(que41())

# 42
def que42():#only for singlle digit 
    a = "a3b2c2"
    vl=""
    times=""
    out=""
    for i in a:
        if i.isalpha():
            vl+=i
        elif i.isdigit():
            times+=i
    for i,j in zip(vl,times):
        out+=i*int(j)
    return out

# print(que42())

# 43
def que43():
    a = "hello world hello"
    s=a.split()
    # return {i:s.count(i) for i in s} slow for large On^2
    freq = {}
    for word in s:
        freq[word] = freq.get(word, 0) + 1
    return freq

# print(que43())

# 44
def que44():
    a = "hello world python"
    return " ".join(reversed(a.split()))
# print(que44())

# 45
def que45():
    a = "hello    world   python"
    return " ".join(a.split())
# print(que45())

# 46
def que46():
    a = "listen"
    b="silent"
    return sorted(a)==sorted(b)
# print(que46())

# 47
def que47():
    a = "abc"
    out = [a[i:j] for i in range(len(a)) for j in range(i+1, len(a)+1)]
    return sorted(out, key=len)

# print(que47())
# ['a', 'b', 'c', 'ab', 'bc', 'abc']



# 48
def que48():
    a = ["flower", "flow", "flight"]
    p=""


    # for i in range(len(a)):
    #     b=[]
    #     for j in range(max(len(n) for n in a)):
    #         if a[0][:j] in a[i]:
    #             b.append(a[0:j])
    # p+=max(a,key=len)
    # return p

    for j in range(len(min(a, key=len)) + 1): #if we dont add +1 then a[0][:j] at j=0 is ""
        prefix = a[0][:j]   # take prefix from first string
        if all(word.startswith(prefix) for word in a):
            p = prefix
        else:
            break
    return p
# print(que48())

# 49
def que49():
    a = "abcdef"
    k=2
    return a[2:]+a[:2]
# print(que49())

# 50
def que50():#"((()))" → True "(()())" → True "(()" → False ")(" → False     ( (( )) ) is balanced 
    a = "((()))"
    a="".join(a.split())


    # b=len(a)//2
    # return a[:b]==a[b:] if len(a)%2==0 else False
    count=0
    for i in a:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:   # more closing than opening
            return False
    return count == 0   # must end balanced

# print(que50())

# 51
def que51():
    a = "HelloWorldPython"
    res = ""
    for i, ch in enumerate(a):
        if ch.isupper() and i != 0:   # uppercase but not first char
            res += "_" + ch.lower()
        else:
            res += ch.lower()
    return res

# print(que51())

# 52
def que52():
    a = "The quick brown fox jumps"
    return "".join((i for i in "abcdefghijklmnopqrstuvwxyz" if i not in a ))
# print(que52())

# 53
def que53():
    a = "abc"
    b = "123"
    s= "".join((i+j for i,j in zip(a,b)))
    return s + a[len(b):] + b[len(a):]
# print(que53())

# 54
def que54():
    a = "aabbaaghikaba"
    
    def is_palindrome(s):
        return s == s[::-1] and len(s) > 1

    changed = True
    while changed:   # keep removing until no palindromes left
        changed = False
        n = len(a)
        i = 0
        while i < n:
            j = i + 2
            while j <= n:
                if is_palindrome(a[i:j]):
                    a = a[:i] + a[j:]   # remove palindrome
                    changed = True
                    n = len(a)
                    i = -1   # reset scan after change
                    break
                j += 1
            i += 1
    return a

# print(que54())

# 55
def que55():
    a = "hello"
    d={}
    for i in a:
        d[i]=d.get(i,0)+1
    return d
# print(que55())

# 56
def que56():
    s1= "ace"
    s2= "abcde"
    i = j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
        j += 1
    return i == len(s1)
# print(que56())

# 57
def que57():
    a = "hello world"
    seen=set()
    out=""
    for i  in a:
        if i not in  seen:
            seen.add(i)
            out+=i
    return out
# print(que57())

# 58
def que58():
    a = "abcde"
    b = "ace"
    
    return "".join((i for i in a if i not in b))
print(que58())

# 59
# def que59():
    
# print(que59())

# 60
def que60():
    s = "abcabcabc"
    n = len(s)
    
    # Build LPS (Longest Prefix Suffix) array
    lps = [0] * n
    length = 0  # length of the previous longest prefix suffix
    i = 1
    while i < n:
        if s[i] == s[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    # Length of repeating pattern
    pattern_len = n - lps[-1]
    
    if n % pattern_len == 0:
        return s[:pattern_len]
    else:
        return s  # no repeating pattern
# print(que60())

def que61():
    a = "user@example.com"#partition will not give error but still
    return True if "@" and a.partition("@")[-1].endswith(".com") else None
# print(que61())

def que62():
    a = "user@example.com"
    b=a.partition("@") if "@" in a else None 
    return b[-1] if b else None
#print(que62())

def que63():
    a = "aaaa"
    s ="aa"
    return a.count(s)# give non overlaping count


'''Overlapping means a substring can start inside a previous match,
e.g., in "aaaa", "aa" appears 3 times overlapping: positions 0–1, 1–2, 2–3.'''

# print(que63())

def que64():
    a = "hello world from python"
    return a.title()
# print(que64())

def que65():
    a = "Password123"
    if len(a)<8:
        return False

    x=any(c.isupper() for c in a)
    y=any(c.islower() for c in a)
    z=any(c.isdigit() for c in a)
    return x and y and z
# print(que65())

def que66():
    a = "1234567890"
    c=True 
    if len(a)!=10:
        c=False
    #or we can just do if len(a)!=10: return None         as return is final statement other will not run
    return f"({a[:3]}) {a[3:6]}-{a[6:10]}" if c else None
# print(que66())

def que67():
    s = "apple,banana;orange:grape"
    delimiters=",;:"
    for d in delimiters:
        s = s.replace(d, ",")
    return s.split(",")
# print(que67())

def que68():
    strings = ["hello", "world", "goal"]
    common = set(strings[0])
    for s in strings[1:]:
        common &= set(s)
    return "".join(ch for ch in strings[0] if ch in common)

# print(que68())

def que69():
    a = "abc"
    b = "bca"
    return sorted(a)==sorted(b)
#print(que69())

def que70():
    s = "<p>Hello <b>World</b></p>"
    result = ""
    inside_tag = False
    for ch in s:
        if ch == "<":
            inside_tag = True
        elif ch == ">":
            inside_tag = False
        elif not inside_tag:
            result += ch
    return result
# print(que70())

def que71():#use ord() to convert to ascii value
    text = "hello"
    shift = 3
    result = ""
    for ch in text:
        if ch.isalpha():  # shift letters only
            offset = ord('a') if ch.islower() else ord('A')
            result += chr((ord(ch) - offset + shift) % 26 + offset)
        else:
            result += ch  # keep non-letters unchanged
    return result

# print(que71())



def que72():
    text = "khoor"
    shift = 3
    result = ""
    for ch in text:
        if ch.isalpha():
            offset = ord('a') if ch.islower() else ord('A')
            result += chr((ord(ch) - offset - shift) % 26 + offset)
        else:
            result += ch
    return result

# print(que72())


def que73():
    a = "The quick brown fox"
    return min(a.split(), key=len)
# print(que73())

def que74():
    s = "abcdef"
    seen = set()
    for ch in s:
        if ch in seen:
            return False
        seen.add(ch)
    return True

# print(que74())


def que75():
    s1 = "karolin"
    s2 = "kathrin"
    if len(s1) != len(s2):
        return None  # Hamming distance requires equal length
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

# print(que75())


def que76():
    name = "John Doe Smith"
    return "".join(word[0].upper() for word in name.split())

# print(que76())


def que77():
    a ="A man a plan a canal Panama"
    c ="".join(i.lower() for i in a if a.isalnum())
    return c==c[::-1]
# print(que77())

def que78():
    a = 0
    return 0
#print(que78())

def que79():
    a = 0
    return 0
#print(que79())

def que80():
    a = 0
    return 0
#print(que80())

def que81():
    a = 0
    return 0
#print(que81())

def que82():
    a = 0
    return 0
#print(que82())

def que83():
    a = 0
    return 0
#print(que83())

def que84():
    a = 0
    return 0
#print(que84())

def que85():
    a = 0
    return 0
#print(que85())

def que86():
    a = 0
    return 0
#print(que86())

def que87():
    a = 0
    return 0
#print(que87())

def que88():
    a = 0
    return 0
#print(que88())

def que89():
    a = 0
    return 0
#print(que89())

def que90():
    a = 0
    return 0
#print(que90())

