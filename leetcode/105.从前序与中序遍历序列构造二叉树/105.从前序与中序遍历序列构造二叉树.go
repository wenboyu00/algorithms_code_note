package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func buildTree(preorder []int, inorder []int) *TreeNode {
	return build(preorder, 0, len(preorder)-1,
		inorder, 0, len(inorder)-1)
}

func build(preorder []int, preStart int, preEnd int,
	inorder []int, inStart int, inEnd int) *TreeNode {
	if preStart > preEnd {
		return nil
	}
	rootVal := preorder[preStart]
	index := 0
	for i := inStart; i <= inEnd; i++ {
		if inorder[i] == rootVal {
			index = i
			break
		}
	}
	leftSize := index - inStart
	root := &TreeNode{Val: rootVal}
	root.Left = build(preorder, preStart+1, preStart+leftSize, inorder, inStart, index-1)
	root.Right = build(preorder, preStart+leftSize+1, preEnd, inorder, index+1, inEnd)
	return root
}

func main() {
	preorder := []int{3, 9, 20, 15, 7}
	inorder := []int{9, 3, 15, 20, 7}
	result := buildTree(preorder, inorder)
	println(result.Val)
}
