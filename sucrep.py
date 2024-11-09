a=input("Enter a string=")
l=len(a)
x=list(a)
#print(type(x))
i=0
j=i+1
while i<l-1:
    if x[i]==x[j]:
        j='?'
    i=i+1
    j=j+1
print(x)
