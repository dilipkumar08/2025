import math
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        symmetric_count=0
        for integers in range(low,high+1):
            l=(math.floor(math.log10(integers)) + 1)
            if l%2==0:
                mid=l//2
                check_symmetric=0

                for i in range(l):
                    if i<mid:
                        check_symmetric+=integers%10
                        integers=integers//10
                    else:
                        check_symmetric-=integers%10
                        integers=integers//10
                if check_symmetric==0:
                    symmetric_count+=1
        return symmetric_count
                
        


        
