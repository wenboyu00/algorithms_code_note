package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func countNodes(root *TreeNode) int {
	// 记录左右子树的高度
	left := root
	right := root
	leftHigh := 0
	rightHigh := 0
	for left != nil {
		left = left.Left
		leftHigh += 1
	}
	for right != nil {
		right = right.Right
		rightHigh += 1

	}
	// 左右子树高度相等是是满二叉树
	// 满二叉树情况下 节点总数 = 2^high - 1
	if leftHigh == rightHigh {
		return IntPow(2, leftHigh) - 1
	}
	// 普通二叉树递归计算，1为当前节点数量
	return 1 + countNodes(root.Left) + countNodes(root.Right)
}

func IntPow(n, m int) int {
	if m == 0 {
		return 1
	}
	result := n
	for i := 2; i <= m; i++ {
		result *= n
	}
	return result
}
