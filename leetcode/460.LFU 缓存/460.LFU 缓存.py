class Node:
    """
    双向链表节点
    """

    def __init__(self, key=None, val=None, freq=0):
        self.key = key
        self.value = val
        self.pre = None
        self.next = None
        self.freq = freq


class DLinkedList:
    """
    双向链表和一些列所需要的操作
    """

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head

    def insert_first(self, node):
        node.next = self.head.next
        node.pre = self.head
        self.head.next.pre = node
        self.head.next = node

    def delete(self, node):
        if self.head.next == self.tail:
            return
        node.pre.next = node.next
        node.next.pre = node.pre

    def get_last(self):
        if self.head.next == self.tail:
            return None
        return self.tail.pre

    def is_empty(self):
        return self.head.next == self.tail


class LFUCache:
    def __init__(self, capacity: int):
        """
        key_map: {key: Node} - 字典
        freq_map: {freq: LinkedList} -字典
        """
        self.capacity = capacity
        self.min_freq = 0
        self.freq_map = dict()
        self.key_map = dict()

    def get(self, key: int) -> int:
        """
        获得元素
        - 如果存在 就返回应对val，更新访问元素访问频率
        - 如果不在，返回 -1
        """
        if key not in self.key_map:
            return -1
        node = self.key_map[key]
        self._increase(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        """
        插入指定key:value
        如果key存在则更新value和频率
        如果key不存在，计划插入新元素
            - 如果已满，则删除频率最低的元素，
            - 插入新元素
        """
        if key in self.key_map:
            node = self.key_map[key]
            node.value = value
            self._increase(node)
        else:
            if self.capacity == 0:
                return
            if len(self.key_map) == self.capacity:
                self._remove_min_freq_node()
            node = Node(key, value, 1)
            self._increase(node, True)
            self.key_map[key] = node

    def _increase(self, node, is_new_node=False):
        """
        更新节点访问频率(freq)
        """
        if is_new_node:
            self.min_freq = 1
            self._insert_first(node)
        else:
            self._delete(node)
            node.freq += 1
            self._insert_first(node)
            if self.min_freq not in self.freq_map:
                self.min_freq += 1

    def _insert_first(self, node):
        """
        根据节点的频率，插入对应的LinkedList中，没有则创建
        """
        if node.freq not in self.freq_map:
            self.freq_map[node.freq] = DLinkedList()
        d_linked_list = self.freq_map[node.freq]
        d_linked_list.insert_first(node)

    def _delete(self, node):
        if node.freq not in self.freq_map:
            return
        d_linked_list = self.freq_map[node.freq]
        freq = node.freq
        d_linked_list.delete(node)
        # 列表为空时，删除freq_map上的索引
        if d_linked_list.is_empty():
            del self.freq_map[freq]
        return node.key

    def _remove_min_freq_node(self):
        """
        删除频率最低的元素
        找到freq_map[min_freq]中最后一个节点删除，同时在key_map也删除
        如果链表为空，则删除此链表
        """
        d_linked_list = self.freq_map[self.min_freq]
        node = d_linked_list.get_last()
        d_linked_list.delete(node)
        del self.key_map[node.key]
        # 列表为空时，删除freq_map上的索引
        if d_linked_list.is_empty():
            del self.freq_map[node.freq]


if __name__ == '__main__':
    lfu = LFUCache(2)
    print(lfu.put(2, 2))
    print(lfu.put(1, 1))
    print(lfu.get(2))
    print(lfu.get(1))
    print(lfu.get(2))
    print(lfu.put(3, 3))
    print(lfu.put(4, 4))
    print(lfu.get(3))
    print(lfu.get(2))
    print(lfu.get(1))
    print(lfu.get(4))
