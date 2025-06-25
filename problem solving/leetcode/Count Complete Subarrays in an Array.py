class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        l=len(set(nums))
        count=Counter()
        length=len(nums)
        right=0
        res=0
        for left in range(length):
            while right<length and len(count)<l:
                count[nums[right]]+=1
                right+=1
            if  len(count)==l:
                res+=length-right+1
            count[nums[left]]-=1
            if count[nums[left]]==0:
                del count[nums[left]]
        
        return res
