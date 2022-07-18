from typing import List

"""
比较nums[mid]与nums[mid+1]，left==right 循环结束
大于时,在[l, mid]  必然存在峰值。nums[mid]相对大，所以保留
小于时,在[mid+1, r]必然存在峰值
"""


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        # 相等时结束循环
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    print(Solution().findPeakElement(nums))
