# 题目
<p>你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 <strong>围成一圈</strong> ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，<strong>如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警</strong> 。</p>

<p>给定一个代表每个房屋存放金额的非负整数数组，计算你 <strong>在不触动警报装置的情况下</strong> ，今晚能够偷窃到的最高金额。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,3,2]
<strong>输出：</strong>3
<strong>解释：</strong>你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,1]
<strong>输出：</strong>4
<strong>解释：</strong>你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [0]
<strong>输出：</strong>0
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 100</code></li>
	<li><code>0 <= nums[i] <= 1000</code></li>
</ul>
<div><div>Related Topics</div><div><li>数组</li><li>动态规划</li></div></div>

# Python

```python
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
```

# go

```go
func rob(nums []int) int {
   n := len(nums)
   if n == 1 {
      return nums[0]
   }
   return max(robRange(nums, 0, n-1), robRange(nums, 1, n))
}

func robRange(nums []int, start int, end int) int {
   n := len(nums)
   dp := make([]int, n+2)
   for i := end - 1; i > start-1; i-- {
      dp[i] = max(dp[i+1], nums[i]+dp[i+2])

   }
   return dp[start]
}
```