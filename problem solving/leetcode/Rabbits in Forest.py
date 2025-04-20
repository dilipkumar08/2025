class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count={}
        res=0
        for i in answers:
            if i==0:
                res+=1
            else:
                count[i]=count.get(i,0)+1

        for key,value in count.items():
            key+=1
            res+=((value//key)*key)
            if (value%key):
                res+=key

        return res

            
