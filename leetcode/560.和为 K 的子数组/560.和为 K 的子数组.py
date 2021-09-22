from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        pre_sum_map 记录前缀和出现次数，用于统计, base case {0:1}
        sum_j = sum_i - k 用两数和思路，找到适合的前缀和 sum_j
        从前缀和map找到次数
        """
        pre_sum_map = {0: 1}
        ans = sum_i = 0
        for num in nums:
            sum_i += num
            sum_j = sum_i - k
            # 存在就 ans+1
            if sum_j in pre_sum_map:
                ans += pre_sum_map[sum_j]
            # 更新前缀和map
            pre_sum_map[sum_i] = pre_sum_map.get(sum_i, 0) + 1
        return ans


if __name__ == '__main__':
    nums = [1, 1, 1]
    k = 2
    result = Solution().subarraySum(nums, k)
    print(result)
