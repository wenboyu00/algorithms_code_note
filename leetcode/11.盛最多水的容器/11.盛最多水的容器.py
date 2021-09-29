from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        水的高度有最短板决定，面积公式：min(h[i],h[j]) * (j-1)
        - 高度  min(h[i],h[j])，
        - 宽度 j-1
        初始化左右双指针在两端
        循环时，更新最大面积，并把短板往前进一步，以获得更大的面积
        """
        left = 0
        right = len(height) - 1
        res = 0
        while left < right:
            # 水的面积
            area = min(height[left], height[right]) * (right - left)
            res = max(res, area)
            # 短板向前进一步
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res
