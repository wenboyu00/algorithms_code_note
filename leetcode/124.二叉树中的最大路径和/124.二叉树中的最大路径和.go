package main

import "math"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxPathSum(root *TreeNode) int {

	ans := math.MinInt64
	var maxPath func(root *TreeNode) int
	maxPath = func(root *TreeNode) int {
		if root == nil {
			return 0
		}
		left := max(0, maxPath(root.Left))
		right := max(0, maxPath(root.Right))
		ans = max(ans, left+root.Val+right)
		return root.Val + max(left, right)
	}
	maxPath(root)
	return ans
}
func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
