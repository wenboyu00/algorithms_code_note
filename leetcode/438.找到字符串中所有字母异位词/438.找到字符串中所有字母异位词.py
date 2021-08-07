from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need, window = {}, {}
        for i in p:
            need[i] = need.get(i, 0) + 1
            window[i] = 0

        left, right = 0, 0
        valid = 0
        result = list()
        # 扩大窗口，对需求的字符计数
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            # 缩小窗口，窗口长度大于需求字符串长度时对窗口内容进行判断，满足时添加初始索引即 窗口左区间
            while right - left >= len(p):
                if valid == len(need):
                    result.append(left)
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return result


if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    result = Solution().findAnagrams(s, p)
    print(result)
