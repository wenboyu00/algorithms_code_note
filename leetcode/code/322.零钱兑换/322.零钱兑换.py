"""
状态：目标金额 amount
选择：coins 数组中列出的所有金币面额
函数的定义：凑出总金额amount，至少需要coinChange(coins, amount)枚硬币
base case : amount ==0 是，需要0枚；amount < 0 时 不可能凑出
"""


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
