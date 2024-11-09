"""Armstrong No: A no,thats sum of its same power upon
every single value is same to,that no.Ex-153"""

n=int(input("enter a no:"))
x=n
sum=0
digit=len(str(n))
while n>0:
    a=n%10
    sum=sum+a**digit
    n=n//10
if sum==x:
    print("Arm")
else:
    print("Not")
