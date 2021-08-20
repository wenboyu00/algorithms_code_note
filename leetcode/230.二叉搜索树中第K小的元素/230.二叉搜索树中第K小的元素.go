package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func kthSmallest(root *TreeNode, k int) int {
	res := 0
	rank := 0

	var reverse func(root *TreeNode, k int)

	reverse = func(root *TreeNode, k int) {
		if root == nil {
			return
		}
		reverse(root.Left, k)
		rank += 1
		if rank == k {
			res = root.Val
		}
		reverse(root.Right, k)
	}
	reverse(root, k)
	return res
}
