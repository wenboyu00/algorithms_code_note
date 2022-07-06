from typing import List

"""
数字看成32位
位值累加，肯定是3倍或者3N+1
3N就是出现三次的数
+1 就是出现一次的数
对每位累加，用3取余，结果就是出现一次的数
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            bit = 0
            for num in nums:
                # 累加 第i位的值
                bit += (num >> i) & 1
            # 对3取余 并把余放到i位上
            res += bit % 3 << i
        return res


if __name__ == '__main__':
    # nums = [9, 1, 7, 9, 7, 9, 7]
    nums = [3, 4, 3, 3]
    print(Solution().singleNumber(nums))
