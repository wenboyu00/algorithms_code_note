class Solution:
    def numSquares(self, n: int) -> int:
        """
        动态规划-类似硬币问题
        从固定的数组里面选数，凑一个值
         - 完全平方数，就是j平方
        base case
        - dp[i]= i 是最坏结果，即i个1相加，凑出当前值
        动态转移方程:
        - dp[i]= min(dp[i], dp[i - j*j]+1)
        - min(当前最坏情况, i-j^2的情况再+1)
            - 加1是加上最小的完全平方数
        """
        dp = [0]
        for i in range(1, n + 1):
            j = 1
            dp.append(i)
            while i - j * j >= 0:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[n]


if __name__ == '__main__':
    n = 13
    print(Solution().numSquares(n))
