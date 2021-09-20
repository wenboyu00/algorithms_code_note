import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.ori = nums

    def reset(self) -> List[int]:
        return self.ori

    def shuffle(self) -> List[int]:
        """
        洗牌算法：随机选取元素进行交换来获取随机性，必须产生n!种可能
        关键：根据i~n长度来实现阶乘效果 rand = random.randrange(i, n)
            第一次：0~n-1, n 种可能
            第二次：1~n-1, n-1 种可能
            第三次：2~n-1, n-2 种可能
            最终完成n!种结果，满足条件实现洗牌算法
        """
        array = list(self.ori)
        n = len(array)
        for i in range(n):
            rand = random.randrange(i, n)
            array[i], array[rand] = array[rand], array[i]
        return array


if __name__ == '__main__':
    nums = [1, 2, 3]
    obj = Solution(nums)
    print(obj.shuffle())
    print(obj.reset())
    print(obj.shuffle())
