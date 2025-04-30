class Solution:
    def digits(self,num):
        if num!=0:
            return self.digits(num//10)+1
        else:
            return 0

    def findNumbers(self, nums: List[int]) -> int:
        res=0
        for num in nums:
            if self.digits(num)%2==0:
                res+=1
        
        return res
