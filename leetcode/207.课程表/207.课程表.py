from typing import List


class Solution:
    """
    把问题转换成 有向无环图，求是否有环
    flags 用于标记节点状态
    adjacency 存节点与其他节点关系
    flags[i]:
        - 0: 未被访问过
        - 1: 已经当前节点访问过
            本轮DFS中被第二次访问过，即图有环，返回False
        - -1: 已经被其他节点访问过
            已经被其他节点访问过，无需重复
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 存储已pre_index为前置课程的课程列表
        adjacency = [[] for _ in range(numCourses)]
        # 当前节点被访问情况
        flags = [0 for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)

        def dfs(idx):
            if flags[idx] == -1:
                return True
            if flags[idx] == 1:
                return False
            flags[idx] = 1
            for j in adjacency[idx]:
                if not dfs(j):
                    return False
            flags[idx] = -1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    # print(Solution().canFinish(numCourses, prerequisites))
    print(Solution().canFinish(2, [[1, 0]]))
