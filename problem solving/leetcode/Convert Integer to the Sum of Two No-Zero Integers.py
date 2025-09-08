class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        
        for num1 in range(n):
            if '0' in str(num1):
                continue
            for num2 in range(n):
                if num1+num2 == n and ('0' not in str(num2)):
                    return [num1,num2]
