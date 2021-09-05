from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 求速度最小，用二分查找
        # 速度最小，耗时最长
        left = 1
        # 速度最大，耗时最短
        right = 1000000000 + 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_hour = self.find_hour(piles, mid)
            # 耗时太多，说明速度太慢，加快速度，下一轮搜索区间[mid+1，right]
            if mid_hour > h:
                left = mid + 1
            # 耗时小，说明速度太快，减慢速度，下一轮搜索区间[left，mid-1]
            else:
                right = mid - 1
        return left

    def find_hour(self, piles: List[int], x: int):
        hour = 0
        for pile in piles:
            # 数量//速度 = 时间（小时）
            hour += pile // x
            # 如果数量//速度有余数，说明还需要一个小时才能吃完。就加上1个小时。
            if pile % x > 0:
                hour += 1
        return hour


if __name__ == '__main__':
    piles = [3, 6, 7, 11]
    H = 8
    result = Solution().minEatingSpeed(piles, H)
    print(result)
