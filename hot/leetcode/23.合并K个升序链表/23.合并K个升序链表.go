package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeKLists(lists []*ListNode) *ListNode {
	return merge(lists, 0, len(lists)-1)
}
func merge(lists []*ListNode, left int, right int) *ListNode {
	// base case 递归结束条件
	// - 相同数组
	if left == right {
		return lists[left]
	}
	// - 超过边界
	if left > right {
		return nil
	}
	// 二分后列表，进行递归合并
	mid := (left + right) / 2
	return mergeTwoList(merge(lists, left, mid), merge(lists, mid+1, right))
}

func mergeTwoList(a *ListNode, b *ListNode) *ListNode {
	// leetcode.21 穿针引线合并两个链表
	dummy := &ListNode{}
	tail := dummy
	for a != nil && b != nil {
		if a.Val <= b.Val {
			tail.Next = a
			a = a.Next
		} else {
			tail.Next = b
			b = b.Next
		}
		tail = tail.Next
	}
	if a != nil {
		tail.Next = a
	}
	if b != nil {
		tail.Next = b
	}
	return dummy.Next
}
