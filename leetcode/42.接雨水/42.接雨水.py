from typing import List


class Solution:
    """
    对于当前i，水最大高度等于i两边的最大高度的最小值，水量高度减去 height[i]
    使用动态规划方法，得到每个位置两边的最大高度。
    再遍历，得到水量并累加
    """

    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        # 初始化备忘录
        # 备忘录为索引i的左、右的最大高度
        l_max = [0] * n
        r_max = [0] * n
        # base case，
        # 左最大0为 height[0], 右最大[-1] = height[-1]
        l_max[0] = height[0]
        r_max[-1] = height[-1]
        # 从左到右计算，得到索引i的左最大高度，跳过base case
        for i in range(1, n):
            l_max[i] = max(height[i], l_max[i - 1])
        # 从右到左计算，得到索引i的右最大高度，跳过base case
        for i in range(n - 2, -1, -1):
            r_max[i] = max(height[i], r_max[i + 1])
        # 计算答案
        # 水的高度 = 左右高度最小值。水量 = 水高度 - 当前高度i
        # 最高累加 = 总水量
        res = 0
        for i in range(n):
            res += min(l_max[i], r_max[i]) - height[i]
        return res


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(Solution().trap(height))
