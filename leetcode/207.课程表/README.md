# 题目
<p>你这个学期必须选修 <code>numCourses</code> 门课程，记为 <code>0</code> 到 <code>numCourses - 1</code> 。</p>

<p>在选修某些课程之前需要一些先修课程。 先修课程按数组 <code>prerequisites</code> 给出，其中 <code>prerequisites[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> ，表示如果要学习课程 <code>a<sub>i</sub></code> 则 <strong>必须</strong> 先学习课程  <code>b<sub>i</sub></code><sub> </sub>。</p>

<ul>
	<li>例如，先修课程对 <code>[0, 1]</code> 表示：想要学习课程 <code>0</code> ，你需要先完成课程 <code>1</code> 。</li>
</ul>

<p>请你判断是否可能完成所有课程的学习？如果可以，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>numCourses = 2, prerequisites = [[1,0]]
<strong>输出：</strong>true
<strong>解释：</strong>总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>numCourses = 2, prerequisites = [[1,0],[0,1]]
<strong>输出：</strong>false
<strong>解释：</strong>总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= numCourses <= 10<sup>5</sup></code></li>
	<li><code>0 <= prerequisites.length <= 5000</code></li>
	<li><code>prerequisites[i].length == 2</code></li>
	<li><code>0 <= a<sub>i</sub>, b<sub>i</sub> < numCourses</code></li>
	<li><code>prerequisites[i]</code> 中的所有课程对 <strong>互不相同</strong></li>
</ul>
<div><div>Related Topics</div><div><li>深度优先搜索</li><li>广度优先搜索</li><li>图</li><li>拓扑排序</li></div></div>



# Python

```python
class Solution:
    """
    把问题转换成 有向无环图，求是否有环
    flags 用于标记节点状态
    adjacency 存节点与其他节点关系
    flags[i]:
        - 0: 未被访问过
        - 1: 已经当前节点访问过
            本轮DFS中被第二次访问过，即图有环，返回False
        - -1: 已经被其他节点访问过
            已经被其他节点访问过，无需重复
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 存储已pre_index为前置课程的课程列表
        adjacency = [[] for _ in range(numCourses)]
        # 当前节点被访问情况
        flags = [0 for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)

        def dfs(idx):
            if flags[idx] == -1:
                return True
            if flags[idx] == 1:
                return False
            flags[idx] = 1
            for j in adjacency[idx]:
                if not dfs(j):
                    return False
            flags[idx] = -1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
```

# Go

```go
func canFinish(numCourses int, prerequisites [][]int) bool {
   edges := make([][]int, numCourses)
   flags := make([]int, numCourses)
   for _, nums := range prerequisites {
      edges[nums[1]] = append(edges[nums[1]], nums[0])
   }

   var dfs func(idx int) bool
   dfs = func(idx int) bool {
      if flags[idx] == -1 {
         return true
      }
      if flags[idx] == 1 {
         return false
      }
      flags[idx] = 1
      for _, j := range edges[idx] {
         if dfs(j) == false {
            return false
         }
      }
      flags[idx] = -1
      return true
   }

   for i := 0; i < numCourses; i++ {
      if dfs(i) == false {
         return false
      }
   }
   return true
}
```