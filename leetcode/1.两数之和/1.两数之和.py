from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = dict()
        for i in range(len(nums)):
            if mapping.get(target-nums[i]) is not None:
                return [i, mapping[target-nums[i]]]
            mapping[nums[i]] = i
        return []