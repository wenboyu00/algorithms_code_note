from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        找到最长子序列，num为起点，用num递增值在nums查询是否存在，并更新长度。
        用hashSet进行优化查询过程
        在set中查询num-1是否存在，不存在就作为起点，
            查询num递增值在set中存在时，更新长度
            结束时更新答案
        """
        nums_set = set(nums)
        ans = 0
        for num in nums:
            # num-1来确定起点
            if num - 1 not in nums_set:
                size = 0
                # num递增值存在就更新长度
                while num in nums_set:
                    size += 1
                    num += 1
                # 结束后，更新答案
                ans = max(ans, size)
        return ans


if __name__ == '__main__':
    print(Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
