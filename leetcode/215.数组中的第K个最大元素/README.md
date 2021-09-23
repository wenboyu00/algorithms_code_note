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

