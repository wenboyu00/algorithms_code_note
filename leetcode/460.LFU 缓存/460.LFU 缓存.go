package main

type Node struct {
	key, value, freq int
	pre, next        *Node
}

func initNode(key, value int) *Node {
	return &Node{key: key, value: value}
}

type DLinkedList struct {
	head, tail *Node
}

func initDLinkedList() *DLinkedList {
	DLinked := &DLinkedList{
		head: initNode(0, 0),
		tail: initNode(0, 0),
	}
	DLinked.head.next = DLinked.tail
	DLinked.tail.pre = DLinked.head
	return DLinked
}

type LFUCache struct {
}

func Constructor(capacity int) LFUCache {

}

func (this *LFUCache) Get(key int) int {

}

func (this *LFUCache) Put(key int, value int) {

}
