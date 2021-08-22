# 题目
<p>给你一个有&nbsp;<code>n</code>&nbsp;个节点的 <strong>有向无环图（DAG）</strong>，请你找出所有从节点 <code>0</code>&nbsp;到节点 <code>n-1</code>&nbsp;的路径并输出（<strong>不要求按特定顺序</strong>）</p>

<p>二维数组的第 <code>i</code> 个数组中的单元都表示有向图中 <code>i</code> 号节点所能到达的下一些节点，空就是没有下一个结点了。</p>

<p>译者注：有向图是有方向的，即规定了 a→b 你就不能从 b→a 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2020/09/28/all_1.jpg" style="height: 242px; width: 242px;" /></p>

<pre>
<strong>输入：</strong>graph = [[1,2],[3],[3],[]]
<strong>输出：</strong>[[0,1,3],[0,2,3]]
<strong>解释：</strong>有两条路径 0 -&gt; 1 -&gt; 3 和 0 -&gt; 2 -&gt; 3
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2020/09/28/all_2.jpg" style="height: 301px; width: 423px;" /></p>

<pre>
<strong>输入：</strong>graph = [[4,3,1],[3,2,4],[3],[4],[]]
<strong>输出：</strong>[[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>graph = [[1],[]]
<strong>输出：</strong>[[0,1]]
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>graph = [[1,2,3],[2],[3],[]]
<strong>输出：</strong>[[0,1,2,3],[0,2,3],[0,3]]
</pre>

<p><strong>示例 5：</strong></p>

<pre>
<strong>输入：</strong>graph = [[1,3],[2],[3],[]]
<strong>输出：</strong>[[0,1,2,3],[0,3]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == graph.length</code></li>
	<li><code>2 &lt;= n &lt;= 15</code></li>
	<li><code>0 &lt;= graph[i][j] &lt; n</code></li>
	<li><code>graph[i][j] != i</code>（即，不存在自环）</li>
	<li><code>graph[i]</code> 中的所有元素 <strong>互不相同</strong></li>
	<li>保证输入为 <strong>有向无环图（DAG）</strong></li>
</ul>
<div><div>Related Topics</div><div><li>深度优先搜索</li><li>广度优先搜索</li><li>图</li><li>回溯</li></div></div>

# Python

```python
class Solution:
    def __init__(self):
        # 记录所有路径
        self.res = []

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path = list()
        self.traverse(graph, 0, path)
        return self.res

    def traverse(self, graph: List[List[int]], s: int, path: List[int]):
        # 添加节点 s 到路径
        path.append(s)
        n = len(graph)
        # base case 到达终点
        if s == n - 1:
            # 把路径添加到结果集中,从路径中移除节点s
            self.res.append([i for i in path])
            path.pop()
            return

        # 递归每个相邻的节点
        for v in graph[s]:
            self.traverse(graph, v, path)
        # 从路径移除节点 s
        path.pop()
```

# Go

```go
func allPathsSourceTarget(graph [][]int) [][]int {
   // 回溯算法，DFS
   res := [][]int{}
   // 储存路径
   path := []int{}

   var traverse func(graph [][]int, s int, path []int)
   traverse = func(graph [][]int, s int, path []int) {
      // 记录路径
      path = append(path, s)
      // base case 到达终点，保存
      if s == len(graph)-1 {
         // 把路径添加到结果集中,从路径中移除节点s
         res = append(res, append([]int{}, path...))
         path = path[:len(path)-1]
         return
      }
      // 递归每个相邻的节点
      for _, v := range graph[s] {
         traverse(graph, v, path)
      }
      // 从路径移除节点 s
      path = path[:len(path)-1]
   }
   traverse(graph,0,path)
   return res
}
```