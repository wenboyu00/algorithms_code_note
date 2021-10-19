from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        动态规划
        类似：最大子序列和
        dp[i] 当前最大的子序列乘积
        base case
        dp[0]= nums[0]
        转移方程 dp[i] = max(nums[i], dp[i-1]*nums[i])
        """
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            print(nums)
            dp[i] = max(dp[i-1], dp[i - 1] * nums[i])
        return dp[n - 1]


if __name__ == '__main__':
    print(Solution().maxProduct([2, 3, -2, 4]))
