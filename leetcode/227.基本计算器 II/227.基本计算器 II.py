class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        stk = []
        num = 0
        sign = "+"
        for i in range(n):
            c = s[i]
            # 如何是数字字符且不为空,更新c到num上
            if c.isdigit():
                num = 10 * num + int(c)
            # 如果是非数字 or 是最后一个元素
            if (not c.isdigit() and c != " ") or i == n - 1:
                if sign == "+":
                    stk.append(num)
                elif sign == '-':
                    stk.append(-num)
                # 实现先乘除，后加减
                # 把栈顶元素和当前元素计算后重新写入栈顶
                elif sign == '*':
                    stk[-1] = stk[-1] * num
                elif sign == '/':
                    stk[-1] = int(stk[-1] / float(num))
                num = 0
                sign = c
        return sum(stk)


if __name__ == '__main__':
    # s = "42"
    # s = "3+2*2"
    s = " 3/2 "
    result = Solution().calculate(s)
    print(result)
