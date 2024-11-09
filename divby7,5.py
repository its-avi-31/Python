def comm(a,b):
    l1=len(a)
    l2=len(b)
    i=0
    while i<l1:
        j=0
        while j<l2:
            if a[i]==b[j]:
                return True
            j=j+1
        i=i+1 
a=[1,2,13,4,5]
b=[6,21,8,15,3]
x=comm(a,b)
if x==True:
    print("Presents")
else:
    print("Not")
