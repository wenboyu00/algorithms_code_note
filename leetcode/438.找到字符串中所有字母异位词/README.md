# 题目
<p>给定两个字符串 <code>s</code> 和 <code>p</code>，找到 <code>s</code><strong> </strong>中所有 <code>p</code><strong> </strong>的 <strong>异位词 </strong>的子串，返回这些子串的起始索引。不考虑答案输出的顺序。</p>

<p><strong>异位词 </strong>指字母相同，但排列不同的字符串。</p>

<p> </p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入: </strong>s = "cbaebabacd", p = "abc"
<strong>输出: </strong>[0,6]
<strong>解释:</strong>
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
</pre>

<p><strong> 示例 2:</strong></p>

<pre>
<strong>输入: </strong>s = "abab", p = "ab"
<strong>输出: </strong>[0,1,2]
<strong>解释:</strong>
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
</pre>

<p> </p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 <= s.length, p.length <= 3 * 10<sup>4</sup></code></li>
	<li><code>s</code> 和 <code>p</code> 仅包含小写字母</li>
</ul>
<div><div>Related Topics</div><div><li>哈希表</li><li>字符串</li><li>滑动窗口</li></div></div>

# Python

```python
def findAnagrams(self, s: str, p: str) -> List[int]:
    need, window = {}, {}
    for i in p:
        need[i] = need.get(i, 0) + 1
        window[i] = 0

    left, right = 0, 0
    valid = 0
    result = list()
    # 扩大窗口，对需求的字符计数
    while right < len(s):
        c = s[right]
        right += 1
        if c in need:
            window[c] += 1
            if window[c] == need[c]:
                valid += 1
        # 缩小窗口，窗口长度大于需求字符串长度时对窗口内容进行判断，满足时添加初始索引即 窗口左区间
        while right - left >= len(p):
            if valid == len(need):
                result.append(left)
            d = s[left]
            left += 1
            if d in need:
                if window[d] == need[d]:
                    valid -= 1
                window[d] -= 1

    return result
```

# Go

```go
func findAnagrams(s string, p string) []int {
   need := map[int32]int{}
   window := map[int32]int{}
   for _, i := range p{
      need[i] += 1
      window[i] = 0
   }
   left := 0
   right := 0
   valid := 0
   var result []int
   for right < len(s) {
      c := int32(s[right])
      right += 1
      if _, ok := need[c]; ok {
         window[c] += 1
         if window[c] == need[c] {
            valid += 1
         }
      }
      for right-left >= len(p) {
         if valid == len(need) {
            result = append(result, left)
         }
         d := int32(s[left])
         left += 1
         if _, ok := need[d]; ok {
            if window[d] == need[d] {
               valid -= 1
            }
            window[d] -= 1
         }
      }
   }
   return result
}
```