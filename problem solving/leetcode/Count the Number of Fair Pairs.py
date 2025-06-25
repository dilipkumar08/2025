class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        left=0
        right=len(nums)-1
        lesser=0
        greater=0
        while left!=right:
            if nums[left]+nums[right]<lower:
                lesser+=right-left
                left+=1
            else:
                right-=1
        left,right=0,len(nums)-1

        while left!=right:
            if nums[left]+nums[right]<=upper:
                greater+=right-left
                left+=1
            else:
                right-=1
        
        return abs(greater-lesser)

