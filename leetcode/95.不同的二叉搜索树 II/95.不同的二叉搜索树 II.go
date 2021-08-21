package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func generateTrees(n int) []*TreeNode {
	if n == 0 {
		return []*TreeNode{}
	}
	return generate(1, n)
}
func generate(low int, high int) []*TreeNode {
	res := []*TreeNode{}
	// base case 无区间时，返回nil节点
	if low > high {
		res = append(res, nil)
		return res
	}
	for i := low; i <= high; i++ {
		// 递归构建左右子树
		left := generate(low, i-1)
		right := generate(i+1, high)
		// 给root节点穷举所有左右子树
		for _, l := range left {
			for _, r := range right {
				root := &TreeNode{Val: i}
				root.Left = l
				root.Right = r
				res = append(res, root)
			}
		}
	}
	return res
}
