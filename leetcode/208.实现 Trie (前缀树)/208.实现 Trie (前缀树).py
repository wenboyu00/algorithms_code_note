class Trie:
    """
    前缀树
    嵌套字典的方式来生成前缀树
    key表示前缀存在
    value表示后缀（字典）
    ['#']表示有字符串在此结束
    """
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        p = self.root
        for c in word:
            # 找不到就创建新的字典
            if c not in p:
                p[c] = {}
            # 继续嵌套
            p = p[c]
        # ’#‘存在表示字符串结束
        p['#'] = True

    def search(self, word: str) -> bool:
        node = self.find(word)
        # '#'存在表示字符串结束
        return node is not None and '#' in node

    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix) is not None

    def find(self, word):
        p = self.root
        for c in word:
            # 找不到返回None
            if c not in p:
                return None
            # 找到就，继续深入
            p = p[c]
        return p
