class Solution:
	def rotateClockwise(self, arr: list[int], k: int) -> list[int]:
	   if arr:
	       arr_length=len(arr)
	       if k==0 or arr_length-k==0:
	           return arr
	       else:
	           half=abs(k-arr_length)
	           return arr[half:]+arr[:half]
	   else:
	       return "Please enter a valid list of sequence"
	               
	    

if __name__ == "__main__":
	solution = Solution()
	print(solution.rotateClockwise([1, 2, 3, 4, 5], 2))         # Expected: [4, 5, 1, 2, 3]
	print(solution.rotateClockwise([10, 20, 30, 40], 6))        # Expected: [30, 40, 10, 20]
	print(solution.rotateClockwise([1,2,3,5],0))
	print(solution.rotateClockwise([1,2,3],3))
