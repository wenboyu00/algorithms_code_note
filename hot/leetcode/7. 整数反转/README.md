# 题目
<p>给你一个 32 位的有符号整数 <code>x</code> ，返回将 <code>x</code> 中的数字部分反转后的结果。</p>

<p>如果反转后整数超过 32 位的有符号整数的范围 <code>[−2<sup>31</sup>,  2<sup>31 </sup>− 1]</code> ，就返回 0。</p>
<strong>假设环境不允许存储 64 位整数（有符号或无符号）。</strong>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>x = 123
<strong>输出：</strong>321
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>x = -123
<strong>输出：</strong>-321
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>x = 120
<strong>输出：</strong>21
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>x = 0
<strong>输出：</strong>0
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>-2<sup>31</sup> <= x <= 2<sup>31</sup> - 1</code></li>
</ul>
<div><div>Related Topics</div><div><li>数学</li></div></div>

# Python

```python
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
        if res <= INT_MIN or res >= INT_MAX:
            return 0
        return res
```



# Go

```go
func reverse(x int) int {
        res := 0
        for x !=0 {
            digit := x % 10
            x /= 10
            res = res*10+digit
        }
        if res < math.MinInt32 || res > math.MaxInt32{
            return 0
        }
        return res
}
```