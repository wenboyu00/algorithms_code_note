# 题目
<p>序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。</p>

<p>请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。</p>

<p><strong>提示: </strong>输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 <a href="/faq/#binary-tree">LeetCode 序列化二叉树的格式</a>。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/15/serdeser.jpg" style="width: 442px; height: 324px;" />
<pre>
<strong>输入：</strong>root = [1,2,3,null,null,4,5]
<strong>输出：</strong>[1,2,3,null,null,4,5]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>root = []
<strong>输出：</strong>[]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>root = [1]
<strong>输出：</strong>[1]
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>root = [1,2]
<strong>输出：</strong>[1,2]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中结点数在范围 <code>[0, 10<sup>4</sup>]</code> 内</li>
	<li><code>-1000 <= Node.val <= 1000</code></li>
</ul>
<div><div>Related Topics</div><div><li>树</li><li>深度优先搜索</li><li>广度优先搜索</li><li>设计</li><li>字符串</li><li>二叉树</li></div></div>

# Python

```python
class Codec:
    def __init__(self):
        self.sep = ","
        self.null = "#"

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        def serialize_preorder(root: TreeNode, res: List[str]):
            if root is None:
                res.append(self.null)
                return
            # 前序遍历位置
            res.append(str(root.val))
            serialize_preorder(root.left, res)
            serialize_preorder(root.right, res)

        serialize_preorder(root, res)
        return self.sep.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # 将字符串转化成列表
        nodes = data.split(self.sep)

        def deserialize_preorder(nodes: List[str]):
            if nodes == []:
                return None
            # 前序遍历位置
            # 列表最左侧就是根节点
            first = nodes.pop(0)
            if first == self.null:
                return None
            root = TreeNode(int(first))

            root.left = deserialize_preorder(nodes)
            root.right = deserialize_preorder(nodes)
            return root

        return deserialize_preorder(nodes)
```

# Go

```go
type Codec struct {
}

func Constructor() (_ Codec) {
   return
}

// Serializes a tree to a single string.
func (this *Codec) serialize(root *TreeNode) string {
   // 以字符串方式储存
   sb := strings.Builder{}
   var serializePreOrder func(root *TreeNode)
   serializePreOrder = func(root *TreeNode) {
      // base case
      if root == nil {
         sb.WriteString("null,")
         return
      }
      // 前序遍历，转换int为字符串
      sb.WriteString(strconv.Itoa(root.Val))
      sb.WriteString(",")
      // 递归左右子树
      serializePreOrder(root.Left)
      serializePreOrder(root.Right)

   }
   serializePreOrder(root)
   return sb.String()
}

// Deserializes your encoded data to tree.
func (this *Codec) deserialize(data string) *TreeNode {
   // 以“,”分割字符串，为字符串数组
   sp := strings.Split(data, ",")
   var deserializePreOrder func() *TreeNode
   deserializePreOrder = func() *TreeNode {
      // 前序遍历,并弹出index0
      if sp[0] == "null" {
         sp = sp[1:]
         return nil
      }
      // 转换str为int
      val, _ := strconv.Atoi(sp[0])
      sp = sp[1:]
      node := &TreeNode{Val: val}
      // 递归调用左右子树
      node.Left = deserializePreOrder()
      node.Right = deserializePreOrder()
      return node
   }
   return deserializePreOrder()
}
```