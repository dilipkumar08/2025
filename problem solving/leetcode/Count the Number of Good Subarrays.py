class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        if nums:
            length=len(nums)
            record={}
            l=0
            r=0
            pair_count=0
            good_subarrays=0
            while r<length:
                val=nums[r]
                pair_count+=record.get(val,0)
                record[val]=record.get(val,0)+1
                while pair_count>=k:
                    good_subarrays+=length-r
                    record[nums[l]]-=1
                    pair_count-=record[nums[l]]
                    l+=1
                r+=1
            return good_subarrays



                
                
                

            
        
