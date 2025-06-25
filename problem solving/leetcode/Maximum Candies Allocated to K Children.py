#Brute Force
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        s=sum(candies)
        if s<k:
            return 0
        elif s==k:
            return 1

        mx=max(candies)
        res=0
        for i in range(1,mx+1):
            temp=[]
            for j in candies:
                temp.append(j//i)
            if sum(temp)<k:
                break
            res=i
        return res

#Optimized using binary search
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        if sum(candies)<k:
            return 0
        res=[]
        start = 1
        end=max(candies) 
        res=[]
        while start<=end:
            mid=(start+end)//2
            childrens=sum(j//mid for j in candies)
            if childrens>=k:
                res=mid
                start=mid+1
            else:
                end=mid-1

        return res

            


        
