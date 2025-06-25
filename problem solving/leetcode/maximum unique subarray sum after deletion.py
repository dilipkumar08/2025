class Solution:
    def maxSum(self, nums: List[int]) -> int:
        l=len(nums)
        if l==1:
            return nums[0]
        if max(nums)<=0:
            return max(nums)
        res=0
        for i in list(set(nums)):
            if i>0:
                res+=i
        return res


-----------------------------------------------------------------

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums.sort()
        temp=[]
        if nums[-1]<=0:
            return nums[-1]
        else:
            res=0
            for i in nums:
                if i>0 and i not in temp:
                    res+=i
                temp.append(i)
            return res
            
                

