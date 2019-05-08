print( 'howdy' in ['hello', 'hi', 'howdy', 'heyas'] )
spam = ['hello', 'hi', 'howdy', 'heyas']
print( 'cat' in spam )
print( 'howdy' not in spam )
print( 'cat' not in spam )

myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')