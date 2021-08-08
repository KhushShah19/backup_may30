import random

# help(None)
# quit(0)

'''''
# NEW
l, s = None, None
n = [28, 58, 92, 55, 74]
for i in n:
    if l is None:
        l = i

    elif i > l:
        l = i
    print(l)


28 in n
print(28 in n)
'''  # imp (none part)
'''   # yo
m, c, u = {}, {7: 7}, {}  # dic
p = {'anything': 10, 'adding': 4}
d = [1, 3, 5, 2, 3, 5, 4, 6, 5, 4, 3, 2, 3, 4, 3, 2, 4]
for r in d:
    if r not in m:
        m[r] = 1
    else:
        m[r] = m[int(r)] + 1
    # d = [1, 3, 5, 2, 3, 5, 4, 6, 5, 4, 3, 2, 3, 4, 3, 2, 4]
print(m, c, u)

# m = d.get(r, 0)
b = {}
d = [1, 3, 5, 2, 3, 5, 4, 6, 5, 4, 3, 2, 3, 4, 3, 2, 4]
#for n in d:
 #   b = b.get(int(n), 0)

#print(b)
# dictionary.get(keyname, value)
print(p.get("adding", "not again"))
h = c.get(7, "not again")
print(h)


c = dict()
s = ["c", "w", "c", "z", "w"]
for n in s:
    if n not in c:
        c[n] = 1
    else:
        c[n] = c[n] + 1
print(c)
q = {}
for n in s:
    q[n] = q.get(n, 0) + 1
print(c, "did it")

w = {'c': 2, 'w': 2, 'z': 1}
t = {1: 1, 3: 5, 5: 3, 2: 3, 4: 4, 6: 1}
# dictionary.get(key, value)
y = [t.get(3, "three"), w.get(3, "three")]
print(y)
'''  # dic try and error
'''
# new questions
n1, n2, n3 = int(input("n1=")), int(input("n2=")), int(input("n3="))
  
# 7. factors of n1
# 8. whether n2 is prime or not
# 9. all prime until n2
# 10. just greater prime number then n2
'''  # new questions(incomplete)
''' lambda expression or anonymous functions
# lambda is use in place of def fun. when we need a temporary fun. which hardly be used for twice or thrice
# key(name of fun. = var) = lambda var's: (only one express, may or may not use the var's)
# for example: var1 = lambda var1, var2, var3: "it's what we get(return value) with var or not"

x, y, z = lambda: "this is = return value", lambda a, b, c, y: (y**2) + c, lambda m, n: "this var's may not be used"
print(x(), y(2, 3, 4, 5), z(4, 5))'''  # lambda
'''import array
a = [2, 4, 4, 8]
b = a / 2
print(a, b)
'''  # array - incomplete
""" Regular Expressions(RE or regex or regexp) 
it not build in function so we have to import it by "import re" 

it very very power also it code can be writen in one line(short codes)
we can match or extract a particular thing (intelligent form of search)    
it old concept which deals with usages of languages(it's writen in form of language)       
to match something use "re.search()"   (== to find() in str) ( returns F/T and used with 'if' function)
to extract something use "re.findall"  (== to find() and slicing in str) (return what we ask for in LIST)


^   matches the beginning of a line 
$   matches the end of the line 
.   matches any character 
\s  matches any whitespace (can remove blankspaceS whit '\s' follewed by '+')   
\S  matches any non-whitespace character (no blankspac include) 
*   Repeats a character zero or more time (like '.' can be repeated n times by '*' but n will be max) [Asterisk = *]
*?  Repeats a character zero or more time (non greedy) (greedy means try to take the max things)
+   Repeats a character one or more time  (repeats more than zero times- doesn't include empty space for no match)
+?  Repeats a character one or more time (non greedy)  (non greedy means instead of taking many it takes one{min})
[az]    Matches a Single character in the listed set  ([abcd] match letter a,b,c,d ONLY may not be combined)
[^az]   Matches a Single character NOT in the listed set ([^ ] = \S == no blankspac include) 
[a0-9]  the Set of characters that can be include in range ([1-3] = int no. b/w 0 and 4 and [1-3.] include float also)
(   Indication where string Extraction is to START  (matching is different from extracting)
)   Indication where string Extraction is to END  
\   if it's a not a normal character then then it should be follewed by '\' (not nomral == $ types) 

"""  # RE
'''
import re
'import re'

fw = open("ex1", "w")
fw.write(" from iitkhush.shah4123@gmail.com   6/5/2020 2:22 monday \n to   no.reply@gmail.com \n from for.public4123@gmail.com      3/2/2020 1:12 sunday \n to   none.reply@gmail.com \n from for.public4123@gmail.com      2/5/2020 4:05 friday \n to   no.reply@gmail.com ")
print(fw)

fw = open("ex1", "r")
sm1 = fw.read()
# print(sm1)

print("it is")

# print(re.search("to", sm1))  # to match
print(re.findall("^ from.(.*)@gmail.com", sm1))  # to extract
print(re.findall(" to...(.+).", sm1))
print(re.findall("to\s+(\S+)", sm1))
print(re.findall("([0-1]+)", sm1))
print(re.findall("([gmail]+).com", sm1))
print(re.findall(" from.([^ ]*)@gmail.com", sm1))

# print(len(re.findall("(.g...l.com)+?", sm1)))

if re.search("to", sm1):
    print(55)

print("it did")

fw.close()  # not compulsory
'''  # re trial
''' unicode 
each 

print(ord("h"))
m = data.decode()
'''  # unicode incomplete
"""
import smtplib
import config
import time

def send_email(subject, msg):

    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login(config.ADD, config.PASS)
    message = "Subject: {}\n\n{}".format(subject, msg)
    server.sendmail(config.ADD, config.ADD, message)
    server.quit()
    print("done")

config.ADD = "my.personal4123@gmail.com"
config.PASS = "red4123one"

subject = "ghost"
msg = "i did it"

while True:
    send_email(subject, msg)
   # time.sleep(5)

"""  # sending emails
"""
class clg:  # here clg is main class
    def __init__(self, fname, bday):
        self.n = fname

        self.b = bday
        pie = fname.split(" ")
        cake = fname.replace("goa", "zzz")
        cat = fname.capitalize
        self.cake = cake
        self.fn = pie[0]
        self.ln = pie[-1]
        print(pie)


user1 = clg("goa party", "1947")  # user1 is called object (aka instance)
print(user1, user1.n, user1.fn, user1.ln, user1.b, user1.cake)
"""  # Class and subject(aka instance)

# print(*range(1, int(input()) + 1), sep="")
# print(range(1, int(input(">>>")) + 1), sep=".")

# help((strip))


s, sub, c = "ABCDCDCDCDBA", "DC", 0  # sub occurs 3 times in s

kon = [8] * 7
print()
print(" " * 4, kon, "  !" * 4, [2] * 4)

print("..............................................................................................................")
print()
"""
#print(gohere(1, 1))

def totalsteps(j, k):
    print("pairs taken:", j, k)
    if j == 1 and k == 1:
        return 1
    elif j == 1:
        return j
    elif k == 1:
        return k

    return (totalsteps(j-1, k) + totalsteps(j, k-1))


print("number of ways", totalsteps(3, 3))

def newmethod(d,f):
    print("pairs :", d, f)
    if d == 1 or f == 1:
        return 1
    return (newmethod(d - 1, f) + newmethod(d, f - 1))

print("total :" ,newmethod(3,3))






def gfg(cw, wa, ars, na):
    global martix
    print(ars, wa, cw, na)
    if na == 0 or cw == 0:    # (0, [10, 20, 30], [60, 100, 120], 0)
        return 0
    else:
        return max(ars[na - 1] + gfg(cw - wa[na - 1], wa, ars, na - 1), gfg(cw, wa, ars, na - 1))

##print(gfg(ars, wa, cw, na))

# The following implementation assumes that the activities are already sorted according to their finish time

#Prints a maximum set of activities that can be done by a single person, one at a time
# n --> Total number of activities
# s[]--> An array that contains start time of all activities
# f[] --> An array that contains finish time of all activities


def MaxActivities(s, f):
    n = len(f)

    i = 0
    m = 0
    #print(i)

    for j in range(n):
        if s[j] >= f[i]:
            print("the pairs of activities :", i, j)
            m += 1
            i = j
    return ("total number of activities :", m)
# Driver program to test above function


s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 9]
print(MaxActivities(s, f))
"""  # understanding gfg problems

n = 3
list_n = [None] * (n + 1)
print((n, list_n))


def fabs(n, list_n):
    print(list_n[n])
    if n == 0 or n == 1:
        list_n[n] = n

    elif (list_n[n] is None):
        list_n[n] = fabs(n - 1, list_n) + fabs(n - 2, list_n)

    return list_n[n]


# print("fabs last :", fabs(n, list_n))


# A naive Python implementation of LIS problem

""" To make use of recursive calls, this function must return 
two things: 
1) Length of LIS ending with element arr[n-1]. We use 
max_ending_here for this purpose 
2) Overall maximum as the LIS may end with an element 
before arr[n-1] max_ref is used this purpose. 
The value of LIS of full array of size n is stored in 
*max_ref which is our final result """

# global variable to store the maximum
global maximum


def _lis(arr, l):
    # to allow the access of global variable
    global maximum

    # Base Case
    if l == 1:
        return 1

    # maxEndingHere is the length of LIS ending with arr[n-1]
    maxEndingHere = 1

    """Recursively get all LIS ending with arr[0], arr[1]..arr[n-2] 
	IF arr[n-1] is smaller than arr[n-1], and max ending with 
	arr[n-1] needs to be updated, then update it"""
    for i in range(1, l):
        res = _lis(arr, i)
        if arr[i - 1] < arr[l - 1] and res + 1 > maxEndingHere:
            maxEndingHere = res + 1

    # Compare maxEndingHere with overall maximum. And
    # update the overall maximum if needed
    maximum = max(maximum, maxEndingHere)

    return maxEndingHere


def lis(arr):
    global maximum
    l = len(arr)
    # maximum variable holds the result
    maximum = 1

    # The function _lis() stores its result in maximum
    _lis(arr, l)

    return maximum


arr_ = [10, 22, 9, 33, 21, 50, 41, 60]
l = len(arr_)
print("Length of lis is ", lis(arr_))

max_value = 0
array_01 = [4, 22, 12, 9, 46, 38, 19, 27, 31]

