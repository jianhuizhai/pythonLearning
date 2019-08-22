
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
* examples are taken from Python documentation or Python high performance (book).
