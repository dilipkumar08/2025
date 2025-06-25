class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l,r=1,ranks[0]*cars*cars

        def get_count(time):
            count=0
            for i in ranks:
                count+=int(sqrt(time/i))
            return count
        res=-1
        while(l<=r):
            time=(l+r)//2
            repaired=get_count(time)
            if repaired>=cars:
                r=time-1
                res=time
            else:
                l=time+1
        return res
