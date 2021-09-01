import heapq


class MedianFinder:

    def __init__(self):
        """
        large列表：小顶堆
        small列表：大顶堆
        heapq.heappush()是往堆中添加新值，此时自动建立了小顶堆
        创建大顶堆每次push时给元素加一个负号
        """
        self.large = list()
        self.small = list()

    def addNum(self, num: int) -> None:
        """
        添加元素，使用堆的方法添加
        谁元素少，就加到它那里（隔山打牛)
            - 先把num添加到 元素多的堆里
            - 再把元素多的堆 对顶添加到元素少的堆里面
        注意：大顶堆值 负号的问题
        """
        small_ = self.small
        large_ = self.large

        if len(small_) >= len(large_):
            heapq.heappush(small_, -num)
            heapq.heappush(large_, -heapq.heappop(small_))
        else:
            heapq.heappush(large_, num)
            heapq.heappush(small_, -heapq.heappop(large_))

    def findMedian(self) -> float:
        """
        查找中值，不需要pop
        谁元素多，谁就是中值
        一样多，顶值相加 / 2
        """
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        return (-self.small[0] + self.large[0]) / 2


if __name__ == '__main__':
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    param_2 = obj.findMedian()
    print(param_2)
    obj.addNum(3)
    param_3 = obj.findMedian()
    print(param_3)
