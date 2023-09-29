from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        一圈一圈旋转赋值，用tmp做临时变量
        """
        # 一轮完成4个元素旋转，因此从左上角开始旋转到1/4处
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                # 保存左上角
                tmp = matrix[i][j]
                # 左下角->到左上角
                matrix[i][j] = matrix[n - 1 - j][i]
                # 右下角->左下角
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                # 右上角 -> 右下角
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                # 保存左上角 -> 右上角
                matrix[j][n - 1 - i] = tmp


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate(matrix)
