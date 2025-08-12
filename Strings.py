def function_len():
    a="Hello World I am a Proud INDIAN"# string 

    print(len(a)) # prints the lrngth of string length counts space as 1
    print(len(122)) #it will give type error as int is not iterable


def functions_upper():
    a="Hello World I am a PROUD INDIAN , 12345 , @##$$%^%$#" #string example

    b=a.upper() # it will convert all the charachters to CAPITAL letters
    print(b)


def function_lower():
    a="Hello World I am a PROUD INDIAN , 12345 , @##$$%^%$#" #string example

    b=a.lower() # it will convert all the charachters to lowercase letters
    print(b)

def function_capitalize():
    a="Hello World I am a PROUD INDIAN , 12345 , @##$$%^%$#" #string example
    b="a for apple b for batman"
    c="C FOR CAR D FOR DOREAMON"

    print(a.capitalize()) # it will capitalize thjhe first letter only and lower the rest if they are uppercase
    print(b.capitalize())
    print(c.capitalize())

def functions_title():
    a="Hello World I am a PROUD INDIAN , 12345 , @##$$%^%$#" #string example
    b="a for apple b for batman"
    c="C FOR CAR D FOR DOREAMON"

    print(a.title()) # it will capitalize the first letter of each word only and lower the rest if they are uppercase
    print(b.title())
    print(c.title())

def functin_strip():
    a="\t\nHELLO WORLD\n\t"
    b="                  hello world       "
    c="xxxxxxHellowordl0000@@@#$$xxxxxxxxx"
    d="HELLOHELLO"
    e="@@@@@@@!!!????HELLO????!!!@@@@@@@@"
    f="?HELLO?"


    print(a.strip()) #it will by defaut remove the spaces \n \t \r \f \v 
    print(b.strip()) # it will remove the blank spaces
    print(c.strip("x")) # it will remove the "x" from each side 
    print(d.strip("HELLO")) # it will strip "HELLO " from both side making it empty
    print(e.strip("@")) # it will strip @ oUTPUT !!!????HELLO????!!!
    print(e.strip("@!")) # it will strip @!  OUTPUT ????HELLO????
    print(e.strip("@!?")) # it will strip @!? OUTPUT HELLO
    print(f.strip("?")) # it will strip ?

def function_Rstrip():
    a="\t\nHELLO WORLD\n\t"
    b="                  hello world       "
    c="xxxxxxHellowordl0000@@@#$$xxxxxxxxx"
    d="HELLOHELLO"
    e="@@@@@@@!!!????HELLO????!!!@@@@@@@@"
    f="?HELLO?"


    print(a.rstrip()) #it will by defaut remove the spaces \n \t \r \f \v from right  
    print(b.rstrip()) # it will remove the blank spaces from right 
    print(c.rstrip("x")) # it will remove the "x" from each side from right
    print(d.rstrip("HELLO")) # it will strip "HELLO " from both side making it empty from right
    print(e.rstrip("@")) # it will strip @ oUTPUT !!!????HELLO????!!!@@@@@@@ from right
    print(e.rstrip("@!")) # it will strip @!  OUTPUT ????HELLO????@@@@@@ from right
    print(e.rstrip("@!?")) # it will strip @!? OUTPUT HELLO????!!!@@@@@@ from right  
    print(f.rstrip("?")) # it will strip ? from right


def function_Lstrip():
    a="\t\nHELLO WORLD\n\t"
    b="                  hello world       "
    c="xxxxxxHellowordl0000@@@#$$xxxxxxxxx"
    d="HELLOHELLO"
    e="@@@@@@@!!!????HELLO????!!!@@@@@@@@"
    f="?HELLO?"

    print(a.lstrip()) #it will by defaut remove the spaces \n \t \r \f \v from left
    print(b.lstrip()) # it will remove the blank spaces from left
    print(c.lstrip("x")) # it will remove the "x" from each side from left
    print(d.lstrip("HELLO")) # it will strip "HELLO " from both side making it empty from left
    print(e.lstrip("@")) # it will strip @ oUTPUT !!!????HELLO????!!!@@@@@@@ from left
    print(e.lstrip("@!")) # it will strip @!  OUTPUT ????HELLO????@@@@@@@ from left
    print(e.lstrip("@!?")) # it will strip @!? OUTPUT HELLO????!!!@@@@@@@ from left 
    print(f.lstrip("?")) # it will strip ? from left

def function_replace():
    a="TEST TEST TEST MONKEY MONKEY"

    print(a.replace("A","X"))# nothing changed as A not present
    print(a.replace("E","X"))#replace E with X
    print(a.replace("E","X",3)) # it will replace only first 3 occurance of E to 3
    print(a.replace("E")) # TypeError as it requires at least 2 argunments

def function_find():

    a="TEST APPLE TEST CHOCO TEST RUSSIA MONKEY MONKEY"

    print(a.find("X")) # it will check and give the index of first occurance of X -1 means not present
    print(a.find("A")) # it will check A in all atring
    print(a.find("C",4,19)) # it will search C from 4 from 19 index
    print(a.find("T",5))# it will search T from index 5 to end of list
    print(a.find("@"))#not present

def function_rfind():
    a="TEST APPLE TEST CHOCO TEST RUSSIA MONKEY MONKEY"

    print(a.rfind("X")) # it will check and give the index of first occurance of X -1 means not present  RIGHT TO LEFT
    print(a.rfind("A")) # it will check A in all atring  RIGHT TO LEFT
    print(a.rfind("C",4,19)) # it will search C from 4 from 19 index  RIGHT TO LEFT
    print(a.rfind("T",5))# it will search T from index 5 to end of list  RIGHT TO LEFT
    print(a.rfind("@"))#not present searches  RIGHT TO LEFT 



def function_index():
    a="TEST APPLE TEST CHOCO TEST RUSSIA MONKEY MONKEY"

    print(a.index("X")) # it will check and give the index of first occurance of X Raise a ValueError as not present
    print(a.index("A")) # it will check A in all atring
    print(a.index("C",4,19)) # it will search C from 4 from 19 index
    print(a.index("T",5))# it will search T from index 5 to end of list
    print(a.index("@"))#not present Raise a value error


def function_rindex():
    a="TEST APPLE TEST CHOCO TEST RUSSIA MONKEY MONKEY"

    print(a.rindex("X")) # it will check and give the index of first occurance of X Raise a ValueError as not present FROM RIGHT TO LEFT
    print(a.rindex("A")) # it will check A in all atring FROM RIGHT TO LEFT
    print(a.rindex("C",4,19)) # it will search C from 4 from 19 index FROM RIGHT TO LEFT  
    print(a.rindex("T",5))# it will search T from index 5 to end of list FROM RIGHT TO LEFT 
    print(a.rindex("@"))#not present Raise a value error FROM RIGHT TO LEFT

def function_count():
    a="TEST APPLE TEST CHOCO TEST  RUSSIA MONKEY MONKEY"

    print(a.count("A")) #prints the no of time A is present
    print(a.count("TEST")) # prints the no of THE PRESENT
    print(a.count(" "))#prints the ciunt o " " single space present =8
    print(a.count("  "))# prints the count Of "  " double space present =1
    print(a.count("E",5,30))# prints the no of E present in ndex from 5 to 30
    print(a.count("T",5))# prints the count of T from 5 to end of list
    print(a.count("T",5 ,43))# still no error
    print(a.count(2,4,56))# gives type error as foirst argunmentt is string 

def function_split():
    a="TEST APPLE TEST CHOCO TEST  RUSSIA MONKEY MONKEY"

    print(a.split())# splits the string by " "
    print(a.split("T"))# splits the string by T and do not five seperator
    print(a.split("TEST",2))# it splits string on TEST and upto 2 splits as per TEST
    print(a.split("T",4))# it split string upto 4 as on T

def function_rsplit():
    a="TEST APPLE TEST CHOCO TEST  RUSSIA MONKEY MONKEY"

    print(a.rsplit())# splits the string by " " FROM RIGHT TO LEFT
    print(a.rsplit("T"))# splits the string by T and do not five seperator FROM RIGHT TO LEFT
    print(a.rsplit("TEST",2))# it splits string on TEST and upto 2 splits as per TEST FROM RIGHT TO LEFT
    print(a.rsplit("T",4))# it split string upto 4 as on T  FROM RIGHT TO LEFT


def function_join():
    a="TEST APPLE TEST CHOCO TEST  RUSSIA MONKEY MONKEY"
    b=["A","B","c","d"]
    c=("A","B","c","D" ,"E","f" ,"G","H ")

    print(" ".join(b))
    print(":".join(b))
    print("_____".join(b))
    print("-".join(c))
    print("000".join(c))
    print("==".join(a))
    print("".join(c))

    #A B c d
    #A:B:c:d
    #A_____B_____c_____d
    #A-B-c-D-E-f-G-H 
    #A000B000c000D000E000f000G000H 
    #T==E==S==T== ==A==P==P==L==E== ==T==E==S==T== ==C==H==O==C==O== ==T==E==S==T== == ==R==U==S==S==I==A== ==M==O==N==K==E==Y== ==M==O==N==K==E==Y
    #ABcDEfGH 

def function_startswith_endswith():
    a="TEST APPLE TEST CHOCO TEST RUSSIA MONKEY MONKEY"


    print(type(a.startswith("T")))# class bool
    print(type(a.endswith("NKEY")))# class bool
    print((a.startswith("T"))) #true
    print((a.endswith("NKEY")))#true
    print(a.startswith("TEST   "))#false
    print(a.endswith("     MONKEY"))#false



    print(a.startswith())#typeerroe as it take as least one argunment

def funcnction_is():
    a="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b="                             "
    c="5463241412414525101111000"
    d="12334ASDDFDCSDSDSS"
    e="1212 212c sdd   dsd"
    f="dasas sasadssa sas "
    g="Hello World"


    print(a.isupper())#true
    print(a.isdigit())#false
    print(b.isspace())#true
    print(d.isalnum())#true
    print(e.isalnum())#false
    print(g.istitle())#true
    print(f.isalpha())#false
    print(c.isdigit())#true
    print(e.islower())#true


def fuction_zFILL():
    a="ABC"#string
    print(id(a))# gives the id of striing string is immutable
    c="+abc"


    b=a.zfill(7)# len of a is 3 given argunment is 7 so it will fill 4 zero to make it len7
    print(id(b)) # creates a new strng
    print(b)

    print(a.zfill(2))# as 2<len(a) it will return the a 
    print(c.zfill(5))# it preserves the sign - or +  ans = +0abc
    print("--abcc".zfill(24))#ANS -000000000000000000-abcc
    print("+-=332@$$E$@HELLO".zfill(90)) #+0000000000000000000000000000000000000000000000000000000000000000000000000-=332@$$E$@HELLO
    print("A".zfill())#TypeError as it takes at least one argunment

def function_partition():
    a="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b="5463241412414525101111000"
    c="1212 212c sdd   dsd"
    d="one:two:three"

    print(a.partition("I"))#it will split the a at first occurance I and give the seperator as a tuple of strings
    print(b.partition("1"))#it will split the b at first occurance1 and give seperator 
    print(b.partition(1))#typeError as it must me str
    print(b.partition())#type error as it require at least one argunment#print(c.partition(""))# Value Error as it is a empty seperator
    print(c.partition(" "))#('1212', ' ', '212c sdd   dsd')
    print(d.partition(":"))#('one', ':', 'two:three')

def function_rpartition():
    a="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b="5463241412414525101111000"
    c="1212 212c sdd   dsd"
    d="one:two:three"

    print(a.rpartition("I"))#it will split the a at first occurance I and give the seperator as a tuple  of strings FROM RIGHT TO LEFT
    print(b.rpartition("1"))#it will split the b at first occurance1 and give seperator strings FROM RIGHT TO LEFT
    print(b.rpartition(1))#typeError as it must me strings FROM RIGHT TO LEFT
    print(b.rpartition())#type error as it require at least one argunment#print(c.partition(""))# Value Error as it is a empty seperator
    print(c.rpartition(" "))#('1212 212c sdd  ', ' ', 'dsd')
    print(d.rpartition(":"))#('one:two', ':', 'three')












