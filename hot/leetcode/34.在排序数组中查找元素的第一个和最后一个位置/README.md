# 题目

<p>给定一个按照升序排列的整数数组 <code>nums</code>，和一个目标值 <code>target</code>。找出给定目标值在数组中的开始位置和结束位置。</p>

<p>如果数组中不存在目标值 <code>target</code>，返回 <code>[-1, -1]</code>。</p>

<p><strong>进阶：</strong></p>

<ul>
	<li>你可以设计并实现时间复杂度为 <code>O(log n)</code> 的算法解决此问题吗？</li>
</ul>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [<code>5,7,7,8,8,10]</code>, target = 8
<strong>输出：</strong>[3,4]</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [<code>5,7,7,8,8,10]</code>, target = 6
<strong>输出：</strong>[-1,-1]</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [], target = 0
<strong>输出：</strong>[-1,-1]</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 <= nums.length <= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code></li>
	<li><code>nums</code> 是一个非递减数组</li>
	<li><code>-10<sup>9</sup> <= target <= 10<sup>9</sup></code></li>
</ul>
<div><div>Related Topics</div><div><li>数组</li><li>二分查找</li></div></div>

# Python

```python
"""
根据基础二分查询
修改：
 - 相等后，锁定所求边界，推进另外一边
 - 检查是否越界，值相等
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_index = self.left_bound(nums, target)
        right_index = self.right_bound(nums, target)
        return [left_index, right_index]

    def left_bound(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                # 相等后，继续把右边界向前推，锁定左边界
                right = mid - 1
        # 检测越界，值相等
        if left >= len(nums) or nums[left] != target:
            return -1
        return left

    def right_bound(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                # 相等后，继续把左边界向后推，锁定右边界
                left = mid + 1
        # 检查边界，值相等
        if right < 0 or nums[right] != target:
            return -1
        return right
```

# Go

```go
func searchRange(nums []int, target int) []int {
   leftIndex := leftBound(nums, target)
   rightIndex := rightBound(nums, target)
   return []int{leftIndex, rightIndex}
}
func leftBound(nums []int, target int) int {
   left := 0
   right := len(nums)
   for left <= right {
      mid := left + (right-left)/2
      if nums[mid] < target {
         left = mid + 1
      } else if nums[mid] > target {
         right = mid - 1
      } else if nums[mid] == target {
         right = mid - 1
      }
   }
   if left >= len(nums) || nums[left] != target {
      return -1
   }
   return left
}

func rightBound(nums []int, target int) int {
   left := 0
   right := len(nums)
   for left <= right {
      mid := left + (right-left)/2
      if nums[mid] > target {
         right = mid - 1
      } else if nums[mid] < target {
         left = mid + 1
      } else if nums[mid] == target {
         left = mid + 1
      }
   }
   if right < 0 || nums[right] != target {
      return -1
   }
   return right
}
```