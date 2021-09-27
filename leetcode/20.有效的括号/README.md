# 题目
<p>给定一个只包括 <code>'('</code>，<code>')'</code>，<code>'{'</code>，<code>'}'</code>，<code>'['</code>，<code>']'</code> 的字符串 <code>s</code> ，判断字符串是否有效。</p>

<p>有效字符串需满足：</p>

<ol>
	<li>左括号必须用相同类型的右括号闭合。</li>
	<li>左括号必须以正确的顺序闭合。</li>
</ol>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "()"
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "()[]{}"
<strong>输出：</strong>true
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "(]"
<strong>输出：</strong>false
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>s = "([)]"
<strong>输出：</strong>false
</pre>

<p><strong>示例 5：</strong></p>

<pre>
<strong>输入：</strong>s = "{[]}"
<strong>输出：</strong>true</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= s.length <= 10<sup>4</sup></code></li>
	<li><code>s</code> 仅由括号 <code>'()[]{}'</code> 组成</li>
</ul>
<div><div>Related Topics</div><div><li>栈</li><li>字符串</li></div></div>

# Python

```python
def isValid(self, s: str) -> bool:
    # 如果长度不是偶数，说明不成对，不合法。
    if len(s) % 2 == 1:
        return False
    # 存放左括号
    stk = []
    # 右括号和左括号对应
    mapping = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    # 遍历字符串
    for ch in s:
        # 如果发现右括号，在栈中找到对应左括号，找到就弹出，找不到 就不合法
        if ch in mapping:
            # 如果发现右括号时，栈为空，说不成对，不合法。
            if not stk or stk[-1] != mapping[ch]:
                return False
            stk.pop()
        else:
            stk.append(ch)
    return not stk
```

# Go

```go
func isValid(s string) bool {
   if len(s)%2 == 1 {
      return false
   }
   mapping := map[rune]rune{
      ')': '(',
      ']': '[',
      '}': '{',
   }
   stk := []rune{}
   for _, ch := range s {
      if val, ok := mapping[ch]; ok {
         if len(stk) == 0 || stk[len(stk)-1] != val{
            return false
         }
         stk = stk[:len(stk)-1]
      } else {
         stk = append(stk, ch)
      }
   }
   return len(stk) == 0
}
```