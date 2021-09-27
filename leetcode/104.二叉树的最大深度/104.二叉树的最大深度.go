package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	leftDepth := maxDepth(root.Left)
	rightDepth := maxDepth(root.Right)
	nodeDepth := leftDepth
	if nodeDepth < rightDepth {
		nodeDepth = rightDepth
	}
	return nodeDepth + 1
}
