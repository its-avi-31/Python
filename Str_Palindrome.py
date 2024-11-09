# Check the given String is palindrome or not(Jiska reverse whi ho, 121==121) -->

def palstr():
    str=input("Enter a string: ")
    rev=''
    l=len(str)
    while l>0:
        rev=str[-1::-1]
        l=l-1
    if str==rev:
        print("Palindrome String")
    else:
        print("Not palindrome string")
palstr()
