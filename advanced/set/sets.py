#! /usr/bin/python3

'''
Sets are containers that share properties and operations with sets in mathematics.
'''
linecomment = '======================================================================'

A = {1,2,3,4}
B = {5}
C = A.union(B)         # returns set([1,2,3,4,5])
D = A.intersection(C)  # returns set([1,2,3,4])
E = C.difference(A)    # returns set([5])
5 in C                 # returns True

# Sets contain an element only once, corresponding to the aforementioned definition:
A = {1,2,3,3,3}
B = {1,2,3}
A == B # returns True

# And a set is unordered; that is, the order of the elements in the set is not defined:
A = {1,2,3}
B = {1,3,2}
A == B # returns True

# Also, sets can be compared using the methods issubset and issuperset :
{2,4}.issubset({1,2,3,4,5}) # returns True
{1,2,3,4,5}.issuperset({2,4}) # returns True

'''
Empty set
An empty set is defined in Python by empty_set=set([]) and not by {} ,
which would define an empty dictionary!
'''
empty_set=set([])
print( linecomment )
print( empty_set )