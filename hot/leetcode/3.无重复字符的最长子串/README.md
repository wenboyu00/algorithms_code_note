# 题目
<p>给定一个字符串 <code>s</code> ，请你找出其中不含有重复字符的 <strong>最长子串 </strong>的长度。</p>

<p> </p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入: </strong>s = "abcabcbb"
<strong>输出: </strong>3 
<strong>解释:</strong> 因为无重复字符的最长子串是 <code>"abc"，所以其</code>长度为 3。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入: </strong>s = "bbbbb"
<strong>输出: </strong>1
<strong>解释: </strong>因为无重复字符的最长子串是 <code>"b"</code>，所以其长度为 1。
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入: </strong>s = "pwwkew"
<strong>输出: </strong>3
<strong>解释: </strong>因为无重复字符的最长子串是 <code>"wke"</code>，所以其长度为 3。
     请注意，你的答案必须是 <strong>子串 </strong>的长度，<code>"pwke"</code> 是一个<em>子序列，</em>不是子串。
</pre>

<p><strong>示例 4:</strong></p>

<pre>
<strong>输入: </strong>s = ""
<strong>输出: </strong>0
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 <= s.length <= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code> 由英文字母、数字、符号和空格组成</li>
</ul>
<div><div>Related Topics</div><div><li>哈希表</li><li>字符串</li><li>滑动窗口</li></div></div>

# Python

```python
def lengthOfLongestSubstring(self, s: str) -> int:
    window = {}
    left, right = 0, 0
    result = 0
    # 扩大窗口，添加字符
    while right < len(s):
        c = s[right]
        right += 1
        window[c] = window.get(c, 0) + 1
        # 字符计数超过1 说明重复，需要缩小窗口
        while window[c] > 1:
            d = s[left]
            left += 1
            window[d] -= 1
        # 当缩小窗口完成时，说明没有重复，符合 最长子串，并和旧长度对比储存
        result = max(result, right - left)
    return result
```

# Go

```go
func lengthOfLongestSubstring(s string) int {
   window := map[int32]int{}
   left := 0
   right := 0
   result := 0
   for right < len(s) {
      c := int32(s[right])
      right += 1
      window[c] += 1
      for window[c] > 1 {
         d := int32(s[left])
         left += 1
         window[d] -= 1
      }
      if result < right-left {
         result = right - left
      }
   }
   return result
}
```