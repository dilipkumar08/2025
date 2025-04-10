class Solution:
    def numberOfPowerfulInt(start: int, finish: int, limit: int, s: str) -> int:
        level2=True
        int_s=int(s)
        powerfulIntegers=0
        if int_s<=finish:#level1
            l=len(s)
            if len(str(start))<l:
                start=int_s
            print("level1")
            for digits in s:
                if int(digits)>limit:
                    level2=False
                    break
            if level2:
                print(l)
                full_list=[value for value in range(start,finish+1) if str(value)[-l:]==s]
                print(full_list)
                for match in full_list:
                    true_match=True
                    for digit in str(match)[:-l]:
                        if int(digit)>limit:
                            true_match=False
                    if true_match:
                        powerfulIntegers+=1
        if powerfulIntegers:
            return powerfulIntegers
        else:
            return 0
        
