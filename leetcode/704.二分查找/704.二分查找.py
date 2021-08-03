from typing import List
"""
二分查找框架

int binarySearch(int[] nums, int target) {
    int left = 0, right = ...;

    while(...) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            ...
        } else if (nums[mid] < target) {
            left = ...
        } else if (nums[mid] > target) {
            right = ...
        }
    }
    return ...;
}
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [left, right]左右闭区间，大小为len(nums)会越界
        left = 0
        right = len(nums) - 1
        # left <= right的终止条件是left>right ==> left == right +1 ==> 区间写法[right+1, right]，此时区间为空。
        while left <= right:
            # 防止right+left相加太大溢出  left+(right-left)// 2 和 left_right // 2 结果相等
            mid = left + (right - left) // 2
            # 因为mid==target已经判断过了，所以区间变成了 [left, mid-1] or [mid+1, right]
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return -1


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    result = Solution().search(nums, target)
    print(result)
