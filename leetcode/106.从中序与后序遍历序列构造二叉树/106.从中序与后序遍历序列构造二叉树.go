package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func buildTree(inorder []int, postorder []int) *TreeNode {
	return build(inorder, 0, len(inorder)-1,
		postorder, 0, len(postorder)-1)
}
func build(inorder []int, inStart int, inEnd int,
	postorder []int, postStart int, postEnd int) *TreeNode {
	if postStart > postEnd {
		return nil
	}
	// 后序[-1]是根节点
	rootVal := postorder[postEnd]
	index := 0
	for i := inStart; i <= inEnd; i++ {
		if inorder[i] == rootVal {
			index = i
			break
		}
	}
	leftSize := index - inStart
	root := &TreeNode{Val: rootVal}
	// 构造左子树
	// - 中序，左右根，左子树起始：原起始值，右子树终点：根节点-1（跳过根节点）
	// - 后序，根左右，左子树起始：原起始值；左子树终点：左子树起点+左子树长度-1（跳过右子树起点）
	root.Left = build(inorder, inStart, index-1, postorder, postStart, postStart+leftSize-1)
	// 构造右子树
	// - 中序，右子树起始：根节点+1（跳过根节点）；右子树终点：原终点
	// - 后序，右子树起始：左子树起点+左子树长度；右子树终点：根节点-1（跳过根节点）
	root.Right = build(inorder, index+1, inEnd, postorder, postStart+leftSize, postEnd-1)

	return root
}
func main() {
	postorder := []int{9, 15, 7, 20, 3}
	inorder := []int{9, 3, 15, 20, 7}
	result := buildTree(inorder, postorder)
	println(result.Val)
}
