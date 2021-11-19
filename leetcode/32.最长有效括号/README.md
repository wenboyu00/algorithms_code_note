# 题目
<p>给你一个只包含 <code>'('</code> 和 <code>')'</code> 的字符串，找出最长有效（格式正确且连续）括号子串的长度。</p>

<p> </p>

<div class="original__bRMd">
<div>
<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "(()"
<strong>输出：</strong>2
<strong>解释：</strong>最长有效括号子串是 "()"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = ")()())"
<strong>输出：</strong>4
<strong>解释：</strong>最长有效括号子串是 "()()"
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = ""
<strong>输出：</strong>0
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 <= s.length <= 3 * 10<sup>4</sup></code></li>
	<li><code>s[i]</code> 为 <code>'('</code> 或 <code>')'</code></li>
</ul>
</div>
</div>

<div><div>Related Topics</div><div><li>栈</li><li>字符串</li><li>动态规划</li></div></div><br>

# Python

```python
def longestValidParentheses(self, s: str) -> int:
    """
    栈
    遍历中
    存入'('到栈与之后')'匹配，索引之间差值长度。用没有匹配的右括号下标做有效括号分割
    """
    max_ans = 0
    # 初始化栈，base case: -1，表示最后一个没有比匹配的下标
    stk = [-1]
    for i in range(len(s)):
        # 直接入栈
        if s[i] == '(':
            stk.append(i)
        # 把匹配到的( 将栈中索引弹出
        else:
            stk.pop()
            # 如果不为空，说明保存着"最后一个没有匹配到的右括号下标"
            # - 当前i减去最后没有匹配到的括号下标=当前最长括号的长度
            # - 然后取最大值
            if stk:
                max_ans = max(max_ans, i - stk[-1])
            # 如果为空，此索引为最后一个没有匹配的右括号下标
            else:
                stk.append(i)
    return max_ans
```

# Go

```go
func longestValidParentheses(s string) int {
   /*
   栈
   - 用无法匹配的右括号索引做分割，存入栈底，base case: -1作为初始化的无法匹配的索引
   - 入栈的(的索引和后面)的索引匹配，弹出(索引后，右括号索引和栈底元素索引之间的差值就是有效括号的长度。
   */
   maxAns := 0
   stk := []int{-1}
   for i := 0; i < len(s); i++ {
      if s[i] == '(' {
         stk = append(stk, i)
      } else {
         stk = stk[:len(stk)-1]
         if len(stk) == 0 {
            stk = append(stk, i)
         } else {
            sLen := i - stk[len(stk)-1]
            if sLen > maxAns {
               maxAns = sLen
            }
         }
      }
   }
   return maxAns
}
```