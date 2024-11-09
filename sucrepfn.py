def suc_rep(s):
    sr=s[-1::-1]
    i=0
    s1=""
    for x in sr:
        if sr.index(x)==i:
            s1=s1+x
        else:
            char=sr[i]
            s1=s1.replace(char,"?")
            s1=s1+x
        i=i+1
    s2=s1[-1::-1]
    return s2
s=(input("String="))
print(suc_rep(s))
