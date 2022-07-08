# 题目
<p>把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。</p>

<p>给你一个可能存在&nbsp;<strong>重复</strong>&nbsp;元素值的数组&nbsp;<code>numbers</code>&nbsp;，它原来是一个升序排列的数组，并按上述情形进行了一次旋转。请返回旋转数组的<strong>最小元素</strong>。例如，数组&nbsp;<code>[3,4,5,1,2]</code> 为 <code>[1,2,3,4,5]</code> 的一次旋转，该数组的最小值为 1。&nbsp;&nbsp;</p>

<p>注意，数组 <code>[a[0], a[1], a[2], ..., a[n-1]]</code> 旋转一次 的结果为数组 <code>[a[n-1], a[0], a[1], a[2], ..., a[n-2]]</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong><code>numbers = </code>[3,4,5,1,2]
<strong>输出：</strong>1
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong><code>numbers = </code>[2,2,2,0,1]
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == numbers.length</code></li>
	<li><code>1 &lt;= n &lt;= 5000</code></li>
	<li><code>-5000 &lt;= numbers[i] &lt;= 5000</code></li>
	<li><code>numbers</code> 原来是一个升序排序的数组，并进行了 <code>1</code> 至 <code>n</code> 次旋转</li>
</ul>

<p>注意：本题与主站 154 题相同：<a href="https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/">https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/</a></p>

# Python

```python
py"""
二分法，在有序数组中到某值。
旋转点做为有序数组的最小值。旋转后，左边都是大于等于最小值，右边都是小于等于最小值，排除左边和右边区域就可以找到最小值。
根据二分进行查找
 - nums[mid]<nums[right]时nums[mid]是最小值右侧的元素，忽略这次右边区域 ,不排除mid是否最小值，所以 right = mid
 - nums[mid]>nums[right]时nums[mid]是最小值左侧的元素，忽略这次左边区域 ,可以排除mid是否最小值，所以 left = mid+1
    - 因为最小值左侧是 大于等于最小值且有序的，nums[mid]肯定大于 最小值 可以排除
 - nums[mid]==nums[right]时无法确定nums[mid]是左侧还是右侧。因为右侧是不存在最小值,减少最右边使其逼近最小值。right -= 1
"""


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        # 二分查找
        left = 0
        right = len(numbers) - 1
        while left <= right:
            mid = left + (right - left) // 2
            # 忽略右侧区域
            if numbers[mid] < numbers[right]:
                right = mid
            # 忽略左侧区域
            elif numbers[mid] > numbers[right]:
                left = mid + 1
            # 相等时，让right-=1 使其逼近最小值
            else:
                right -= 1
        return numbers[left]

```

# Go

```go
func minArray(numbers []int) int {
   left := 0
   right := len(numbers) - 1
   for left <= right {
      mid := left + (right-left)/2
      if numbers[mid] < numbers[right]{
         right = mid
      }else if numbers[mid]> numbers[right]{
         left = mid+1
      }else {
         right -= 1
      }
   }
   return numbers[left]
}
```

