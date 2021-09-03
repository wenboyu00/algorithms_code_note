package main

type MyStack struct {
	q []int
}

func Constructor() MyStack {
	return MyStack{q: []int{}}
}

func (this *MyStack) Push(x int) {
	this.q = append(this.q, x)
}

func (this *MyStack) Pop() int {
	n := len(this.q)
	last := this.q[n-1]
	this.q = this.q[:n-1]
	return last
}

/** Get the top element. */
func (this *MyStack) Top() int {
	return this.q[len(this.q)-1]
}

/** Returns whether the stack is empty. */
func (this *MyStack) Empty() bool {
	return len(this.q) == 0
}
