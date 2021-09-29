package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func diameterOfBinaryTree(root *TreeNode) int {
	ans := 0
	var depth func(root *TreeNode) int
	depth = func(root *TreeNode) int {
		if root == nil {
			return 0
		}
		left := depth(root.Left)
		right := depth(root.Right)
		if left+right > ans {
			ans = left + right
		}
		if left > right {
			return left + 1
		} else {
			return right + 1
		}
	}
	depth(root)
	return ans
}
