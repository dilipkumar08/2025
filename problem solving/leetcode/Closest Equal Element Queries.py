class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        output=[]
        l=len(nums)-1
        if l==0:
            return [-1]
        for i in queries:
            if i==l:
                right=0
            else:
                right=i+1
            if i==0:
                left=l
            else:
                left=i-1
            lres=0
            rres=0
            while right!=i and left!=i:
                rres+=1
                lres+=1
                if nums[right]==nums[i]:
                    output.append(rres)
                    break
                if nums[left]==nums[i]:
                    output.append(lres)
                    break
                if left==0:
                    left=l
                else:
                    left-=1
                if right==l:
                    right=0
                else:
                    right+=1
                if right==i:
                    output.append(-1)
        return output
                    
        
