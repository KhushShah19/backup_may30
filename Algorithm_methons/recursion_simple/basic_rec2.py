
# Q5 Is string Palindrone

from ast import IsNot
from curses.ascii import isupper


string_Palindrone = 'xxaxx'

def is_string_Palindrone(str_palind, full_string):

    if len(str_palind) in [1, 0]:
        return full_string

    if str_palind[0] != str_palind[len(str_palind)-1]:
        return 'Not Palindrone'

    return  is_string_Palindrone(str_palind[1:-1], full_string)

print('Palindrone :', is_string_Palindrone(string_Palindrone, string_Palindrone))

# ............................................................................

# Q6 reserve the string

resv_string = 'jihgfedcba'

def reserve_string(res_string):

    if len(res_string) in [0, 1]:
        return res_string

    return res_string[len(res_string)-1] + reserve_string(res_string[:-1])

print('rese_string :', reserve_string(resv_string))

# ............................................................................
# Q7 making giving list to simplified list

lwith_value, l_without_value = [[1], [2, [3]], [4, [5, [6, 7], 8], 9]], []

def make_list_with_value(wvalues):

    for i in wvalues:
        
        if type(i) is list:
            make_list_with_value(i)
        else:
            l_without_value.append(i)

    return l_without_value

print("simplified list :", make_list_with_value(lwith_value))


# ................................................................
# Q8 lowercase to uppercase

smaller_list, bigger_list = ['FOOD', 'Can', 'bE', 'eaTen'], []

def smallertobigger(sblist):

    if len(sblist) == 0:
        return bigger_list

    bigger_list.append(sblist[0].upper())
    smallertobigger(sblist[1:])

    return bigger_list

print("smaller to bigger :",smallertobigger(smaller_list))

# ..................................................................
# Q10 (since 9 was wasy)

given_dic = {"z": 2,
  "b": {"y": 4, "zxc": {"foo": 3, "xcv": {"x": 8}}},
  "c": {"poo": {"w": 16, "rat": 5}, "qun": 'ball', "ruo": 7},
  "d": {"nno": {"v": 32}, "mum": 'car'}}

evensum = []

def dic_inside(insidedic): 
    # when dealing with dict(key, value) pair be carefull 
    # just putting key instance of value can create lots of confusion

    for i in insidedic:
        #print(i)
        #print(i, insidedic[i], type(insidedic[i]))
        if type(insidedic[i]) == dict:
            dic_inside(insidedic[i])

        elif isinstance(insidedic[i], int):
            if ( insidedic[i] % 2 ) == 0:
                #print(i, insidedic[i], type(insidedic[i]))
                evensum.append(insidedic[i])
                #print(evensum)

    return (evensum)

#print(given_dic)
print("sun of even no. in dict :", sum(dic_inside(given_dic)), [dic_inside(given_dic)])
# got the required answer but some things unclear here


""" Simplified code

def evenSum(obj, sum=0):
    for k in obj.values():
        if type(k) == int and k%2 ==0:
            sum += k
        elif isinstance(k, dict):
            sum += evenSum(k, sum=0)
    return sum
    
"""

# with this i hope i can deal with recursion problems in future
