package main

type TreeNode struct {
	Val  int
	Left *TreeNode
	Right *TreeNode
}

func invertTree(root *TreeNode) *TreeNode {
	// base case
	if root == nil{
		return nil
	}
	// 前序遍历
	// root节点的左右节点交换
	temp := root.Left
	root.Left = root.Right
	root.Right = temp
	// 让左右子节点继续翻转它们的子节点
	invertTree(root.Left)
	invertTree(root.Right)
	return root
}
