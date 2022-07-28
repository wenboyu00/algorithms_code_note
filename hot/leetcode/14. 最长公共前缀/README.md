# 题目
<p>编写一个函数来查找字符串数组中的最长公共前缀。</p>

<p>如果不存在公共前缀，返回空字符串&nbsp;<code>""</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>strs = ["flower","flow","flight"]
<strong>输出：</strong>"fl"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>strs = ["dog","racecar","car"]
<strong>输出：</strong>""
<strong>解释：</strong>输入不存在公共前缀。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul> 
 <li><code>1 &lt;= strs.length &lt;= 200</code></li> 
 <li><code>0 &lt;= strs[i].length &lt;= 200</code></li> 
 <li><code>strs[i]</code> 仅由小写英文字母组成</li> 
</ul>

<div><div>Related Topics</div><div><li>字符串</li></div></div>

# Python

```python
"""
依次比较所有字符串 对应的字符
双层for循环
1层循环，循环第一个字符串 strs[0][i] 
2层循环, 循环每个字符串 strs[j][i] 在i位置上所有字符进行对比
i超出strs[j]长度 ，或者 和第一个字符不想等时 返回
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 循环第一个字符串
        for i in range(len(strs[0])):
            c = strs[0][i]
            # 循环所有字符串
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][0:i]
        return strs[0]
```

# Go

```go
func longestCommonPrefix(strs []string) string {
    for i:=0; i<len(strs[0]);i++{
        c := strs[0][i]
        for j:=1; j < len(strs);j++{
            if i == len(strs[j]) || c != strs[j][i]{
                return strs[0][:i]
            }
        }
    }
   return strs[0]
}
```

