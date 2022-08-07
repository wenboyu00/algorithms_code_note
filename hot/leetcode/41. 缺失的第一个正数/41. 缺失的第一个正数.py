"""
O(N) 不符合空间复杂度要求
1. 遍历nums存到哈希表中
2. 遍历正整数是否在哈希表中，正整数 1到len(nums)+1
"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        mapping = {}
        for num in nums:
            mapping[num] = True

        for i in range(1, len(nums) + 1):
            if i not in mapping:
                return i
        return len(nums) + 1
