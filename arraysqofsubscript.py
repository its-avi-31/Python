# Store square of subscript as array elements..
from array import *
a=array('i',[5,6,7,8,9])
b=array('i',[])
l=len(a)
for i in range(5):
    b.append(i**2)
print(b)
