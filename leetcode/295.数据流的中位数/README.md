# 题目
<p>中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。</p>

<p>例如，</p>

<p>[2,3,4]&nbsp;的中位数是 3</p>

<p>[2,3] 的中位数是 (2 + 3) / 2 = 2.5</p>

<p>设计一个支持以下两种操作的数据结构：</p>

<ul>
	<li>void addNum(int num) - 从数据流中添加一个整数到数据结构中。</li>
	<li>double findMedian() - 返回目前所有元素的中位数。</li>
</ul>

<p><strong>示例：</strong></p>

<pre>addNum(1)
addNum(2)
findMedian() -&gt; 1.5
addNum(3) 
findMedian() -&gt; 2</pre>

<p><strong>进阶:</strong></p>

<ol>
	<li>如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？</li>
	<li>如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？</li>
</ol>
<div><div>Related Topics</div><div><li>设计</li><li>双指针</li><li>数据流</li><li>排序</li><li>堆（优先队列）</li></div></div>

# Python

```python
class MedianFinder:

    def __init__(self):
        """
        large列表：小顶堆
        small列表：大顶堆
        heapq.heappush()是往堆中添加新值，此时自动建立了小顶堆
        创建大顶堆每次push时给元素加一个负号
        """
        self.large = list()
        self.small = list()

    def addNum(self, num: int) -> None:
        """
        添加元素，使用堆的方法添加
        谁元素少，就加到它那里（隔山打牛)
            - 先把num添加到 元素多的堆里
            - 再把元素多的堆 对顶添加到元素少的堆里面
        注意：大顶堆值 负号的问题
        """
        small_ = self.small
        large_ = self.large

        if len(small_) >= len(large_):
            heapq.heappush(small_, -num)
            heapq.heappush(large_, -heapq.heappop(small_))
        else:
            heapq.heappush(large_, num)
            heapq.heappush(small_, -heapq.heappop(large_))

    def findMedian(self) -> float:
        """
        查找中值，不需要pop
        谁元素多，谁就是中值
        一样多，顶值相加 / 2
        """
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        return (-self.small[0] + self.large[0]) / 2
```

# Go

```go
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
```