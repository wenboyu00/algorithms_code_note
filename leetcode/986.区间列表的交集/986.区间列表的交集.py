from typing import List

"""
1.先排序，题目已经排序
2.观察区间关系
    1.没有交集：b2<a1 or a2 < b2
    2.存在交集：b2>a1 and a2 >b1(没交集取相反操作)
        1.找到交集区间，相交的两个区间中，左端点最大的和右端点最大的
        2.推进两个数组前进对比，谁最右端点小，说明落后，谁进一
"""


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        # 双指针，i对A，j对B
        i, j = 0, 0
        res = []
        while i < len(A) and j < len(B):
            a1, a2 = A[i][0], A[i][1]
            b1, b2 = B[j][0], B[j][1]
            # 找到相交区间，ab的最大左端和最小右端
            if b2 >= a1 and a2 >= b1:
                res.append([max(a1, b1), min(a2, b2)])
            # 谁小 谁前进
            if b2 < a2:
                j += 1
            else:
                i += 1
        return res


if __name__ == '__main__':
    firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
    secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
    result = Solution().intervalIntersection(firstList, secondList)
    print(result)
