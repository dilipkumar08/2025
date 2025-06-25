class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        res = list('L' + dominoes + 'R')
        l, r = 0, 1
        while r < len(res):
            if res[r] == '.':
                r += 1
                continue
            elif res[r] == 'L' and res[l] == 'R':
                h = (r - l - 1) // 2
                res[l+1:l+1+h] = ['R'] * h
                res[r-h:r] = ['L'] * h
            elif res[l] == res[r]:
                res[l+1:r] = [res[l]] * (r - l - 1)
            l, r = r, r + 1
        return ''.join(res[1:-1])
