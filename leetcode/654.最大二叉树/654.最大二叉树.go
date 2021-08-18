package main

import "math"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func constructMaximumBinaryTree(nums []int) *TreeNode {
	return build(nums, 0, len(nums)-1)
}

func build(nums []int, low int, high int) *TreeNode {
	if low > high {
		return nil
	}
	maxVal := math.MinInt64
	index := 0
	for i := low; i <= high; i++ {
		if nums[i] > maxVal {
			maxVal = nums[i]
			index = i
		}
	}
	root := &TreeNode{Val: maxVal}
	root.Left = build(nums, low, index-1)
	root.Right = build(nums, index+1, high)
	return root
}

func main() {
	nums := []int{3, 2, 1, 6, 0, 5}
	result := constructMaximumBinaryTree(nums)
	println(result.Val)
}
