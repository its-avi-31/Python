def fib(n):
    a,b=0,1
    print(a)
    print(b)
    while n>1:
        c=a+b
        a=b
        b=c
        if c>10:
            break
        print(c)
fib(10)
