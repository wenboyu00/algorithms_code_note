from typing import List

"""
依次比较所有字符串 对应的字符
双层for循环
1层循环，循环第一个字符串 strs[0][i] 
2层循环, 循环每个字符串 strs[j][i] 在i位置上所有字符进行对比
i超出strs[j]长度 ，或者 和第一个字符不想等时 返回
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 循环第一个字符串
        for i in range(len(strs[0])):
            c = strs[0][i]
            # 循环所有字符串
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][0:i]
        return strs[0]
