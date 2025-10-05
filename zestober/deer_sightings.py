class Solution:
	def mostSightedDeer(self, sightings: list[int]) -> int:
		if sightings:
		   max_count=0
		   res_tag=sightings[0]
		   sight_count=dict()
		   for tag in sightings:
		       sight_count[tag]=sight_count.get(tag,0)+1
		       if sight_count[tag]>max_count:
		           max_count=sight_count[tag]
		           res_tag=tag
		       if sight_count[tag]==max_count and res_tag>tag:
		           res_tag=tag
		   return res_tag
		else:
		    return "Please provide a valid array of tags"
		       
		pass

if __name__ == "__main__":
	solution = Solution()
	print(solution.mostSightedDeer([101, 102, 101, 103, 102, 101, 104, 103]))  # Expected: 101
	print(solution.mostSightedDeer([201, 202, 201, 202, 203]))                  # Expected: 201
