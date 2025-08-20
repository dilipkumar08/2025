class Solution:
    def isValid(self, word: str) -> bool:
        vowel=False
        consonant=False
        symbols=False
        length=0
        word=word.lower()
        for i in word:
            length+=1
            if i in ['a','e','i','o','u']:
                vowel=True
            elif i in ['b','c','f','d','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']:
                consonant=True
            else:
                try:
                    if int(i)>=0:continue
                except:
                    symbols=True
            
        if (vowel and consonant) and not symbols and length>2:
            return True
        else:
            return False