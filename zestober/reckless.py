class Solution:
   def reverseJumps(self, jumps: list[int]) -> list[int]:
      if jumps:
         length=len(jumps)
         if length==1:
            return jumps 
         elif length==2:
         	return [jumps[1],jumps[0]]
         elif length%2==0:
         	 for start_index in range(length):
         	    end_index=length-(start_index)
         	    if end_index==start_index:
         	       break
         	    else:
         	       jumps[start_index],jumps[end_index-1]=jumps[end_index-1],jumps[start_index]
         	 return jumps
         else:
            for start_index in range(length):
                end_index=length-(start_index+1)
                if end_index==start_index:
                    break
                else:
                    jumps[start_index],jumps[end_index]=jumps[end_index],jumps[start_index]
            return jumps
      else:
         return "Please enter a valid list of values"

if __name__ == "__main__":
	solution = Solution()
	print(solution.reverseJumps([3, 5, 2, 8, 6]))	# Expected: [6, 8, 2, 5, 3]
	print(solution.reverseJumps([1, 2, 3]))	# Expected: [3, 2, 1]
