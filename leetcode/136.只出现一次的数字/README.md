# 题目
<p>给定一个<strong>非空</strong>整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。</p>

<p><strong>说明：</strong></p>

<p>你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> [2,2,1]
<strong>输出:</strong> 1
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> [4,1,2,1,2]
<strong>输出:</strong> 4</pre>
<div><div>Related Topics</div><div><li>位运算</li><li>数组</li></div></div>

# Python

```python
"""
异或运算
a ^ a = 0
a ^ 0 = a
遍历数组，出现多次的变成了0，出现一次的变成了a，最后值就是a
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res
```

# Go

```go
func singleNumber(nums []int) int {
   res := 0
   for _, num := range nums {
      res ^= num
   }
   return res
}
```