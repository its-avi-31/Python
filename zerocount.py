n=int(input("enter a no:"))
count=0
while n>0:
    a=n%10
    if a==0:
        count=count+1
    n=n//10
print("Total no of zero=",count)
