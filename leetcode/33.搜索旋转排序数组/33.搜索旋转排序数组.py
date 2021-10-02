from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        题目要求 logn，暗示二分查找
        在一个旋转后的数组进行二分查找？
        旋转后数组局部是有序的，通过mid和target的关系来找部分有序的地方，进行二分查找。
        如果 nums[left]<= nums[mid]并且 nums[left]<=target<num[mid]时 前半部是有序的，在前半部找，否则去后半找，
        如果 nums[left]> nums[mid]并且 nums[mid]< target<=num[right]时，后半部有序，在后半部找，否则去前半找。
        """
        if not nums:
            return -1
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    nums = [3, 1]
    target = 1
    print(Solution().search(nums, target))
