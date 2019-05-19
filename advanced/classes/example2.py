#! /usr/bin/python3

linecomment = '=================================================================='

from numpy import array, cross # it will not work if put this in class
'''
class Triangle:
    
    def __init__(self,  A, B, C):
        self.A = array(A)
        self.B = array(B)
        self.C = array(C)
        self.a = self.C - self.B
        self.b = self.C - self.A
        self.c = self.B - self.A
    def area(self):
        return abs(cross(self.b, self.c)) / 2

tr = Triangle([0., 0.], [1., 0.], [0., 1.])
print( tr.area() )
tr.B = [12., 0.]
print( tr.B )
print( tr.area() )
'''
print( linecomment )
print( '''The property function''' )
print( linecomment )
class Triangle:
    def __init__(self, A, B, C):
        self._A = array(A)
        self._B = array(B)
        self._C = array(C)
        self._a = self._C - self._B
        self._b = self._C - self._A
        self._c = self._B - self._A
    def area(self):
        return abs(cross(self._c, self._b)) / 2.
    def set_B(self, B):
        self._B = B
        self._a = self._C - self._B
        self._c = self._B - self._A
    def get_B(self):
        return self._B
    def del_Pt(self):
        raise Exception('A triangle point cannot be deleted')
    B = property(fget = get_B, fset = set_B, fdel = del_Pt)

tr = Triangle([0., 0.], [1., 0.], [0., 1.])
print( tr.area() )
tr.B = [12., 0.]
print( tr.area() ) # returns 6.0

class A:
    def func(self, arg):
        pass
A.func  # <unbound method A.func>
instA = A()  # we create an instance
instA.func  #  <bound method A.func of ... >
# A.func(1)  ## would result in an error
instA.func(1)

