from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        快慢指针
        快指针遍历找到重复的元素
        慢指针替换前排合法的元素，达到移除数据效果
        """
        n = len(nums)
        if n == 0:
            return 0
        slow = 0
        for fast in range(n):
            # 如果不是去除值，就替换值并前进
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow


if __name__ == '__main__':
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    result = Solution().removeElement(nums, val)
    print(result)
