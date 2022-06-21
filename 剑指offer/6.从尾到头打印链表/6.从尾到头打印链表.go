package main

type ListNode struct {
	Val  int
	Next *ListNode
}

/*
遍历一遍把val添加到数组中，然从后向前遍历数组并添加到结果列表中
*/
func reversePrint(head *ListNode) []int {
	stack := []int{}
	result := []int{}
	if head == nil {
		return result
	}
	for head != nil {
		stack = append(stack, head.Val)
		head = head.Next
	}

	for i := len(stack) - 1; i > -1; i-- {
		result = append(result, stack[i])
	}
	return result
}
