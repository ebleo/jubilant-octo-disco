# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 16:14:33 2016

@author: danielle.leong
"""

string = 'Banana Joe Z'
asc = []
caes = []
offs = 3

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

# offsetting code
caesOff = []

for c in range(len(caes)):
    new = caes[c] + offs
    caesOff.append(new)
    if caesOff[c] > 26:
        caesOff[c] = caesOff[c] - 26

encode = []
codeLen = len(caes)

"""
must use append since it cannot assign to non-existing index--cannot assign
to empty indices
"""

# print things out nicely
for c in range(codeLen):
    if (minLow <= asc[c] <= maxLow) or (minUp <= asc[c] <= maxUp):
       encode.append(caesOff[c])
       if c < (codeLen-1): # will not print '-' after last letter
           encode.append('-')
    else:
       encode.append(' ')
       remDash = encode.index(' ') - 1
       del encode[remDash]


for c in range(len(encode)):
    print(encode[c], end = " ")
