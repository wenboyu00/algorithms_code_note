"""
数学规律
digits: 位数
start: 区间起始数字
num: n所在的数字  = start+(n-1)// digits
index: n所在数字的位数 = (n-1)% digits

# 找到 n位所对应的区间
9 * start: 数字数量
digits: 数字位数
相乘 数字所占位数量
if n > 9 * start * digits:

    n -= 9 * start * digits
"""


class Solution:
    def findNthDigit(self, n: int) -> int:
        # 区间起始数字
        start = 1
        # 位数
        digits = 1
        # 找到 n 位对应区间
        while n > 9 * start * digits:
            # n 减去 数字占位数量，因此n是从起始数字start
            n -= 9 * start * digits
            # 增大
            start *= 10
            digits += 1
        # 区间是从1开始计数，因此n-1，除位数
        num = start + (n - 1) // digits
        index = (n - 1) % digits
        return int(str(num)[index])


if __name__ == '__main__':
    n = 11061
    print(Solution().findNthDigit(n))
