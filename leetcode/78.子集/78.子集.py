from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 路径
        track = []
        res = []
        n = len(nums)

        def back_track(start):
            # 满足结束条件
            res.append(list(track))
            # 遍历 选择
            for i in range(start, n):
                # 做选择
                track.append(nums[i])
                # 递归
                back_track(i + 1)
                # 撤销选择
                track.pop()

        back_track(0)
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    result = Solution().subsets(nums)
    print(result)
