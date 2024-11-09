n1=int(input("F no="))
n2=int(input("S no="))
def add(n1,n2):
    if n2==0:
        return 0
    else:
        return n1+add(n1,n2-1)
sum=add(n1,n2)
print("Repeated addition=",sum)
