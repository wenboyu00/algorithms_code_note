from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        1.左上-右下  主对角线行列互换对称 翻转
        2.左右 垂直线对称翻转
        """
        n = len(matrix)
        # 左上右下 主对角线对称翻转
        for i in range(n):
            for j in range(i):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
        # 左右 垂直线对称翻转
        for i in range(n):
            left = 0
            right = n - 1
            while left < right:
                temp = matrix[i][left]
                matrix[i][left] = matrix[i][right]
                matrix[i][right] = temp
                left += 1
                right -= 1


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate(matrix)
