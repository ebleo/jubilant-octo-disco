# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 16:14:33 2016

@author: danielle.leong
"""

string = 'Banana Joe ZZ'
asc = []
caes = []

maxLow = ord('z')
minLow = ord('a')
minUp = ord('A')
maxUp = ord('Z')
# ord type is int

# this could all be one loop
for c in range(len(string)):
    x = string[c]
    ascNum = ord(x)
    asc.append(ascNum)

for c in range(len(asc)):
    asci = asc[c]
    if minLow <= asci <= maxLow:
        cNum = asci - minLow + 1
    elif minUp <= asci <= maxUp:
        cNum = asci - minUp + 1
    else:
        cNum = 0
    caes.append(cNum)

encode = []
codeLen = len(caes)

"""
must use append since it cannot assign to non-existing index--cannot assign
to empty indices
"""
#for c in range(codeLen):
#    print("the loop is on: ", c)
#    if (minLow <= asc[c] <= maxLow) or (minUp <= asc[c] <= maxUp):
#        print("got to if")
#        encode[counter] = caes[c]
#        counter = counter + 1
#        encode[counter] = '-'
#        counter = counter + 1
#    else:
#        print("else")
#        encode[counter] = ' '
#        counter = counter + 1

for c in range(codeLen):
    print(c, "\tthe is run NUMBER:\t", codeLen)
    print(caes[c])
    if (minLow <= asc[c] <= maxLow) or (minUp <= asc[c] <= maxUp):
       encode.append(caes[c])
       print(encode)
       if c < (codeLen-1): # will not print '-' after last letter
           encode.append('-')
           print(encode)
    elif caes[c] == 0

       
for c in range(len(encode)):
    print(encode[c], end = " ")
