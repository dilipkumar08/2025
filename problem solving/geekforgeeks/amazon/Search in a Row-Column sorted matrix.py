def binarySearch(li :list,target :int,mini:int,maxi:int):
    while (mini<=maxi):
        mid=(maxi+mini)//2
        if li[mid]==target:
            return True
        elif li[mid]<target:
            mini=mid+1
        else:
            maxi=mid-1
    return False
class Solution:
	def matSearch(self, mat, x):
	    if mat:
	        l=len(mat[0])
	        if l==0:
	            return False
	        elif l==1:
	            for li in mat:
	                if li[0]==x:
	                    return True 
    	    else:
    	        for li in mat:
        		    minx=0
                    maxx=l-1
                    if binarySearch(li,x,minx,maxx):
                        return True
    	       
                        
        return False
