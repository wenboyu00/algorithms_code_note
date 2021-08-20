package main

import "math"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isValidBST(root *TreeNode) bool {

	var isValid func(root *TreeNode, min int, max int) bool
	isValid = func(root *TreeNode, min int, max int) bool {
		if root == nil {
			return true
		}
		if min < root.Val && root.Val < max {
			// 左子树最大值：root.val；右子树最小值:root.val
			return isValid(root.Left, min, root.Val) && isValid(root.Right, root.Val, max)
		} else {
			return false
		}

	}
	return isValid(root, math.MinInt64, math.MaxInt64)
}
