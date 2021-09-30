from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        题目要求：找到比这个数更大的数中最小的那个，找不到就重新排列成升序排列
        思路：
            把后面的 大数 和前面的 小数 交换，得到一个更大的数
            同时 增加的幅度尽可能小：
                1. 尽可能在靠右的低位上交换，因此 从后向前找，找到第一个小数
                2. 将尽可能小的大数 和 找到的 小数 进行交换
                3. 交换后 将大数后面所有的数都反转成升序，升序是最小排列
                4. 如果从后向前到0，依然找不到小数，说明数字是降序，直接反转，刚好接上3的情况
        """

        n = len(nums)
        i = n - 2
        # 从后向前，找到第一个小数，相等是去重
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 找到第一个比 小数大的数
        if i >= 0:
            j = n - 1
            while j > i and nums[i] >= nums[j]:
                j -= 1
            self.swap(nums, i, j)
        # 反转，交换后到尾部的数
        self.reverse(nums, i + 1, n - 1)

    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def reverse(self, nums, low, high):
        while low < high:
            self.swap(nums, low, high)
            low += 1
            high -= 1


if __name__ == '__main__':
    Solution().nextPermutation([1, 2, 3])
    Solution().nextPermutation([1, 2])
