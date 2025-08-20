def RotateString(string:str,type:str,count:int):
    if type=='l':
        while(count):
            string=string[1:]+string[0]
            count-=1
        return string
    elif type=='r':
        while(count):
            string=string[-1]+string[:-1]
            count-=1
        return string
    else:
        return string


if __name__=="__main__":
 
    inputString=str(input("Enter the string to be rotated:"))
    rotateType=str(input("Enter the rotation type (Left/Right):"))[0].lower()
    rotateCount=int(input("How many positions do you want to rotate?:"))
    resultString=RotateString(inputString,rotateType,rotateCount)
    print(resultString)
    

