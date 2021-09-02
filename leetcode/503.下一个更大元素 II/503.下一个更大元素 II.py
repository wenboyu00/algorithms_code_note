from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        利用循环数组技巧来模拟数组长度2倍的结果
        n~2n-1 就是2倍长度，在这个范围内找到下一个最大的值放到单调栈中
        0~n-1循环时，nums[n-1]就以单调栈中的数据找到下一个最大值
        因为res对应nums的下一个最大值，所以取值nums[i%n]和存储位置res[i%n]都是要%取模，来模拟长度2倍的效果
        """
        n = len(nums)
        res = [-1] * n
        stk = []
        for i in range(n * 2 - 1, -1, -1):
            while stk and nums[i % n] >= stk[-1]:
                stk.pop()
            res[i % n] = stk[-1] if stk else -1
            stk.append(nums[i % n])
        return res


if __name__ == '__main__':
    nums = [1, 2, 1]
    result = Solution().nextGreaterElements(nums)
    print(result)
