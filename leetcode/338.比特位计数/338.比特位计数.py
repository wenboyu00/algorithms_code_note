from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # dp数组, 同时也是结果数组
        result = [0] * (n + 1)
        # base case result[0] = 0, 0的1的个数是0
        for i in range(n + 1):

            if i % 2 == 1:
                # 奇数比前面偶数低位上多1
                result[i] = result[i - 1] + 1
            else:
                # 偶数是除2(0右移，消除一个零)之后的值
                result[i] = result[i // 2]
        return result
