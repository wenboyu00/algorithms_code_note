# 题目
<p>给你一个含 <code>n</code> 个整数的数组 <code>nums</code> ，其中 <code>nums[i]</code> 在区间 <code>[1, n]</code> 内。请你找出所有在 <code>[1, n]</code> 范围内但没有出现在 <code>nums</code> 中的数字，并以数组的形式返回结果。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [4,3,2,7,8,2,3,1]
<strong>输出：</strong>[5,6]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1]
<strong>输出：</strong>[2]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 <= n <= 10<sup>5</sup></code></li>
	<li><code>1 <= nums[i] <= n</code></li>
</ul>

<p><strong>进阶：</strong>你能在不使用额外空间且时间复杂度为<em> </em><code>O(n)</code><em> </em>的情况下解决这个问题吗? 你可以假定返回的数组不算在额外空间内。</p>
<div><div>Related Topics</div><div><li>数组</li><li>哈希表</li></div></div>

# Python

```python
"""
遍历用set进行保存
再生成1~n+1的数值，进行查找，如果不存在就存入结果集
"""


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        nums_set = set()
        for num in nums:
            nums_set.add(num)

        for i in range(1, n + 1):
            if i not in nums_set:
                res.append(i)

        return res
```

# Go

```go
func findDisappearedNumbers(nums []int) []int {
   n := len(nums)
   res := make([]int, 0, n)
   numsMap := make(map[int]int8, n)
   for _, num := range nums {
      numsMap[num] = 0
   }
   for i := 1; i < n+1; i++ {
      if _, ok := numsMap[i]; !ok {
         res = append(res, i)
      }
   }
   return res
}
```