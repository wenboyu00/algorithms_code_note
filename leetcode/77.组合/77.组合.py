from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        track = []
        res = []

        def back_track(start):
            # 满足结束条件，路径数量多大限制数量
            # 多大树底部
            if len(track) == k:
                res.append(list(track))
                return
            # 遍历选择，范围[1~n]
            for i in range(start, n + 1):
                # 做选择
                track.append(i)
                # dfs
                back_track(i + 1)
                # 撤销选择
                track.pop()

        # 范围[1~n] 所以从1开始
        back_track(1)
        return res


if __name__ == '__main__':
    n = 4
    k = 2
    result = Solution().combine(n, k)
    print(result)
