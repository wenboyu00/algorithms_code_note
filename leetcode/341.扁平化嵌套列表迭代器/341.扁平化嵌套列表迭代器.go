package main

//type NestedIterator struct {
//	Stack []*NestedInteger
//}
//
//func Constructor(nestedList []*NestedInteger) *NestedIterator {
//	stack := []*NestedInteger{}
//	for i := len(nestedList) - 1; i >= 0; i-- {
//		stack = append(stack, nestedList[i])
//	}
//	return &NestedIterator{Stack: stack}
//}
//
//func (this *NestedIterator) Next() int {
//	cur := this.Stack[len(this.Stack)-1]
//	this.Stack = this.Stack[:len(this.Stack)-1]
//	return cur.GetInteger()
//}
//
//func (this *NestedIterator) HasNext() bool {
//	for len(this.Stack) > 0 {
//		cur := this.Stack[len(this.Stack)-1]
//		if cur.IsInteger() {
//			return true
//		}
//		this.Stack = this.Stack[:len(this.Stack)-1]
//		list := cur.GetList()
//		for i := len(list) - 1; i >= 0; i-- {
//			this.Stack = append(this.Stack, list[i])
//
//		}
//	}
//	return false
//}
