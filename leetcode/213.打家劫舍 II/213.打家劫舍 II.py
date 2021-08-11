from typing import List


class Solution:

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        # 因为首尾不能同时抢，所以把不抢首和不抢尾，分开求值并求最大。
        # 0，n-1:不抢尾，n-1去掉尾部
        # 1，n-1:不抢头，从1开始去掉索引0的头
        return max(self.rob_range(nums, 0, n - 1),
                   self.rob_range(nums, 1, n),
                   )

    def rob_range(self, nums: List[int], start, end):
        # 自子底向上操作
        # 因为需要下下一个房子，所以dp长度为 n + 2， base case=0
        n = len(nums)
        dp = [0] * (n + 2)
        # 长度比索引大1，所以从长度 -1 开始
        # start-1 循环范围前闭后开，不包括start，到start要-1
        # -1 倒叙，从大到小
        for i in range(end - 1, start-2, -1):
            dp[i] = max(dp[i + 1], nums[i] + dp[i + 2])
        return dp[start]


if __name__ == '__main__':
    nums = [1, 2]
    result = Solution().rob(nums)
    print(result)
