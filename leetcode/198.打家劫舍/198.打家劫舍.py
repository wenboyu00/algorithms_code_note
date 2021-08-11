from typing import List

"""
动态规划问题
选择：打 or 不打
状态：当前房子的索引
base case ： 0，没打劫就没钱
状态转移方程：
dp[i] = max(dp[i+1], nums[i] + dp[i+2])
当前房子 = max(下一个房子不抢，下下一个房子抢），每次都选择最大的，最终就得到最多。
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        # 自子底向上操作
        n = len(nums)
        # 因为需要下下一个房子，所以dp长度为 n + 2， base case=0
        dp = [0] * (n + 2)
        # n-1 长度比索引大1，所以从长度 - 1开始
        # -1 是前闭后开，不包括-1，所以索引到0
        # -1 倒叙，从大到笑
        for i in range(n - 1, -1, -1):
            dp[i] = max(dp[i + 1], nums[i] + dp[i + 2])
        return dp[0]


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    result = Solution().rob(nums)
    print(result)
