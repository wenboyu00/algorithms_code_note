package main

type MinStack struct {
	stk    []int
	minStk []int
}

func Constructor() MinStack {
	return MinStack{stk: []int{},
		minStk: []int{}}
}

func (this *MinStack) Push(val int) {
	this.stk = append(this.stk, val)
	if len(this.minStk) == 0 || val <= this.minStk[len(this.minStk)-1] {
		this.minStk = append(this.minStk, val)
	}
}

func (this *MinStack) Pop() {
	val := this.stk[len(this.stk)-1]
	this.stk = this.stk[:len(this.stk)-1]
	if val == this.minStk[len(this.minStk)-1] {
		this.minStk = this.minStk[:len(this.minStk)-1]
	}
}

func (this *MinStack) Top() int {
	return this.stk[len(this.stk)-1]
}

func (this *MinStack) GetMin() int {
	return this.minStk[len(this.minStk)-1]
}
