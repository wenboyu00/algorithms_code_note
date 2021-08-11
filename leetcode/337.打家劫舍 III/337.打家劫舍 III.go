package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func rob(root *TreeNode) int {
	memo := make(map[*TreeNode]int)
	return doRob(root, memo)
}

func doRob(root *TreeNode, memo map[*TreeNode]int) int {
	if root == nil {
		return 0
	}
	if val, ok := memo[root]; ok {
		return val
	}
	doItL := 0
	doItR := 0
	if root.Left != nil{
		doItL = doRob(root.Left.Left, memo) + doRob(root.Left.Right, memo)
	}
	if root.Right != nil{
		doItR = doRob(root.Right.Left, memo) + doRob(root.Right.Right, memo)
	}
	doIt := root.Val + doItL + doItR
	notDoIt := doRob(root.Left, memo) + doRob(root.Right, memo)
	res := max(doIt, notDoIt)
	memo[root] = res
	return res
}

func max(int1 int, int2 int) int {
	if int1 < int2 {
		return int2
	} else {
		return int1
	}
}
