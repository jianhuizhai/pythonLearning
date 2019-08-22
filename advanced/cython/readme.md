
### Following is an example for how to use Cython.

#### It will contain a simple function that prints Hello, World! as the output.

1. create a new hello.pyx file containning following code:
```
def hello():
    print("hello world!")
```
2. The cython command will read hello.pyx and generate the `hello.c` file:

* examples are taken from Python documentation or Python high performance (book).
