# 题目

<p>一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> [0,1,3]
<strong>输出:</strong> 2
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> [0,1,2,3,4,5,6,7,9]
<strong>输出:</strong> 8</pre>

<p>&nbsp;</p>

<p><strong>限制：</strong></p>

<p><code>1 &lt;= 数组长度 &lt;= 10000</code></p>

# Python

```python
"""
在排序数组中搜索一个数，二分法
左子数组， nums[i] = i 那部分
右子数组, nums[i] != i 那部分的
查找右子数组的首位
nums[mid] == mid时，说明在左子数组中，右子数组首位在 [mid+1,left]中,因此 right = mid+1
nums[mid] != mid时, 说明在右子数组中，左子数组的末尾在 [right, m-1]中,因此 left = mid -1

返回值：当right == left时，分别指向左子数组末尾和右子数组的首位，也就是缺失的那个数字
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == mid:
                left = mid + 1
            else:
                right = mid - 1
        return left
```

# Go

```go
func missingNumber(nums []int) int {
    left := 0
    right := len(nums)-1
    for left <= right{
        mid := left + (right-left) / 2
        if nums[mid] == mid{
            left = mid +1
        }else{
            right = mid- 1
        }
    }
    return left
}
```
