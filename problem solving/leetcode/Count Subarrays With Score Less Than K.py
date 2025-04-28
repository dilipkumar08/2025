class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res=0
        l=len(nums)
        for i in range(l):
            temp_sum=nums[i]
            size=1
            if temp_sum<k:
                res+=1
            else:
                continue
            for j in range(i+1,l):
                size+=1
                temp_sum+=nums[j]
                if temp_sum*(size)<k:
                    res+=1
                else:
                    break
        return res

-------------------------------------
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        left = 0
        current_sum = 0
        for right in range(n):
            current_sum += nums[right]
            while left <= right and current_sum * (right - left + 1) >= k:
                current_sum -= nums[left]
                left += 1
            count += (right - left + 1)
        return count
