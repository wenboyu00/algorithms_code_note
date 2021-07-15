from typing import List
"""
杨辉三角对齐后
除了开头结尾是1的
其他都是上一层的当前位置值+当前位置-1
num = result[i-1][j]+result[i-1][j-1]

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            res = []
            for j in range(i + 1):
                # 在开头和结尾都是1
                if j == 0 or j == i:
                    res.append(1)
                else:
                    # 其他位置都是上一层，当前位置1和当前位置-1
                    pre = result[i - 1]     # 上一层
                    res.append(pre[j] + pre[j - 1])
            result.append(res)
        return result


if __name__ == '__main__':
    result = Solution().generate(5)
    print(result)
