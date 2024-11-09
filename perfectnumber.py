#A no, which Sum of its factorial are equal to that no is called 'Perfect No'.Ex- 6
n=int(input("Enter a no:"))
fact=1
sum=0
while n>fact:
    if n%fact==0:
        sum=sum+fact
    fact=fact+1
if sum==n:
    print("Perfect")
else:
    print("Not")
