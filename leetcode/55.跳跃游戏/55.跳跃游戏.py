from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        动态规划
        dp数组：dp[i]当前最大的跳跃长度
        base case dp[0] = nums[0]
        选择：dp[i+1] = max(dp[i](当前最大跳跃长度), nums[i](跳跃长度) + i(当前位置)
        状态:无
        如果dp[i+1] <= i:
            return False
        return dp[n-1]跳跃距离 >= 最后长度
        """
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(n - 1):
            dp[i + 1] = max(dp[i], i + nums[i])
            if dp[i + 1] <= i:
                return False
        return dp[n - 1] >= n - 1


if __name__ == '__main__':
    print(Solution().canJump(nums=[2, 3, 1, 1, 4]))
    print(Solution().canJump(nums=[3, 2, 1, 0, 4]))
    print(Solution().canJump(nums=[0, 2, 3]))
