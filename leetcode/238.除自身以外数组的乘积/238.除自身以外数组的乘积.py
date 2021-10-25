from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        b, tmp = [1] * n, 1
        for i in range(1, n):
            b[i] = b[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            tmp *= nums[i + 1]
            b[i] *= tmp
        return b


if __name__ == '__main__':
    print(Solution().productExceptSelf([1, 2, 3, 4]))
