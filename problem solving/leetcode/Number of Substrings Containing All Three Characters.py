class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res=0
        length=len(s)
        for i in range(2,length):
            lib={'a':0,'b':0,'c':0}
            for temp in s[:i+1]:
                lib[temp]+=1
            
            if 0 not in lib.values():
                res+=1
            r=0
            l=i
            while l<length-1:
                lib[s[r]]-=1
                r+=1
                l+=1
                lib[s[l]]+=1
                if 0 not in lib.values():
                    res+=1

        return res
                
            

        
        
