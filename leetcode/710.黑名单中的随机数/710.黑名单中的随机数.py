import random
from typing import List


class Solution:
    """
    共有N个数字，黑名单个数=len(blacklist), 白名单个数 n - len(blacklist).
    为了可以使用random.randint(0, self.white_len - 1)随机取得white_len个白名单数字中的一个。
    使用 map 将white_len中黑名单的数字和white_len之后白名单的数字映射起来
    pick时，使用random随机选择一个索引，如果这个索引被到黑名单上，就返回对应的白名单的位置
    """

    def __init__(self, n: int, blacklist: List[int]):
        # 黑名单个数: len(blacklist)
        # 白名单个数(white_len): n - len(blacklist)
        self.white_len = n - len(blacklist)
        # black_set，在white_len之前黑名单中的数字
        black_set = set()
        for i in blacklist:
            if i < self.white_len:
                black_set.add(i)

        # white_set：在white_len之后的白名单中的数字
        white_set = set()
        blacklist_set = set(blacklist)
        for i in range(self.white_len, n):
            if i not in blacklist_set:
                white_set.add(i)
        # 使用map将black_set中的元素和white—set映射起来
        self.map = dict(zip(black_set, white_set))

    def pick(self) -> int:
        # 在前white_len个数字中随机选取
        res = random.randint(0, self.white_len - 1)
        # 如res是map的key，说明这个位置是黑名单中的数字，通过映射取出其对应的白名单的数字
        if res in self.map:
            return self.map[res]
        # 如res不是map的key，说明这个位置是白名单中的数字，直接返回
        else:
            return res


if __name__ == '__main__':
    N = 5
    blacklist = [1, 3]
    result = Solution(N, blacklist).pick()
    print(result)
