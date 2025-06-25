class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        res=set()
        l=len(digits)

        for i in range(l):
            for j in range(l):
                for k in range(l):
                    if i!=j and  j!=k and k!=i:
                        first,second,third=digits[i],digits[j],digits[k]
                        if first!=0 and third%2==0:
                            num=first*100+second*10+third
                            res.add(num)

        return len(res)
        ©leetcode
