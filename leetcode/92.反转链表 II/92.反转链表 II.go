package main

type ListNode struct {
	Val  int
	Next *ListNode
}

// 声明全局遍历，successor为指向ListNode的地址的指针类型
var successor *ListNode

//反转以head为开始第left到right个节点，并返回头节点
func reverseBetween(head *ListNode, left int, right int) *ListNode {
	if left == 1 {
		return reverseN(head, left)
	}
	// 前进到反转的起点
	head.Next = reverseBetween(head.Next, left-1, right-1)
	return head
}

func reverseN(head *ListNode, n int) *ListNode {
	// 数量为1时保存head的后续，反转之后将head接上
	if n == 1 {
		successor = head.Next
		return head
	}
	last := reverseN(head.Next, n-1)
	head.Next.Next = head
	head.Next = successor
	return last
}
