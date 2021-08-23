from typing import List


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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
