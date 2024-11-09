# Sum of no untill the given no is 0 -->

n=int(input("Enter a no:"))
sum=0
while n>0:
    sum=sum+n
    n=int(input("Enter a next no:"))
print(sum)
