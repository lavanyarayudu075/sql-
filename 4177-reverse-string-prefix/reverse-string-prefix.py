class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        if k<=1 or k>len(s):
            return s
        chars = list(s)
        left = 0
        right = k-1

        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
        return "".join(chars)