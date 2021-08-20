package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}
/*
题目要求：累加比自己大的节点和其本事，如5，累加等于6+7+8+5=26
BST 左小有大，子树依然，但是其父节点也可能大于其节点，所以不能单纯使用中序递归
中序递归，从小到大。此题需要比其节点大的值，因此可以调转中序递归位置，实现降序（从大到小）
又因为父节点也可能比当前节点大，所以使用sum来辅助储存累加的值
*/
func convertBST(root *TreeNode) *TreeNode {
	sum := 0
	var convert func(root *TreeNode)
	convert = func(root *TreeNode) {
		if root == nil {
			return
		}
		// 调换递归顺序，右中左，变为降序
		convert(root.Right)
		// 更新累加值，并赋值给根节点
		sum += root.Val
		root.Val = sum
		convert(root.Left)
	}
	convert(root)
	return root
}
