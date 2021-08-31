package main

type Node struct {
	key, value, freq int
	pre, next        *Node
}

type DLinkedList struct {
	head, tail *Node
}

func initDLinkedList() *DLinkedList {
	DLinked := &DLinkedList{
		head: &Node{key: 0, value: 0},
		tail: &Node{key: 0, value: 0},
	}
	DLinked.head.next = DLinked.tail
	DLinked.tail.pre = DLinked.head
	return DLinked
}
func (this *DLinkedList) addFirst(node *Node) {
	node.next = this.head.next
	node.pre = this.head
	this.head.next.pre = node
	this.head.next = node

}
func (this *DLinkedList) delete(node *Node) int {
	if this.head.next == this.tail{
		return -1
	}
	node.next.pre = node.pre
	node.pre.next = node.next
	return node.key
}
func (this *DLinkedList) getList() *Node {
	if this.head.next == this.tail {
		return nil
	}
	return this.tail.pre
}
func (this *DLinkedList) isEmpty() bool {
	return this.head.next == this.tail
}

type LFUCache struct {
	capacity int
	keyMap   map[int]*Node
	freqMap  map[int]*DLinkedList
	minFreq  int
}

func Constructor(capacity int) LFUCache {
	lfu := LFUCache{capacity: capacity,
		keyMap:  map[int]*Node{},
		freqMap: map[int]*DLinkedList{},
		minFreq: 0,
	}
	return lfu
}

func (this *LFUCache) Get(key int) int {
	// 获得值并更新freq值
	if node, ok := this.keyMap[key]; ok {
		// 更新freq值
		this.updateFreqMap(node, false)
		return node.value
	}
	return -1

}

func (this *LFUCache) Put(key int, value int) {
	if this.capacity == 0{
		return
	}
	if _, ok := this.keyMap[key]; ok {
		node := this.keyMap[key]
		node.value = value
		this.updateFreqMap(node, false)
	} else {
		node := &Node{key: key, value: value, freq: 1}
		// 更新到keyMap
		this.keyMap[key] = node
		// 超过容量删除
		if len(this.keyMap) == this.capacity {
			this.removeMinFreqLastNode()
		}
		// 更新到FreqMap
		this.updateFreqMap(node, true)

	}

}

func (this *LFUCache) updateFreqMap(node *Node, isNew bool) {
	if isNew {
		println(node.key, node.value,node.freq)
		this.minFreq = 1
		// 插入到链表头部
		this.insertFirst(node)
	} else {
		// 删除链表在原有位置
		this.deleteNode(node)
		// 频率+1
		node.freq += 1
		// 插入到链表头部
		this.insertFirst(node)
		// 更新最小freq
		if _, ok := this.keyMap[this.minFreq]; !ok {
			this.minFreq += 1
		}
	}
}

func (this *LFUCache) insertFirst(node *Node) {
	// 插入节点到对应freq对应的链表
	if _, ok := this.freqMap[node.freq]; !ok {
		this.freqMap[node.freq] = initDLinkedList()
	}

	dLinkedList := this.freqMap[node.freq]
	dLinkedList.addFirst(node)
}

func (this *LFUCache) deleteNode(node *Node) {
	// 在freq链表中删除节点
	if _, ok := this.keyMap[node.freq]; !ok {
		return
	}
	dLinkedList := this.freqMap[node.freq]
	dLinkedList.delete(node)
	// 此freq链表不存在就删除
	if dLinkedList.isEmpty() {
		delete(this.freqMap, node.freq)
	}
}
func (this *LFUCache) removeMinFreqLastNode() {
	// 在freq 链表找到最少频率的最后一个节点，并删除
	dLinkedList := this.freqMap[this.minFreq]
	node := dLinkedList.getList()
	dLinkedList.delete(node)
	// 此freq链表不存在就删除
	if dLinkedList.isEmpty() {
		delete(this.freqMap, node.freq)
		// 在keyMap删除节点
		delete(this.keyMap, node.key)
	}
}

func main() {
	cache := Constructor(2)
	cache.Put(1,1)
}