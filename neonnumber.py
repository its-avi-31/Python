n=int(input("enter a number="))
sq=n**2
sum=0
while sq>0:
    a=sq%10
    sum=sum+a
    sq=sq//10
if sum==n:
    print("Neon")
else:
    print("Not")
    
