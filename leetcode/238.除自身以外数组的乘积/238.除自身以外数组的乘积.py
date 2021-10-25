from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        避开当前nums[i]的之外的乘积
        计算乘积的时候跳过nums[i]
        - 前缀乘积*后缀乘积，跳过nums[i]
        - 前缀乘积时跳过nums[0]
        - 后缀乘积时跳过nums[-1]
        """
        n = len(nums)
        res, tmp = [1] * n, 1
        # 前缀乘积，下三角，跳过nums[i]
        # 对第一位处理，跳过nums[0]
        for i in range(1, n):
            # 当前结果 = 上一个结果 * 上一个数值
            res[i] = res[i - 1] * nums[i - 1]
        # 后缀乘积，上三角，跳过nums[i]，从后向前
        # 最最后一位处理，跳过nums[-1]
        for i in range(n - 2, -1, -1):
            # 当前结果 = 上一个数值的累计结果 * 当前结果值
            tmp *= nums[i + 1]
            res[i] *= tmp
        return res


if __name__ == '__main__':
    print(Solution().productExceptSelf([1, 2, 3, 4]))
