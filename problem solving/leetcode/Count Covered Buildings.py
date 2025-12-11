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
                

  
