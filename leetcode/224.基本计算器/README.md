# 题目
<p>给你一个字符串表达式 <code>s</code> ，请你实现一个基本计算器来计算并返回它的值。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "1 + 1"
<strong>输出：</strong>2
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = " 2-1 + 2 "
<strong>输出：</strong>3
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "(1+(4+5+2)-3)+(6+8)"
<strong>输出：</strong>23
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= s.length <= 3 * 10<sup>5</sup></code></li>
	<li><code>s</code> 由数字、<code>'+'</code>、<code>'-'</code>、<code>'('</code>、<code>')'</code>、和 <code>' '</code> 组成</li>
	<li><code>s</code> 表示一个有效的表达式</li>
</ul>
<div><div>Related Topics</div><div><li>栈</li><li>递归</li><li>数学</li><li>字符串</li></div></div>

# Python

```python
"""
递归解法：
括号包含的算式，视为一个数字(整体)就行了。
遇到 ( 开始递归
遇到 ) 结束递归
注意：递归时s的变化，递归后s要变更，否则会重复计算
"""


class Solution:
    def calculate(self, s: str) -> int:
        def do(s):
            stk = []
            num = 0
            sign = "+"
            while len(s) > 0:
                c = s.popleft()
                # 如何是数字字符且不为空,更新c到num上
                # *10是应对多位数字的进位
                if c.isdigit():
                    num = 10 * num + int(c)
                # 遇到左括号开始递归 计算 s
                if c == '(':
                    num = do(s)
                # 如果是非数字 or 是最后一个元素
                if (not c.isdigit() and c != " ") or len(s) == 0:
                    if sign == "+":
                        stk.append(num)
                    elif sign == '-':
                        stk.append(-num)
                    # 实现先乘除，后加减
                    # 把栈顶元素和当前元素计算后重新写入栈顶
                    elif sign == '*':
                        stk[-1] *= num
                    elif sign == '/':
                        stk[-1] = int(stk[-1] / float(num))
                    num = 0
                    sign = c
                # 遇到右括号结束递归
                if c == ')':
                    return sum(stk)
            return sum(stk)
        return do(deque(s))
```

# Go

```go
func calculate(s string) int {
   res, s := do(s)
   return res
}

func do(s string) (int,string) {
   stk := []int{}
   num := 0
   sign := '+'
   for len(s) > 0 {
      ch := s[0]
      s = s[1:]
      isDigit := '0' <= ch && ch <= '9'
      if isDigit {
         num = 10*num + int(ch-'0')
      }
      if ch == '(' {
         num, s = do(s)
      }
      if (!isDigit && ch != ' ') || len(s) == 0 {
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
         sign = rune(ch)
      }
      if ch == ')' {
         return sum(stk),s
      }

   }
   return sum(stk),s
}
func sum(list []int) (count int) {
   for _, value := range list {
      count += value
   }
   return count
}
```

