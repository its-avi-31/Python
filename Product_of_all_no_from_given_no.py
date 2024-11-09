# Find the Product of all no whereas the number is given -->

# def prod(n):
#     pro=1
#     while n>0:
#         pro=pro*n
#         n=n-1
#     print("Product of all no from given no= ",pro)
# n=int(input("Enter a number: ")) 
# prod(n)    


# Find the Product of all no whereas the number is given with recurtion -->

def prod(n):
    pro=1
    if n==0:
        return 0
    else:
        while n>0:
            pro=pro*n
            n=n-1
        return pro
n=int(input("Enter a number: ")) 
product=prod(n)
print("Product of all no from given no= ",product)   