"""
通过word1[m-1]到word2[n-1]的方法找到word1转换为word2最少次数
dp数组
- dp[i][j] 代表 word1 中前 i 个字符，变换到 word2 中前 j 个字符，最短需要操作的次数
- 保存word1[i]word2[j]具体修改成一样的最小操作次数，至于字符串具体修改什么样不用操心
base case
- dp[0][j] 和 dp[i][0]
-  word1 或 word2 一个字母都没有的情况
状态转移
加1步：
- 增：dp[i][j] = dp[i][j - 1] + 1
- 删，dp[i][j] = dp[i - 1][j] + 1
- 改，dp[i][j] = dp[i - 1][j - 1] + 1
- 计算这几步并找到最小值，存储到dp[i][j]
不加1步：
- 字母相等： word1[i - 1] = word2[j - 1] = dp[i - 1][j - 1]
    操作不用+1，相当于上一位的步数数量
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = []
        # 初始化dp数组
        # m是行，n是列，从0开始，相当于word为空的时的操作
        for i in range(m + 1):
            dp.append([0] * (n + 1))
        # base case
        # 第一单词前面有 i 个字符，第二个前面有 0 个字符，需要 i 次操作
        # 第一单词前面有 0 个字符，第二个前面有 j 个字符，需要 j 次操作
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        # 状态转移
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 循环中下标减一，下标变成了从0开始到结束
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min((dp[i - 1][j] + 1,
                                    dp[i][j - 1] + 1,
                                    dp[i - 1][j - 1] + 1))

        return dp[m][n]


if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"
    result = Solution().minDistance(word1, word2)
    print(result)
