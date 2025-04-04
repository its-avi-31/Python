"""Armstrong No: A positive integer where the sum of its digits, each raised to the power of the number of digits,
   equals the original number. Ex-153"""

n=int(input("Enter a no: "))
x=n
sum=0
digit=len(str(n))
while n>0:
    a=n%10
    sum=sum+a**digit
    n=n//10
if sum==x:
    print("Armstrong")
else:
    print("Not Armstrong")

# Armstrong no in certain interval -

dest = int(input("Enter the ending value: "))
for i in range(1,dest+1):
    count = 0
    no = n = i
    while i > 0:
        a = i % 10
        count = count + 1
        i = i // 10
    arm = 0
    while n > 0:
        x = n % 10
        arm = arm + x ** count
        n = n // 10
    if arm == no:
        print(arm)


