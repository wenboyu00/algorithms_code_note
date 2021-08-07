class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        left, right = 0, 0
        result = 0
        # 扩大窗口，添加字符
        while right < len(s):
            c = s[right]
            right += 1
            window[c] = window.get(c, 0) + 1
            # 字符计数超过1 说明重复，需要缩小窗口
            while window[c] > 1:
                d = s[left]
                left += 1
                window[d] -= 1
            # 当缩小窗口完成时，说明没有重复，符合 最长子串，并和旧长度对比储存
            result = max(result, right - left)
        return result


if __name__ == '__main__':
    s = "abcabcbb"
    result = Solution().lengthOfLongestSubstring(s)
    print(result)
