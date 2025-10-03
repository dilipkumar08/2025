class Solution:
	def countCrownWords(self, words: list[str]) -> int:
	    crownWordsCount=0
	    if list:
	        for word in words:
	            length=len(word)
	            if length==1:
	                crownWordsCount+=1
	            elif length>1:
	                if word[0]==word[length-1]:
	                    crownWordsCount+=1
	        return crownWordsCount
	    else:
	        print("Please provide a valid list with words")
	       
if __name__ == "__main__":
	solution = Solution()
	print(solution.countCrownWords(["apple", "civic", "crown", "aba"]))    
	# Expected: 2

	print(solution.countCrownWords(["noon", "level", "moon", "night", "racecar"]))  
	# Expected: 3

	print(solution.countCrownWords(["a", "b", "c", "aa", "bb", "ab"]))  
	# Expected: 5
