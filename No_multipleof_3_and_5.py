# Find that given no is multiple of 3 and 5 -->

def mult():
    n=int(input("Enter a no: "))
    if n%3==0 and n%5==0:
        print("No is multiple of 3 and 5")
    else:
        print("Not multiple of 3 and 5")
mult()