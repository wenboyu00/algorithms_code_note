class Node:
    def __init__(self, key, val, freq=0):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None
        self.freq = freq


class DLinkedList:
    """
    双向链表
    """

    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head

    def insert_first(self, node):
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node
        node.pre = self.head

    def delete(self, node):
        if self.head.next == self.tail:
            return
        node.pre.next = node.next
        node.next.pre = node.pre
        node.next = None
        node.pre = None

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
        self.freq_map = {}
        self.key_map = {}

    def _increase(self, node, is_new_node=False):
        """
        更新节点访问频率(freq)
        """
        if is_new_node:
            self._minFreq = 1
            self._set_default_linked_list(node)
        else:
            self._delete(node)
            node.freq += 1
            self._set_default_linked_list(node)
            if self.min_freq not in self.freq_map:
                self.min_freq += 1

    def _set_default_linked_list(self, node):
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
        if d_linked_list.is_empty():
            del self.freq_map[freq]

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
        if d_linked_list.is_empty():
            del self.freq_map[node.freq]

    def get(self, key: int) -> int:
        """
        获得元素
        - 如果存在 就返回应对val，更新访问元素访问频率
        - 如果不在，返回 -1
        :param key:
        :return:
        """
        if key in self.key_map:
            node = self.key_map[key]
            self._increase(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        """
        插入指定key:value
        如果key存在则更新value和频率
        如果key不存在，插入新元素
            - 如果已满，则删除频率最低的元素，
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
