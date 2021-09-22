package _15_数组中的第K个最大元素

import (
	"container/heap"
	"sort"
)

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
