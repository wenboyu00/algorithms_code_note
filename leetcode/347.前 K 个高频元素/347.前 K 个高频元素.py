from typing import List


class Solution:
    # 桶排序
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 统计每个元素出现的次数，num为key，count为value
        mapping = {}
        for num in nums:
            mapping[num] = mapping.get(num, 0) + 1

        # 桶排序
        # 以频率作为数组下标
        freq_list = [[] for _ in range(len(nums)+1)]
        for num, count in mapping.items():
            freq_list[count].append(num)
        #  倒序遍历数组，添加数组的值到结果集中。遍历到k是返回
        ans = []
        for i in range(len(nums), 0, -1):
            ans.extend(freq_list[i])
            if len(ans) == k:
                return ans
        return ans


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(Solution().topKFrequent(nums, k))
