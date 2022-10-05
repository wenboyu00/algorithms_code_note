package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseKGroup(head *ListNode, k int) *ListNode {
	if head == nil {
		return head
	}
	a := head
	b := head
	// b节点前进k位，反转a~b之间共k个节点
	// 如果数量不够，就不反转直接返回
	for i := 0; i < k; i++ {
		if b == nil {
			return head
		}
		b = b.Next
	}
	// 反转ab，再对后续进行递归
	newHead := reverseAB(a, b)
	a.Next = reverseKGroup(b, k)
	return newHead
}

func reverseAB(a *ListNode, b *ListNode) *ListNode {
	// 反转a-(b-1)之间的节点，并返回新头节点
	var pre *ListNode
	cur := a
	// cur==b，完成a~b之间的反转
	for cur != b {
		// 实现反转
		tmp := cur.Next
		cur.Next = pre

		// 前，当前节点进一步
		pre = cur
		cur = tmp
	}
	return pre
}
