# 题目

<p>给定两个字符串形式的非负整数&nbsp;<code>num1</code> 和<code>num2</code>&nbsp;，计算它们的和并同样以字符串形式返回。</p>

<p>你不能使用任何內建的用于处理大整数的库（比如 <code>BigInteger</code>），&nbsp;也不能直接将输入的字符串转换为整数形式。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>num1 = "11", num2 = "123"
<strong>输出：</strong>"134"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>num1 = "456", num2 = "77"
<strong>输出：</strong>"533"
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>num1 = "0", num2 = "0"
<strong>输出：</strong>"0"
</pre>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul> 
 <li><code>1 &lt;= num1.length, num2.length &lt;= 10<sup>4</sup></code></li> 
 <li><code>num1</code> 和<code>num2</code> 都只包含数字&nbsp;<code>0-9</code></li> 
 <li><code>num1</code> 和<code>num2</code> 都不包含任何前导零</li> 
</ul>
# Python

```python
def addStrings(self, num1: str, num2: str) -> str:
    c = 0
    ans = ""
    # 双指针，从尾部开始
    i, j = len(num1) - 1, len(num2) - 1
    while i >= 0 or j >= 0 or c:
        n1 = int(num1[i]) if i >= 0 else 0
        n2 = int(num2[j]) if j >= 0 else 0
        cur = c + n1 + n2
        c = cur // 10
        ans = str(cur % 10) + ans
        i -= 1
        j -= 1
    return ans
```