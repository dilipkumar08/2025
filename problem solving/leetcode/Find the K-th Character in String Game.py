class Solution:
    def kthCharacter(self, k: int) -> str:
        next_alphabet={'a':'b','b':'c','c':'d','d':'e','e':'f','f':'g','g':'h',
        'h':'i','i':'j','j':'k','k':'l','l':'m','m':'n','n':'o','o':'p','p':'q','q':'r',
        'r':'s','s':'t','t':'u','u':'v','v':'w','w':'x','x':'y','y':'z','z':'a'}
        word="a"
        length=1
        while length<k:
            for digit in word:
                word+=next_alphabet[digit]
                length+=1
        
        return word[k-1]