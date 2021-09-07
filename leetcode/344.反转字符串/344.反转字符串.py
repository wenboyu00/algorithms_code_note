from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1
        while left < right:
            tmp = s[right]
            s[right] = s[left]
            s[left] = tmp
            left += 1
            right -= 1

