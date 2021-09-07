from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 数组有序，使用双指针技巧，从数组两边开始，类似于二分查找
        left = 0
        right = len(numbers) - 1
        while left < right:
            num = numbers[left] + numbers[right]
            if num == target:
                # 题目要求的索引是从 1 开始的，所有+1
                return [left + 1, right + 1]
            # 让num大一些
            elif num < target:
                left += 1
            # 让num小一些
            else:
                right -= 1
        return [-1, -1]


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9
    result = Solution().twoSum(numbers, target)
    print(result)
