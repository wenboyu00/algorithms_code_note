package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func deleteNode(root *TreeNode, key int) *TreeNode {
	if root == nil{
		return root
	}
	//找到值
	if root.Val == key{
		// 处理有一个子树，或者无子树时情况
		if root.Left == nil{
			return root.Right
		}
		if root.Right == nil{
			return root.Left
		}
		// 有双节点时，找到右子树最小的值，替换值，删除最小值的节点
		minNode := findMin(root.Right)
		root.Val = minNode.Val
		root.Right = deleteNode(root.Right, minNode.Val)
	}else if root.Val > key {
		root.Left = deleteNode(root.Left, key)
	}else if root.Val < key{
		root.Right = deleteNode(root.Right, key)
	}
	return root
}
func findMin(node *TreeNode) *TreeNode{
	for node.Left != nil{
		node = node.Left
	}
	return node
}
