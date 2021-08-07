# 题目
<p>给你两个字符串&nbsp;<code>s1</code>&nbsp;和&nbsp;<code>s2</code> ，写一个函数来判断 <code>s2</code> 是否包含 <code>s1</code><strong>&nbsp;</strong>的排列。</p>

<p>换句话说，<code>s1</code> 的排列之一是 <code>s2</code> 的 <strong>子串</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s1 = "ab" s2 = "eidbaooo"
<strong>输出：</strong>true
<strong>解释：</strong>s2 包含 s1 的排列之一 ("ba").
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s1= "ab" s2 = "eidboaoo"
<strong>输出：</strong>false
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s1.length, s2.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s1</code> 和 <code>s2</code> 仅包含小写字母</li>
</ul>
<div><div>Related Topics</div><div><li>哈希表</li><li>双指针</li><li>字符串</li><li>滑动窗口</li></div></div>

# Python

```python
# 判断s1是否存在s2排列中
def checkInclusion(self, s1: str, s2: str) -> bool:
    # 初始化需求字典和窗口字典，用于判断数量
    need = dict()
    window = dict()
    for s in s1:
        need[s] = need.get(s, 0) + 1
        window[s] = 0
    left, right = 0, 0
    valid = 0
    # 扩大窗口，更新window数量，如果是需求字符，更新有效数量
    while right < len(s2):
        c = s2[right]
        right += 1
        if c in need:
            window[c] += 1
            if window[c] == need[c]:
                valid += 1
        # 缩小窗口
        while (right - left) >= len(s1):
            # 判断是否找到合法子串
            if valid == len(need):
                return True
            d = s2[left]
            left += 1
            if d in need:
                if window[d] == need[d]:
                    valid -= 1
                window[d] -= 1

    return False
```

# GO

```go
func checkInclusion(s1 string, s2 string) bool {
   need := map[int32]int{}
   window := map[int32]int{}
   for _, s := range s1 {
      need[s] += 1
      window[s] = 0
   }
   left := 0
   right := 0
   valid := 0
   for right < len(s2){
      c := int32(s2[right])
      right += 1
      if _, ok := need[c]; ok{
         window[c] +=1
         if window[c] == need[c]{
            valid += 1
         }
      }
      for right-left >= len(s1){
         if valid == len(need){
            return true
         }
         d := int32(s2[left])
         left += 1
         if _,ok := need[d];ok{
            if window[d] == need[d]{
               valid -= 1
            }
            window[d] -= 1
         }
      }
   }
   return false
}
```