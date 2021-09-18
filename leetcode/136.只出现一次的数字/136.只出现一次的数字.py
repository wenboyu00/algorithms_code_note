from typing import List

"""
异或运算
a ^ a = 0
a ^ 0 = a
遍历数组，出现多次的变成了0，出现一次的变成了a，最后值就是a
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res
