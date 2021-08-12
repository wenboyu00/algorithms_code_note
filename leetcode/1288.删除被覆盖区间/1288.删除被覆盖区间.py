from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # 按照起点升序排序，起点相同时终点降序
        intvs = sorted(intervals, key=lambda x: [x[0], -x[1]])
        # 记录合并区间的起点和终点
        left, right = intvs[0][0], intvs[0][1]
        res = 0
        for lf, r in intvs[1:]:
            # 找到覆盖区间
            if left <= lf and right >= r:
                res += 1
            # 找到相交区间，合并
            if lf <= right <= r:
                right = r
            # 完全不相交，更新起点和终点
            if right < lf:
                left = lf
                right = r
        return len(intervals) - res


if __name__ == '__main__':
    # intervals = [[1, 4], [3, 6], [2, 8]]
    intervals = [[1, 4], [2, 3]]
    result = Solution().removeCoveredIntervals(intervals)
    print(result)
