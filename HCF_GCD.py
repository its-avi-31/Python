# Find Highest Common Factor/ Greatest Common Divisior -->

n1=int(input("enter first no:"))
n2=int(input("enter sec no:"))
if n2>n1:
    min=n1
else:
    min=n2
for i in range(1,min+1):
    if n1%i==0 and n2%i==0:
        hcf=i
print("HCF/GCD=",hcf)

# Second Method -->


n1=int(input("enter first no:"))
n2=int(input("enter sec no:"))
while n2!=0:
    temp=n2
    n2=n1%n2
    n1=temp
print(n1)
    

    
