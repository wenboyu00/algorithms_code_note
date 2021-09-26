from collections import deque

"""
和224 递归解法一样的运算过程
去掉括号的判断
"""


class Solution:
    def calculate(self, s: str) -> int:
        s = deque(s)
        stk = []
        num = 0
        sign = "+"
        while len(s) > 0:
            c = s.popleft()
            # 如何是数字字符且不为空,更新c到num上
            # *10是应对多位数字的进位
            if c.isdigit():
                num = 10 * num + int(c)
            # 如果是非数字 or 是最后一个元素
            if (not c.isdigit() and c != " ") or len(s) == 0:
                if sign == "+":
                    stk.append(num)
                elif sign == '-':
                    stk.append(-num)
                # 实现先乘除，后加减
                # 把栈顶元素和当前元素计算后重新写入栈顶
                elif sign == '*':
                    stk[-1] *= num
                elif sign == '/':
                    stk[-1] = int(stk[-1] / float(num))
                num = 0
                sign = c
        return sum(stk)


if __name__ == '__main__':
    s = " 3/2 "
    result = Solution().calculate(s)
    print(result)
