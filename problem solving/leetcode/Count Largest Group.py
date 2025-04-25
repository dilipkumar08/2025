class Solution:
    def digitssum(self,num):
        if num:
            return num%10 + self.digitssum(num//10)
        return 0
        
    def countLargestGroup(self, n: int) -> int:
        records={}
        for i in range(1,n+1):
            num=self.digitssum(i)
            records[num]=records.get(num,0)+1
    
        largest=max(records.values())
        res=0

        for j in records.values():
            if j==largest:
                res+=1
        return res

        
