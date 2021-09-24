class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        模拟手算方式
        1. m, n = len(num1), len(num2)，相乘结果最多为m+n
        2. 索引对应结果个位为res[i+j+1], 十位[i+j]
        3. 两层循环，从后到前(手算顺序)
            把 n1*n2+原来个位[i+j+1]上的值 = sum_num
            处理进位问题
            i+j+1 = sum_sum % 10 得到个位值
            i+j += sum_num // 10 得到十位值并和原来的相加
        4.处理0开头数字，并转换成str
        """
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            n1 = int(num1[i])
            for j in range(n - 1, -1, -1):
                n2 = int(num2[j])
                sum_num = res[i + j + 1] + n1 * n2
                res[i + j + 1] = sum_num % 10
                res[i + j] += sum_num // 10

        # 处理开头为0的情况
        if res[0] == 0:
            index = 1
        else:
            index = 0
        return ''.join([str(i) for i in res[index:]])


if __name__ == '__main__':
    num1 = "123"
    num2 = "456"
    result = Solution().multiply(num1, num2)
    print(result)
