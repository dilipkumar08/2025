#Brute force
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos,neg=0,0
        for i in nums:
            if i<0:
                neg+=1
            elif i>0:
                pos+=1
            
        return max(pos,neg)  
#Optimized
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos,neg=0,0
        l=len(nums)-1
        while (nums[l]>=0 and l>=0):
            if  nums[l]!=0:
                pos+=1
            l-=1
        neg=l+1
        return max(pos,neg)
