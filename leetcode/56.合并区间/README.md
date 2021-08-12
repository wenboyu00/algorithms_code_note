# 题目
<p>以数组 <code>intervals</code> 表示若干个区间的集合，其中单个区间为 <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code> 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>intervals = [[1,3],[2,6],[8,10],[15,18]]
<strong>输出：</strong>[[1,6],[8,10],[15,18]]
<strong>解释：</strong>区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>intervals = [[1,4],[4,5]]
<strong>输出：</strong>[[1,5]]
<strong>解释：</strong>区间 [1,4] 和 [4,5] 可被视为重叠区间。</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= intervals.length <= 10<sup>4</sup></code></li>
	<li><code>intervals[i].length == 2</code></li>
	<li><code>0 <= start<sub>i</sub> <= end<sub>i</sub> <= 10<sup>4</sup></code></li>
</ul>
<div><div>Related Topics</div><div><li>数组</li><li>排序</li></div></div>

# Python

```python
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    # 按照左端升序排序
    intvs = sorted(intervals, key=lambda x: [x[0], -x[1]])
    # x.左端是最小，x.右端是最大。从列表中找到更大的x.右端加上去
    res = [intvs[0]]
    for cur in intvs[1:]:
        # 取出结果的最后一个
        last = res[-1]
        # 当前的左小于最后结果的右，说明交叉区间，拿到他们两个最大的右，作为新的右。
        if cur[0] <= last[1]:
            last[1] = max(last[1], cur[1])
        # 当前左大于 结果右，说明不相交，是一个新的区间。添加到结果列表。
        else:
            res.append(cur)
    return res
```

# Go

```go
func merge(intervals [][]int) [][]int {
   less := func(i, j int) bool {
      return intervals[i][0] <= intervals[j][0]
   }
   // 进行排序
   sort.Slice(intervals, less)
   res := [][]int{intervals[0]}
   for i := 1; i < len(intervals); i++ {
      cur := intervals[i]
      last := res[len(res)-1]
      if cur[0] <= last[1] {
         last[1] = max(cur[1], last[1])
      } else {
         res = append(res, cur)
      }
   }
   return res
}
```