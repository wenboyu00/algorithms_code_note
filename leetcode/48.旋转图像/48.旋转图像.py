from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        1.左上-右下 对角线翻转
        2.左右 垂直线翻转
        """
        n = len(matrix)
        # 左上右下 对角线翻转
        for i in range(n):
            for j in range(i):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
        # 左右 垂直线翻转
        for i in range(n):
            left = 0
            right = n - 1
            while left < right:
                temp = matrix[i][left]
                matrix[i][left] = matrix[i][right]
                matrix[i][right] = temp
                left += 1
                right -= 1
