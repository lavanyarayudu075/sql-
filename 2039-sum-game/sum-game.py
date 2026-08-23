class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)//2
        left = 0
        right = 0
        for i in num[:n]:#left checking
            left += 4.5 if i == "?" else int(i)
        for i in num[n:]: # right checking
            right += 4.5 if i == "?" else int(i)
        return left != right



        