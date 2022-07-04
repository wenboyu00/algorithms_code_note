package hot

import "algorithms-code-note/util/structures"

type TreeNode = structures.TreeNode

func kthLargest(root *TreeNode, k int) int {
	count := 0
	result := -1
	var reverse func(root *TreeNode, k int)

	reverse = func(root *TreeNode, k int) {
		if root == nil {
			return
		}
		reverse(root.Right, k)
		count += 1
		if count == k {
			result = root.Val
		}
		reverse(root.Left, k)
	}
	reverse(root, k)
	return result
}
