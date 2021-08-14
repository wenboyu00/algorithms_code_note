from typing import List

"""
[   -4, -1, -1,  0,  1, 2   ]
    i   l               r
     ->  -->          <--                           
对排序的数组遍历，使用三指针，固定一个值i，对i后面的数组使用左右双指针，通过目标值的对比来移动l和r 已使达到目标
对数组排序，排序固定一个数nums[i]，再使用左右指针只想nums[i]后两端，计算和0的关系，
    - 大于0：减小r 使值变的更小
    - 小于0：增大l 使值变的更大
    - 等于0：添加到结果集，
        - 对l指针进行去重，和前值相等进一
        - 对r指针进行去重，和后值相等减一
        - 去重后 l加一，r减一
    - 对i指针去重， 和前值相等跳过
时间复杂度O(n^2)
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        ans = []
        for i in range(n):
            val = nums[i]
            if val > 0:
                continue
            # i 去重（和前值相等就跳过，实现去重）
            if i > 0 and val == nums[i - 1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                three_sum = val + nums[l] + nums[r]
                if three_sum == 0:
                    ans.append([val, nums[l], nums[r]])
                    # l去重，和前值相等进一
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    # r去重，和后值相等减一
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
        return ans


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    result = Solution().threeSum(nums)
    print(result)
