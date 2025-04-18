class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        elif n==2:
            return "11"
        else:
            res="11"
            i=0
            while i<n-2:
                temp=''
                word=''
                count=0
                for al in res:
                    if word!=al:
                        if count!=0:
                            temp+=str(count)+word
                        word=al
                        count=1
                    else:
                        count+=1
                temp+=str(count)+word
                res=temp
                i+=1
            return res
                        
      
