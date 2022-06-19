# 题目

<p>找出数组中重复的数字。</p>

<p><br>
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>
[2, 3, 1, 0, 2, 5, 3]
<strong>输出：</strong>2 或 3 
</pre>

<p>&nbsp;</p>

<p><strong>限制：</strong></p>

<p><code>2 &lt;= n &lt;= 100000</code></p>

# Python

```python
def findRepeatNumber(self, nums: List[int]) -> int:
    result = -1
    if not nums:
        return result
    aset = set()
    for num in nums:
        if num in aset:
            result = num
        aset.add(num)
    return result
```

# Go

```go
func findRepeatNumber(nums []int) int {
   result := -1
   if len(nums) == 0{
      return 0
   }
   mapping := make(map[int]int, len(nums))
   for _, num := range nums{
      if _, ok := mapping[num]; ok{
         result = num
      }
      mapping[num] = num
   }
   return result
}
```
