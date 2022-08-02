class Solution:
    def isValid(self, s: str) -> bool:
        # 如果长度不是偶数，说明不成对，不合法。
        if len(s) % 2 == 1:
            return False
        # 存放左括号
        stk = []
        # 右括号和左括号对应
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        # 遍历字符串
        for ch in s:
            # 如果发现右括号，在栈中找到对应左括号，找到就弹出，找不到 就不合法
            if ch in mapping:
                # 如果发现右括号时，栈为空，说不成对，不合法。
                if not stk or stk[-1] != mapping[ch]:
                    return False
                stk.pop()
            else:
                stk.append(ch)
        return not stk


if __name__ == '__main__':
    s = "()[]{}"
    print(Solution().isValid(s))
