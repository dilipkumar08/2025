
#function to compare the versions
def versionComparison(version1:str,version2:str)->bool:

    #splitting and type casting to compare each partitions
    version1Partitions=list(map(int,version1.split(".")))
    version2Partitions=list(map(int,version2.split(".")))
    version1Length=len(version1Partitions)
    version2Length=len(version2Partitions)
    tempIndex=0 #temporary index for comparing partitions

    while tempIndex<version1Length and tempIndex<version2Length:
        #version1 > version2
        if int(version1Partitions[tempIndex])>int(version2Partitions[tempIndex]):
            return version1
        #version1 < version2
        elif int(version1Partitions[tempIndex])<int(version2Partitions[tempIndex]):
            return version2
        tempIndex+=1

    #checking if version1 has more partition which are non zer0
    if tempIndex!=version1Length and tempIndex==version2Length:
        while tempIndex<version1Length:
            if version1Partitions[tempIndex]!=0:
                return 1
            tempIndex+=1
    
    #checking if version2 has more partition which are non zer0
    if tempIndex==version1Length and tempIndex!=version2Length:
        while tempIndex<version2Length:
            if version2Partitions[tempIndex]!=0:
                return -1
            tempIndex+=1
    
    #both are same  
    return 0

#main block
if __name__ == "__main__":
    version1=str(input("Enter version one: "))
    version2=str(input("Enter version two: "))
    #final output
    print("Result :",versionComparison(version1,version2))
