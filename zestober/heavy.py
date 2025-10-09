class Solution:
	def findHeaviestCrate(self, crates: list[int]) -> int:
 		
 		if crates:
 		    length=len(crates)
 		    if length==1:
 		        return 0
 		    elif length==2:
 		        if crates[0]>crates[1] or crates[0]==crates[1]:
 		            return 0
 		        else:
 		            return 1
 		    else:
 		        max_index=0
 		        current_max=crates[0]
 		        for index in range(1,length):
 		            if crates[index]>current_max:
 		                current_max=crates[index]
 		                max_index=index
 		        return max_index
 		else:
 		    return "Please provide a valid list of values"

if __name__ == "__main__":
	solution = Solution()
	print(solution.findHeaviestCrate([50, 75, 20, 75, 60]))	# Expected: 1
	print(solution.findHeaviestCrate([10, 20, 30, 40, 50]))	# Expected: 4
