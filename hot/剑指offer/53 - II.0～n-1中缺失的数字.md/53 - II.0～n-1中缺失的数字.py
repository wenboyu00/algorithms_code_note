"""
在排序数组中搜索一个数，二分法
左子数组， nums[i] = i 那部分
右子数组, nums[i] != i 那部分的
查找右子数组的首位
nums[mid] == mid时，说明在左子数组中，右子数组首位在 [mid+1,left]中,因此 right = mid+1
nums[mid] != mid时, 说明在右子数组中，左子数组的末尾在 [right, m-1]中,因此 left = mid -1

返回值：当right == left时，分别指向左子数组末尾和右子数组的首位，也就是缺失的那个数字
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == mid:
                left = mid + 1
            else:
                right = mid - 1
        return left
