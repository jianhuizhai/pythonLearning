import pdb 
from numpy import sqrt, arctan2

def complex_to_polar(z):
    pdb.set_trace()
    r = sqrt(z.real ** 2 + z.imag ** 2)
    phi = arctan2(z.imag, z.real)
    return (r,phi)

z = 3 + 5j
r,phi = complex_to_polar(z)

print(r,phi)