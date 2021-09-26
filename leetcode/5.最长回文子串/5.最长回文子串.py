"""
回文串：正着读和反着读都一样的字符串。
核心：双指针
寻找回文串的思路：从中间向两边扩散来判断回文数
注意：中心为奇数or偶数的情况
思路代码：
for 0 <= i < len(s):
    找到以 s[i] 为中心的回文串
    找到以 s[i] 和 s[i+1] 为中心的回文串
    更新答案
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # 以s[i]为中心的最长回文子串，中心为奇数情况
            s1 = self.palindrome(s, i, i)
            # 以s[i]和s[i+1]为中心的最长回文子串，中心为偶数情况
            s2 = self.palindrome(s, i, i + 1)
            # 结果为最长的子串
            res = self.max_len_str(res, s1)
            res = self.max_len_str(res, s2)
        return res

    def palindrome(self, s, left, right):
        # 防止越界，当左右相等时，向两边展开
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]

    def max_len_str(self, s1, s2):
        # 返回最长的字符串
        if len(s1) > len(s2):
            return s1
        else:
            return s2


if __name__ == '__main__':
    s = "babad"
    print(Solution().longestPalindrome(s))
    # print(Solution().palindrome(s, 1, 1))
