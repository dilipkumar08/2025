class Solution:
   def weaveStrings(self, s1: str, s2: str) -> str:
       res=''
       if s1 and s2:
           length1=len(s1)
           length2=len(s2)
           if length1>length2:
               diff=length2-length1
               for idx in range(length2):
                   res+=s1[idx]+s2[idx]
               res+=s1[diff:]
               return res
                   
           elif length1<length2:
               diff=length1-length2
               for idx in range(length1):
                   res+=s1[idx]+s2[idx]
               res+=s2[diff:]
               return res
           else:
               for idx in range(length2):
                   res+=s1[idx]+s2[idx]
               return res
       else:
          res=s1+s2
          return res
	    
	  
		        
		            

if __name__ == "__main__":
	solution = Solution()
	print(solution.weaveStrings("abc", "pqr"))     # Expected: "apbqcr"
	print(solution.weaveStrings("ab", "pqrs"))     # Expected: "apbqrs"
	print(solution.weaveStrings("abcd", "xy"))     # Expected: "axbycd"
	#There's some issue with the intendation in the editor 
