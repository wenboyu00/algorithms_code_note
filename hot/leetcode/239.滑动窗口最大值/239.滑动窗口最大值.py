from collections import deque
from typing import List


class MQuque:
    def __init__(self):
        self.queue = deque()

    def push(self, num):
        while self.queue and self.queue[-1] < num:
            self.queue.pop()
        self.queue.append(num)

    def max(self):
        return self.queue[0]

    def pop(self, num):
        if num == self.queue[0]:
            self.queue.popleft()


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = MQuque()
        res = []

        for i in range(len(nums)):
            # 先填窗口的前 k -1
            if i < (k - 1):
                window.push(nums[i])
            else:
                # 窗口向前滑动，加入新数字
                window.push(nums[i])
                res.append(window.max())
                # 窗口向前滑动，移除旧数字
                # i是0~n， k是1~k, i+1 才能对上k的index
                window.pop(nums[i + 1 - k])
        return res


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    result = Solution().maxSlidingWindow(nums, k)
    print(result)
