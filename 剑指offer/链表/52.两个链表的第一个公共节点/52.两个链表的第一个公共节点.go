package 链表

import "algorithms-code-note/剑指offer/structures"

type ListNode = structures.ListNode

func getIntersectionNode(headA, headB *ListNode) *ListNode {
    visit := map[*ListNode]bool{}
    a := headA
    for a !=nil{
        visit[a] = true
        a = a.Next
    }
    b := headB
    for b != nil{
        if visit[b]{
            return b
        }
        b = b.Next
    }
    return nil
}