from typing import List

"""
利用回溯算法
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return
    
    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择

路径：board 中小于 row 的那些行都已经成功放置了皇后
选择列表：第 row 行的所有列都是放置皇后的选择
结束条件：row 超过 board 的最后一行
"""


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = list()
        # '.' 表示空，初始化空棋盘。
        board = list()
        for i in range(n):
            board.append(["."] * n)

        def is_valid(board, row, col):
            """
            因为同一行row只放置一个 Q，所以不需要判断
            因为Q下面都为空，所以左下，右下不需要判断
            """
            n = len(board)   # n = 棋盘的长度
            # 检查同一列是否有皇后冲突
            for i in range(n):
                if board[i][col] == 'Q':
                    return False
            # 右上角行和右上角列的index列表生成
            # row-1，从上一列开始到0，step=-1表示递减
            right_up_row_index = [i for i in range(row - 1, -1, -1)]
            right_up_col_index = [i for i in range(col + 1, n)]
            # 判断右上角是否有皇后冲突
            for i, j in zip(right_up_row_index, right_up_col_index):
                if board[i][j] == "Q":
                    return False

            # 判断左上角是否有皇后冲突
            left_up_row_index = [i for i in range(row - 1, -1, -1)]
            left_up_col_index = [i for i in range(col - 1, -1, -1)]
            for i, j in zip(left_up_row_index, left_up_col_index):
                if board[i][j] == "Q":
                    return False
            return True

        def back_track(board, row):
            # 结束条件，函数到棋盘格底了，保存结果。
            if row == len(board):
                str_res = list()
                for b in board:
                    str_res.append(''.join(b))
                result.append(str_res)
                return

            n = len(board[row])
            for col in range(n):
                # 判断是否合法
                if not is_valid(board, row, col):
                    continue
                # 做选择
                board[row][col] = 'Q'
                # 进入下一行决策
                back_track(board, row + 1)
                # 撤销选择
                board[row][col] = '.'
        # 做最初的选择
        back_track(board, 0)
        return result


if __name__ == '__main__':
    res = Solution().solveNQueens(4)
    print(res)
