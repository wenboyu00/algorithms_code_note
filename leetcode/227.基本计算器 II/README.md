# 题目

<p>给你一个字符串表达式 <code>s</code> ，请你实现一个基本计算器来计算并返回它的值。</p>

<p>整数除法仅保留整数部分。</p>

<div class="original__bRMd">
<div>
<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "3+2*2"
<strong>输出：</strong>7
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = " 3/2 "
<strong>输出：</strong>1
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = " 3+5 / 2 "
<strong>输出：</strong>5
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= s.length <= 3 * 10<sup>5</sup></code></li>
	<li><code>s</code> 由整数和算符 <code>('+', '-', '*', '/')</code> 组成，中间由一些空格隔开</li>
	<li><code>s</code> 表示一个 <strong>有效表达式</strong></li>
	<li>表达式中的所有整数都是非负整数，且在范围 <code>[0, 2<sup>31</sup> - 1]</code> 内</li>
	<li>题目数据保证答案是一个 <strong>32-bit 整数</strong></li>
</ul>
</div>
</div>

<div><div>Related Topics</div><div><li>栈</li><li>数学</li><li>字符串</li></div></div>

# Python

```python
def calculate(self, s: str) -> int:
    n = len(s)
    stk = []
    num = 0
    sign = "+"
    for i in range(n):
        c = s[i]
        # 如何是数字字符且不为空,更新c到num上
        if c.isdigit():
            num = 10 * num + int(c)
        # 如果是非数字 or 是最后一个元素
        if (not c.isdigit() and c != " ") or i == n - 1:
            if sign == "+":
                stk.append(num)
            elif sign == '-':
                stk.append(-num)
            # 实现先乘除，后加减
            # 把栈顶元素和当前元素计算后重新写入栈顶
            elif sign == '*':
                stk[-1] = stk[-1] * num
            elif sign == '/':
                stk[-1] = int(stk[-1] / float(num))
            num = 0
            sign = c
    return sum(stk)
```

# Go

```go
func calculate(s string) int {
   stk := []int{}
   sign := '+'
   num := 0
   for i, ch := range s {
      isDigit := '0' <= ch && ch <= '9'
      if isDigit {
         num = 10*num + int(ch-'0')
      }
      if !isDigit && ch != ' ' || i == len(s)-1 {
         if sign == '+' {
            stk = append(stk, num)
         } else if sign == '-' {
            stk = append(stk, -num)
         } else if sign == '*' {
            stk[len(stk)-1] *= num
         } else if sign == '/' {
            stk[len(stk)-1] /= num
         }
         num = 0
         sign = ch
      }
   }
   ans := 0
   for _, v := range stk {
      ans += v
   }
   return ans
}
```

