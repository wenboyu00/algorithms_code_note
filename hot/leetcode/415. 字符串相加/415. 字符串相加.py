class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        c = 0
        ans = ""
        # 双指针，从尾部开始
        i, j = len(num1) - 1, len(num2) - 1
        while i >= 0 or j >= 0 or c:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            cur = c + n1 + n2
            c = cur // 10
            ans = str(cur % 10) + ans
            i -= 1
            j -= 1
        return ans