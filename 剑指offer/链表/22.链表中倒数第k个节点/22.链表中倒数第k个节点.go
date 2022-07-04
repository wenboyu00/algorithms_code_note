package 链表

import "algorithms-code-note/util/structures"

type ListNode = structures.ListNode

func getKthFromEnd(head *ListNode, k int) *ListNode {
	if head == nil {
		return head
	}
	fast := head
	slow := head
	for i := 0; i < k; i++ {
		fast = fast.Next
	}
	for fast != nil {
		fast = fast.Next
		slow = slow.Next
	}
	return slow
}
