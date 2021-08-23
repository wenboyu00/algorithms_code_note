package main

import (
	"strconv"
	"strings"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type Codec struct {
}

func Constructor() (_ Codec) {
	return
}

// Serializes a tree to a single string.
func (this *Codec) serialize(root *TreeNode) string {
	// 以字符串方式储存
	sb := strings.Builder{}
	var serializePreOrder func(root *TreeNode)
	serializePreOrder = func(root *TreeNode) {
		// base case
		if root == nil {
			sb.WriteString("null,")
			return
		}
		// 前序遍历，转换int为字符串
		sb.WriteString(strconv.Itoa(root.Val))
		sb.WriteString(",")
		// 递归左右子树
		serializePreOrder(root.Left)
		serializePreOrder(root.Right)

	}
	serializePreOrder(root)
	return sb.String()
}

// Deserializes your encoded data to tree.
func (this *Codec) deserialize(data string) *TreeNode {
	// 以“,”分割字符串，为字符串数组
	sp := strings.Split(data, ",")
	var deserializePreOrder func() *TreeNode
	deserializePreOrder = func() *TreeNode {
		// 前序遍历,并弹出index0
		if sp[0] == "null" {
			sp = sp[1:]
			return nil
		}
		// 转换str为int
		val, _ := strconv.Atoi(sp[0])
		sp = sp[1:]
		node := &TreeNode{Val: val}
		// 递归调用左右子树
		node.Left = deserializePreOrder()
		node.Right = deserializePreOrder()
		return node
	}
	return deserializePreOrder()
}
