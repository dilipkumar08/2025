class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res=""
        for i in range(len(nums)):
            if nums[i][i]=="0":
                temp="1"
            else:
                temp="0"
            res+=temp
        return res
