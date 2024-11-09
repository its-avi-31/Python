# Fn returns the no of properties in an object -->

n=input("Enter a string/object: ")
def prop(a):
    ncount=alcount=spcount=0
    for i in a:
        if True==i.isalpha():
            ncount=ncount+1
        elif True==i.isdigit():
            alcount=alcount+1
        else:
            spcount=spcount+1
    print("No of digit = ",ncount)
    print("No of Alphabet = ",alcount)
    print("No of Special Char = ",spcount)
prop(n)


