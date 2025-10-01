class Solution:
	def twoLongest(self, lengths: list[int]) -> list[int]:
	    if len(lengths)>1:
	        if lengths[0]>lengths[1]:
	            max1=lengths[0]
	            max2=lengths[1]
	        
	        else:
	           max1=lengths[1]
	           max2=lengths[0]
	       
	        for moustache_length in lengths[2:]:
	            if moustache_length>max1:
	                max1=max2
	                max1=moustache_length
	            elif moustache_length>max2:
	               max2=moustache_length
	       
	        return [max1,max2]
	    else:
	        return "Enter a list of moustache's length greater than 1"
	                
 	# TODO: implement the logic to return the two largest moustache lengths pass

if __name__ == "__main__":
	solution = Solution()
	print(solution.twoLongest([4, 1, 7, 3, 9]))	# Expected: [9, 7]
	print(solution.twoLongest([2, 2, 2]))	# Expected: [2, 2]
	print(solution.twoLongest([1]))
	
