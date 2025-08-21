

if "__main__"==__name__:
    matrix=["abc","def","ghi"]
    n=int(input("Enter the input:"))
    starLineCount=n%3
    for i in range(starLineCount):
        print("*"*n)
    print("*abc*\n*def*\n*ghi*")
    for i in range(starLineCount):
        print("*"*n)