"""
二叉堆解法-小顶堆
把小顶堆 small 理解成一个筛子，较大的元素会沉淀下去，较小的元素会浮上来；

当堆大小超过 k 的时候，删掉堆顶的元素，因为这些元素比较小。
遍历一遍后，小顶堆里面留下第k个大的元素就是堆顶，堆底是最大的
"""
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        small = []
        for num in nums:
            heapq.heappush(small, num)
            if len(small) > k:
                heapq.heappop(small)
        return small[0]


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    result = Solution().findKthLargest(nums, k)
    print(result)
