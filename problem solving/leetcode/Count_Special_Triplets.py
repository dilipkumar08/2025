class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        length=len(nums)
        if length<3:
           return 0
        else:
            res=0
            for idx1 in range(1,length-1):
                countL,countR=0,0
                for idx2 in range(length):
                    if idx2<idx1 and nums[idx1]*2==nums[idx2]:
                        countL+=1
                    if idx2>idx1 and nums[idx1]*2==nums[idx2]:
                        countR+=1
                if countL>0 and countR>0:
                    res+= countL*countR
                    
        return res
