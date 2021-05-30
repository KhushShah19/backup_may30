
# LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.

l =  ["a", "b", "c", "d", "e", "a", "c", "e"]
l2 = ["a", "b", "c", "h"]
l3 = []

for i in l:
    if i in l2:
        if len(l3) >= len(l2):
            break
        l3 = l3 + [i]

     
 
print(l3)


