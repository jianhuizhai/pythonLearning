#! /usr/bin/python3

linecomment ='=========================================================================='

'''
merging list
'''
ind = [0,1,2,3,4]
color = ["red", "green", "blue", "alpha"]
a = list(zip(color,ind)) # gives [('red', 0), ('green', 1),('blue', 2), ('alpha', 3)]
print(linecomment)
print( a )

'''
# list comprehension
[<expr> for <variable> in <list>]
or more generally:
[<expr> for <variable> in <list> if <condition>]
'''
L = [2, 3, 10, 1, 5]
L2 = [x*2 for x in L] # [4, 6, 20, 2, 10]
L3 = [x*2 for x in L if 4 < x <= 10] # [20, 10]

print( linecomment )
print( L )
print( L2 )
print( L3 )

M = [[1,2,3],[4,5,6]]
flat = [M[i][j] for i in range(2) for j in range(3)] # returns [1, 2, 3, 4, 5, 6]

print( linecomment )
print( M )
print( flat )

# test x is list or not
isinstance(x, list) # True