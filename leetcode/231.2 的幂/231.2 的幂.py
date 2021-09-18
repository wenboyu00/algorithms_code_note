"""
一个数如果是 2 的指数，那么它的二进制表示一定只含有一个 1：
2^0 = 1 = 0b0001
2^1 = 2 = 0b0010
2^2 = 4 = 0b0100
n&(n-1)去掉唯一的1，就等0
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return n & (n - 1) == 0
