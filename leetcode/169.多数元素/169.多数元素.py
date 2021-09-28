from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_count = {}
        n = len(nums)
        half_n = n // 2
        for num in nums:
            count = num_count.get(num, 0) + 1
            if count > half_n:
                return num
            num_count[num] = count
