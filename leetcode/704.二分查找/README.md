# 题目

<p>给定一个&nbsp;<code>n</code>&nbsp;个元素有序的（升序）整型数组&nbsp;<code>nums</code> 和一个目标值&nbsp;<code>target</code> &nbsp;，写一个函数搜索&nbsp;<code>nums</code>&nbsp;中的 <code>target</code>，如果目标值存在返回下标，否则返回 <code>-1</code>。</p>

<p><br>
<strong>示例 1:</strong></p>

<pre><strong>输入:</strong> <code>nums</code> = [-1,0,3,5,9,12], <code>target</code> = 9
<strong>输出:</strong> 4
<strong>解释:</strong> 9 出现在 <code>nums</code> 中并且下标为 4
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> <code>nums</code> = [-1,0,3,5,9,12], <code>target</code> = 2
<strong>输出:</strong> -1
<strong>解释:</strong> 2 不存在 <code>nums</code> 中因此返回 -1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li>你可以假设 <code>nums</code>&nbsp;中的所有元素是不重复的。</li>
	<li><code>n</code>&nbsp;将在&nbsp;<code>[1, 10000]</code>之间。</li>
	<li><code>nums</code>&nbsp;的每个元素都将在&nbsp;<code>[-9999, 9999]</code>之间。</li>
</ol>
<div><div>Related Topics</div><div><li>数组</li><li>二分查找</li></div></div>



# Python

```python
"""
二分查找框架

int binarySearch(int[] nums, int target) {
    int left = 0, right = ...;

    while(...) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            ...
        } else if (nums[mid] < target) {
            left = ...
        } else if (nums[mid] > target) {
            right = ...
        }
    }
    return ...;
}
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [left, right]左右闭区间，大小为len(nums)会越界
        left = 0
        right = len(nums) - 1
        # left <= right的终止条件是left>right ==> left == right +1 ==> 区间写法[right+1, right]，此时区间为空。
        while left <= right:
            # 防止right+left相加太大溢出  left+(right-left)// 2 和 left_right // 2 结果相等
            mid = left + (right - left) // 2
            # 因为mid==target已经判断过了，所以区间变成了 [left, mid-1] or [mid+1, right]
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return -1
```

# Go

```go
func search(nums []int, target int) int {
   left := 0
   right := len(nums) - 1
   for left <= right {
      mid := left + (right-left)/2
      if nums[mid] == target {
         return mid
      } else if nums[mid] < target {
         left = mid + 1
      } else if nums[mid] > target {
         right = mid - 1
      }
   }
   return -1
}
```