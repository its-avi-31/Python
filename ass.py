n=int(input("starting range="))
n1=int(input("end range="))
for i in range(n,n1+1):
    a=i
    count=0
    while a>0:
        if i%a==0:
            count=count+1
        a=a-1
    if count==2:
            print(i)
    
