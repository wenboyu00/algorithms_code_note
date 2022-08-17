from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        判断s是否可以被连续被wordDict拆分
            找到s[i]是否被拆分，首先要判断s[i-1]可以被拆分

        动态规划
        dp数组: 0 ~ n+1 是否可以被拆分相应单词（index向前移一位）
        base case: dp[0] = True,空字符，可以被拆分，作为开始
                dp[1~n]= False，默认不可拆分
        遍历s，
        判断s[low:high]等于word时，dp[high]=True
            - high = low + 单个单词长度
        遍历s，判断以low为起点+查找单词长度为终点，判断是否查找到
        返回：dp[n]
        """
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for low in range(n):
            if not dp[low]:
                continue
            for word in wordDict:
                high = low + len(word)
                if high < n + 1 and s[low:high] == word:
                    dp[high] = True
        return dp[n]


if __name__ == '__main__':
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(Solution().wordBreak(s, wordDict))
