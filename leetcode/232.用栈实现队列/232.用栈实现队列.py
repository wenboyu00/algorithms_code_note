class MyQueue:
    """
    用两个栈实现一个队列
    栈1，压入1，2，3，弹出是3，2，1
    栈2，压入3，2，1，弹出是1，2，3
    这样完成队列的先进先出
    """
    def __init__(self):
        self.s1 = []
        self.s2 = []

    # 添加到队尾
    def push(self, x: int) -> None:
        self.s1.append(x)

    # 删除队头并返回
    def pop(self) -> int:
        self.peek()
        return self.s2.pop()

    def peek(self) -> int:
        """
        返回头元素
        如果s2为空，就从s1中压入数据
        返回s2最后一个元素
        """
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        """
        判断队列是否为空
        如果两个栈都为空时，为空
        """
        return not self.s1 and not self.s2


if __name__ == '__main__':
    mq = MyQueue()
    print(mq.push(1))
    print(mq.push(2))
    print(mq.peek())
    print(mq.pop())
    print(mq.empty())
