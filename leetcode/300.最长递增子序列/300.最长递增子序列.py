from typing import List

"""
[2,5,3,7]
[2,5,3]
[2,5]

列表：[2,5,3,7],需要从nums[0]到nums[n]最优解；
列表：[2,5,3],可以通过nums[0]到nums[n-1]推导出来。
反过来呢，既然是递增子序列，
所以找到前面那些结尾比 7 小的子序列，然后把 7 接到最后，就可以形成一个新的递增子序列，而且这个新的子序列长度加一。
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # 以每一项为结尾的最长子序列的长度 作为dp[i]的值
        dp = [1] * len(nums)
        # 遍历每个数
        for i in range(len(nums)):
            for j in range(i):
                # 如果nums[i]大于nums[j]，相当于nums[i]的值接上nums[0...j]子序列，称为新的子序列
                # dp[j]+1 要和 dp[i]做一个大小比较，因为dp[i]可能是最大的，然后赋值给dp[i]
                print(f'nums[j]:{nums[j]} | nums[i] :{nums[i]}')
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
        # 遍历取出最大值，即最长子序列的长度
        res = 0
        for i in dp:
            res = max(res, i)
        return res


if __name__ == '__main__':
    l = [10, 9, 2, 5, 3, 7, 101, 18]
    result = Solution().lengthOfLIS(l)
    print(result)
