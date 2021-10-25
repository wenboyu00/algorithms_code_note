# 题目
<p>给你一个长度为&nbsp;<em>n</em>&nbsp;的整数数组&nbsp;<code>nums</code>，其中&nbsp;<em>n</em> &gt; 1，返回输出数组&nbsp;<code>output</code>&nbsp;，其中 <code>output[i]</code>&nbsp;等于&nbsp;<code>nums</code>&nbsp;中除&nbsp;<code>nums[i]</code>&nbsp;之外其余各元素的乘积。</p>

<p>&nbsp;</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> <code>[1,2,3,4]</code>
<strong>输出:</strong> <code>[24,12,8,6]</code></pre>

<p>&nbsp;</p>

<p><strong>提示：</strong>题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。</p>

<p><strong>说明: </strong>请<strong>不要使用除法，</strong>且在&nbsp;O(<em>n</em>) 时间复杂度内完成此题。</p>

<p><strong>进阶：</strong><br>
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组<strong>不被视为</strong>额外空间。）</p>
<div><div>Related Topics</div><div><li>数组</li><li>前缀和</li></div></div>

# Python

```python
def productExceptSelf(self, nums: List[int]) -> List[int]:
    """
    避开当前nums[i]的之外的乘积
    计算乘积的时候跳过nums[i]
    - 前缀乘积*后缀乘积，跳过nums[i]
    - 前缀乘积时跳过nums[0]
    - 后缀乘积时跳过nums[-1]
    """
    n = len(nums)
    res, tmp = [1] * n, 1
    # 前缀乘积，下三角，跳过nums[i]
    # 对第一位处理，跳过nums[0]
    for i in range(1, n):
        # 当前结果 = 上一个结果 * 上一个数值
        res[i] = res[i - 1] * nums[i - 1]
    # 后缀乘积，上三角，跳过nums[i]，从后向前
    # 最最后一位处理，跳过nums[-1]
    for i in range(n - 2, -1, -1):
        # 当前结果 = 上一个数值的累计结果 * 当前结果值
        tmp *= nums[i + 1]
        res[i] *= tmp
    return res
```

# Go

```go
func productExceptSelf(nums []int) []int {
   // 计算乘积时跳过 nums[1]
   // 前缀乘积*后缀乘积
   n := len(nums)
   res := make([]int, n)
   for i := 0; i < n; i++ {
      res[i] = 1
   }
   // 前缀乘积，下三角，跳过nums[0]
   for i := 1; i < n; i++ {
      res[i] = res[i-1] * nums[i-1]
   }
   // 后缀乘积，上三角，跳过nums[-1]
   tmp := 1
   for i := n - 2; i > -1; i-- {
      tmp *= nums[i+1]
      res[i] *= tmp
   }
   return res
}
```