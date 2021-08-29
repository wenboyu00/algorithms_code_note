class DLinkNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        # 使用伪头节点和尾节点
        self.head = DLinkNode()
        self.tail = DLinkNode()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 如果key存在，先通过哈希表找到位置，再移到头部
        node = self.cache[key]
        self.move2head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 如果key不存在，创建一个新的节点
            node = DLinkNode(key, value)
            # 添加进哈希表
            self.cache[key] = node
            # 添加到链表头部
            self.add2head(node)
            self.size += 1
            # 超出容量，删除链表尾部节点
            if self.size > self.capacity:
                remove = self.remove_tail()
                # 删除哈希表中对应的节点
                self.cache.pop(remove.key)
                self.size -= 1
        else:
            # 如果key存在，先通过哈希表定位，再修改value，最后移到头部
            node = self.cache[key]
            node.value = value
            self.move2head(node)

    # 添加节点到链表头部
    def add2head(self, node):
        node.pre = self.head
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node

    # 删除节点
    def remove_node(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    # 移动节点到头部
    def move2head(self, node):
        self.remove_node(node)
        self.add2head(node)

    # 删除尾部节点
    def remove_tail(self):
        node = self.tail.pre
        self.remove_node(node)
        return node
