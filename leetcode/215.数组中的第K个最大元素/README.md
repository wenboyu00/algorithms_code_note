# 题目
<p>给定整数数组 <code>nums</code> 和整数 <code>k</code>，请返回数组中第 <code><strong>k</strong></code> 个最大的元素。</p>

<p>请注意，你需要找的是数组排序后的第 <code>k</code> 个最大的元素，而不是第 <code>k</code> 个不同的元素。</p>

<p> </p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> <code>[3,2,1,5,6,4] 和</code> k = 2
<strong>输出:</strong> 5
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> <code>[3,2,3,1,2,4,5,5,6] 和</code> k = 4
<strong>输出:</strong> 4</pre>

<p> </p>

<p><strong>提示： </strong></p>

<ul>
	<li><code>1 <= k <= nums.length <= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code></li>
</ul>
<div><div>Related Topics</div><div><li>数组</li><li>分治</li><li>快速选择</li><li>排序</li><li>堆（优先队列）</li></div></div>



# 二叉堆解法-时间复杂度O(NlogK)

## python

```python
def findKthLargest(self, nums: List[int], k: int) -> int:
    small = []
    for num in nums:
        heapq.heappush(small, num)
        if len(small) > k:
            heapq.heappop(small)
    return small[0]
```

## Go

```go
// 二叉堆解法-小顶堆
type hp struct {
   sort.IntSlice
}

func (h *hp) Push(v interface{}) {
   h.IntSlice = append(h.IntSlice, v.(int))
}
func (h *hp) Pop() interface{} {
   a := h.IntSlice
   v := a[len(a)-1]
   h.IntSlice = a[:len(a)-1]
   return v
}

func findKthLargest(nums []int, k int) int {
   small := &hp{}
   for _, num := range nums {
      heap.Push(small, num)
      if small.Len() > k {
         heap.Pop(small)
      }
   }
   return small.IntSlice[0]
}
```

# 快排解法-O(N)

## Python

```python
"""
快排解法
双指针+分治
双指针：随机一个基准点(base)，把比base大的放base右边，比base小放base左边，最后返回 base的index(位置)
分治: 找第topk大，
    - index==k，找到topk大，返回
    - index < k, index偏小，递归(index+1, right)
    - index > k, index偏大，递归(left, index-1)
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        self.quick_split(nums, n - k, 0, n - 1)
        return nums[n - k]

    def quick_split(self, nums, k, left, right):
        index = self.partition(nums, left, right)
        if index < k:
            self.quick_split(nums, k, index + 1, right)
        elif index > k:
            self.quick_split(nums, k, 0, index - 1)
        else:
            return

    def partition(self, nums, left, right):
        # 随机化初始元素，避免递归树退化
        random_idx = random.randint(left, right)
        # 把初始元素和随机值交换
        nums[left], nums[random_idx] = nums[random_idx], nums[left]
        # 左右指针循环，把base小的放左边，比base小的放右边
        pviot = nums[left]
        i, j = left, right
        while i < j:
            while i < j and nums[j] >= pviot:
                j -= 1
            nums[i] = nums[j]
            while i < j and nums[i] <= pviot:
                i += 1
            nums[j] = nums[i]
        nums[i] = pviot
        # 返回最后pivot的index
        return i
```

## Go

```go
import (
	"math/rand"
)

// 快排解法
func findKthLargest2(nums []int, k int) int {
	n := len(nums)
	// 要求topk大，排序后是升序。
	// k在n-k位置，让index左边为前n-k个小的数，则index右边为前k个大的数
	findKth(nums, n-k, 0, n-1)
	return nums[n-k]
}
func findKth(nums []int, k int, left int, right int) {
	/*
	对比k和index的关系，递归调用
	*/
	index := partition(nums, left, right)
	if index < k {
		findKth(nums, k, index+1, right)

	} else if index > k {
		findKth(nums, k, left, index-1)
	} else {
		return
	}
}
func partition(nums []int, left int, right int) int {
	/*
	随机一个基准点base，把base的小的数放在base前面，大的放在后面。返回base最终的index
	*/
	// 随机一个base值，交换到头部，防止算法退化
	randomIndex := rand.Int() % (right - left + 1) + left
	nums[left], nums[randomIndex] = nums[randomIndex], nums[left]
	// 比base小在前，比base大在后
	base := nums[left]
	i := left
	j := right
	for i < j {
		//从后向前找，找到比base小的数，交换
		for i < j && nums[j] >= base {
			j--
		}
		nums[i] = nums[j]
		// 从前向后，找到比base大的数，交换
		for i < j && nums[i] <= base {
			i++
		}
		nums[j] = nums[i]
	}
	nums[i] = base
	return i
}
```