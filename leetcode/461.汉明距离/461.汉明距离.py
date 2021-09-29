class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        """
        位运算-异或
        异或规则：位上相同为0，不同为1
        两数异或后，1的位置就是不同的位置，1的数量就是1就是答案
        再使用 n&(n-1)去掉二进制最后一个1，并统计数量，即可
        """
        n = x ^ y
        count = 0
        while n != 0:
            n = n & (n - 1)
            count += 1
        return count
