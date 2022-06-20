class Solution:
    def replaceSpace(self, s: str) -> str:
        result = list()
        for c in s:
            if c == ' ':
                result.append('%20')
            else:
                result.append(c)
        return ''.join(result)
