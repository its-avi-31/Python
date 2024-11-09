# Fn that String contains given substring -->

str=input("Enter a string : ")
str=str.lower()
st=input("Enter searching substring : ")
st=st.lower()
def substr(s):
    while st in str:
        print(f"{st} substring is present in the given String  :)")
        break
    else:
        print("Substring is not found :(")
substr(str)

