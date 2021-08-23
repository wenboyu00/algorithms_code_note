package main

import "math"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxSumBST(root *TreeNode) int {
	maxSum := 0
	var traverse func(root *TreeNode) []int
	traverse = func(root *TreeNode) []int {
		/*
		res是4个值的数组
		res[0] 以root为根的二叉树是否为bst，1是，0否
		res[1] 以root为根的二叉树所有节点的最小值
		res[2] 以root为根的二叉树所有节点的最大值
		res[3] 以root为根的二叉树所有节点值之和
		*/
		// base case
		if root == nil {
			return []int{1, math.MaxInt64, math.MinInt64, 0}
		}
		left := traverse(root.Left)
		right := traverse(root.Right)
		res := []int{0, 0, 0, 0}
		if left[0] == 1 && right[0] == 1 && left[2] < root.Val && right[1] > root.Val {
			res[0] = 1
			res[1] = min(left[1], root.Val)
			res[2] = max(right[2], root.Val)
			res[3] = left[3] + right[3] + root.Val
			maxSum = max(maxSum, res[3])
		} else
		{
			res[0] = 0
		}
		return res
	}
	traverse(root)
	return maxSum
}
func max(int1 int, int2 int) int {
	if int1 < int2 {
		return int2
	} else {
		return int1
	}
}

func min(int1 int, int2 int) int {
	if int1 > int2 {
		return int2
	} else {
		return int1
	}
}
