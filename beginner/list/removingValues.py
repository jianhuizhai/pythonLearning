'''
The remove() method is good when you
know the value you want to remove from the list.
'''

spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
print( spam )

'''
spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('chicken')
'''

# If the value appears multiple times in the list, only the first instance of
# the value will be removed. Enter the following into the interactive shell:

spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
print( spam )
spam.remove('cat')
print( spam )