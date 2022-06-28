package 链表

type Node struct {
	Val    int
	Next   *Node
	Random *Node
}

/*
深复制 = 新建值，关系一致
1.拷贝值，构建原节点和新节点映射关系
2.拷贝关系，根据原节点关系 得到新节点关系
*/
func copyRandomList(head *Node) *Node {
	mapping := map[*Node]*Node{}
	// 1. 拷贝值
	cur := head
	for cur != nil {
		n := &Node{cur.Val, nil, nil}
		mapping[cur] = n
		cur = cur.Next
	}
	// 1. 拷贝关系
	cur = head
	for cur != nil {
		mapping[cur].Next = mapping[cur.Next]
		mapping[cur].Random = mapping[cur.Random]
		cur = cur.Next
	}
	return mapping[head]
}
