from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        回溯算法-dfs
        先找到和第一个字母相同的位置 开始回溯找
        """

        m = len(board)
        n = len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # 找到和字母第一位相同的位置开始回溯
                if word[0] == board[i][j]:
                    if self.backtrack(board, i, j, word, 0, visited):
                        return True
        return False

    def backtrack(self, board, row, col, word, idx, visited):
        """
        回溯算法,如果此格子上的值和word[idx]相等就接着回溯找下一个
        board:二维网格
        row：行值
        col:列值
        word:需要找到的字符串
        idx:需要找到字符的索引
        visited:标记是否已经访问，避免重复

        结束条件：回溯长度和word长度相等
        """
        # 结束条件
        if idx == len(word):
            return True
        # 处理越界情况
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
            return False
        # 已经访问过
        if visited[row][col]:
            return False
        # 是否相等，不相等就返回
        if board[row][col] != word[idx]:
            return False
        # 回溯，加入列表中
        visited[row][col] = True
        # 从格子的上下左右寻找(回溯)
        if self.backtrack(board, row + 1, col, word, idx + 1, visited) or \
                self.backtrack(board, row - 1, col, word, idx + 1, visited) or \
                self.backtrack(board, row, col + 1, word, idx + 1, visited) or \
                self.backtrack(board, row, col - 1, word, idx + 1, visited):
            return True
        # 撤销选择
        visited[row][col] = False
        return False


if __name__ == '__main__':
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    print(Solution().exist(board, word))
