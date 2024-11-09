n=int(input("enter a no:"))
count=0
while n>0:
    a=n%10
    if a==0:
        count=count+1
    n=n//10
if count>=1:
    print("Duck")
else:
    print("Not")
