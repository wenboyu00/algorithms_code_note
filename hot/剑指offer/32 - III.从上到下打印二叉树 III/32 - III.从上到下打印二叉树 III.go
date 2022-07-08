package hot

import "algorithms-code-note/util/structures"

type TreeNode = structures.TreeNode

func levelOrder(root *TreeNode) [][]int {
	result := make([][]int, 0)
	if root == nil {
		return result
	}
	stk := []*TreeNode{root}
	level := 1
	for len(stk) != 0 {
		length := len(stk)
		vals := make([]int, length)
		tmp := []*TreeNode{}
		for i := 0; i < length; i++ {
			if stk[i] == nil{
				continue
			}
			if level%2 != 0 {
				vals[i] = stk[i].Val
			} else {
				vals[length-1-i] = stk[i].Val
			}
			if stk[i].Left != nil {
				tmp = append(tmp, stk[i].Left)
			}
			if stk[i].Right != nil {
				tmp = append(tmp, stk[i].Right)
			}
		}
		stk = tmp
		result = append(result, vals)
		level += 1
	}
	return result
}
