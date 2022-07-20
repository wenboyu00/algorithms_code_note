class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1
        res = 0
        #  python3在取模和整数除法时，负数也会有正数结果，因此需要取得记录符号和abs(x)
        flag = False
        if x < 0:
            flag = True
        x = abs(x)
        while x != 0:
            # 取尾数
            digit = x % 10
            # 舍尾数
            x //= 10
            # 把之前结果*10进一位+尾数
            res = res * 10 + digit
        if flag:
            res *= -1
        if res < INT_MIN or res > INT_MAX:
            return 0
        return res


if __name__ == '__main__':
    x = 123
    print(Solution().reverse(x))
