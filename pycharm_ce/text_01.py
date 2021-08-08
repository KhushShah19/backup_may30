
'''
1. reserved words - are words which are by default in computer. we can't used them as variable names/identity.
2. variable - they are something which is not fix, not constant. name of variable Doesn't matter
  (example goOD, _gOO_D, GO234od            30bad, #bad, ba.d           Different, different, diffERent, differENT)
3. function - to perform any task we need function, they guild the python to do a task as the functions are reserved.
4. constant - something which don't change it's value, it's fix. they Become reserved words
5. operator - we can perform operations using operator (like =, +, *, **, ect)
6. expression - a sentence with operators
6. parameter - type of variable assign by user
7. syntax - basically the line
8. conditional - which has some condition, it can be function,syntax, ect.
9. input - the things given by user
10. output - the result we get from python
11. print - python can see and read our code but if we want to see that then we must use print.
12. indent - is the extra space after the function to tell these things are also a part of function
13. de-indent - get out of indent
14. string(str) - just a group of letters and numbers in [ "." OR '.' ]
15. integer(int) - all normal integers (like 2, 0, -2)
16. float(float) - int with decimal (like 2.0, 0.0, -2.0)
    we can inter convert int and float using build-in functions int(var) and float(var), usage - var_01 = int(var_02)
17. parenthesis() - bracket, all kind of brackets
18. comments(#) - python simply ignores it so write whatever u like ( # x = 5 is not considered by python)
19. argument - the input we put into the function in parenthesis. the thing in bracket in any functions.
20. return - very similar to print. It gives(return) the value we write their.
22. break - it ends the current loop and jumps out of it ( leave the loop and do things which immediately follow loop )  it's like get out NOW!!
23. continue - to continue it ( it goes up start again )
24. pass - it's a null operation(when it is executed, nothing happens) it's useful as a placeholder when a statement is required syntactically,but no code needs to be executed
    for example:- def fun(arg): pass  # a function that does nothing (yet)
24. for i (iterator) in X (iterable) -> here iterable = which can be loop through
25. iteration variables - which change each time as they go through the loop ( iteration- repetition of process )
26. import - some functions can't be use without importing them
27. input - we ask user to give some data [usage - ip = input(" >>>")] , it can't read further until data give(by user), it's always string
28. del - delete anything which we created , usage - del variable_01, variable_02 
29. abs - it's makes value to positive one, similar to |mod| in maths

# we don't directly write the code in python and end with error instead we write them in file and tell python to run it
# the code is like instruction manual where we go line by line, we can skip, repeat, remember it same goes with python

# ## Basic Maths ## #
a = -10
a = (a + 60)/5*10 - 11  # follow bodmas(== pemdas in computers and here p for parentheses which means brackets)
b = abs(a) = abs(-10) => abs makes negative value to positive, similar to |mod|

# addition(+), subtraction(-), multiplication(*), division(/), power(**), [reminder(%) - it can be int OR float], [floor(//) - (result is the quotient and not the reminder)]
# operations can be done b/w int and int OR str and str BUT not b/w int and str
# a lesser/smaller to b(a < b), greater(a > b), equal(a == b), lesser or equal(a <= b), greater or equal(a >= b), not equal(a != b) NOTE: (=<, => is not gonna work)
# comparison operators return true or false that it. they just compare .
# REMEMBER: "=" is use for assigning and "==" means equal to.( a = 1 and a == b is two different thing )
'''  # basics(terms and understanding of it with some operations) for revision

""""
a = 1  # as 'a' is variable chosen by ous, we can change it any time we want to
print(type(a))  # knowing the TYPE is every important (sometimes we may use str instead of int)
print()  # without writing print it won't show and this can be use to add spaces in result(what we see)

if a > 555:
    print("colon(:) followed by indent is the basic form to run ANY function")
    print("indent is importance for being a part of functions")
    print("as 'a' is reserved word, it won't run until the function is true or the condition is satisfies")
    print(66, 88, 99)  # comma (,) adds the blank space by default

    if a == 6000:
        print("*** function in function is called nesting ***")
        print("it's false so its never gonna read it, python will skip or ignores it")
        if a > 7:
            pass  # null operation - when it's executed, nothing happens (a function that does nothing (yet))
        else:  # it's two way decision so either 'if' OR 'else' function will run and one of them is sure to run.
            print("else makes it two way decision")
            print("it's not compulsory to use it, 'if' function is false then else(no other chose)")
            print("it choose ONLY one not both, like this or that, you have only TWO options")

            print("this is also possible" if a > 7 else "not again")  # simpler way to use 'if' AND 'else' function
    elif a > 10:  # instead of using many if for same function we use elif (which is followed by if)
        print("elif is basically the combo of else and if, it's Always followed by 'if'")  # doesn't matter if you use else or not
        print("if, elif, else are conditional and ONLY one of them runs NOT more than one")
        print("you can use elif n number of times but remember it goes in order and once find 'True' ignore the rest")
        print("if you ignore 'Else' then loop may choose either one or None")
"""""  # all about if, elif, else function

"""
# what if you are not sure for some output, we can do try and error method(try and except method in python)
p = "for example"
try:
    q = int(p) # trying to convert letter string to integer which is not allowed
    # if 'try' function can't run, then it goes to 'except' function and runs it
    # either 'try' OR 'except' will run, this or that, you have ONLY two options
    # it's similar to if else function, different is instead of finding true/false it see whether it can be run or not
except:
    q = str(p)    
"""  # short intro about try and except method
"""
b = 2
while b > 1000:  # runs ONLY if it's TRUE
    # it's called While Loop as it loops until it gets a false
    # working: check the condition(if true) run the code then go back to top to check the condition again and continue
    # sometimes you might not know how many times it will loop(run) through it (maybe finite or infinite)
    # it like 'if' function but as long as it gets true it continues
    if b > 555:
        pass  # it's a null operation(when it is executed, nothing happens), a function that does nothing (yet)
    elif b > 444:
        break  # break is to stop and get out of ANY function
    elif b > 777:
        continue  # continue is to start again ANY function

    for i in range(b):  # as it loop(runs) to a finite value(which is given by coder) it's called FOR Loop
        # for i(iterator) in X(iterable) -> here iterable = which can be loop through(like list,dic,tuple,array)
        # iteration variables - which change each time as they go through the loop(iteration - repetition of process)
        # working: check the condition run the code then go back to top to check the condition again and continue
        # for example: for i in range(3) == i going through each value of [0, 1, 2] == i will 0, 1 and 2
        # range(n, m) = starting from n and ending at (m-1) => [n, n+1,......, m-1]......type => range class
        # [range(n, m)] = a list from n to (m-1) terms .......type => list
        pass
"""  # while and for loop

# ......................................................................................................................


def foot(lol):  # def - define the function, can call it whenever needed
        if lol == "joke":
            print("joke")
        elif lol == "no no":
            return "ha ha ha ha"
        else:
            print("ha ha")
        # it's a default function which is saved and can be run anytime
# parentheses are the brackets ( )

foot('lol')
print(foot("no no"), "yes")
u = max(1, 11, 111, 100)  # biggest among all
print(u)


def lose(m, n, o):
    win = m**n**o
    return win


last = lose(2, 4, 3)
print(last)


''' lambda expression or anonymous functions
# lambda is use in place of def fun. when we need a temporary fun. which hardly be used for twice or thrice
# key(name of fun. = var) = lambda var's: (only one express, may or may not use the var's)
# for example: var1 = lambda var1, var2, var3: "it's what we get(return value) with var or not"

x, y, z = lambda: "this is = return value", lambda a, b, c, y: (y**2) + c, lambda m, n: "this var's may not be used"
print(x(), y(2, 3, 4, 5), z(4, 5))'''

A = 80
print(type(A))
while A > 5:
    print(A)
    A = A - 10
    if A == 60:
        A = A - 20
    elif A == 20:
        break
    else:
        continue
    # continue is to start again the function and break is to get out of it
print("definite loop")
S = [6, 48, 12, 36, 24, 18]
Q, W, E, Z, X = -1, 0, None, 0, 0
print(type(E))
# the None is neither int nor str. basically its Nothing
for z in S:
    W = W + z  # to find total
    Z = Z + 1
    if z > X:  # to find largest
        X = z
    if E is None:  # to find smallest
        # is = Equal To and " = " = Similar To. Their is so much of difference in is and =
        E = z
    elif z < E:
        E = z

    print(Z, z, E, X, W, W/z)
# for loop and while loop is similar
# all the for loop can be converted to while loop and vise versa is not true
# for loop work better with lists
K = [[0 for p in range(4)] for q in range(5)]
# print(K) => [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# In_General = [["vai_01" for i in range(inward_int)] for j in range(outward_int)]    (vai_01 can be int or str)
# In_General = [["vai_01", "vai_01", "vai_01", .... inward], [....inward], outward (number of inwards) ]

# we can know what things can be done with dir()

# don't forget about Class C:

'''STRING(str) is a sequence of Characters... str are represented in " " OR ' ' ( quotes ).
 Integer(int) can also be str if they are in Quotes... we can inter convert str and int.
 we can ONLY add strings NOT str + int...input(we get from user) is Always str.
 as string is character it has a specific value given to each of its character called index. 
 index of a str starts with ZERO... Length of str can be know by func len().   
 if we know the index we can easily change the str as they are mutable.        
 we add, break it (its called Slicing),                                        
 find(), str.upper, str.lower, str.capitalize, str.strip([]), str.replace("." , "."), \n   
 str.l strip(try), str.r strip(try), str.start with(try), str.split()                   
 they are immutable ( which means not changeable)...'''

print("to make some space use ' '*6", " "*6, "enjoy your space")
n = 6
for i in range(1, n+1):
    print(' '*(n-i)+'#'*(i), " "*(i) + "again!!"*i + "use the space")

gold = "Monty\nPython"  # subsets of string can be taken using [] and [:] (slice operator)
print(gold[4:8], gold[8:20], gold[:])
# the blank space is always consider in index

print(dir(gold))
print(len(dir(gold)))
print(range(len(dir(gold))))
print(list(range(len(dir(gold)))))
print(list(range(206)))
print(range(4), list(range(4)))  # range has 4 element including 0

del gold  # can delete all the assign values
for i in range(4):
    i = i**2
    print(i)


# "in" is a function which returns T/F
# open(..., r)......... r == read , w == writing

# help("zip")
# quit() - to just end the code, it won't read beyond it

''' all about FILE 
 open(".") - which file we are going to use 
 var1 = open("filename", mode) - var1 is to manipulate the file ( var is just a variable ) 
 filename is always string (".")
 mode = r, w - r = read and w = write , if u leave it its by default going to read it
 new line - \n ( its one character) - to end any line and skip to next one 
 a print statement adds a new line by default 
 a file is sequence of string which is an ordered set 
 we can take the help of for loop to go thought it 
 var2 = var1.read() - it make all the lines into one single line ( into a single string ) '''

# Algorithms - a set of rules or step used to solve the problem
# Data Structures - a particular way of organizing data in computer
# lists, dictionaries and tuples are the basic data structures
# these are the collection of one or  more than one variable


''' all about [ LISTS ]  
list is a collection of string ([23, red, [4, blue] - it's has only 3 elements)
list also have index which is specified in square brackets. ( var[int] )
as we know the index always starts with zero 
list is mutable ( which means changeable or item assignment )
to change a string ( which is immutable ) in list is to make a new list ( int can be changed ) 
len(var) - length counts the no. of element in list ( blank space also counts )
if we want list of any range then list(range(integer))
the list is mostly use in "for" loop 
add, slicing( var[int_1: int_2]), append, length(len), count, extend, index, insert, pop, remove, reverse, sort.'''

# testing powers of LISTS...[sometimes print and operator Together can result in None, do them separately]
b, c, n, abc = [12, 24, 8, 4, 20], [24, 12, 18, 6, 30], [], "let's make it better [uk]"
n.extend(b)  # adds a new list to existing list in order
a = b + c    # adds lists to new list, $| list can have two same value( 12, 12) |$
ABC = abc.split()  # Split - breaks the string and produce a New list (blank space is removed from str )
ab = abc.split('e')  # split can be done w.r.t anything
print("ABC =", ABC, "ab =", ab, ".", ABC[3])
print("len(ABC):", len(ABC))  # len - counts no. of element in [.] (blank space also counts)
print("a =", a, ", b =", b, ", c =", c)
print("a[1:20] =", a[1:20], "b[:] =", b[:])  # slicing operator(up to but not included)- cut the list
dir(b), print("thing can be done with list are", dir(b))
a[0], a[1] = 28, 36  # ONLY int can be changed, for str to change we have to make new list
c.append(48), c.append(42)  # append - add value at the End in List, one value one time
print("a =", a, ", b =", b, ", c =", c)
print("'in' operator:", 12 in b, "or", 12 not in b)  # "in" tell T/F (whether if value is in or not)
(a.sort(reverse=False), b.sort(reverse=0))   # 0 = False, (int - 0) = True,,,False is small to big and True is big small
a.reverse(), c.remove(12,)  # reverse - can be done with sort also, remove - one value at once
print("len(a):", len(a), ", max(a):", max(a), ", min(a):", min(a), ", sum(a):", sum(a), ", avg[sum(a)/len(a)]:", sum(a)/len(a))
print("a =", a, ", b =", b, ", c =", c)
print("pop:", b.pop(0),)  # pop(index) - brings out the value we want
print("count:", a.count(24))  # count(int) - no. of times that int have occurred
print("index:", b.index(24))  # index(int) - to know the index of any element
h = list(range(4, 9))
g = h.__reversed__()   # to reverse
print("h =", h, "and reverse of h = list(g) =", list(g))
x = "a string(str)"
y = list(x)   # to make it a list by each letter, y = ['a', ' ', 's', 't', 'r', 'i', 'n', 'g', '(', 's', 't', 'r', ')']
print(x, "."*4, "convert to list -", y)
z = "".join(y)  # to make it srting again
list01 = [42, 43, 44, 45, 46, 47, 48, 49, 50]
for index, value in enumerate(list01):  # enumerate - read value and index together
    if value == index*7:
        print("can read the value and index of value in list simultaneously by using 'enumerate'")
print("list convert to", str(z), "by "".join(str)")
n = 6
for i in range(1, n+1):
    print(i, end="   .")  # 'end' is way to separate elements of lists

v, p = "FiitJEE", ["s sss ssssssss", "d", "f"]
print(v.swapcase(), v.replace("", "-"), " ".join(p)) # v.replace("", "-") which is FiitJEE -> -F-i-i-t-J-E-E-
'''
list2str = ["way to", "convert", "list to str", "4123 4123"]
print(" ".join(list2str))'''  # way to convert list to str

# false class return is finally none if for lambda continue true def from while nonlocal and del global
# not with as elif try or yield assert else import pass break except in raise

# finally lambda nonlocal del global yield assert pass raise

import random  # importing functions
R = random.randint(1, 100000000)  # randint = randomness in int ( range and both side include )
dice = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 0: "six"}  # type = dictionary(dict)
print(R, R % 6, dice[R % 6])
print(type(dice))


''' all about dictionaries {key: value}
denoted by {} and are similar to list
they say it's the most powerful data collection and allows to do fast data like operation 
they don't have any order but have a index(= key) to call on 
they are immutable (can't be changed) 
GET (dic.get(key, "this if key not present") - it's to get any value using the key in dic 
    get can also be use instead of "if else" function in dic
 we can't have two e's (as e, e in list)
'''

# d
a, c = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 0: "six"}, {}
c["GET"] = "= get"  # dic[key] = value -> we chose a key and give it a value
c["'for' loop takes Only key word"] = 2
c["'for' loop takes Only key word"] = c["'for' loop takes Only key word"] - 2
a[0] = "zero"
print(a, c)
print("'in' operator:", 12 in a, "or", 12 not in a)  # "in" tell T/F (whether if value is in or not)
# (dic.get(key, "This IF key not present") - it's to get any value using the key in dic
print(c.get("GET", 0), a.get("adding", "is easy one"))
b, d = {}, [1, 3, 5, 2, 3, 5, 4, 6, 5, 4, 3, 2, 3, 4, 3, 2, 4]
for n in d:
    b[n] = b.get(n, 0) + 1  # get can also be use instead of "if else" function in dic
    # print("b =", b)
print("b =", b)
for keys in c:  # takes ONLY key word NOT value
    print(keys, c[keys])
for k, v in c.items():  # can take 2 iteration, first one goes for keys and second for values
    print(k, v)  # imp..................................
N, n = None, None
for bigword, bigcount in b.items():
    if n is None or bigcount >= n:
        N = bigword
        n = bigcount
print(N, n)
# relation with list
print(list(c), c.keys, c.values(), c.items)
a, c = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 0: "six"}, []
for k, v in a.items():
    c.append((v, k))  # to inverse the dic and make into list
print("c =", c)

''' TUPLES ()
they are bit similar to list (have index and similar functions of that of list)
can't modify them (immutable, unchangeable) (str and tuple both object doesn't support item assignment)
they more efficient and simple then lists (tuple are prefer when making "temporary variables")

'''
# t
a, b = (12, 24, 8, 4, 20, 24, 12, 18, 6, 30), ("let's", 'make', 'it', 'better', '(uk)')
print(a[3], max(a), )
u = max(1, 11, 111, 100)  # biggest among all
print(u)

for c in b:
    break

# as tuples are immutable, you CAN'T sort, append, reverse, extend, pop, remove, insert them ( Only count, index works)
print(sorted(a))  # tuple Can't be sort BUT can be sort and Becomes List
# print(dir(tuple()))
(x, y, z) = (-1, 0, +1)
print((0, 999, 100000) < (1, 0,), ("z" > "a"), ("z") > ("a") > ("Z"))  # we can compare str and tuple
# if the FIRST item is same, Then ONLY it goes for second term. (for All comparison operators) (z > a > Z)
print("copy")


# convert l to d , d to t, t to l, .....
