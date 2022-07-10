package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	// l1和l2都为ListNode指针
	// 初始化头节点
	dummy := ListNode{Val: 0, Next: nil}
	// tail 等于头节点指针
	tail := &dummy
	s := 0
	// 在l1或者l2或者s不为空时继续循环
	for l1 != nil || l2 != nil || s > 0 {
		l1Val := 0
		l2Val := 0

		if l1 != nil {
			l1Val = l1.Val
		}
		if l2 != nil {
			l2Val = l2.Val
		}
		// s等于l1和l2和上次进位数的值
		s = l1Val + l2Val + s
		// s%10 取位数，s/10 取进位数
		node := ListNode{Val: s % 10, Next: nil}
		// Next等于新节点的地址
		tail.Next = &node
		fmt.Println(node)
		// 总和数 前进一位。l1，l2和尾节点都前进一位
		s = s / 10
		if l1 != nil {
			l1 = l1.Next
		}
		if l2 != nil {
			l2 = l2.Next
		}
		tail = tail.Next
	}
	// 因为头节点，值为空，next节点为第一个新节点地址，所以返回dummy.Next
	return dummy.Next
}
