#  Printing the reverse of a string -->

str=input("Enter a string: ")
l=len(str)
rev=''
while l>0:
    rev=str[::-1]       #or str[-1::-1]
    l=l-1
print("Reverse String = ",rev)


# Second Method:

# str=input("Enter a string: ")
# rev=''
# for x in str:
#     rev=x+rev
# print("Reverse of String = ",rev)
