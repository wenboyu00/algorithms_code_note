class Solution:
    def decodeString(self, s: str) -> str:
        # 存储括号之前结果
        stk = []
        ans = ''
        # 重复倍数
        num = 0
        # 遍历字符串s
        for c in s:
            # 发现括号[,存储之前内容到栈，并重置
            if c == "[":
                stk.append([num, ans])
                ans, num = "", 0
            # 括号结束,拼接括号内容到之前结果中
            elif c == ']':
                cur_num, last_ans = stk.pop()
                ans = last_ans + cur_num * ans
            # 更新重复倍数，注意进位
            elif c.isdigit():
                num = num * 10 + int(c)
            # 更新字符到结果尾部
            else:
                ans += c
        return ans


if __name__ == '__main__':
    print(Solution().decodeString('3[a]2[bc]'))
    print(Solution().decodeString('3[a2[c]]'))
