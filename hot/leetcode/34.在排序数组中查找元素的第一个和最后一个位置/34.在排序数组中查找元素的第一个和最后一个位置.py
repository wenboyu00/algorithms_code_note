from typing import List
"""
根据基础二分查询
修改：
 - 相等后，锁定所求边界，推进另外一边
 - 检查是否越界，值相等
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_index = self.left_bound(nums, target)
        right_index = self.right_bound(nums, target)
        return [left_index, right_index]

    def left_bound(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                # 相等后，继续把右边界向前推，锁定左边界
                right = mid - 1
        # 检测越界，值相等
        if left >= len(nums) or nums[left] != target:
            return -1
        return left

    def right_bound(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                # 相等后，继续把左边界向后推，锁定右边界
                left = mid + 1
        # 检查边界，值相等
        if right < 0 or nums[right] != target:
            return -1
        return right


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    result = Solution().searchRange(nums=nums, target=target)
    print(result)
