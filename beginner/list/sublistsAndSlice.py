spam = ['cat', 'bat', 'rat', 'elephant']
print( spam[0:4] )  # go up to 4, not include 4
print( spam[1:3] )
print( spam[0:-1] ) # -1 is the last iterm
print( spam[:2] )
print( spam[1:] )
print( spam[:] )
print( len(spam) ) # get the length of list
spam[1] = 'aardvark'
print(spam)
#spam[2] = spam[1]
#print( spam )
spam[-1] = 12345
print( spam )
del spam[2] # delete the third item
print(spam)
del spam[2]
print( spam )
del spam[2] # keep this command. do not delete it
print( spam )