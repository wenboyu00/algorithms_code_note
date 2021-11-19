class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        栈
        遍历中
        存入'('到栈与之后')'匹配，索引之间差值长度。用没有匹配的右括号下标做有效括号分割
        """
        max_ans = 0
        # 初始化栈，base case: -1，表示最后一个没有比匹配的下标
        stk = [-1]
        for i in range(len(s)):
            # 直接入栈
            if s[i] == '(':
                stk.append(i)
            # 把匹配到的( 将栈中索引弹出
            else:
                stk.pop()
                # 如果不为空，说明保存着"最后一个没有匹配到的右括号下标"
                # - 当前i减去最后没有匹配到的括号下标=当前最长括号的长度
                # - 然后取最大值
                if stk:
                    max_ans = max(max_ans, i - stk[-1])
                # 如果为空，此索引为最后一个没有匹配的右括号下标
                else:
                    stk.append(i)
        return max_ans


if __name__ == '__main__':
    s = "(()"
    print(Solution().longestValidParentheses(s))
