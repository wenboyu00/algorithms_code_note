# 请实现两个函数，分别用来序列化和反序列化二叉树。
#
#  示例:
#
#  你可以将以下二叉树：
#
#     1
#    / \
#   2   3
#      / \
#     4   5
#
# 序列化为 "[1,2,3,null,null,4,5]"
#
#  注意：本题与主站 297 题相同：https://leetcode-cn.com/problems/serialize-and-deserialize-b
# inary-tree/
#  Related Topics 树 设计


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '[]'
        res = []
        # 借助队列，进行层序遍历，把叶节点的null也加进去
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append('null')
        # 把一个列表数据合并成字符串
        res_str = ','.join(res)
        return f'[{res_str}]'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return None
        # 去掉开头和结尾的括号，用 ','隔开字符串成为列表
        vals = data[1:-1].split(',')
        i = 1
        root = TreeNode(int(vals[0]))
        # 用队列按层构建二叉树
        # 用下标i指向node的左右节点，然后右移1位
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if vals[i] != 'null':
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1

            if vals[i] != 'null':
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# leetcode submit region end(Prohibit modification and deletion)
