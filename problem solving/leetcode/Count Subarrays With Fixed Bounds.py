class Solution:
    def countSubarrays(self, nums: List[int], mink: int, maxk: int) -> int:
        right=0
        length =len(nums)
        res=0
        for left in range(length):
            check_min,check_max=0,0
            if nums[left]==mink:
                check_min+=1
            if nums[left]==maxk:
                check_max+=1
            if nums[left]<mink or nums[left]>maxk:
                continue
            if check_min and check_max:
                res+=1
            for right in range(left+1,length):
                if nums[right]==mink:
                    check_min+=1
                if nums[right]==maxk:
                    check_max+=1
                if nums[right]<mink or nums[right]>maxk:
                    break
                if check_min and check_max:
                    res+=1
        return res



class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        result = 0
        n = len(nums)
        
        
        last_out_of_bounds = -1  
        last_min = -1            
        last_max = -1            
        
        for i in range(n):
            
            if nums[i] < minK or nums[i] > maxK:
                last_out_of_bounds = i
            if nums[i] == minK:
                last_min = i
            if nums[i] == maxK:
                last_max = i
            valid_subarrays = min(last_min, last_max) - last_out_of_bounds if last_min > last_out_of_bounds and last_max > last_out_of_bounds else 0
            result += valid_subarrays
            
        return result
