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
	root := TreeNode{rootVal, nil, nil}
	// find in root index
	index := inStart
	for i := inStart; i < inEnd+1; i++ {
		if inorder[i] == rootVal {
			index = i
		}
	}
	leftSize := index - inStart
	root.Left = build(preorder, preStart+1, preStart+leftSize,
		inorder, inStart, index-1)
	root.Right = build(preorder, preStart+leftSize+1, preEnd,
		inorder, index+1, inEnd)
	return &root
}
