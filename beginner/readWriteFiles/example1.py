import os

linecomment = '====================================================================='
# If you pass it the string values of individual file and folder names in your path,
# os.path.join() will return a string with a file path using the correct path separators.

print(linecomment)
path = os.path.join('usr', 'bin', 'spam')
print( path )

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join(path, filename))

print(linecomment)
print('''
The Current Working Directory
Python will display an error if you try to change to a directory that does not exist.
''')
print( linecomment )

print( os.getcwd() )
os.chdir('/home/jianhui/Code/python/codesForBeginners')
print( os.getcwd() )

print( linecomment )
print('''
Creating New Folders with os.makedirs()
''')
print( linecomment )
# os.makedirs() will create any necessary intermediate folders in order to ensure that the full path exists.
if not os.path.exists( '/home/jianhui/Code/python/codesForBeginners/readWriteFiles/test/test1' ):
    os.makedirs('/home/jianhui/Code/python/codesForBeginners/readWriteFiles/test/test1')

print( linecomment )
print('''Handling Absolute and Relative Paths''' )
print( linecomment )
'''
os.path.abspath(path) will return a string of the absolute path of the argument.
os.path.isabs(path) will return True if the argument is an absolute path and False if it is a relative path.
os.path.relpath(path, start) will return a string of a relative path from the start path to path .
'''
print( os.path.abspath('.') )
print( os.path.abspath('./test') )
print( os.path.isabs('.') )
print( os.path.isabs(os.path.abspath('.')) )

print( os.path.relpath('/home/jianhui/Code/python/codesForBeginners/readWriteFiles', '/home/jianhui/Code/python') )

path = '/home/jianhui/Code/python/codesForBeginners/readWriteFiles/example1.py'
print( os.path.basename(path) )
print( os.path.dirname(path)  )
print( os.path.split(path) )  # get a tuple  
print( path.split(os.path.sep) )

print( linecomment )
print( '''Finding File Sizes and Folder Contents''' )
print( linecomment )
# os.path.getsize(path) will return the size in bytes of the file in the path argument.
# os.listdir(path) will return a list of filename strings for each file in the path argument.
print( os.path.getsize(path) ,'bytes' )
os.chdir( '/home/jianhui/Code/python/codesForBeginners/readWriteFiles' )
print( os.listdir('/home/jianhui/Code/python/codesForBeginners/readWriteFiles') )
print( os.listdir('.') )

totalSize = 0
for filename in os.listdir('/home/jianhui/Code/python/codesForBeginners/readWriteFiles'):
    totalSize = totalSize + os.path.getsize(os.path.join('/home/jianhui/Code/python/codesForBeginners/readWriteFiles', filename))
print(totalSize,'bytes')
# the above command can be replaced by following command
totalSize = 0
for filename in os.listdir('.'):
    totalSize = totalSize + os.path.getsize( os.path.join('.', filename) )
print(totalSize,'bytes')

print( linecomment )
print( '''Checking Path Validity''' )
print( linecomment )
# os.path.exists(path) will return True if the file or folder referred 
# to in the argument exists and will return False if it does not exist.
# os.path.isfile(path) will return True if the path argument exists
# and is a file and will return False otherwise.
# os.path.isdir(path) will return True if the path argument exists
# and is a folder and will return False otherwise.
for thing in os.listdir('.'):
    if os.path.isdir(thing):
        print( '{:10s}{:15s}'.format('dir :',thing) )
    if os.path.isfile(thing):
        print( '{:10s}{:15s}'.format('file:',thing) )