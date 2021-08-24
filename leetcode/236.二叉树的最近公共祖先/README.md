# 题目
<p>给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。</p>

<p><a href="https://baike.baidu.com/item/%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88/8918834?fr=aladdin" target="_blank">百度百科</a>中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（<strong>一个节点也可以是它自己的祖先</strong>）。”</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/14/binarytree.png" style="width: 200px; height: 190px;" />
<pre>
<strong>输入：</strong>root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
<strong>输出：</strong>3
<strong>解释：</strong>节点 <code>5 </code>和节点 <code>1 </code>的最近公共祖先是节点 <code>3 。</code>
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/14/binarytree.png" style="width: 200px; height: 190px;" />
<pre>
<strong>输入：</strong>root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
<strong>输出：</strong>5
<strong>解释：</strong>节点 <code>5 </code>和节点 <code>4 </code>的最近公共祖先是节点 <code>5 。</code>因为根据定义最近公共祖先节点可以为节点本身。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>root = [1,2], p = 1, q = 2
<strong>输出：</strong>1
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点数目在范围 <code>[2, 10<sup>5</sup>]</code> 内。</li>
	<li><code>-10<sup>9</sup> <= Node.val <= 10<sup>9</sup></code></li>
	<li>所有 <code>Node.val</code> <code>互不相同</code> 。</li>
	<li><code>p != q</code></li>
	<li><code>p</code> 和 <code>q</code> 均存在于给定的二叉树中。</li>
</ul>
<div><div>Related Topics</div><div><li>树</li><li>深度优先搜索</li><li>二叉树</li></div></div>

# Python

```python
"""
1.此函数是干什么的？
    输入 root , p , q, 返回一个节点
    情况1，如果p和q都是以root为根的树中，返回root
    情况2，如果p和q都不在root为根的树中，返回None
    情况3，如果p或者q 在以root为根的书中，返回存在节点
        - 情况2和情况3 合并返回如果left is None  返回right 反之依然；
         - 保证能返回在以root为根的树中节点和都不存在的情况了
2.函数的参数是干什么的？
函数遍历是root，主要用于状态改变为root.left和root.right
p和q 是固定值
3.递归得到结果该干什么？
递归调用后，做什么”选择“
base case
    - root 为None，返回None
    - root = p或者q， 返回 root
        - 如果 p 或 q 等于root，说明此节点存在root为根的树中，root就是最近的公共祖先
4.遍历顺序？
因为需要左右子树来确定根的状态，所以使用后序遍历
后序遍历是从下到上遍历
"""


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 后续遍历
        # base case
        # 节点为空返回空
        # 如果 p 或 q 等于root，说明此节点存在root为根的树中，root就是最近的公共祖先
        if root is None:
            return root
        if root == q or root == p:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 情况1，p和q都是以root为根的树中，left和right一定分别是p和q
        if left and right:
            return root
        # 情况2和3，p和q都不是，或者其中一个是并返回
        # left不是，返回right，right不是返回left，如果两个都不是，那么返回后也是None
        if left is None:
            return right
        if right is None:
            return left
```

# Go

```go
func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
   if root == nil {
      return root
   }
   if root == q || root == p {
      return root
   }
   left := lowestCommonAncestor(root.Left, p, q)
   right := lowestCommonAncestor(root.Right, p, q)
   if left != nil && right != nil {
      return root
   }
   if left == nil {
      return right
   } else {
      return left
   }
}
```

