# 题目 
<p>输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。</p>

<p>&nbsp;</p>

<p>为了让您更好地理解问题，以下面的二叉搜索树为例：</p>

<p>&nbsp;</p>

<p><img src="https://assets.leetcode.com/uploads/2018/10/12/bstdlloriginalbst.png"></p>

<p>&nbsp;</p>

<p>我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。</p>

<p>下图展示了上面的二叉搜索树转化成的链表。&ldquo;head&rdquo; 表示指向链表中有最小元素的节点。</p>

<p>&nbsp;</p>

<p><img src="https://assets.leetcode.com/uploads/2018/10/12/bstdllreturndll.png"></p>

<p>&nbsp;</p>

<p>特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中的第一个节点的指针。</p>

<p>&nbsp;</p>

<p><strong>注意：</strong>本题与主站 426 题相同：<a href="https://leetcode-cn.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/">https://leetcode-cn.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/</a></p>

<p><strong>注意：</strong>此题对比原题有改动。</p>

# Python

```python
"""
二叉搜索树，中序遍历 从小到大
双向链表：在构建相邻节点的引用关系时，设前驱节点 pre 和当前节点 cur ，不仅应构建 pre.right = cur ，也应构建 cur.left = pre
循环链表：头结点head和尾节点tail，应构建 head.left = tail 和 tail.right = head 
    - 在没有前驱节点时 当前节点就是头结点
    - 结尾时，pre就是尾节点
"""


class Solution:
    def __init__(self):
        self.pre = None
        self.head = None

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def build(cur):
            if not cur:
                return cur
            # 二叉搜索树，中序遍历
            build(cur.left)
            # 建立双向链表
            if self.pre:
                self.pre.right = cur
                cur.left = self.pre
            # 没有前驱节点时，当前节点就是头节点
            else:
                self.head = cur
            # 递归时，当前节点为前驱节点
            self.pre = cur
            build(cur.right)

        if not root:
            return root
        build(root)
        # 构建循环链表头尾节点引用关系
        self.pre.right = self.head
        self.head.left = self.pre
        return self.head
```
