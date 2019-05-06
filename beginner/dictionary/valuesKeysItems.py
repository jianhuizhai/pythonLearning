spam = {'color': 'red', 'age': 42}
for i in spam.values():
    print(i)

for j in spam.keys():
    print(j)
    
for k in spam.items():
    print(k)
    
spam.keys()
list(spam.keys())  # change dictionary keys to lists

spam = {'color': 'red', 'age': 42}
for k, v in spam.items():
    print('Key: ' + k + ' Value: ' + str(v))
    
# check a key or a value exists in a dictionary
spam = {'name': 'Zophie', 'age': 7}
'name' in spam.keys()
'Zophie' in spam.values()
'color' in spam.keys()
'color' not in spam.keys()
'color' in spam           # check 'color' in spam.keys()

# Fortunately, dictionaries have a get() method that takes two arguments: 
# the key of the value to retrieve and a fallback value to return if that key does not exist.

picnicItems = {'apples': 5, 'cups': 2}
'I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.'
'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.'

# The setdefault() Method
spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'

spam = {'name': 'Pooka',  'age': 5}
spam.setdefault('color', 'black')
spam.setdefault('color', 'white')
