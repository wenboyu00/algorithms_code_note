package main

type ListNode struct {
	Val  int
	Next *ListNode
}
/*
快慢指针
快指针二倍速，慢指针一倍速
如果有环，快指针追（fast==slow)上慢指针
*/
func hasCycle(head *ListNode) bool {
	fast := head
	slow := head
	for fast != nil && fast.Next != nil {
		fast = fast.Next.Next
		slow = slow.Next
        if fast == slow {
            return true
        }
	}
	return false
}
