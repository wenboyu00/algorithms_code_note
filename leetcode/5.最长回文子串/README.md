# 题目
<p>给你一个字符串 <code>s</code>，找到 <code>s</code> 中最长的回文子串。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "babad"
<strong>输出：</strong>"bab"
<strong>解释：</strong>"aba" 同样是符合题意的答案。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "cbbd"
<strong>输出：</strong>"bb"
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "a"
<strong>输出：</strong>"a"
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>s = "ac"
<strong>输出：</strong>"a"
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= s.length <= 1000</code></li>
	<li><code>s</code> 仅由数字和英文字母（大写和/或小写）组成</li>
</ul>
<div><div>Related Topics</div><div><li>字符串</li><li>动态规划</li></div></div>

# Python

```python
"""
回文串：正着读和反着读都一样的字符串。
核心：双指针
寻找回文串的思路：从中间向两边扩散来判断回文数
注意：中心为奇数or偶数的情况
思路代码：
for 0 <= i < len(s):
    找到以 s[i] 为中心的回文串
    找到以 s[i] 和 s[i+1] 为中心的回文串
    更新答案
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # 以s[i]为中心的最长回文子串，中心为奇数情况
            s1 = self.palindrome(s, i, i)
            # 以s[i]和s[i+1]为中心的最长回文子串，中心为偶数情况
            s2 = self.palindrome(s, i, i + 1)
            # 结果为最长的子串
            res = self.max_len_str(res, s1)
            res = self.max_len_str(res, s2)
        return res

    def palindrome(self, s, left, right):
        # 防止越界，当左右相等时，向两边展开
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]

    def max_len_str(self, s1, s2):
        # 返回最长的字符串
        if len(s1) > len(s2):
            return s1
        else:
            return s2
```

# Go

```go
func longestPalindrome(s string) string {
   n := len(s)
   res := ""
   for i := 0; i < n; i++ {
      s1 := palindrome(s, i, i)
      s2 := palindrome(s, i, i+1)
      res = maxLenStr(res, s1)
      res = maxLenStr(res, s2)
   }
   return res
}
func palindrome(s string, left int, right int) string {
   for left >= 0 && right < len(s) && s[left] == s[right] {
      left -= 1
      right += 1
   }
   return s[left+1 : right]
}
func maxLenStr(s1 string, s2 string) string {
   if len(s1) > len(s2) {
      return s1
   } else {
      return s2
   }
}
```

