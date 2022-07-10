<p>数字以0123456789101112131415&hellip;的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。</p>

<p>请写一个函数，求任意第n位对应的数字。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = 3
<strong>输出：</strong>3
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = 11
<strong>输出：</strong>0</pre>

<p>&nbsp;</p>

<p><strong>限制：</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;&nbsp;2^31</code></li>
</ul>
<p>注意：本题与主站 400 题相同：<a href="https://leetcode-cn.com/problems/nth-digit/">https://leetcode-cn.com/problems/nth-digit/</a></p>

# Python

```python
"""
数学规律
digits: 位数
start: 区间起始数字
num: n所在的数字  = start+(n-1)// digits
index: n所在数字的位数 = (n-1)% digits

# 找到 n位所对应的区间
9 * start: 数字数量
digits: 数字位数
相乘 数字所占位数量
if n > 9 * start * digits:

    n -= 9 * start * digits
"""


class Solution:
    def findNthDigit(self, n: int) -> int:
        # 区间起始数字
        start = 1
        # 位数
        digits = 1
        # 找到 n 位对应区间
        while n > 9 * start * digits:
            # n 减去 数字占位数量，因此n是从起始数字start
            n -= 9 * start * digits
            # 增大
            start *= 10
            digits += 1
        # 区间是从1开始计数，因此n-1，除位数
        num = start + (n - 1) // digits
        index = (n - 1) % digits
        return int(str(num)[index])
```

# Go

```go
func findNthDigit(n int) int {
    start:=1
    digits :=1
    for n > 9*start*digits{
        n -= 9*start*digits
        start*=10
        digits+=1
    }
    num := start + (n-1)/ digits
    index := (n-1) % digits
    numStr := strconv.Itoa(num)
    return int(numStr[index]-'0')
}
```