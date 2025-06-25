class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        s=sum(nums)
        m=max(nums)
        if m>len(queries):
            return False
        elif s:
            for i,j in queries:
                for index in range(i,j+1):
                    if nums[index]!=0:
                        nums[index]-=1
                        s-=1
                if not s:
                    return True
            return False
        else:
            return True
                


