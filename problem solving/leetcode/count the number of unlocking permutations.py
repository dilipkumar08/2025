import math
class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
            length=len(complexity)
            if length==1:
                return 1
            else:
                order=dict()
                zero=complexity[0]
                for computer in complexity:
                    order[computer]=order.get(computer,0)+1
                    if computer<zero:
                        return 0
                
                if order[zero]>1:
                    return 0

                else:
                    result=math.factorial(length-1)
                    return result%(10**9+7) 
            
