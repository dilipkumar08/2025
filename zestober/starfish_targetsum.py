class Solution:
	def canReachTarget(self, treasures: list[int], target: int) -> str:
 		if treasures:
 		    length=len(treasures)
 		    for idx1 in range(length):
 		        temp_sum=0
 		        for idx2 in range(idx1,length):
 		            if idx1==0 and idx2==length-1:
 		                break
 		            temp_sum+=treasures[idx2]
 		            if temp_sum==target:
 		                return "Yes"
 		    return "No"
 		else:
 		   return "Please enter a valid list of values"
 		 
 		

if __name__ == "__main__":
	solution = Solution()
	print(solution.canReachTarget([2, 3, 5], 8))	# Expected: Yes
	print(solution.canReachTarget([1, 4, 6], 8))	# Expected: No
	print(solution.canReachTarget([2, 3, 7, 8], 12))	# Expected: Yes
