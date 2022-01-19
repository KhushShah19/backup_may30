# for easy storing and accessing of data, pyhton have many ways
# Data Structures are the ways to do them
# DS like Lists, Tuple, Dictionary(Dict), Sets (LTDS) and many more

from typing import List


LTDS = 10

if LTDS == 10: # Lists
    #print(help(list))
    LIST = 30
    if LIST == 10: # basic intro about lists [] 
        # list Must be iterable(can loop thought) and are mutable(can be changed)
        l1 = [] # it's call empty list 
        l1 = [1, 4, 3, "6", "gfg", 9.88, (3, 8, 3.8), True] # allows all data type
        print(l1)
        # each element in list has a loction given by Index (starting from 0)
        print(l1[0], l1[4], l1[1:6], l1[-1]) # index is using for calling or slicing
        print(len(l1)) # len = to find the lenght of the list
        print(list(range(4, 8))) # list created from 4 to 7 == [4, 5, 6, 7]

    if LIST == 20: # Methods in list

        l2 = [2, 3, 5, 7, 4, 2, 3] # creating a list
        # append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort, 
        l2.append(9) # to add value in end of list(one at a time)
        l2.clear() # remove all items from lists
        l3 = l2.copy() # copy the whole list
        l3 = [3, 4, 3, 1, 9, 7, 2] 
        l2.count(2) # counts number of occurrences of any one value(here 2)
        l2.extend(l3) # add all elements from another iterable to itself
        l2[0] = 5 # using index to call specific loction
        l2.insert(0, 11) # insert(index, value) = add value to index given
        l2.pop(2) # remove and return the value at given index (default last)
        l2.remove(11) # remove First occurrence of value, error if value not present
        l2.reverse() # reverse the list
        l2.sort() # sort the list in increaing order(can change order)

        print(help(list))

    if LIST == 30:
        # _add_, _contains_, _delitem_
        l3 = [3, 4, 3, 1, 9, 7, 2]
        l3 = l3.__add__(List[8, 3])
        print(l3)



















