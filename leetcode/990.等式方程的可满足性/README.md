# 题目
<p>给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 <code>equations[i]</code> 的长度为 <code>4</code>，并采用两种不同的形式之一：<code>&quot;a==b&quot;</code> 或&nbsp;<code>&quot;a!=b&quot;</code>。在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。</p>

<p>只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回&nbsp;<code>true</code>，否则返回 <code>false</code>。&nbsp;</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[&quot;a==b&quot;,&quot;b!=a&quot;]
<strong>输出：</strong>false
<strong>解释：</strong>如果我们指定，a = 1 且 b = 1，那么可以满足第一个方程，但无法满足第二个方程。没有办法分配变量同时满足这两个方程。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[&quot;b==a&quot;,&quot;a==b&quot;]
<strong>输出：</strong>true
<strong>解释：</strong>我们可以指定 a = 1 且 b = 1 以满足满足这两个方程。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>[&quot;a==b&quot;,&quot;b==c&quot;,&quot;a==c&quot;]
<strong>输出：</strong>true
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>[&quot;a==b&quot;,&quot;b!=c&quot;,&quot;c==a&quot;]
<strong>输出：</strong>false
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>[&quot;c==c&quot;,&quot;b==d&quot;,&quot;x!=z&quot;]
<strong>输出：</strong>true
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= equations.length &lt;= 500</code></li>
	<li><code>equations[i].length == 4</code></li>
	<li><code>equations[i][0]</code> 和&nbsp;<code>equations[i][3]</code>&nbsp;是小写字母</li>
	<li><code>equations[i][1]</code> 要么是&nbsp;<code>&#39;=&#39;</code>，要么是&nbsp;<code>&#39;!&#39;</code></li>
	<li><code>equations[i][2]</code>&nbsp;是&nbsp;<code>&#39;=&#39;</code></li>
</ol>
<div><div>Related Topics</div><div><li>并查集</li><li>图</li><li>数组</li><li>字符串</li></div></div>

# Python

```python
"""
如果a==b和b==c成立，则a==c也成立，因此我们可以使用并查集来维护这种连通关系
1.遍历所有等式，构造并查集。相等值是在一个集，共有一个parent
2.遍历所有不等式，查找两个值的是否是同一parent，如果是则冲突，就返回False
3.遍历完所以不等式发现没有矛盾，则返回True
"""


class Solution:
    class UnionFind:
        def __init__(self):
            # 26个小写字母
            self.parent = list(range(26))

        # 递归构造，并压缩
        def find(self, index):
            # 如果父节点是自身，说明该变量为根节点
            if index == self.parent[index]:
                return index
            # 沿着当前变量的父节点一路向上查找，直到找到根节点。
            self.parent[index] = self.find(self.parent[index])
            return self.parent[index]

        # 合并，将index1的根节点 指向 index2的根节点
        def union(self, index1, index2):
            self.parent[self.find(index1)] = self.find(index2)

    def equationsPossible(self, equations: List[str]) -> bool:
        uf = Solution.UnionFind()
        for st in equations:
            if st[1] == "=":
                # ord把字符串转换成数字，缩小范围便于计算
                # 字符相减实质是ascll码值相减 所有a~z 减去a之后 的范围是0~25
                index1 = ord(st[0]) - ord("a")
                index2 = ord(st[3]) - ord("a")
                uf.union(index1, index2)

        for st in equations:
            if st[1] == "!":
                index1 = ord(st[0]) - ord("a")
                index2 = ord(st[3]) - ord("a")
                if uf.find(index1) == uf.find(index2):
                    return False
        return True
```

# Go

```go
func equationsPossible(equations []string) bool {
   // 初始化并查集合数组
   parent := make([]int, 26)
   for i := 0; i < 26; i++ {
      parent[i] = i
   }
   // 相等，连通
   for _, str := range equations {
      if str[1] == '=' {
         // -'a' 后范围是0~25 刚好和parent数组长度一致，节省空间
         index1 := int(str[0] - 'a')
         index2 := int(str[3] - 'a')
         union(parent, index1, index2)
      }
   }
   // 不相等，判断根节点是否一致，一致表示已经相等过，等式不成立 False
   for _, str := range equations {
      if str[1] == '!' {
         index1 := int(str[0] - 'a')
         index2 := int(str[3] - 'a')
         if find(parent, index1) == find(parent, index2) {
            return false
         }
      }
   }
   return true
}

func union(parent []int, index1, index2 int) {
   parent[find(parent, index1)] = find(parent, index2)
}
func find(parent []int, index int) int {
   for parent[index] != index {
      parent[index] = parent[parent[index]]
      index = parent[index]
   }
   return parent[index]
}
```

