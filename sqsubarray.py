from array import *
a=array('i',[1,2,3,4,5])
b=array('i',[])
l=len(a)
i=0
while i<l:
    sq=a[i]**2
    b.append(sq)
    i=i+1
print("array a:",a)
print("array b:",b)
