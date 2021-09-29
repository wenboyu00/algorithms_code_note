class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 组合，回溯算法
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        need_list = []
        for s in digits:
            need_list.append(mapping.get(s, ''))
        need_str = "".join(need_list)
        result = []
        path = []

        def backtrack(path, need_str):
            if len(path) == len(need_list):
                result.append(''.join(path))
                return
            for s in need_list:
                path.append(s)
                backtrack(path, need_str)
                path.pop()

        backtrack(path, need_str)
