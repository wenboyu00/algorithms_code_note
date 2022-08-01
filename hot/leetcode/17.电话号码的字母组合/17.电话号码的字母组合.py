from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 组合问题，回溯算法(DFS)
        # 每个数字对应多个字母 进行组合
        # 每组数字的长度 是 每个数字的长度 len(digits)
        # 每次循环拿对应的字母 添加到路径列表中
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        result = []
        path = []
        if not digits:
            return result
        n = len(digits)

        def backtrack(path, index):
            if len(path) == n:
                result.append(''.join(path))
                return
            # 选择列表 数字对应的列表
            # 但是选择的是 数字，所以传入index对数字进行选择
            digit = digits[index]
            for s in phone[digit]:
                path.append(s)
                backtrack(path, index + 1)
                path.pop()

        backtrack(path, 0)
        return result


if __name__ == '__main__':
    digits = "23"
    print(Solution().letterCombinations(digits))
