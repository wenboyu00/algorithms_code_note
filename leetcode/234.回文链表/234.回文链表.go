package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func isPalindrome(head *ListNode) bool {
	slow := head
	fast := head
	stack := []int{}
	for fast != nil && fast.Next != nil {
		stack = append(stack, slow.Val)
		slow = slow.Next
		fast = fast.Next.Next
	}
	if fast != nil {
		slow = slow.Next
	}
	n := len(stack)
	for i := n - 1; i >= 0; i-- {
		val := stack[i]
		if val != slow.Val {
			return false
		}
		slow = slow.Next
	}
	return true
}
