# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
#
#
#
#  示例 1：
#
#  输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#
#
#  示例 2：
#
#  输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#
#
#
#
#  限制：
#
#
#  0 <= matrix.length <= 100
#  0 <= matrix[i].length <= 100
#
#
#  注意：本题与主站 54 题相同：https://leetcode-cn.com/problems/spiral-matrix/
#  Related Topics 数组


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        # 行，列
        row = len(matrix)
        col = len(matrix[0])
        # 第一个行, 从左到右
        res = matrix[0]
        if row > 1:
            # 从上到下，最右边一列
            for i in range(1, row):
                res.append(matrix[i][col - 1])
            # 从右到左，最下边一行；倒数第二开始到第一个：col-2 ~ 0
            for i in range(col - 2, -1, -1):
                res.append(matrix[row - 1][i])

            if col > 1:
                # 从下到上，最左边一列；倒数第二开始到第二个：row-2 ~ 1
                for i in range(row - 2, 0, -1):
                    res.append(matrix[i][0])
        #  得到里边的数据进行递归
        m = []
        for k in range(1, row - 1):
            m.append(matrix[k][1:-1])
        return res + self.spiralOrder(m)


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    res = Solution().spiralOrder(matrix)
    print(res)
