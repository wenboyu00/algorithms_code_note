"""
子串不连续
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # need 需求字符出现次数，window窗口字符出现次数
        need = dict()
        window = dict()
        # need初始化字符为1，window初始化为0
        for i in t:
            need[i] = need.get(i, 0) + 1
            window[i] = window.get(i, 0)
        # 窗口区间
        left, right = 0, 0
        # 有效字符数量
        valid = 0
        # 记录覆盖最小字串的起始索引和长度
        start, str_len = 0, len(s) + 1
        # 增大窗口寻找可行解
        while right < len(s):
            # c是将移入窗口的字符串
            c = s[right]
            right += 1
            # 进行窗口内数据的操作
            if c in need:
                # 窗口内字符出现次数
                window[c] += 1
                # 记录有效次数
                if window[c] == need[c]:
                    valid += 1
            # 减小窗口优化可行解，判断左侧窗口是否要收缩，有效次数==需求字符数量
            while valid == len(need):
                # 更新最小覆盖子串
                # 比上次短，才更新 right-left是匹配到字符串长度
                if right - left < str_len:
                    start = left
                    str_len = right - left
                # d是将移除窗口的字符
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        if str_len == len(s) + 1:
            return ""
        return s[start:start + str_len]


if __name__ == '__main__':
    # s = "ADOBECODEBANC"
    # t = "ABC"
    s = "cabwefgewcwaefgcf"
    t = "cae"
    result = Solution().minWindow(s=s, t=t)
    print(result)
