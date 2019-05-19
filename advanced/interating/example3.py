#! /usr/bin/python3

linecomment = '==================================================================='

'''
List filling patterns
'''
'''
L = []
for k in range(n):
    # call various functions here
    # that compute "result"
    L.append(result)
'''
'''
ABoving approach has a number of disadvantages:
1. The number of iterations is decided in advance. If there is a break instruction,
then the preceding code takes care of both generating values and deciding when
to stop. This is not desirable and lacks flexibility.
2. It makes the assumption that the user wants the whole history of the
computation, for all the iterations. Suppose we are only interested in the sum of
all the computed values. If there are many computed values, it does not make
sense to store them, as it is much more efficient to add them one at a time.
'''
'''
def result_iterator():
    for k in itertools.count(): # infinite iterator
    # call various functions here
    # that compute "result"
    ...
    yield result

L = list(itertools.islice(result_iterator(), n)) # no append needed!
# make sure that you do not use scipy.sum here
s = sum(itertools.islice(result_iterator(), n))

L = [some_function(k) for k in range(n)]
'''
print( linecomment )
print( '''Storing generated values when an exception is raised''' )
print( linecomment )
import itertools
def power_sequence(u0):
    u = u0
    while True:
        yield u
        u = u**2
# print( list(itertools.islice(power_sequence(2.), 20)) )
generator = power_sequence(2.)
L = []
for iteration in range(20):
    try:
        L.append(next(generator))
    except Exception:
        break
print(L)
print( linecomment )
print( '''Iterator Objects''')
print( linecomment )
class OdeStore:
    """Class to store results of ode computations"""
    def __init__(self, data):
        "data is a list of the form [[t0, u0], [t1, u1],...]"
        self.data = data
    def __iter__(self):
        "By default, we iterate on the values u0, u1,..."
        for t, u in self.data:
            yield u

store = OdeStore([[0, 1], [0.1, 1.1], [0.2, 1.3]])
for u in store:
    print(u)
print( list(store) )