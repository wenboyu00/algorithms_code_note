from typing import List


class Solution:
    """
    1. 移动非零的数据到 队前
        - 快慢指针
        - 快指针遍历数组找到非0的数据，0的索引跳过
        - 慢指针替换非0数据到前排，留下0数组长度在队尾
    2. 队尾[slow, n)长度赋值为0
    """
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        if n == 0:
            return None
        slow = 0
        for fast in range(n):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
        for i in range(slow, n):
            nums[i] = 0


if __name__ == '__main__':
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    result = Solution().moveZeroes(nums)
    print(nums)
