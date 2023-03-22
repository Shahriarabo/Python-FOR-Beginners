def fibo(n):
    if n== 0:
        return 0
    else:
        x=0
        y=1
        print(x)
        print(y)

        for i in range(1,n):
            w=x+y
            x=y
            y=w
            print(w)

fibo(6)
