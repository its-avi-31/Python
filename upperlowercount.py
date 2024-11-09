n=input("Enter a string=")
count=0
cout=0
for i in n:
    if True==i.isupper():
        count=count+1
    elif True==i.islower():
        cout=cout+1
    else:
        pass
print("Total upper laters=",count)
print("Total lower laters=",cout)    
