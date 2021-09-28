class MinStack:

    def __init__(self):
        self.stk = []
        # 最小值为栈顶，保持栈为降序，push和pop值后栈顶保持可以最小值
        self.min_stk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        # 新值 <= 栈顶值(最小值)，保持栈为降序
        if not self.min_stk or val <= self.min_stk[-1]:
            self.min_stk.append(val)

    def pop(self) -> None:
        val = self.stk.pop()
        # 如果值是最小值栈顶，也要pop出来，保持数据同步和降序要求
        if val == self.min_stk[-1]:
            self.min_stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min_stk[-1]
