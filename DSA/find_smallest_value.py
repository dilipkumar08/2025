import numpy as np

def find_smallest(arr:np.array):
    l=len(arr)
    if l==1:
        return arr[0]
    else:
        temp=arr[0]
        for i in range(l):
            
            if temp>arr[i]:
                temp=arr[i]
        return temp
    
if __name__=='__main__':
    print(find_smallest(np.array([1,2,3,4,0,-5])))
