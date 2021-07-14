class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return nums
        # 存储最大值
        ans = nums[0]
        # dp[i-1]
        count = nums[0]
        for i in range(1, len(nums)):
            # count > 0，则count对结果有正贡献，count保留并加上当前遍历数字
            if count > 0:
                count += nums[i]
            # count <= 0，则sum对结果负贡献，抛弃当前count，更新当前数字为count
            else:
                count = nums[i]
            # 比较count和ans的大小，将最大值置为ans
            if count > ans:
                ans = count
        return ans
