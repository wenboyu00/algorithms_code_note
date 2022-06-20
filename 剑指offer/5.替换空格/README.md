# 题目
<p>请实现一个函数，把字符串 <code>s</code> 中的每个空格替换成&quot;%20&quot;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = &quot;We are happy.&quot;
<strong>输出：</strong>&quot;We%20are%20happy.&quot;</pre>

<p>&nbsp;</p>

<p><strong>限制：</strong></p>

<p><code>0 &lt;= s 的长度 &lt;= 10000</code></p>

# Python

```python
class Solution:
    def replaceSpace(self, s: str) -> str:
        result = list()
        for c in s:
            if c == ' ':
                result.append('%20')
            else:
                result.append(c)
        return ''.join(result)
```

# Go

```go
/*
range遍历是rune格式，unicode
*/
func replaceSpace(s string) string {
    result := ""
    for _,c := range s{
        if c == ' '{
            result += "%20"
        }else{
            result += string(c)
        }
    }
    return result
}
```
