class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i=0
        operations=blocks.count('W')
        while (k+i<=len(blocks)):
            if blocks[i:k+i].count('W')<operations:
                operations=blocks[i:k+i].count('W')
            i+=1
        return operations
            
            
#O(n) time and O(1) space         
class Solution:
    def minimumRecolors2(self, blocks: str, k: int) -> int:
        res=k
        recolor=0
        l=0
        for  r in range(len(blocks)):
            if blocks[r]=='W':
                recolor+=1
            if r-l+1==k:
                res=min(res,recolor)
                if blocks[l]=='W':
                    recolor-=1
                l+=1
            if res==0:
                break
        return res

            
            
        
