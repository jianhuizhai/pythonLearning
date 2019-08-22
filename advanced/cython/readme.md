
### Following is an example for how to use Cython.

#### It will contain a simple function that prints Hello, World! as the output.

1. create a new `hello.pyx` file containning following code:
```
def hello():
    print("hello world!")
```
2. The cython command will read `hello.pyx` and generate the `hello.c` file:
```
cython hello.pyx
```

before this, you need to install cython module.

3. To compile `hello.c` to a Python extension module, we will use the GCC compiler. We
need to add some Python-specific compilation options that depend on the operating system.
It's important to specify the directory that contains the header files; in the following
example, the directory is /usr/include/python3.6m/ (you can find the directory by typing `locate Python.h`) :
```
gcc -shared -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing -lm -I/usr/include/python3.6m/ -o hello.so hello.c
```

This will produce a file called hello.so , a C extension module that is directly importable into a Python session:
```
>>> import hello
>>> hello.hello()
Hello, World!
```
______
Cython accepts both Python 2 and Python 3 as input and output languages. In other words, you can compile a Python 3 script hello.pyx file using the -3 option:
```
cython -3 hello.pyx
```

The generated hello.c can be compiled without any changes to Python 2 and Python 3 by
including the corresponding headers with the -I option, as follows:
```
gcc -I/usr/include/python3.5 # ... other options
gcc -I/usr/include/python2.7 # ... other options
```
There is also some other methods to compile a Cython program.
* writing a `setup.py` script;

* using pyximport;

* IPython use `cythonmagic` extention.

__Now, we will have a look at how to write a `setup.py` script.__
By writing a setup.py script, we can compile the `.pyx` file directly to an extension module. To compile our `hello.pyx` example, we can write a minimal `setup.py` containing the following code:
```
from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='Hello',
    ext_modules = cythonize('hello.pyx')
)
```
In the first two lines of the preceding code, we import the `setup` function and the `cythonize` helper. The setup function contains a few key-value pairs that specify the name of the application and the extensions that need to be built.

The cythonize helper takes either a string or a list of strings containing the Cython modules we want to compile. You can also use glob patterns using the following code:
```
cythonize(['hello.pyx', 'world.pyx', '*.pyx'])
```
To compile our extension module using `distutils` , you can execute the `setup.py` script using the following code:
```
python setup.py build_ext --inplace
```
The `build_ext` option tells the script to build the extension modules indicated in `ext_modules` , while the `--inplace` option tells the script to place the `hello.so` output file in the same location as the source file (instead of a build directory).

__For other two methods, please see Gabriele Lanaro, Python high performance, 2nd (2017).__

#### One thing we should note that 
* examples are taken from Python documentation or Python high performance (book).
