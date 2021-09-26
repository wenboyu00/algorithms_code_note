# 题目
<p>给定 <em>n</em> 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<p><img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/22/rainwatertrap.png" style="height: 161px; width: 412px;" /></p>

<pre>
<strong>输入：</strong>height = [0,1,0,2,1,0,1,3,2,1,2,1]
<strong>输出：</strong>6
<strong>解释：</strong>上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>height = [4,2,0,3,2,5]
<strong>输出：</strong>9
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == height.length</code></li>
	<li><code>0 <= n <= 3 * 10<sup>4</sup></code></li>
	<li><code>0 <= height[i] <= 10<sup>5</sup></code></li>
</ul>
<div><div>Related Topics</div><div><li>栈</li><li>数组</li><li>双指针</li><li>动态规划</li><li>单调栈</li></div></div>

# Python

```python
def trap(self, height: List[int]) -> int:
    if not height:
        return 0
    n = len(height)
    # 初始化备忘录
    # 备忘录为索引i的左、右的最大高度
    l_max = [0] * n
    r_max = [0] * n
    # base case，
    # 左最大0为 height[0], 右最大[-1] = height[-1]
    l_max[0] = height[0]
    r_max[-1] = height[-1]
    # 从左到右计算，得到索引i的左最大高度，跳过base case
    for i in range(1, n):
        l_max[i] = max(height[i], l_max[i - 1])
    # 从右到左计算，得到索引i的右最大高度，跳过base case
    for i in range(n - 2, -1, -1):
        r_max[i] = max(height[i], r_max[i + 1])
    # 计算答案
    # 水的高度 = 左右高度最小值。水量 = 水高度 - 当前高度i
    # 最高累加 = 总水量
    res = 0
    for i in range(n):
        res += min(l_max[i], r_max[i]) - height[i]
    return res
```

# Go

```go
func trap(height []int) int {
   n := len(height)
   if n == 0 {
      return 0
   }
   // 初始化备忘录
   // 备忘录为 索引i的左、右最大高度
   lMax := make([]int, n)
   rMax := make([]int, n)
   // 初始化备忘录 base case
   lMax[0] = height[0]
   rMax[n-1] = height[n-1]
   // 从左到右，得到索引i的左最大高度
   for i := 1; i < n; i++ {
      lMax[i] = max(height[i], lMax[i-1])
   }
   // 从右到左，得到索引i的右最大高度
   for i := n - 2; i > -1; i-- {
      rMax[i] = max(height[i], rMax[i+1])
   }
   // 计算结果
   // 水的高度 = 左右高度最小值。水量 = 水高度 - 当前高度i
   // 最高累加 = 总水量
   res := 0
   for i, h := range height {
      res += min(lMax[i], rMax[i]) - h
   }
   return res
}
```