# 题目

<p>数字 <code>n</code>&nbsp;代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 <strong>有效的 </strong>括号组合。</p>

<p>有效括号组合需满足：左括号必须以正确的顺序闭合。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 3
<strong>输出：</strong>["((()))","(()())","(())()","()(())","()()()"]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 1
<strong>输出：</strong>["()"]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 8</code></li>
</ul>
<div><div>Related Topics</div><div><li>字符串</li><li>动态规划</li><li>回溯</li></div></div>

# Python

```python
"""
括号性质：
    1. 一个合法括号的左括号数量一定等于右括号数量
    2. 一个合法括号的字串的左括号数量都大于活等于右括号数量
问题分解：
计算n对括号的组合
    组合（回溯）
    合法括号（根据性质）
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        track = []
        if n == 0:
            return res

        # left 左括号数量，right 右括号数量
        def backtrack(left, right):
            # 若左括号剩下的多，说明不合法
            if right < left:
                return
            # 括号数量小于0
            if left < 0 or right < 0:
                return
            # 合法数量都为0
            if left == 0 and right == 0:
                res.append(''.join(track))
                return 
            # 遍历选择，放括号
            # 放左括号
            track.append('(')
            backtrack(left - 1, right)
            track.pop()

            # 放右括号
            track.append(')')
            backtrack(left, right - 1)
            track.pop()

        backtrack(n, n)
        return res
```

# Go

```go
func generateParenthesis(n int) []string {
   res := []string{}
   if n == 0 {
      return res
   }
   track := []string{}
   var backtrack func(left int, right int)
   backtrack = func(left int, right int) {
      if left > right {
         return
      }
      if left < 0 || right < 0 {
         return
      }
      if left == 0 && right == 0 {
         res = append(res, strings.Join(track, ""))
         return
      }
      track = append(track, "(")
      backtrack(left-1, right)
      track = track[:len(track)-1]

      track = append(track, ")")
      backtrack(left, right-1)
      track = track[:len(track)-1]
   }
   backtrack(n, n)
   return res
}
```