from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left, right = max(nums), sum(nums)

        while left <= right:
            mid = left + (right - left) // 2
            # mid_m > m, 数组和小了，增加数组和，取右半边
            if self.get_mid_m(nums, mid) > m:
                left = mid + 1
            # mid_m < m, 数组和大了，减少数组和，取左半边。
            # 当mid_m = m，范围内不止一个数，范围继续向左半边收敛，找到最小值。
            else:
                right = mid - 1
        return left

    def get_mid_m(self, nums: List[int], sum_val: int):
        # sum_val是数组和，count是数组数量，cur是当前数组和
        count = 1
        cur = 0
        for num in nums:
            # 如果当前数组大于x数组和时，开启一个新的数组
            if cur + num > sum_val:
                count += 1
                cur = 0
            # 每次都叠加
            cur += num
        return count


if __name__ == '__main__':
    nums = [7, 2, 5, 10, 8]
    m = 2
    result = Solution().splitArray(nums, m)
    print(result)
