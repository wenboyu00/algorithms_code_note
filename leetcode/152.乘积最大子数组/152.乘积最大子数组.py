from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        动态规划
        类似：最大子序列和
        不同: 乘法有正负数特性，负负得正，正负的负
        所以：要维护2个变量，最大值和最小值
        动态转移方程：
        - 找到当前节点，最大值和最小值，用于下个节点时应对 乘法特性
        - max_dp = max(max_dp * nums[i], nums[i], min_dp * nums[i])
        - min_dp = min(max_dp * nums[i], nums[i], min_dp * nums[i])
        - 每次遍历后，更新最大值
        base case
        - 最大乘积 = nums[0]
        - 最大值,最小值 = nums[0]
        """
        n = len(nums)
        max_val = nums[0]
        max_dp = nums[0]
        min_dp = nums[0]
        for i in range(1, n):
            max_temp = max_dp
            max_dp = max([max_dp * nums[i], nums[i], min_dp * nums[i]])
            min_dp = min([max_temp * nums[i], nums[i], min_dp * nums[i]])
            max_val = max(max_val, max_dp)
        return max_val


if __name__ == '__main__':
    print(Solution().maxProduct([2, 3, -2, 4]))
