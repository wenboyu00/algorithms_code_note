class Solution:

    def numTrees(self, n: int) -> int:
        # 初始化dp数组值为0
        memo = [[0] * (n + 1) for i in range(n + 1)]
        # 计算闭区间[1,n]组成的BST个数
        return self.count(1, n, memo)

    def count(self, low, high, memo):
        # base case low>high是空区间，对应节点是空，返回1
        if low > high:
            return 1
        if memo[low][high] != 0:
            return memo[low][high]
        res = 0
        for i in range(low, high + 1):
            # i 的值作为根节点 root
            left = self.count(low, i - 1, memo)
            right = self.count(i + 1, high, memo)
            # 左右子树的组合乘积是BST的总数
            res += left * right
        memo[low][high] = res
        return res


if __name__ == '__main__':
    n = 3
    result = Solution().numTrees(n)
    print(result)
