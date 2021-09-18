# 题目
<p>给定一个整数 <code>n</code> ，返回 <code>n!</code> 结果中尾随零的数量。</p>

<p><b>进阶：</b>你可以设计并实现对数时间复杂度的算法来解决此问题吗？</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 3
<strong>输出：</strong>0
<strong>解释：</strong>3! = 6 ，不含尾随 0
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 5
<strong>输出：</strong>1
<strong>解释：</strong>5! = 120 ，有一个尾随 0
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 0
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 10<sup>4</sup></code></li>
</ul>
<div><div>Related Topics</div><div><li>数学</li></div></div>

# Python

```python
"""
n! 最多可以分解为 多少个因子2和5
因为2和5相乘结尾是0，又因为每个偶数都能分解出2，2比5数量多，5成了决定性因子
所以，题目转换为求 多少5
因为5的幂数也可以分解为多个5，所以也要求5的幂数
例如：25可以提供2个5因子，125/25=5个25的倍数，它们可以再提供一个因子5
125! = 25+5+1
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        divs = 5
        while divs <= n:
            res += n // divs
            divs *= 5
        return res
```

# Go

```go
func trailingZeroes(n int) int {
   res := 0
   divs := 5
   for divs <= n {
      res += n / divs
      divs *= 5
   }
   return res
}
```