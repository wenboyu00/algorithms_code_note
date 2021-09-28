# 题目
<p>给定一个大小为 <em>n </em>的数组，找到其中的多数元素。多数元素是指在数组中出现次数 <strong>大于</strong> <code>⌊ n/2 ⌋</code> 的元素。</p>

<p>你可以假设数组是非空的，并且给定的数组总是存在多数元素。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>[3,2,3]
<strong>输出：</strong>3</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>[2,2,1,1,1,2,2]
<strong>输出：</strong>2
</pre>

<p> </p>

<p><strong>进阶：</strong></p>

<ul>
	<li>尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。</li>
</ul>
<div><div>Related Topics</div><div><li>数组</li><li>哈希表</li><li>分治</li><li>计数</li><li>排序</li></div></div>

# Python

```python
def majorityElement(self, nums: List[int]) -> int:
    num_count = {}
    n = len(nums)
    half_n = n // 2
    for num in nums:
        count = num_count.get(num, 0) + 1
        if count > half_n:
            return num
        num_count[num] = count
```

# Go

```go
func majorityElement(nums []int) int {
   halfLen := int(len(nums) / 2)
   numCount := make(map[int]int, halfLen+1)
   for _, num := range nums {
      numCount[num] += 1
      count := numCount[num]
      if count > halfLen {
         return num
      }
   }
   return -1
}
```

