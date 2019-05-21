import timeit
setup_statements="""
from scipy import zeros
from numpy import where
A=zeros((1000,1000))
A[57,63]=10.

def find_elements_1(A):
    b = []
    n, m = A.shape
    for i in range(n):
        for j in range(m):
            if abs(A[i, j]) > 1.e-10:
               b.append(A[i, j])
    return b

def find_elements_2(A):
    return [a for a in A.reshape((-1,)) if abs(a) > 1.e-10]

def find_elements_3(A):
    return [a for a in A.flatten() if abs(a) > 1.e-10]

def find_elements_4(A):
    return A[where( 0.0 != A)]
"""
experiment_1 = timeit.Timer(stmt = 'find_elements_1(A)',setup = setup_statements)
experiment_2 = timeit.Timer(stmt = 'find_elements_2(A)',
                            setup = setup_statements)
experiment_3 = timeit.Timer(stmt = 'find_elements_3(A)',
                            setup = setup_statements)
experiment_4 = timeit.Timer(stmt = 'find_elements_4(A)',
                            setup = setup_statements)
t1 = experiment_1.repeat(3,5) 
t2 = experiment_2.repeat(3,5) 
t3 = experiment_3.repeat(3,5) 
t4 = experiment_4.repeat(3,5) 

# Results per loop in ms
print(min(t1)*1000/5) # 615 ms
print(min(t2)*1000/5) # 543 ms
print(min(t3)*1000/5) # 546 ms
print(min(t4)*1000/5) # 7.26 ms
print("="*80)
print("another method")
print("="*80)
import time
from scipy import zeros
from numpy import where
class Timer:
	def __enter__(self):
		self.start = time.time()
	def __exit__(self, ty, val, tb):
		end = time.time()
		self.elapsed=end-self.start
		print('Time elapsed {} seconds'.format(self.elapsed))
		return False 

def find_elements_1(A):
    b = []
    n, m = A.shape
    for i in range(n):
        for j in range(m):
            if abs(A[i, j]) > 1.e-10:
               b.append(A[i, j])
    return b
A=zeros((1000,1000))
A[57,63]=10.
with Timer():
    find_elements_1(A)

## or
# with Timer() as t1:
#     find_elements_1(A)
# t1.elapsed # contains the result