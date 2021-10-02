# 题目
<p>整数数组 <code>nums</code> 按升序排列，数组中的值 <strong>互不相同</strong> 。</p>

<p>在传递给函数之前，<code>nums</code> 在预先未知的某个下标 <code>k</code>（<code>0 <= k < nums.length</code>）上进行了 <strong>旋转</strong>，使数组变为 <code>[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]</code>（下标 <strong>从 0 开始</strong> 计数）。例如， <code>[0,1,2,4,5,6,7]</code> 在下标 <code>3</code> 处经旋转后可能变为 <code>[4,5,6,7,0,1,2]</code> 。</p>

<p>给你 <strong>旋转后</strong> 的数组 <code>nums</code> 和一个整数 <code>target</code> ，如果 <code>nums</code> 中存在这个目标值 <code>target</code> ，则返回它的下标，否则返回 <code>-1</code> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [<code>4,5,6,7,0,1,2]</code>, target = 0
<strong>输出：</strong>4
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [<code>4,5,6,7,0,1,2]</code>, target = 3
<strong>输出：</strong>-1</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1], target = 0
<strong>输出：</strong>-1
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 5000</code></li>
	<li><code>-10^4 <= nums[i] <= 10^4</code></li>
	<li><code>nums</code> 中的每个值都 <strong>独一无二</strong></li>
	<li>题目数据保证 <code>nums</code> 在预先未知的某个下标上进行了旋转</li>
	<li><code>-10^4 <= target <= 10^4</code></li>
</ul>

<p> </p>

<p><strong>进阶：</strong>你可以设计一个时间复杂度为 <code>O(log n)</code> 的解决方案吗？</p>
<div><div>Related Topics</div><div><li>数组</li><li>二分查找</li></div></div>



# Python

```python
def search(self, nums: List[int], target: int) -> int:
    """
    题目要求 logn，暗示二分查找
    在一个旋转后的数组进行二分查找？
    旋转后数组局部是有序的，通过mid和target的关系来找部分有序的地方，进行二分查找。
    如果 nums[left]<= nums[mid]并且 nums[left]<=target<num[mid]时 前半部是有序的，在前半部找，否则去后半找，
    如果 nums[left]> nums[mid]并且 nums[mid]< target<=num[right]时，后半部有序，在后半部找，否则去前半找。
    """
    if not nums:
        return -1
    n = len(nums)
    left = 0
    right = n - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
```

# Go

```go
func search(nums []int, target int) int {
   n := len(nums)
   if n == 0 {
      return -1
   }
   left := 0
   right := n - 1
   for left <= right {
      mid := left + (right-left)/2
      if nums[mid] == target {
         return mid
      }
      if nums[left] <= nums[mid] {
         if nums[left] <= target && target < nums[mid] {
            right = mid - 1
         } else {
            left = mid + 1
         }
      } else {
         if nums[mid] < target && target <= nums[right] {
            left = mid + 1
         } else {
            right = mid - 1
         }
      }
   }
   return -1
}
```