# 题目
<p>给你一个整数 <code>n</code> ，求恰由 <code>n</code> 个节点组成且节点值从 <code>1</code> 到 <code>n</code> 互不相同的 <strong>二叉搜索树</strong> 有多少种？返回满足题意的二叉搜索树的种数。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/uniquebstn3.jpg" style="width: 600px; height: 148px;" />
<pre>
<strong>输入：</strong>n = 3
<strong>输出：</strong>5
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 1
<strong>输出：</strong>1
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= n <= 19</code></li>
</ul>
<div><div>Related Topics</div><div><li>树</li><li>二叉搜索树</li><li>数学</li><li>动态规划</li><li>二叉树</li></div></div>

# Python

```python
class Solution:

    def numTrees(self, n: int) -> int:
        memo = [[0] * (n + 1) for i in range(n + 1)]
        # 计算闭区间[1,n]组成的BST个数
        return self.count(1, n, memo)

    def count(self, low, high, memo):
        # base case low>high是空区间，对应节点是空，返回1
        if low > high:
            return 1
        if memo[low][high] != 0:
            return memo[low][high]
        res = 0
        for i in range(low, high + 1):
            # i 的值作为根节点 root
            left = self.count(low, i - 1, memo)
            right = self.count(i + 1, high, memo)
            # 左右子树的组合乘积是BST的总数
            res += left * right
        memo[low][high] = res
        return res
```

# Go

```go
func numTrees(n int) int {
   memo := [][]int{}
   for i := 0; i < n+1; i++ {
      memo = append(memo, make([]int, n+1))
   }
   var count func(low int, high int) int
   count = func(low int, high int) int {
      if low > high {
         return 1
      }
      if memo[low][high] != 0 {
         return memo[low][high]
      }
      res := 0
      for i := low; i <= high; i++ {
         left := count(low, i-1)
         right := count(i+1, high)
         res += left * right
      }
      memo[low][high] = res
      return res
   }
   return count(1, n)
}
```
