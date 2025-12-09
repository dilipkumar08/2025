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


class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        length=len(nums)
        if length<3:
           return 0
        else:
            res=0
            rightCount=dict()
            leftCount=dict() 
            for num in nums:
                rightCount[num]=rightCount.get(num,0)+1
                leftCount[num]=0

            rightCount[nums[0]]-=1
            leftCount[nums[0]]=1  
            
            for idx in range(1,length-1):
                target=nums[idx]*2
                rightCount[nums[idx]]-=1
                if rightCount.get(target,0)>0 and leftCount.get(target)>0:
                    res+=rightCount[target]*leftCount[target]
                leftCount[nums[idx]]=leftCount.get(nums[idx],0)+1
                
            return res% (10**9 +7)
