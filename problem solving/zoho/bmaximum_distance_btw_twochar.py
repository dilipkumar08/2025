if __name__=="__main__":
    maxDistance=0
    inputString=str(input("Enter the sample string:"))
    length=len(inputString)
    for idx1 in range(length):
        tempDistance=0
        for idx2 in range(idx1+1,length):
            if inputString[idx1]==inputString[idx2]:
                maxDistance=max(maxDistance,tempDistance)
            else:
                tempDistance+=1
    
    print("Maximum distance between two characters in the given string is:",maxDistance)
            