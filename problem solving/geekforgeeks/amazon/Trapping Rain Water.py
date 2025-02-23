#high time complexity
class Solution:
    def maxWater(self, arr):
        l=len(arr)
        if l==1:
            return 0
        else:
        
            minx=[]
            res=0
            for i in range(l):
                if i==0:
                    minx.append(min(0,max(arr[i+1:l])))
                elif i==l-1:
                    minx.append(min(max(arr[0:i]),0))
                else:
                    
                    minx.append(min(max(arr[i+1:l]),max(arr[0:i])))
                if minx[i]-arr[i]>0:
                    res+=minx[i]-arr[i]
            return(res)

#optimal solution


class Solution:
    def maxWater(self, arr):
        l=len(arr)
        left_pointer=0
        right_pointer=l-1
        left_max=arr[0]
        right_max=arr[l-1]
        res=0
        while left_pointer<right_pointer:
            if left_max<right_max:
                left_pointer+=1
                left_max=max(left_max,arr[left_pointer])
                
                res+=left_max-arr[left_pointer]
            else:
                right_pointer-=1
                right_max=max(right_max,arr[right_pointer])
                res+=right_max-arr[right_pointer]
        return res
        
        
