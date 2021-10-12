from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        通过双指针把数组分为3部分[0,1,2]
        遍历数组，把所有0交换到数组左边，1保持不动放在中间，2交换到右边
        遍历数组，i从左到右，p2从右到左，i超过p2时结束
        i <= p2:
            - nums[i]==0,和nums[p0]交换，p0和i前进
            - nums[i]==1,保持不动，i前进
            - nums[i]==2,和nums[p2]交换, p2前进
                - i 保持不动，因为和nums[p2]交换后，nums[i]可能还是2，所以i要进入下一轮循环
        """
        n = len(nums)
        p0, p2 = 0, n - 1
        i = 0
        while i <= p2:
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1


if __name__ == '__main__':
    res = Solution()
    print(res.sortColors(nums=[2, 0, 2, 1, 1, 0]))
