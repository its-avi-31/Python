# Check the no is prime or not -->

n=int(input("Enter a no: "))
i=1
count=0
while i<=n:
    if n%i==0:
        count=count+1
    i=i+1
if count==2:
    print("prime")
else:
    print("Not")
