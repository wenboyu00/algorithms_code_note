package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func pathSum(root *TreeNode, targetSum int) int {
	/*
		前缀和+dfs回溯
		计算路径上的前缀和，如果有路径和 - 目标值的差值 已经存在，说明有路径和，结果值加上差值的次数
	*/
	// 存储路径和次数， base case：0出现1次
	mapping := map[int]int{0: 1}
	res := 0
	var dfs func(root *TreeNode, cur int)
	dfs = func(root *TreeNode, cur int) {
		if root == nil {
			return
		}
		// 路径和，并记录到哈希表
		cur += root.Val
		mapping[cur] = +1
		// 计算路径和差值，并添加差值出现次数到结果中
		need := cur - targetSum
		res += mapping[need]
		// 递归左右子树
		dfs(root.Left, cur)
		dfs(root.Right, cur)
		// 删除当前路径出现次数
		mapping[cur] -= 1
	}
	dfs(root, 0)
	return res
}
