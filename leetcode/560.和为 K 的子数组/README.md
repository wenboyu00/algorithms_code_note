# 题目
<p>给你一个整数数组 <code>nums</code> 和一个整数&nbsp;<code>k</code> ，请你统计并返回该数组中和为&nbsp;<code>k</code><strong>&nbsp;</strong>的连续子数组的个数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1,1], k = 2
<strong>输出：</strong>2
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3], k = 3
<strong>输出：</strong>2
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>-10<sup>7</sup> &lt;= k &lt;= 10<sup>7</sup></code></li>
</ul>
<div><div>Related Topics</div><div><li>数组</li><li>哈希表</li><li>前缀和</li></div></div>

# Python

```python
def subarraySum(self, nums: List[int], k: int) -> int:
    """
    pre_sum_map 记录前缀和出现次数，用于统计, base case {0:1}
    sum_j = sum_i - k 用两数和思路，找到适合的前缀和 sum_j
    从前缀和map找到次数
    """
    pre_sum_map = {0: 1}
    ans = sum_i = 0
    for num in nums:
        sum_i += num
        sum_j = sum_i - k
        # 存在就 ans+1
        if sum_j in pre_sum_map:
            ans += pre_sum_map[sum_j]
        # 更新前缀和map
        pre_sum_map[sum_i] = pre_sum_map.get(sum_i, 0) + 1
    return ans
```

# Go

```go
func subarraySum(nums []int, k int) int {
   preSum := map[int]int{}
   preSum[0] = 1
   ans, sumI := 0, 0
   for _, num := range nums {
      sumI += num
      sumJ := sumI - k
      if _, ok := preSum[sumJ]; ok {
         ans += preSum[sumJ]
      }
      preSum[sumI] += 1
   }
   return ans
}
```

