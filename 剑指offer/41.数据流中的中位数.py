class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 小顶堆，保存较大的一半
        self.a = []
        # 大顶堆，保存较小的一半
        self.b = []
        # Python 中 heapq 模块是小顶堆。实现 大顶堆 方法： 小顶堆的插入和弹出操作均将元素 取反 即可。
        # 通过弹出另外一个堆顶，来控制2个值相对平衡。

    def addNum(self, num: int) -> None:
        # 不相等时，为奇数，向小顶堆添加
        # 相等时时，为偶数，向大顶堆添加
        if len(self.a) != len(self.b):
            heappush(self.a, num)
            # a弹出最小值到 b，保证a，b数值的大小较平衡
            heappush(self.b, -heappop(self.a))
        else:
            heappush(self.b, -num)
            heappush(self.a, -heappop(self.b))
        # 假设插入数字 num 遇到情况 1.
        # 由于 num 可能属于 “较小的一半” ，因此不能将 num 直接插入至 AA 。
        # 而应先将 num 插入至 BB ，再将 BB 堆顶元素插入至 AA 。这样就可以始终保持 AA 保存较大一半、 BB 保存较小一半。

    def findMedian(self) -> float:
        if len(self.a) != len(self.b):
            return self.a[0]
        else:
            return (self.a[0] - self.b[0]) / 2.0