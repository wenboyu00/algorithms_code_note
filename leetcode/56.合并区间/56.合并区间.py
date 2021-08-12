from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 按照左端升序排序
        intvs = sorted(intervals, key=lambda x: [x[0], -x[1]])
        # x.左端是最小，x.右端是最大。从列表中找到更大的x.右端加上去
        res = [intvs[0]]
        for cur in intvs[1:]:
            # 取出结果的最后一个
            last = res[-1]
            # 当前的左小于最后结果的右，说明交叉区间，拿到他们两个最大的右，作为新的右。
            if cur[0] <= last[1]:
                last[1] = max(last[1], cur[1])
            # 当前左大于 结果右，说明不相交，是一个新的区间。添加到结果列表。
            else:
                res.append(cur)
        return res


if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    result = Solution().merge(intervals)
    print(result)
