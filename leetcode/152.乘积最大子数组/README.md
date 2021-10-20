# 题目
<p>给你一个整数数组 <code>nums</code>&nbsp;，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> [2,3,-2,4]
<strong>输出:</strong> <code>6</code>
<strong>解释:</strong>&nbsp;子数组 [2,3] 有最大乘积 6。
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> [-2,0,-1]
<strong>输出:</strong> 0
<strong>解释:</strong>&nbsp;结果不能为 2, 因为 [-2,-1] 不是子数组。</pre>
<div><div>Related Topics</div><div><li>数组</li><li>动态规划</li></div></div><br>

# Python

```python
def maxProduct(self, nums: List[int]) -> int:
    """
    动态规划
    类似：最大子序列和
    不同: 乘法有正负数特性，负负得正，正负的负
    所以：要维护2个变量，最大值和最小值
    动态转移方程：
    - 找到当前节点，最大值和最小值，用于下个节点时应对 乘法特性
    - max_dp = max(max_dp * nums[i], nums[i], min_dp * nums[i])
    - min_dp = min(max_dp * nums[i], nums[i], min_dp * nums[i])
    - 每次遍历后，更新最大值
    base case
    - 最大乘积 = nums[0]
    - 最大值,最小值 = nums[0]
    """
    n = len(nums)
    max_val = nums[0]
    max_dp = nums[0]
    min_dp = nums[0]
    for i in range(1, n):
        max_temp = max_dp
        max_dp = max([max_dp * nums[i], nums[i], min_dp * nums[i]])
        min_dp = min([max_temp * nums[i], nums[i], min_dp * nums[i]])
        max_val = max(max_val, max_dp)
    return max_val
```

# Go

```go
func maxProduct(nums []int) int {
   // 动态规划
   // 乘法正负特性，要维护dp最大值和dp最小值
   n := len(nums)
   maxVal := nums[0]
   maxDp := nums[0]
   minDp := nums[0]
   for i := 1; i < n; i++ {
      maxTemp := maxDp
      maxDp = max(max(maxDp*nums[i], nums[i]), minDp*nums[i])
      minDp = min(min(maxTemp*nums[i], nums[i]), minDp*nums[i])
      maxVal = max(maxVal, maxDp)
   }
   return maxVal
}
func max(int1 int, int2 int) int {
   if int1 < int2 {
      return int2
   } else {
      return int1
   }
}

func min(int1 int, int2 int) int {
   if int1 > int2 {
      return int2
   } else {
      return int1
   }
}
```