# 题目
<p>给定两个整数 <code>n</code> 和 <code>k</code>，返回范围 <code>[1, n]</code> 中所有可能的 <code>k</code> 个数的组合。</p>

<p>你可以按 <strong>任何顺序</strong> 返回答案。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 4, k = 2
<strong>输出：</strong>
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 1, k = 1
<strong>输出：</strong>[[1]]</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= n <= 20</code></li>
	<li><code>1 <= k <= n</code></li>
</ul>
<div><div>Related Topics</div><div><li>数组</li><li>回溯</li></div></div>

# Python

```python
def combine(self, n: int, k: int) -> List[List[int]]:
    track = []
    res = []

    def back_track(start):
        # 满足结束条件，路径数量多大限制数量
        # 多大树底部
        if len(track) == k:
            res.append(list(track))
            return
        # 遍历选择，范围[1~n]
        for i in range(start, n + 1):
            # 做选择
            track.append(i)
            # dfs
            back_track(i + 1)
            # 撤销选择
            track.pop()

    # 范围[1~n] 所以从1开始
    back_track(1)
    return res
```

# Go

```GO
func combine(n int, k int) [][]int {
   track := make([]int, 0, k)
   res := [][]int{}
   var backTrack func(start int)
   backTrack = func(start int) {
      //  满足结束条件,到达树底
      if len(track) == k {
         res = append(res, append(make([]int, 0, 2), track...))
         return
      }
      for i := start; i < n+1; i++ {
         // 做选择
         track = append(track, i)
         // dfs
         backTrack(i + 1)
         // 撤销选择
         track = track[:len(track)-1]
      }
   }
   backTrack(1)
   return res
}
```