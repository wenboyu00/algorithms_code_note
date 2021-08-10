# 题目
<p>你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，<strong>如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警</strong>。</p>

<p>给定一个代表每个房屋存放金额的非负整数数组，计算你<strong> 不触动警报装置的情况下 </strong>，一夜之内能够偷窃到的最高金额。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>[1,2,3,1]
<strong>输出：</strong>4
<strong>解释：</strong>偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>[2,7,9,3,1]
<strong>输出：</strong>12
<strong>解释：</strong>偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 100</code></li>
	<li><code>0 <= nums[i] <= 400</code></li>
</ul>
<div><div>Related Topics</div><div><li>数组</li><li>动态规划</li></div></div>



# Python

```python
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
```

# Go

```go
func rob(nums []int) int {
   n := len(nums)
   // base case 默认0
   dp := make([]int, n+2)
   for i := n - 1; i > -1; i-- {
      dp[i] = max(dp[i+1], nums[i]+dp[i+2])

   }
   return dp[0]
}
```