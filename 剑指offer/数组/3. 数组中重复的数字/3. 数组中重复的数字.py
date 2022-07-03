from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        result = -1
        if not nums:
            return result
        aset = set()
        for num in nums:
            if num in aset:
                result = num
            aset.add(num)
        return result


if __name__ == '__main__':
    nums = [2, 3, 1, 0, 2, 5, 3]
    print(Solution().findRepeatNumber(nums))
