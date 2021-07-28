package main

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
明确起点和终点
-起点	root 根节点
-终点	叶子节点（两个子节点都为空的节点）
根据框架修改解法
*/
func minDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	// 队列
	q := make([]TreeNode, 0)
	// 初始化起点，初始化层数（root也算一层）
	q = append(q, *root)
	depth := 1
	// 不空时循环
	for len(q) != 0 {
		// 循环一层的节点，此时队列中保存一层的节点数量，通过数量来控制。
		size := len(q)
		for i := 0; i < size; i++ {
			// 获得队首节点和实现队列pop效果
			cur := q[0]
			q = q[1:]
			// 判断是否终点
			if cur.Left == nil && cur.Right == nil {
				return depth
			}
			// 讲cur相邻的节点加入队列
			if cur.Left != nil {
				q = append(q, *cur.Left)
			}
			if cur.Right != nil {
				q = append(q, *cur.Right)

			}
		}
		// 增加层数
		depth += 1
	}
	return depth
}
