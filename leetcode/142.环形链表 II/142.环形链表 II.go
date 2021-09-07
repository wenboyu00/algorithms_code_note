package main

type ListNode struct {
	Val  int
	Next *ListNode
}

/*
1.找到双指针相遇点
2.某一个指针指向head，然后同步前进，直到相等时为相遇点
*/
func detectCycle(head *ListNode) *ListNode {
	if head == nil {
		return head
	}
	meetPoint := findMeetPoint(head)
	if meetPoint == nil {
		return nil
	}
	fast := meetPoint
	slow := head
	for fast != slow {
		fast = fast.Next
		slow = slow.Next
	}
	return slow
}

func findMeetPoint(head *ListNode) *ListNode {
	fast := head
	slow := head
	for fast != nil && fast.Next != nil {
		fast = fast.Next.Next
		slow = slow.Next
		if fast == slow {
			return slow
		}
	}
	return nil
}
