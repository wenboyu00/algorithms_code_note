"""
子串不连续
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = dict()
        window = dict()


if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    result = Solution().minWindow(s=s, t=t)
    print(result)
