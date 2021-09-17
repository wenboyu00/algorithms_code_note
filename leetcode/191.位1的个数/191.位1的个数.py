class Solution:
    """
    n & (n-1) 消除n的二进制表示中的最后一个1
    每消除一个1，res+=1
    """

    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n = n & (n - 1)
            res += 1
        return res


if __name__ == '__main__':
    n = 0o0000000000000000000000000001011
    result = Solution().hammingWeight(n)
    print(result)
