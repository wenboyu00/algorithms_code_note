from typing import List

"""
如果a==b和b==c成立，则a==c也成立，因此我们可以使用并查集来维护这种连通关系
1.遍历所有等式，构造并查集。相等值是在一个集，共有一个parent
2.遍历所有不等式，查找两个值的是否是同一parent，如果是则冲突，就返回False
3.遍历完所以不等式发现没有矛盾，则返回True
"""


class Solution:
    class UnionFind:
        def __init__(self):
            # 26个小写字母
            self.parent = list(range(26))

        # 递归构造，并压缩
        def find(self, index):
            # 如果父节点是自身，说明该变量为根节点
            if index == self.parent[index]:
                return index
            # 沿着当前变量的父节点一路向上查找，直到找到根节点。
            self.parent[index] = self.find(self.parent[index])
            return self.parent[index]

        # 合并，将index1的根节点 指向 index2的根节点
        def union(self, index1, index2):
            self.parent[self.find(index1)] = self.find(index2)

    def equationsPossible(self, equations: List[str]) -> bool:
        uf = Solution.UnionFind()
        for st in equations:
            if st[1] == "=":
                # ord把字符串转换成数字，缩小范围便于计算
                # 字符相减实质是ascll码值相减 所有a~z 减去a之后 的范围是0~25
                index1 = ord(st[0]) - ord("a")
                index2 = ord(st[3]) - ord("a")
                uf.union(index1, index2)

        for st in equations:
            if st[1] == "!":
                index1 = ord(st[0]) - ord("a")
                index2 = ord(st[3]) - ord("a")
                if uf.find(index1) == uf.find(index2):
                    return False
        return True
