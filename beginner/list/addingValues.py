spam = ['cat', 'dog', 'bat']
spam.append('moose')
print(spam)

spam.insert(1, 'chicken')
print( spam )

# Methods belong to a single data type. The append() and insert() ­methods
# are list methods and can be called only on list values, not on other values
# such as strings or integers.

eggs = 'hello'
eggs.append('world')
print( eggs )

bacon = 42
bacon.insert(1, 'world')
print( bacon )