package 链表

import "algorithms-code-note/剑指offer/structures"

type ListNode = structures.ListNode

func deleteNode(head *ListNode, val int) *ListNode {
	dummy := &ListNode{0, head}
	pre := dummy
	cur := head
	for cur != nil {
		if cur.Val == val {
			pre.Next = cur.Next
		}
		pre = pre.Next
		cur = cur.Next
	}
	return dummy.Next
}
