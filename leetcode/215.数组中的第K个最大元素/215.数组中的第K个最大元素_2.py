import random
from typing import List

"""
快排解法
双指针+分治
双指针：随机一个基准点(base)，把比base大的放base右边，比base小放base左边，最后返回 base的index(位置)
分治: 找第topk大，
    - index==k，找到topk大，返回
    - index < k, index偏小，递归(index+1, right)
    - index > k, index偏大，递归(left, index-1)
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        self.quick_split(nums, n - k, 0, n - 1)
        return nums[n - k]

    def quick_split(self, nums, k, left, right):
        index = self.partition(nums, left, right)
        if index < k:
            self.quick_split(nums, k, index + 1, right)
        elif index > k:
            self.quick_split(nums, k, 0, index - 1)
        else:
            return

    def partition(self, nums, left, right):
        # 随机化初始元素，避免递归树退化
        random_idx = random.randint(left, right)
        # 把初始元素和随机值交换
        nums[left], nums[random_idx] = nums[random_idx], nums[left]
        # 左右指针循环，把base小的放左边，比base小的放右边
        pviot = nums[left]
        i, j = left, right
        while i < j:
            while i < j and nums[j] >= pviot:
                j -= 1
            nums[i] = nums[j]
            while i < j and nums[i] <= pviot:
                i += 1
            nums[j] = nums[i]
        nums[i] = pviot
        # 返回最后pivot的index
        return i


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    result = Solution().findKthLargest(nums, k)
    print(result)
