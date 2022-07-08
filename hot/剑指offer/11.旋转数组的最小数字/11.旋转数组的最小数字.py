from typing import List

"""
二分法，在有序数组中到某值。
旋转点做为有序数组的最小值。旋转后，左边都是大于等于最小值，右边都是小于等于最小值，排除左边和右边区域就可以找到最小值。
根据二分进行查找
 - nums[mid]<nums[right]时nums[mid]是最小值右侧的元素，忽略这次右边区域 ,不排除mid是否最小值，所以 right = mid
 - nums[mid]>nums[right]时nums[mid]是最小值左侧的元素，忽略这次左边区域 ,可以排除mid是否最小值，所以 left = mid+1
    - 因为最小值左侧是 大于等于最小值且有序的，nums[mid]肯定大于 最小值 可以排除
 - nums[mid]==nums[right]时无法确定nums[mid]是左侧还是右侧。因为右侧是不存在最小值,减少最右边使其逼近最小值。right -= 1
"""


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        # 二分查找
        left = 0
        right = len(numbers) - 1
        while left <= right:
            mid = left + (right - left) // 2
            # 忽略右侧区域
            if numbers[mid] < numbers[right]:
                right = mid
            # 忽略左侧区域
            elif numbers[mid] > numbers[right]:
                left = mid + 1
            # 相等时，让right-=1 使其逼近最小值
            else:
                right -= 1
        return numbers[left]
