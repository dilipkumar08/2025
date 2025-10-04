class Solution:
	def countMurkyLetters(self, s: str) -> int:
		word_count=dict()
		if s:
		    if len(s)==1:
		        return 1
		    else:
		        murky_count=0
		        for letter in s:
		            word_count[letter.lower()]=word_count.get(letter.lower(),0)+1
		        for key,value in word_count.items():
		            if value==1:
		               murky_count+=1
		        return murky_count
		else:
		    return "Please provide a valid string."
		        
		    
		    

if __name__ == "__main__":
	solution = Solution()
	print(solution.countMurkyLetters("murky")) # Expected: 5
	print(solution.countMurkyLetters("murmur")) # Expected: 0
	print(solution.countMurkyLetters("AlphaBeta")) # Expected: 6
