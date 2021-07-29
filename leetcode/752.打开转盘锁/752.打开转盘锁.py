from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = ["0000"]
        deadends_set = set(deadends)
        visited = {q[0]}
        step = 0

        while len(q) != 0:
            size = len(q)
            for i in range(size):
                cur = q.pop(0)
                if cur == target:
                    return step
                if cur in deadends_set:
                    continue
                for j in range(4):
                    up = self.plus_one(cur, j)
                    if up not in visited:
                        q.append(up)
                        visited.add(up)
                    down = self.minus_one(cur, j)
                    if down not in visited:
                        q.append(down)
                        visited.add(down)
            step += 1
        return -1

    def plus_one(self, s, j):
        ch = list(s)
        if ch[j] == "9":
            ch[j] = "0"
        else:
            ch[j] = str(int(ch[j]) + 1)
        return ''.join(ch)

    def minus_one(self, s, j):
        ch = list(s)
        if ch[j] == "0":
            ch[j] = "9"
        else:
            ch[j] = str(int(ch[j]) - 1)
        return ''.join(ch)


if __name__ == '__main__':
    deadends = ["0201", "0101", "0102", "1212", "2002"]
    target = "0202"
    result = Solution().openLock(deadends, target)
    print(result)
