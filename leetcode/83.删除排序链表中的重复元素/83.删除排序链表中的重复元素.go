package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteDuplicates(head *ListNode) *ListNode {
	if head == nil{
		return head
	}
	slow := head
	fast := head
	for fast != nil{
		if slow.Val != fast.Val{
			slow = slow.Next
			slow.Val = fast.Val
		}
		fast = fast.Next
	}
	slow.Next = nil
	return head
}
