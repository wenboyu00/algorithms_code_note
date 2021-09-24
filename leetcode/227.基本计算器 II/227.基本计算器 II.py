class Solution:
    def calculate(self, s: str) -> int:
        stk = []
        num = 0
        sign = "+"
        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            if c.isdigit():
                num = 10 * num + int(c)
            if (not c.isdigit() and c != " ") or i == 0:
                if sign == "+":
                    stk.append(num)
                elif sign == '-':
                    stk.append(num)
                elif sign == '*':
                    stk[-1] = stk[-1] * num
                elif sign == '/':
                    stk[-1] = int(stk[-1] / float(num))
                num = 0
                sign = c
        return sum(stk)


if __name__ == '__main__':
    s = "42"
    result = Solution().calculate(s)
    print(result)
