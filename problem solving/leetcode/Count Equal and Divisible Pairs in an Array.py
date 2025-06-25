class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        records={}
        pairs=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if i!=j:
                    if nums[i]==nums[j]:
                        if (i*j)%k==0:
                            pairs+=1
        
        
        return pairs

        
