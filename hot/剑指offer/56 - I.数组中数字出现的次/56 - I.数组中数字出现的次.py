from typing import List

"""
异或 ^ ：   相同为0，不同为1
或   & :   同为1时为1，不同时为0
左移1位 <<=

题目:找到数组中出现1次2个数

位运算
找到出现1次的数，用异或
出现2个数，可以对数组进行分组(奇偶分组)。重复的数，数值是一样的，可以被分到同一组中。
如何分组：
    - 得到mask分组值
        对nums遍历进行异或，得到2个数的异或值，因为2个不同的数，至少二进制有一个位是不同的。
        用2数异或值某为1的二进制位，做mask即可对nums进行奇偶分组，因为为1二进制表示这是不同的地方。
    - 遍历nums，num&mask进行奇偶分组再异或，最后得到2组中不同的只出现一次的数。
"""


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        # 得到2数的异或值
        xor = 0
        for num in nums:
            xor ^= num
        mask = 1
        # 得到xor最低位的1，让mask从0001开始，每次都不满足都左移一位
        while (mask & xor) == 0:
            mask <<= 1
        # 用mask对num分组，异或后得出答案
        x, y = 0, 0
        for num in nums:
            if num & mask:
                x ^= num
            else:
                y ^= num
        return [x, y]


if __name__ == '__main__':
    nums = [1, 2, 10, 4, 1, 4, 3, 3]
    print(Solution().singleNumbers(nums))
