package main

type MyQueue struct {
	s1, s2 []int
}

/** 初始化数据结构，2个栈来实现队列. */
func Constructor() MyQueue {
	return MyQueue{s1: []int{}, s2: []int{}}
}

func (this *MyQueue) Push(x int) {
	this.s1 = append(this.s1, x)
}

func (this *MyQueue) Pop() int {
	this.Peek()
	n := len(this.s2)
	s2Last := this.s2[n-1]
	this.s2 = this.s2[:n-1]
	return s2Last
}

func (this *MyQueue) Peek() int {
	if len(this.s2) == 0 {
		for len(this.s1) != 0 {
			n := len(this.s1)
			s1Last := this.s1[n-1]
			this.s1 = this.s1[:n-1]
			this.s2 = append(this.s2, s1Last)
		}
	}
	return this.s2[len(this.s2)-1]
}

func (this *MyQueue) Empty() bool {
	return len(this.s1) == 0 && len(this.s2) == 0
}
