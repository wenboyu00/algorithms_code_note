# 二分查找
# 平方根的整数为 s*s <= x的最大s值，也就是求右边界
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
        return right

