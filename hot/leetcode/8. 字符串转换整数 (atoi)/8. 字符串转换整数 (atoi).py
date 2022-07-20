"""
1.去掉前段空格
2.判断正负号
3.连续把字符串专为数字
4.溢出判断
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31
        res = 0
        sign = 1
        start = 0
        # 去掉前段空格
        while start < len(s) and s[start] == ' ':
            start += 1
        if start == len(s):
            return 0
        # 判断正负号
        if s[start] == '-':
            sign = -1
            start += 1
        elif s[start] == '+':
            start += 1
        # 连续把字符串专为数字，并*正负号
        while start < len(s) and s[start].isdigit():
            res = res * 10 + int(s[start])
            start += 1
        res *= sign
        # 溢出判断
        if res > MAX_INT:
            return MAX_INT
        if res < MIN_INT:
            return MIN_INT
        return res


if __name__ == '__main__':
    s = "42"
    print(Solution().myAtoi(s))
