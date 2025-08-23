if __name__=="__main__":
    uniqueChars={}
    maxDistance=0
    inputString=str(input("Enter the input string: "))
    for index,character in enumerate(inputString):
        if character not in uniqueChars:
            uniqueChars[character]=index+1
        else:
            maxDistance=max(index-(uniqueChars[character]),maxDistance)
    
    print(maxDistance)