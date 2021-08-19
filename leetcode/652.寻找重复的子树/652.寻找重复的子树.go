package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func findDuplicateSubtrees(root *TreeNode) []*TreeNode {
	memo := make(map[string]int)
	var res []*TreeNode
	// 定义函数参数
	var travers func(root *TreeNode) string
	// 赋值给变量
	travers = func (root*TreeNode) string{
		if root == nil{
		return "#"
	}
		left := travers(root.Left)
		right := travers(root.Right)
		subString := fmt.Sprintf("%s,%s,%d", left, right, root.Val)
		// 存储子树字符串出现次数
		memo[subString] += 1
		// 2次时表示有重复，加入至结果列表
		if memo[subString] == 2{
		res = append(res, root)
	}
		return subString
	}

	travers(root)
	return res
}