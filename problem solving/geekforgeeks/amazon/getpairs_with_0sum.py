class Solution:
    def getPairs(self, arr):
        arr.sort()
        l=len(arr)
        ld,rd=0,l-1
        res=[]
        while ld<rd:
            if arr[ld]+arr[rd]==0:
                res.append([arr[ld],arr[rd]])
                ld+=1
                rd-=1
            elif arr[ld]+arr[rd]<0:
                ld+=1
            else:
                rd-=1
            while ld<rd and ld>0 and  arr[ld]==arr[ld-1]:
                ld+=1
            while ld<rd and rd<len(arr)-1 and arr[rd]==arr[rd+1]:
                rd-=1
        return res
