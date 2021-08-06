# 题目：

<p>给你一个字符串 <code>s</code> 、一个字符串 <code>t</code> 。返回 <code>s</code> 中涵盖 <code>t</code> 所有字符的最小子串。如果 <code>s</code> 中不存在涵盖 <code>t</code> 所有字符的子串，则返回空字符串 <code>""</code> 。</p>

<p> </p>

<p><strong>注意：</strong></p>

<ul>
	<li>对于 <code>t</code> 中重复字符，我们寻找的子字符串中该字符数量必须不少于 <code>t</code> 中该字符数量。</li>
	<li>如果 <code>s</code> 中存在这样的子串，我们保证它是唯一的答案。</li>
</ul>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "ADOBECODEBANC", t = "ABC"
<strong>输出：</strong>"BANC"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "a", t = "a"
<strong>输出：</strong>"a"
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> s = "a", t = "aa"
<strong>输出:</strong> ""
<strong>解释:</strong> t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= s.length, t.length <= 10<sup>5</sup></code></li>
	<li><code>s</code> 和 <code>t</code> 由英文字母组成</li>
</ul>

<p> </p>
<strong>进阶：</strong>你能设计一个在 <code>o(n)</code> 时间内解决此问题的算法吗？

# Python

```python
def minWindow(self, s: str, t: str) -> str:
    # need 需求字符出现次数，window窗口字符出现次数
    need = dict()
    window = dict()
    # need初始化字符为1，window初始化为0
    for i in t:
        need[i] = need.get(i, 0) + 1
        window[i] = window.get(i, 0)
    # 窗口区间
    left, right = 0, 0
    # 有效字符数量
    valid = 0
    # 记录覆盖最小字串的起始索引和长度
    start, str_len = 0, len(s) + 1
    # 增大窗口寻找可行解
    while right < len(s):
        # c是将移入窗口的字符串
        c = s[right]
        right += 1
        # 进行窗口内数据的操作
        if c in need:
            # 窗口内字符出现次数
            window[c] += 1
            # 记录有效次数
            if window[c] == need[c]:
                valid += 1
        # 减小窗口优化可行解，判断左侧窗口是否要收缩，有效次数==需求字符数量
        while valid == len(need):
            # 更新最小覆盖子串
            # 比上次短，才更新 right-left是匹配到字符串长度
            if right - left < str_len:
                start = left
                str_len = right - left
            # d是将移除窗口的字符
            d = s[left]
            left += 1
            if d in need:
                if window[d] == need[d]:
                    valid -= 1
                window[d] -= 1
    if str_len == len(s) + 1:
        return ""
    return s[start:start + str_len]
```

# Go

```go
//range遍历的字符串是int32格式
need := map[int32]int{}
window := map[int32]int{}
for _, v := range t {
   need[v] += 1
   window[v] = 0
}
left := 0
right := 0
start := 0
valid := 0
strLen := len(s) + 1
for right < len(s) {
   // 扩大窗口，找到可行解
   // 和int32格式map的key 统一格式
   c := int32(s[right])
   right += 1
   if _, ok := need[c]; ok {
      window[c] += 1
      // 增加有效字符
      if window[c] == need[c] {
         valid += 1
      }
   }
   // 减小窗口，优化可行解
   for valid == len(need) {
      // 新的结果结果比旧的结果短，再更新
      if right-left < strLen {
         start = left
         strLen = right - left
      }
      d := int32(s[left])
      left += 1
      if _, ok := need[d]; ok {
         // 减少有效字符
         if window[d] == need[d] {
            valid -= 1
         }
         window[d] -= 1
      }

   }
}
if strLen == len(s)+1 {
   return ""
}
//和python使用一样
return s[start : start+strLen]
```