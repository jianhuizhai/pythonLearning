linecomment = '============================================================================'

import shutil, os

# shutil.copy() will copy a single file, shutil.copytree() will
# copy an entire folder and every folder and file contained in it.
# shutil.copytree(source, destination)
shutil.copy('../zeroDivide.py', '.')  # first is src file, second is the destination folder
shutil.copy('example1.py', 'example_test.py')

os.chdir("../")
if not os.path.exists('organizingFiles_Test'):
    shutil.copytree('organizingFiles', 'organizingFiles_Test')
os.chdir('organizingFiles')

print(linecomment)
print( '''Moving and Renaming Files and Folders''')
print( linecomment )
'''
# delete the ../example_test.py. If not delete, if ../example_test.py already exists, following command will give an error.
os.unlink('../example_test.py')   # delete the file at '../example_test.py'
# If there had been ../example_test.py file already exists, it would not overwrit.
shutil.move('example_test.py', '../')
'''
os.unlink( '../move_rename.py')
shutil.move('example_test.py', '../move_rename.py')
# os.rmdir(path) will delete the folder at path . This folder must be
# empty of any files or folders.
# shutil.rmtree(path) will remove the folder at path , and all files
# and folders it contains will also be deleted.
for filename in os.listdir():
    if filename.endswith('.rxt'):
        #os.unlink(filename)
        print(filename)  # before delete the file, show the filename to check if there is an accident or not

import send2trash
baconFile = open('bacon.txt', 'a') # creates the file
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
send2trash.send2trash('bacon.txt')  # this is more useful than shutil.rmtree() to avoid accident

