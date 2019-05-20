linecomment = '============================================================'

import shelve
import pprint

print( linecomment )
print( '''Opening Files with the open() Function''' )
print( linecomment )
helloFile = open('hello.txt', 'r').read()  # r --- read
print(helloFile)

sonnetFile = open('sonnet29.txt')
print( sonnetFile.readlines() )
sonnetFile.close()
# with open('data.txt', 'r') as f:
#     process_file_data(f)
## above command will close the file automatically even there is a error during processs file data.
baconFile = open('bacon.txt', 'w')   # w --- write
print( baconFile.write('Hello world!\n') )
baconFile.close()

baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)

shelfFile = shelve.open('mydata')
print( type(shelfFile) )
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
print( shelfFile['cats'] )
# Just like dictionaries, shelf values have keys() and values() methods that
# will return list-like values of the keys and values in the shelf.
print( list(shelfFile.keys()) )
print( list(shelfFile.values()) )
shelfFile.close()

cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()

import myCats
print( myCats.cats  )
print( myCats.cats[0] )
print( myCats.cats[0]['name'] )
