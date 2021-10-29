"""
状态：目标金额 amount
选择：coins 数组中列出的所有金币面额
函数的定义：凑出总金额amount，至少需要coinChange(coins, amount)枚硬币
base case : amount ==0 是，需要0枚；amount < 0 时 不可能凑出
"""
from typing import List


class Solution:
    """自底向上迭代解法"""
    def coinChange(self, coins: List[int], amount: int) -> int:
        """dp 数组初始化特殊值 amount + 1
        amount个金额，至少需要amount个硬币，因此大于amount的值属于特殊值"""
        dp = [amount + 1] * (amount + 1)
        # base ase
        dp[0] = 0
        # 外层for循环遍历所有状态（所有金额）的所有取值
        for i in range(len(dp)):
            # 内循环求所有选择（所有金额）的最小值
            for coin in coins:
                # 子问题无解，跳过
                if (i - coin) < 0:
                    continue
                # 状态转移，得出每个金额最小的硬币数
                dp[i] = min(dp[i], 1 + dp[i - coin])
        if dp[amount] == amount + 1:
            return -1
        else:
            return dp[amount]

    """自底向上迭代解法-优化1"""
    def coinChange_1(self, coins: List[int], amount: int) -> int:
        """
        dp数组：dp[i] 凑出总金额i的需要的硬币个数
        转移方程: dp[i] = min(dp[i], 1+dp[i-coin])
            凑出i金额，min(当前个数，dp（当前总额度-硬币额度)+减去金币个数) 取最小的
        base case: dp[0] = 0, 0总额需要0个硬币
        代码优化空间:循环i额度是，从coin开始，减少计算
        注意：amount是总额，求的是最少金币的个数，dp[i]，凑出i总额时的个数
            动态转移方程，（总额-硬币）+ 1个数= 当前总额凑出硬币的个数
        """
        dp = [amount + 1] * (amount + 1)
        # base ase
        dp[0] = 0
        # 外循环求所有选择(所有硬币)
        for coin in coins:
            # 内循环遍历所有状态(所有总金额)的取值
            # 剪枝优化:从coin开始循环，跳过小于coin的总额
            for i in range(coin, amount+1):
                # 状态转移，得出每个金额最小的硬币数
                dp[i] = min(dp[i], 1 + dp[i - coin])
        if dp[amount] == amount + 1:
            return -1
        else:
            return dp[amount]
