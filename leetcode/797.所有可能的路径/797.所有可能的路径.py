from typing import List


class Solution:
    def __init__(self):
        # 记录所有路径
        self.res = []

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path = list()
        self.traverse(graph, 0, path)
        return self.res

    def traverse(self, graph: List[List[int]], s: int, path: List[int]):
        # 添加节点 s 到路径
        path.append(s)
        n = len(graph)
        # base case 到达终点
        if s == n - 1:
            # 把路径添加到结果集中,从路径中移除节点s
            self.res.append([i for i in path])
            path.pop()
            return

        # 递归每个相邻的节点
        for v in graph[s]:
            self.traverse(graph, v, path)
        # 从路径移除节点 s
        path.pop()


if __name__ == '__main__':
    graph = [[1, 2], [3], [3], []]
    result = Solution().allPathsSourceTarget(graph)
    print(result)
