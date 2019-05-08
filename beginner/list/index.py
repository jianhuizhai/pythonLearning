spam = ['hello', 'hi', 'howdy', 'heyas']
print( spam.index('hello') )
print( spam.index('heyas') )

# print( spam.index('howdy howdy howdy') )

# When there are duplicates of the value in the list, the index of its first
# appearance is returned. Enter the following into the interactive shell, and
# notice that index() returns 1 , not 3 :

spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
print( spam.index('Pooka') )