
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        memo = list()
        for i in range(k + 1):
            memo.append([None] * (n + 1))

        def dp(k, n):
            # base case
            # 一个鸡蛋，只能线性扫描楼层
            if k == 1:
                return n
            # 0层楼，不需要扔鸡蛋
            if n == 0:
                return 0
            # dp数组（备忘录）
            if memo[k][n] is not None:
                return memo[k][n]
            # float('INF')正无穷
            res = float('INF')
            # 二分查找方式低=1，高=n
            low, high = 1, n
            while low <= high:
                # mid = 低+高 整除 2
                mid = (low + high) // 2
                # 碎了：k-1，搜索楼层从1...N变成了1...mid-1共mid-1层
                # 没碎：k, 搜索楼层从1...N变成了mid+1...n共n-mid层
                broken = dp(k - 1, mid - 1)  # 碎
                not_broken = dp(k, n - mid)  # 没碎
                # 最坏情况下的最少次数min(max(broken, notBroken)
                # 疑问点：high = mid-1和low= mid+1
                if broken > not_broken:
                    high = mid - 1
                    res = min(res, broken + 1)
                else:
                    low = mid + 1
                    res = min(res, not_broken + 1)
            memo[k][n] = res
            return res

        return dp(k, n)


if __name__ == '__main__':
    result = Solution().superEggDrop(2, 6)
    print(result)
