from typing import List

"""
全排列，回溯dfs+结果set去重，visit[index]=True跳过已经使用过的元素
"""


class Solution:
    def permutation(self, s: str) -> List[str]:
        """
        回溯
        """
        result = set()  # 用集合去重
        track = list()
        n = len(s)
        visit = [False] * n

        def back_track(track):
            # 满足结束条件
            if n == len(track):
                val = ''.join(track)
                result.add(val)
                return
            for idx in range(n):
                # 剪枝
                if visit[idx]:
                    continue
                # 做选择
                track.append(s[idx])
                visit[idx] = True
                # 进入下一层
                back_track(track)
                # 撤销选择
                track.pop()
                visit[idx] = False

        back_track(track)
        return list(result)


if __name__ == '__main__':
    s = "aab"
    print(Solution().permutation(s))
