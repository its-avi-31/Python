a="Aprit@855545"
n="abcdefghijklmnopqrstwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_@"
a1=list(a)
n1=list(n)
x=""
l1=len(a1)
i=0
while n:
    w=n1[i]
    if w in a1:
        x.append(w)
    i=i+1
    xl=len(x)
    if l1==xl:
        break
if a is x:
    print("Success")
else:
    print("Fail")
    
        
