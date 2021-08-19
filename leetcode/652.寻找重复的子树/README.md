# 题目
<p>给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意<strong>一棵</strong>的根结点即可。</p>

<p>两棵树重复是指它们具有相同的结构以及相同的结点值。</p>

<p><strong>示例 1：</strong></p>

<pre>        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
</pre>

<p>下面是两个重复的子树：</p>

<pre>      2
     /
    4
</pre>

<p>和</p>

<pre>    4
</pre>

<p>因此，你需要以列表的形式返回上述重复子树的根结点。</p>
<div><div>Related Topics</div><div><li>树</li><li>深度优先搜索</li><li>广度优先搜索</li><li>二叉树</li></div></div>



# Go

```go
func findDuplicateSubtrees(root *TreeNode) []*TreeNode {
   memo := make(map[string]int)
   var res []*TreeNode
   // 定义函数参数
   var travers func(root *TreeNode) string
   // 赋值给变量
   travers = func (root*TreeNode) string{
      if root == nil{
      return "#"
   }
      left := travers(root.Left)
      right := travers(root.Right)
      subString := fmt.Sprintf("%s,%s,%d", left, right, root.Val)
      // 存储子树字符串出现次数
      memo[subString] += 1
      // 2次时表示有重复，加入至结果列表
      if memo[subString] == 2{
      res = append(res, root)
   }
      return subString
   }

   travers(root)
   return res
}
```

# Python

```python
class Solution:
    def __init__(self):
        # 存储子树描述字符串，用数量去重，每个子树只有1个
        self.momo = {}
        # 储存结果
        self.res = []

    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        self.travers(root)
        return self.res

    def travers(self, root: TreeNode) -> str:
        # base case
        if root is None:
            return "#"
        # 用后序递归遍历，来描述子树
        left = self.travers(root.left)
        right = self.travers(root.right)
        sub_tree = f'{left},{right},{root.val}'
        # 获得子树字符串在出现次数
        freq = self.momo.get(sub_tree, 0)
        # 为1时，找到相同的树，结果+1，出现次数+1
        if freq == 1:
            self.res.append(root)
        self.momo[sub_tree] = freq + 1

        return sub_tree
```