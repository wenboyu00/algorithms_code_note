# 题目


<p>给你一个区间列表，请你删除列表中被其他区间所覆盖的区间。</p>

<p>只有当&nbsp;<code>c &lt;= a</code>&nbsp;且&nbsp;<code>b &lt;= d</code>&nbsp;时，我们才认为区间&nbsp;<code>[a,b)</code> 被区间&nbsp;<code>[c,d)</code> 覆盖。</p>

<p>在完成所有删除操作后，请你返回列表中剩余区间的数目。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>intervals = [[1,4],[3,6],[2,8]]
<strong>输出：</strong>2
<strong>解释：</strong>区间 [3,6] 被区间 [2,8] 覆盖，所以它被删除了。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong>​​​​​​</p>

<ul>
	<li><code>1 &lt;= intervals.length &lt;= 1000</code></li>
	<li><code>0 &lt;= intervals[i][0] &lt;&nbsp;intervals[i][1] &lt;= 10^5</code></li>
	<li>对于所有的&nbsp;<code>i != j</code>：<code>intervals[i] != intervals[j]</code></li>
</ul>
<div><div>Related Topics</div><div><li>数组</li><li>排序</li></div></div>

# Python

```python
def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
    # 按照起点升序排序，起点相同时终点降序
    intvs = sorted(intervals, key=lambda x: [x[0], -x[1]])
    # 记录合并区间的起点和终点
    left, right = intvs[0][0], intvs[0][1]
    res = 0
    for lf, r in intvs[1:]:
        # 找到覆盖区间
        if left <= lf and right >= r:
            res += 1
        # 找到相交区间，合并
        if lf <= right <= r:
            right = r
        # 完全不相交，更新起点和终点
        if right < lf:
            left = lf
            right = r
    return len(intervals) - res
```

# Go

```go
func removeCoveredIntervals(intervals [][]int) int {
   // 排序规则，左端从大到小，右端从小到大
   less := func(i, j int) bool {
      if intervals[i][0] == intervals[j][0] {
         return intervals[i][1] >= intervals[j][1]
      }
      return intervals[i][0] <= intervals[j][0]
   }
   // 进行排序
   sort.Slice(intervals, less)
   // 初始化记录区间
   left := intervals[0][0]
   right := intervals[0][1]
   res := 0
   n := len(intervals)
   for i := 1; i < n; i++ {
      // 记录左端小于当前左，大于当前右，找到覆盖区，数量+1
      if left <= intervals[i][0] && right >= intervals[i][1] {
         res += 1
      }
      // 记录右端在当前左右之间，找到交叉区间，更新记录右端位置为当前右
      if right >= intervals[i][0] &&  right <= intervals[i][1] {
         right = intervals[i][1]
      }
      // 记录右端位置小于当前左端，更新记录区间左右为当前左右
      if right <= intervals[i][0]{
         left = intervals[i][0]
         right = intervals[i][1]
      }
   }
   // 长度-覆盖数量 = 剩余数目
   return n - res
}
```