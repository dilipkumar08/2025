class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i=0
        operations=blocks.count('W')
        while (k+i<=len(blocks)):
            if blocks[i:k+i].count('W')<operations:
                operations=blocks[i:k+i].count('W')
            i+=1
        return operations
            
            
        
