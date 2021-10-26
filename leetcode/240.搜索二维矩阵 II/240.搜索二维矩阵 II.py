from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        对每一行进行二分查找，如果找不到就去下一行
        时间复杂度: mlogn
        """
        n = len(matrix[0])
        for row in matrix:
            idx = self.search(row, target)
            if idx < n and row[idx] == target:
                return True
        return False

    def search(self, nums, target):
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return left


if __name__ == '__main__':
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]
    target = 5
    #
    # matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24],
    #           [18, 21, 23, 26, 30]]
    # target = 20

    print(Solution().searchMatrix(matrix, target))
