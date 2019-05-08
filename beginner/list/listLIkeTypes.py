name = 'Zophie'
for i in name:
    print('* * * ' + i + ' * * *')

name = 'Zophie a cat'
# name[7] = "t"  # this is wrong because a string is immutable: It cannot be changed.
newName = name[0:7] + 'the' + name[8:12]
print( name )
print( newName )

# The Tuple Data Type
eggs = ('hello', 42, 0.5)
print( eggs[0] )
print( eggs[1:3] )
print( len(eggs) )

'''
eggs = ('hello', 42, 0.5)
eggs[1] = 99    # tuple does not immutable. This property is as same as string.
print( eggs )
'''
print( type(('hello',)) ) # comma is to make python notice it is a tuple when there is only one item in tuple
print( type(('hello'))  )

# You can use tuples to convey to anyone reading your code that you
# don’t intend for that sequence of values to change. If you need an ordered
# sequence of values that never changes, use a tuple.

# Converting Types with the list() and tuple() Functions
print( tuple(['cat', 'dog', 5]) )
print( list(('cat', 'dog', 5))  )
print( list('hello')            )

#==============================================================================
#                               reference
#==============================================================================
spam = 42
cheese = spam
spam = 100
print( spam )
print( cheese )

# spam and cheese point to the same reference
spam = [0, 1, 2, 3, 4, 5]
print( type(spam) )
cheese = spam           # copy the list reference in spam to cheese
print( cheese )
cheese[1] = 'Hello!'  # change the reference
print( spam )
print( cheese )

import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42
print( spam )
print( cheese )

spam = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(spam)
cheese[1] = 42
print( spam )
print( cheese )
# 当list中不包含子list时，copy和deepcopy效果一样。当list中包含子list时，如果不改变子list那么copy和deepcopy效果一样
# 当list中包含子list时，如果改变子list那么a = copy.copy(b)改变a会改变b的值；deepcopy则不会改变，因为a和b完全独立。