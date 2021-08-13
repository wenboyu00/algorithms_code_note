# 题目
<p>给定两个由一些<strong> 闭区间 </strong>组成的列表，<code>firstList</code> 和 <code>secondList</code> ，其中 <code>firstList[i] = [start<sub>i</sub>, end<sub>i</sub>]</code> 而 <code>secondList[j] = [start<sub>j</sub>, end<sub>j</sub>]</code> 。每个区间列表都是成对 <strong>不相交</strong> 的，并且 <strong>已经排序</strong> 。</p>

<p>返回这 <strong>两个区间列表的交集</strong> 。</p>

<p>形式上，<strong>闭区间</strong> <code>[a, b]</code>（其中 <code>a <= b</code>）表示实数 <code>x</code> 的集合，而 <code>a <= x <= b</code> 。</p>

<p>两个闭区间的 <strong>交集</strong> 是一组实数，要么为空集，要么为闭区间。例如，<code>[1, 3]</code> 和 <code>[2, 4]</code> 的交集为 <code>[2, 3]</code> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/01/30/interval1.png" style="width: 700px; height: 194px;" />
<pre>
<strong>输入：</strong>firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
<strong>输出：</strong>[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>firstList = [[1,3],[5,9]], secondList = []
<strong>输出：</strong>[]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>firstList = [], secondList = [[4,8],[10,12]]
<strong>输出：</strong>[]
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>firstList = [[1,7]], secondList = [[3,10]]
<strong>输出：</strong>[[3,7]]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 <= firstList.length, secondList.length <= 1000</code></li>
	<li><code>firstList.length + secondList.length >= 1</code></li>
	<li><code>0 <= start<sub>i</sub> < end<sub>i</sub> <= 10<sup>9</sup></code></li>
	<li><code>end<sub>i</sub> < start<sub>i+1</sub></code></li>
	<li><code>0 <= start<sub>j</sub> < end<sub>j</sub> <= 10<sup>9</sup> </code></li>
	<li><code>end<sub>j</sub> < start<sub>j+1</sub></code></li>
</ul>
<div><div>Related Topics</div><div><li>数组</li><li>双指针</li></div></div>

# Python

```python
"""
1.先排序，题目已经排序
2.观察区间关系
    1.没有交集：b2<a1 or a2 < b2
    2.存在交集：b2>a1 and a2 >b1(没交集取相反操作)
        1.找到交集区间，相交的两个区间中，左端点最大的和右端点最大的
        2.推进两个数组前进对比，谁最右端点小，说明落后，谁进一
"""


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        # 双指针，i对A，j对B
        i, j = 0, 0
        res = []
        while i < len(A) and j < len(B):
            a1, a2 = A[i][0], A[i][1]
            b1, b2 = B[j][0], B[j][1]
            # 找到相交区间，ab的最大左端和最小右端
            if b2 >= a1 and a2 >= b1:
                res.append([max(a1, b1), min(a2, b2)])
            # 谁小 谁前进
            if b2 < a2:
                j += 1
            else:
                i += 1
        return res
```

# Go

```go
func intervalIntersection(a [][]int, b [][]int) [][]int {
   i := 0
   j := 0
   res := [][]int{}
   for i < len(a) && j < len(b) {
      a1 := a[i][0]
      a2 := a[i][1]
      b1 := b[j][0]
      b2 := b[j][1]
      if b2 >= a1 && a2 >= b1 {
         res = append(res, []int{max(a1, b1), min(a2, b2)})
      }
      if b2 < a2 {
         j += 1
      } else {
         i += 1
      }
   }
   return res

}
```