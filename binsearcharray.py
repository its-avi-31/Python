from array import *
a=array('i',[])
size=int(input("array size="))
print("Elements of array a in sorted order:")
i=0
while i<size:
    a.append(int(input()))
    i=i+1
s=int(input("Enter searching element="))
f=0
l=size-1
while f<=l:
    mid=(f+l)//2
    if s==a[mid]:
        print("Searching element found")
        break
    elif s<a[mid]:
        l=mid-1
    else:
        f=mid+1
else:
    print("Searching element not found")
    
