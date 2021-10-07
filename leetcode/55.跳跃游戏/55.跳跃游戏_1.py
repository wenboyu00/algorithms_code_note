from typing import List


class Solution:
        def canJump(self, nums: List[int]) -> bool:
            """
            动态规划-优化
            far(最远距离)代替dp数组：
            base case: far = nums[0]
            选择：far = max(far, nums[i](跳跃长度) + i(当前位置))
            状态:无
            如果 far <= i:
                return False
            return far>= 最后长度
            """
            n = len(nums)
            far = nums[0]
            for i in range(n - 1):
                # 不断计算能跳到的最远距离
                far = max(far, i + nums[i])
                # 最远距离 <= 当前位置距离，就跳不动了
                if far <= i:
                    return False
            return far >= n - 1


if __name__ == '__main__':
    print(Solution().canJump(nums=[2, 3, 1, 1, 4]))
    print(Solution().canJump(nums=[3, 2, 1, 0, 4]))
    print(Solution().canJump(nums=[0, 2, 3]))
