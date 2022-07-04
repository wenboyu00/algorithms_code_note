package 链表

import "algorithms-code-note/util/structures"

type ListNode = structures.ListNode

/*
迭代方式
pre 前节点，迭代结束后成为队尾节点
cur 当前节点
循环时：
    把cur.next保存到tmp
    把cur.next 只想pre，实现反转
    推进节点-注意推进顺序，先pre后cur：
        - pre = cur 前节点推荐到当前
        - cur = tmp 当前节点推进到原next节点

*/
func reverseList(head *ListNode) *ListNode {
	if head == nil {
		return head
	}
	var pre *ListNode
	cur := head
	for cur != nil {
		tmp := cur.Next
		cur.Next = pre
		pre = cur
		cur = tmp
	}
	return pre
}
