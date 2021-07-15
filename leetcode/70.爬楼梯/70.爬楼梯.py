"""
0层台阶： 1种
1层台阶: 1种
2层台阶: [2, 1+1] 2种
3层台阶：
    先走1层 3-1 = 2层台阶
    先走2层 3-2 = 1层台阶
    dp[3] = dp[3-1] + dp[3-2]
把走n层的需要几种种方法问题推到
    先走1层台阶的方法数和先走2层台阶的方法数
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # 初始化把dp数组存储结果
        dp = [0] * (n + 1)
        # base case
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            # n阶 = n-1阶 + n-2阶
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
