from scipy import *

def f(x):
    try:
        return 1/x
    except Exception:
        print("ZeroDivision.")
f(0)

try:
    f = open('data1.txt', 'r')
    data = f.readline()
    value = float(data)
except OSError as oe:
    print("{}:  {}".format(oe.strerror, oe.filename))
except ValueError:
    print("Could not convert data to float.")

try:
    f = open('data2.txt', 'r')
    data = f.readline()
    value = float(data)
except OSError as oe:
    print("{}:  {}".format(oe.strerror, oe.filename))
except ValueError:
    print("Could not convert data to float.")

try:
    f = open('data1.txt', 'w')
    # some function that does something with the file
    f.write('some text')
except:
    print('Some message')
finally:
    f.close() 

print('='*50)
print('''user defined exceptions''')
print('='*50)

class MyError(Exception):
    def __init__(self, expr):
        self.expr = expr
    def __str__(self):
        return str(self.expr)


try:
    x = random.rand()
    if x < 0.5: 
        raise MyError(x)
except MyError as  e:
    print("Random number too small", e.expr)
else:
    print(x)

print('='*50)
print('context managers -- the with command')
print('='*50)

## If anything goes wrong during the execution of process_file_data , the
## file is closed properly and then the exception is raised.
with open('data.txt', 'r') as f:
    process_file_data(f)

import numpy as np

with np.errstate(invalid='ignore'):
    print(np.sqrt(-1)) # prints 'nan'

with errstate(invalid='warn'):
    print(np.sqrt(-1)) # prints 'nan' and 'RuntimeWarning: invalid value encountered in sqrt'

with errstate(invalid='raise'):
    print(np.sqrt(-1)) # prints nothing and raises FloatingPointError
