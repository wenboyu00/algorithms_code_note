package main

import "math/rand"

type ListNode struct {
	Val  int
	Next *ListNode
}

type Solution struct {
	head *ListNode
}

func Constructor(head *ListNode) Solution {
	return Solution{
		head: head,
	}
}

/** Returns a random node's value. */
func (this *Solution) GetRandom() int {
	count := 0
	res := 0
	cur := this.head
	for cur != nil {
		count += 1
		randNum := rand.Intn(count) + 1
		if randNum == count {
			res = cur.Val
		}
		cur = cur.Next
	}
	return res
}

/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(head);
 * param_1 := obj.GetRandom();
 */
