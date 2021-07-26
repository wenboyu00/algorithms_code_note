from typing import List


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        result = list()

        def back_track(nums, track):
            # 满足结束条件
            # 达到叶子根节点，将路径装入结果列表
            if len(track) == len(nums):
                result.append(tuple(track))
                return None

            for i in nums:
                # 排除不合法选择
                if i in track:
                    continue
                # 做选择
                track.append(i)
                # 进入下一层决策树
                back_track(nums, track)
                # 取消选择
                track.pop(-1)

        back_track(nums, [])
        return result


if __name__ == '__main__':
    nums = [1, 2, 3]
    res = Solution().permute(nums)
    print(res)
