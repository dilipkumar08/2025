class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix. 
    def spirallyTraverse(self, mat):
        left,right=0,len(mat[0])-1
        top,bottom=0,len(mat)-1
        res=[]
        while top<=bottom and left<=right:
            
            for i in range(left,right+1):
                res.append(mat[top][i])
            top+=1
            for j in range(top,bottom+1):
                res.append(mat[j][right])
            right-=1
            for k in range(right,left-1,-1):
                res.append(mat[bottom][k])
            bottom-=1
            for l in range(bottom,top-1,-1):
                res.append(mat[l][left])
            left+=1
        return res
   
