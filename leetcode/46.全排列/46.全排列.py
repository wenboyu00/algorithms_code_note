from typing import List


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        1、路径：也就是已经做出的选择。
        2、选择列表：也就是你当前可以做的选择。
        3、结束条件：也就是到达决策树底层，无法再做选择的条件。
        """
        result = []
        track = []

        def back_track(nums, track):
            # 结束条件
            # 路径和选择长度一致，达到叶子根节点，将路径装入结果列表
            if len(track) == len(nums):
                result.append(tuple(track))
                return None

            # for 选择 in 选择列表
            for num in nums:
                if num in track:
                    continue
                # 做选择
                track.append(num)
                # back_track(选择列表, 路径) 进入下一层
                back_track(nums, track)
                # 撤销选择
                track.pop()

        back_track(nums, track)
        return result


if __name__ == '__main__':
    nums = [1, 2, 3]
    res = Solution().permute(nums)
    print(res)
