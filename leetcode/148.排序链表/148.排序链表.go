package main

type ListNode struct {
	Val  int
	Next *ListNode
}

/*
   nlogn时间要求 ->二分法，使用 归并排序
   归并排序 分为：分,和
   分:快慢指针,找到中间第一个节点,拆分
   和:对拆分后的链表进行从小达到的排序遍历
*/
func sortList(head *ListNode) *ListNode {
	// 分
	if head == nil || head.Next == nil {
		return head
	}
	// 快慢指针 不一致时 slow=中间第一个节点
	slow := head
	fast := head.Next
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}
	// 取第一个中间节点的下一个做分开点
	mid := slow.Next
	slow.Next = nil
	//	对分开2个链表进行合并
	return merge(sortList(head), sortList(mid))
}
func merge(l1 *ListNode, l2 *ListNode) *ListNode {
	// dummy 辅助头节点
	dummy := &ListNode{}
	cur := dummy
	// 对l1和l2进行遍历 并用cur从小到大串联起来
	// 注意:链表每次循环的节点前进
	for l1 != nil && l2 != nil {
		if l1.Val > l2.Val {
			l1, l2 = l2, l1
		}
		cur.Next = l1
		l1 = l1.Next
		cur = cur.Next
	}
	// 连接上剩余节点
	if l1 != nil {
		cur.Next = l1
	}
	if l2 != nil {
		cur.Next = l2
	}
	return dummy.Next
}
