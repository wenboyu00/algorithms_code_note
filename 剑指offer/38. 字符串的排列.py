# 输入一个字符串，打印出该字符串中字符的所有排列。
#
#
#
#  你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
#
#
#
#  示例:
#
#  输入：s = "abc"
# 输出：["abc","acb","bac","bca","cab","cba"]
#
#
#
#
#  限制：
#
#  1 <= s 的长度 <= 8
#  Related Topics 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permutation(self, s: str) -> List[str]:
        if s == '':
            return []
        res = []
        self.backtrack(s, '', res)
        return res

    def backtrack(self, s, exist, res):
        if not s:
            res.append(exist)
        #  排除重复内容
        visited = set()
        #  根据字符串长度遍历
        #  除当前字符之外的字符进行组合；当字符串为空时组合完成，添加到结果中。
        # # 递归结束后返回上一级，遍历会造成字符右移，再进行组合，最后添加到结果中。
        for i in range(len(s)):
            if s[i] in visited:
                continue
            visited.add(s[i])
            #  递归：s[:i]}{s[i+1:]->排除i的字符串和已经存在字符
            self.backtrack(f'{s[:i]}{s[i + 1:]}', f'{exist}{s[i]}', res)
# leetcode submit region end(Prohibit modification and deletion)
