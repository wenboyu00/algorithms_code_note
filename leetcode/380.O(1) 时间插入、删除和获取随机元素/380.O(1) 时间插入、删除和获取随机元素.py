import random


class RandomizedSet:
    """
    等概率在O(1)时间随机取出元素要满足：
    - 底层用数组
    - 数组必须是紧凑的

    数组存储如何满足O(1)插入和删除时间复杂度
    - 对数组尾部进行插入和删除，不涉及到数据搬运，就是O(1)
    - 在 O(1) 的时间删除数组中的某一个元素val，可以先把这个元素交换到数组的尾部，然后再pop掉
    - 交换两个元素必须通过索引进行交换，需要一个哈希表val_index_map来记录每个元素值对应的索引。
    """

    def __init__(self):
        self.l = []
        self.val_idx_map = {}

    def insert(self, val: int) -> bool:
        if val in self.val_idx_map:
            return False
        self.val_idx_map[val] = len(self.l)
        self.l.append(val)

    def remove(self, val: int) -> bool:
        if val in self.val_idx_map:
            val_idx = self.val_idx_map[val]
            last = self.l[-1]
            self.l[val_idx] = last
            self.val_idx_map[last] = val_idx
            self.l.pop()
            self.val_idx_map.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.l)


if __name__ == '__main__':
    obj = RandomizedSet()
    param_1 = obj.insert(0)
    param_2 = obj.insert(1)
    param_3 = obj.remove(0)
    param_4 = obj.insert(2)
    param_5 = obj.remove(1)
    param_6 = obj.getRandom()
    print(param_1)
    print(param_2)
    print(param_3)
    print(param_4)
    print(param_5)
    print(param_6)
