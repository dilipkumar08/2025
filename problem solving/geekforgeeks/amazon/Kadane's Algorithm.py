class Solution:
    def maxSubArraySum(self, arr):
        maxsum=float('-inf')
        currsum=0
        
        for i in arr:
            currsum+=i
            maxsum=max(currsum,maxsum)
            if currsum<0:
                currsum=0
        return maxsum
