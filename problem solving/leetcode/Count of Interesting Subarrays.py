class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        length=len(nums)
        presum=[0]*length
        res=0
        count={0:1}
        precount=0
        for num in nums:
            if num%modulo==k:
                precount+=1

            target=(precount-k+modulo)%modulo      
            res+=count.get(target,0)
            count[precount%modulo]=count.get(precount%modulo,0)+1
        
        return res
        
