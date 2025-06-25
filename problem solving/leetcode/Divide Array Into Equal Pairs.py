class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        l=len(nums)
        if l%2!=0:
            return False
        else:
            pairs=l/2
            collection={}
            for i in range(l):
                collection[nums[i]]=collection.get(nums[i],0)+1
            print(collection)
            for j in collection.values():
                if j%2!=0:
                    return False
            
            return True
