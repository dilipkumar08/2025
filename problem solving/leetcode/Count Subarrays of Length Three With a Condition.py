class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        length=len(nums)
        if length<3:
            return 0
        res=0
        right=2
        left=0
        while right<length:
            if (nums[left]+nums[right])*2==nums[left+1]:
                res+=1
            left+=1
            right+=1    
        return res

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        res=0
        for i in range(1,len(nums)-1):
            if nums[i]==(nums[i-1]+nums[i+1])*2:
                res+=1
        return res

            
