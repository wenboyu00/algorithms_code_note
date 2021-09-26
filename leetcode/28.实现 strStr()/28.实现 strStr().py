class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n_len = len(needle)
        if n_len == 0:
            return 0
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                h_str = haystack[i:i + n_len]
                if h_str == needle:
                    return i
        return -1


if __name__ == '__main__':
    s1 = "hello"
    s2 = "ll"
    s1 = ''
    s2 = ''
    print(Solution().strStr(s1, s2))
