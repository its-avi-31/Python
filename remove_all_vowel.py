# Fn that remove all vowel from a given string -->

str=list(input("Enter a string : "))
vowel=['a','e','i','o','u']

def remvow(str):
    st=[]
    i=0
    l=len(str)
    while i<=l:
        for vowel[i] in str:
            str.remove(vowel[i])
            i=i+1
    print("After removing vowels, String is : ",str)
remvow(str)


