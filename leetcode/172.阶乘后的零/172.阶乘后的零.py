"""
n! 最多可以分解为 多少个因子2和5
因为2和5相乘结尾是0，又因为每个偶数都能分解出2，2比5数量多，5成了决定性因子
所以，题目转换为求 多少5
因为5的幂数也可以分解为多个5，所以也要求5的幂数
例如：25可以提供2个5因子，125/25=5个25的倍数，它们可以再提供一个因子5
125! = 25+5+1
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        divs = 5
        while divs <= n:
            res += n // divs
            divs *= 5
        return res


if __name__ == '__main__':
    n = 125
    result = Solution().trailingZeroes(n)
    print(result)
