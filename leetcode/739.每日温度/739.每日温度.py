from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        计算和下一个最大值之间的索引距离
        """
        n = len(temperatures)
        stack = []
        # 存放索引
        res = [0] * n
        # 单调栈，从尾到头
        for i in range(n - 1, -1, -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            # 得到索引间隙
            if stack:
                res[i] = stack[-1] - i
            else:
                res[i] = 0
            # 索引入栈
            stack.append(i)
        return res


if __name__ == '__main__':
    temperatures = [89, 62, 70, 58, 47, 47, 46, 76, 100, 70]
    result = Solution().dailyTemperatures(temperatures)
    print(result)
