from typing import List

"""
括号性质：
    1. 一个合法括号的左括号数量一定等于右括号数量
    2. 一个合法括号的字串的左括号数量都大于活等于右括号数量
问题分解：
计算n对括号的组合
    组合（回溯）
    合法括号（根据性质）
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        track = []
        if n == 0:
            return res

        # left 左括号数量，right 右括号数量
        def backtrack(left, right):
            # 若左括号剩下的多，说明不合法
            if right < left:
                return
            # 括号数量小于0
            if left < 0 or right < 0:
                return
            # 合法数量都为0
            if left == 0 and right == 0:
                res.append(''.join(track))
                return
            # 遍历选择，放括号
            # 放左括号
            track.append('(')
            backtrack(left - 1, right)
            track.pop()

            # 放右括号
            track.append(')')
            backtrack(left, right - 1)
            track.pop()

        backtrack(n, n)
        return res


if __name__ == '__main__':
    n = 3
    result = Solution().generateParenthesis(n)
    print(result)
