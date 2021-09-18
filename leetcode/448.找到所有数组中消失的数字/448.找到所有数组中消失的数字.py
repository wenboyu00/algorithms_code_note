from typing import List

"""
遍历用set进行保存
再生成1~n+1的数值，进行查找，如果不存在就存入结果集
"""


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        nums_set = set()
        for num in nums:
            nums_set.add(num)

        for i in range(1, n + 1):
            if i not in nums_set:
                res.append(i)

        return res


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    result = Solution().findDisappearedNumbers(nums)
    print(result)
