class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        if n<=2:
            return 0
        else:
            length=len(buildings)
            res=0
            for idx in range(length):
                x,y=buildings[idx]
                xr=False
                xl=False
                yt=False
                yb=False
                for idx1 in range(length):
                    if idx1==idx:
                        continue
                    x1,y1=buildings[idx1]
                    if x1==x and y1<y:
                        yb=True
                    if x1==x and y1>y:
                        yt=True
                    if y1==y and x1>x:
                        xr=True
                    if y1==y and x1<x:
                        xl=True
                    if xl and xr and yb and yt:
                        res+=1
                        break


            return res
                
# another solution
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        if n<=2:
            return 0
        else:
            building_set=set()
            for x,y in buildings:
                building_set.add((x,y))
            
            res=0


            for x,y in buildings:
                left=any((i,y) in building_set for i in range(1,x))
                right=any((j,y) in building_set for j in range(x+1,n+1))
                top=any((x,k) in building_set for k in range(y+1,n+1))
                bottom=any((x,l) in building_set for l in range(1,y))

                if left and right and top and bottom:
                    res+=1

            return res
                

  
    
  
