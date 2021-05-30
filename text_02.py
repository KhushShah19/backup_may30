b = 5
while b >= 0:  # runs ONLY if it's TRUE (we can't tell how many times will it run)
    print(b)
    b = b - 15
    # it runs the loop until it gets a false, this makes it a loop
    # it like if but as long as it gets true it continues(go to top and check the condition again)
    if b < 5:
        break  # continue - to continue it ( it goes up start again )
    print("it's gonna BREAK the loop soon.", "It's a break function")
print("indent gone function gone")



c, d = "c", "d"

try:  # if u r not sure of something then go for try and except method
    print(c+d)  # they both r str so we can Only add them
except:
    print(d)

''' know about INPUT 
# l = input(">>>")  # the parameters in input functions is called prompt
# print("this is input function and input is", l)  # outcome of input is ALWAYS a str

try:
    print(20 + l)
except:
    print("input is always str")...'''

p, q, r, s = 123 % 0.1, 123 % 10, 123 % 100, 123 % 1000
print(p, q, r, s)


def fun(today):  # def - define the function, can call it whenever needed
    if today in range(101, 10001):
        return "ends the function and jump to next one", "the print below it won't work", "smart"
        #print("yes it's", r, x)
        #return "this is return function. It's really helpful"  # it's in ()
    elif today in range(1, 101):
        print("in range", x)
        return "It works as print"
    else:
        print("missing")


''' lambda expression or anonymous functions
# lambda is use in place of def fun. when we need a temporary fun. which hardly be used for twice or thrice
# key(name of fun. = var) = lambda var's: (only one express, may or may not use the var's)
# for example: var1 = lambda var1, var2, var3: "it's what we get(return value) with var or not"

x, y, z = lambda: "this is = return value", lambda a, b, c, y: (y**2) + c, lambda m, n: "this var's may not be used"
print(x(), y(2, 3, 4, 5), z(4, 5))'''

x = 84
if x in range(1, 101):

    print("yeah")

else:
    print("what next ?")

''' # ## testing powers of LISTS...[sometimes print and operator Together can result in None, do them separately]
b, c, n = [12, 24, 8, 4, 20], [24, 12, 18, 6, 30], []
n.extend(b)  # adds a new list to existing list in order
a = b + c    # adds lists to new list, $| list can have two same value( 12, 12) |$
print(a, b, c)
print(len(a), " ", a[1:20], b[:])  # slicing operator ( up to but not including ) and length(len) = no. of elements
dir(b)
print("thing can be done with list are", dir(b))
a[0], a[1] = 28, 36  # ONLY int can be changed, for str to change we have to make new list
c.append(48), c.append(42)  # can append(add value at the End in List)
print(a, b, c)
print("in operator:", 12 in b, "or", 9 in b)  # "in" tell T/F (whether if value is in list or not)
(a.sort(reverse=False), b.sort(reverse=0))   # 0 = False, (int - 0) = True,,,False is small to big and True is big small
a.reverse(), c.remove(12,)  # reverse - can be done with sort also, remove - one value at once
print(a, b, c)
print("pop:", b.pop(0),)  # pop(index) - brings out the value we want
print("count:", a.count(24))  # count(int) - no. of times that int have occurred
print("index:", b.index(24))  # index(int) - to know the index of any element...'''


''' practice input
# l = input(">>>")  # the parameters in input functions is called prompt
# print("this is input function and input is", l)  # outcome of input is ALWAYS a str

try:
    print(20 + l)
except:
    print("input is always str")
'''




"""
from iitkhush.shah4123@gmail.com   6/5/2020 2:22 monday 
to   no.reply@gmail.com
form for.public4123@gmail.com      3/2/2020 1:12 sunday
to   none.reply@gmail.com
form for.public4123@gmail.com      2/5/2020 4:05 friday
to   no.reply@gmail.com
form iitkhsuh.shah4123@gmail.com   1/1/2020 1:11 sunday
to   none.reply@gmail.com

"""



"""
import re


fw = open("ex1", "w")
fw.write(" from iitkhush.shah4123@gmail.com   6/5/2020 2:22 monday \n to   no.reply@gmail.com \n form for.public4123@gmail.com      3/2/2020 1:12 sunday \n to   none.reply@gmail.com \n form for.public4123@gmail.com      2/5/2020 4:05 friday \n to   no.reply@gmail.com")

print(fw)

fw = open("ex1", "r")
sm1 = fw.read()
print(sm1)

fw.close()

print("it is")
for i in sm1:
    print(44)
"""
# alphabet = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25}
 

 
