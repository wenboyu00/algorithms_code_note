class Solution:
    # 判断s1是否存在s2排列中
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 初始化需求字典和窗口字典，用于判断数量
        need = dict()
        window = dict()
        for s in s1:
            need[s] = need.get(s, 0) + 1
            window[s] = 0
        left, right = 0, 0
        valid = 0
        # 扩大窗口，更新window数量，如果是需求字符，更新有效数量
        while right < len(s2):
            c = s2[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            # 缩小窗口
            while (right - left) >= len(s1):
                # 判断是否找到合法子串
                if valid == len(need):
                    return True
                d = s2[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return False


if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidbaooo"
    result = Solution().checkInclusion(s1, s2)
    print(result)