#  Sum of all no from the given no -->

def sumall():
    sum=0
    n=int(input("Enter a number where as you want to add: "))
    while n>0:
        sum=sum+n
        n=n-1
    print(f"Sum of all numbers at before the given no = ",sum)
sumall()




#  Sum of all no from from given no with recurtion -->

def sum(n):
    if n==1:
        return 1
    else:
        return  n+sum(n-1)
n=int(input("Enter the no whereas you want to add :"))
s=sum(n)
print("Sum of all no=",s)
