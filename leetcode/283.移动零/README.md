# 题目
<p>给定一个数组 <code>nums</code>，编写一个函数将所有 <code>0</code> 移动到数组的末尾，同时保持非零元素的相对顺序。</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> <code>[0,1,0,3,12]</code>
<strong>输出:</strong> <code>[1,3,12,0,0]</code></pre>

<p><strong>说明</strong>:</p>

<ol>
	<li>必须在原数组上操作，不能拷贝额外的数组。</li>
	<li>尽量减少操作次数。</li>
</ol>
<div><div>Related Topics</div><div><li>数组</li><li>双指针</li></div></div>

# Python

```python
"""
1. 移动非零的数据到 队前
    - 快慢指针
    - 快指针遍历数组找到非0的数据，0的索引跳过
    - 慢指针替换非0数据到前排，留下0数组长度在队尾
2. 队尾[slow, n)长度赋值为0
"""
def moveZeroes(self, nums: List[int]) -> None:
    n = len(nums)
    if n == 0:
        return None
    slow = 0
    for fast in range(n):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1
    for i in range(slow, n):
        nums[i] = 0
```

# Go

```go
func moveZeroes(nums []int) {
   n := len(nums)
   if n == 0 {
      return
   }
   slow := 0
   for fast := 0; fast < n; fast++ {
      if nums[fast] != 0 {
         nums[slow] = nums[fast]
         slow += 1
      }
   }
   for i := slow; i < n; i++ {
      nums[i] = 0
   }
}
```