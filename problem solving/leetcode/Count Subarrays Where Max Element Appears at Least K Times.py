class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num=max(nums)
        l=len(nums)
        res=0
        for i in range(l):
            count=0
            if nums[i]==max_num:
                count+=1
            if count>=k:
                res+=1
            for j in range(i+1,l):
                if nums[j]==max_num:
                    count+=1
                if count>=k:
                    res+=1

        return res
                
---------------------
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_val = max(nums)
        count = 0
        left = 0
        max_count = 0
        for right in range(n):
            if nums[right] == max_val:
                max_count += 1
            while max_count >= k:
                if nums[left] == max_val:
                    max_count -= 1
                left += 1
            count += left
        return count

                
