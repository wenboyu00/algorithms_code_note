package main

type DLinkNode struct {
	key, value int
	pre, next  *DLinkNode
}

func initDLinkNode(key, value int) *DLinkNode {
	return &DLinkNode{key: key, value: value}
}

type LRUCache struct {
	size       int
	capacity   int
	cache      map[int]*DLinkNode
	head, tail *DLinkNode
}

func Constructor(capacity int) LRUCache {
	l := LRUCache{
		cache:    map[int]*DLinkNode{},
		head:     initDLinkNode(0, 0),
		tail:     initDLinkNode(0, 0),
		capacity: capacity,
		size: 0,
	}
	l.head.next = l.tail
	l.tail.pre = l.head
	return l
}

func (this *LRUCache) Get(key int) int {
	/*
		不存在：返回-1，
		存在：先移动到头部，再返回
	*/
	if _, ok := this.cache[key]; !ok {
		return -1
	}
	node := this.cache[key]
	this.move2Head(node)
	return node.value
}

func (this *LRUCache) Put(key int, value int) {
	/*
		不存在：初始化节点，存入哈希表，存入链表头部，大小+1，检查容量大小
			- 容量满：删除链表尾部节点，并在哈希表中删除，大小-1
		存在：从哈希表中取出node，更新value，并存入链表头部
	*/
	if _, ok := this.cache[key]; !ok {
		node := initDLinkNode(key, value)
		this.cache[key] = node
		this.add2Head(node)
		this.size += 1
		if this.size > this.capacity {
			removed := this.removeTail()
			delete(this.cache, removed.key)
			this.size -= 1
		}

	} else {
		node := this.cache[key]
		node.value = value
		this.move2Head(node)
	}
}

func (this *LRUCache) add2Head(node *DLinkNode) {
	node.pre = this.head
	node.next = this.head.next
	this.head.next.pre = node
	this.head.next = node
}
func (this *LRUCache) removeNode(node *DLinkNode) {
	node.pre.next = node.next
	node.next.pre = node.pre
}

func (this *LRUCache) move2Head(node *DLinkNode) {
	this.removeNode(node)
	this.add2Head(node)
}

func (this *LRUCache) removeTail() *DLinkNode {
	node := this.tail.pre
	this.removeNode(node)
	return node
}
