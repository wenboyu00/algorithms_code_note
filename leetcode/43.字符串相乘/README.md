# 题目
<p>给定两个以字符串形式表示的非负整数&nbsp;<code>num1</code>&nbsp;和&nbsp;<code>num2</code>，返回&nbsp;<code>num1</code>&nbsp;和&nbsp;<code>num2</code>&nbsp;的乘积，它们的乘积也表示为字符串形式。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> num1 = &quot;2&quot;, num2 = &quot;3&quot;
<strong>输出:</strong> &quot;6&quot;</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> num1 = &quot;123&quot;, num2 = &quot;456&quot;
<strong>输出:</strong> &quot;56088&quot;</pre>

<p><strong>说明：</strong></p>

<ol>
	<li><code>num1</code>&nbsp;和&nbsp;<code>num2</code>&nbsp;的长度小于110。</li>
	<li><code>num1</code> 和&nbsp;<code>num2</code> 只包含数字&nbsp;<code>0-9</code>。</li>
	<li><code>num1</code> 和&nbsp;<code>num2</code>&nbsp;均不以零开头，除非是数字 0 本身。</li>
	<li><strong>不能使用任何标准库的大数类型（比如 BigInteger）</strong>或<strong>直接将输入转换为整数来处理</strong>。</li>
</ol>
<div><div>Related Topics</div><div><li>数学</li><li>字符串</li><li>模拟</li></div></div>

# Python

```python
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
```

# Go

```go
func multiply(num1 string, num2 string) string {
   if num1 == "0" && num2 == "0" {
      return "0"
   }
   m, n := len(num1), len(num2)
   res := make([]int, m+n)
   for i := m - 1; i >= 0; i-- {
      n1 := int(num1[i] - '0')
      for j := n - 1; j >= 0; j-- {
         n2 := int(num2[j] - '0')
         sum := res[i+j+1] + n1*n2
         res[i+j+1] = sum % 10
         res[i+j] += sum / 10
      }
   }
   ans := ""
   index := 0
   if res[0] == 0 {
      index = 1
   }
   for ; index < m+n; index++ {
      ans += strconv.Itoa(res[index])
   }
   return ans
}
```

