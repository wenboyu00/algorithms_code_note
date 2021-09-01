package main

import (
	"container/heap"
	"sort"
)

/*
定义类型，用Sort.InSlice做容器，实现heap的Push和Pop接口实现heap功能，完成大小堆的使用
heap 是最小堆，所以最大堆是用负值来实现
注意：最大堆的值和到最小堆中的符号转换
*/
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

type MedianFinder struct {
	// small是最大堆，放是小值
	// large是最小堆，放的大值
	// large和small对接的时候 就是中位数的位置
	small, large *hp
}

/** initialize your data structure here. */
func Constructor() MedianFinder {
	return MedianFinder{
		small: &hp{},
		large: &hp{},
	}
}

func (this *MedianFinder) AddNum(num int) {
	if this.small.Len() >= this.large.Len() {
		heap.Push(this.small, -num)
		heap.Push(this.large, -heap.Pop(this.small).(int))
	} else {
		heap.Push(this.large, num)
		heap.Push(this.small, -heap.Pop(this.large).(int))
	}

}

func (this *MedianFinder) FindMedian() float64 {
	if this.small.Len() > this.large.Len() {
		return float64(-this.small.IntSlice[0])
	} else if this.large.Len() > this.small.Len() {
		return float64(this.large.IntSlice[0])
	}
	// float/2 结果是float，int/2 还是int
	return float64(-this.small.IntSlice[0]+this.large.IntSlice[0]) / 2
}

func main() {
	mf := Constructor()
	mf.AddNum(1)
	mf.AddNum(2)
	println(mf.FindMedian())
	mf.AddNum(3)
	println(mf.FindMedian())
}
