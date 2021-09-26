from collections import deque

"""
递归解法：
括号包含的算式，视为一个数字(整体)就行了。
遇到 ( 开始递归
遇到 ) 结束递归
注意：递归时s的变化，递归后s要变更，否则会重复计算
"""


class Solution:
    def calculate(self, s: str) -> int:
        def do(s):
            stk = []
            num = 0
            sign = "+"
            while len(s) > 0:
                c = s.popleft()
                # 如何是数字字符且不为空,更新c到num上
                # *10是应对多位数字的进位
                if c.isdigit():
                    num = 10 * num + int(c)
                # 遇到左括号开始递归 计算 s
                if c == '(':
                    num = do(s)
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
                # 遇到右括号结束递归
                if c == ')':
                    return sum(stk)
            return sum(stk)
        return do(deque(s))


if __name__ == '__main__':
    s = "1 + 1"
    print(Solution().calculate(s))
    s = " 2-1 + 2 "
    print(Solution().calculate(s))
    s = "(1+(4+5+2)-3)+(6+8)"
    print(Solution().calculate(s))
