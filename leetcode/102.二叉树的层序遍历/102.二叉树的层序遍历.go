package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func levelOrder(root *TreeNode) [][]int {
	res := [][]int{}
	if root == nil {
		return res
	}
	stk := []*TreeNode{root}
	for len(stk) != 0 {
		vals := make([]int, 0, len(stk))
		nodes := append([]*TreeNode{}, stk...)
		stk = []*TreeNode{}
		for _, node := range nodes {
			vals = append(vals, node.Val)
			if node.Left != nil {
				stk = append(stk, node.Left)
			}
			if node.Right != nil {
				stk = append(stk, node.Right)
			}
		}
		res = append(res, append([]int{}, vals...))
	}
	return res
}
