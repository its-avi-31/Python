from array import *
a=array('i',[])
n=int(input("Enter no="))
i=0
while n>0:
    x=n%2
    a.append(x)
    n=n//2
    i=i+1
print("Binary equivalent:")
l=len(a)
i=l-1
print("0b",end='')
while i>=0:
    print(a[i],end='')
    i=i-1
