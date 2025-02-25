def fibonacci_series(n: int):
    a=0
    b=1
    if n==0:
        print("-")
    elif n==1:
        print(a)
    elif n==2:
        print(a)
        print(b)
    else:
        print(a)
        print(b)
        for i in range(n):
            temp=a+b
            print(temp)
            a=b
            b=temp

    
    
fibonacci_series(5);
