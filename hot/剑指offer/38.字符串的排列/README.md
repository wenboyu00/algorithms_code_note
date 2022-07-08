# 题目

<p>输入一个字符串，打印出该字符串中字符的所有排列。</p>

<p>&nbsp;</p>

<p>你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。</p>

<p>&nbsp;</p>

<p><strong>示例:</strong></p>

<pre><strong>输入：</strong>s = &quot;abc&quot;
<strong>输出：[</strong>&quot;abc&quot;,&quot;acb&quot;,&quot;bac&quot;,&quot;bca&quot;,&quot;cab&quot;,&quot;cba&quot;<strong>]</strong>
</pre>

<p>&nbsp;</p>

<p><strong>限制：</strong></p>

<p><code>1 &lt;= s 的长度 &lt;= 8</code></p>

# Python

```python
"""
全排列，回溯dfs+结果set去重，visit[index]=True跳过已经使用过的元素
"""


class Solution:
    def permutation(self, s: str) -> List[str]:
        """
        回溯
        """
        result = set()  # 用集合去重
        track = list()
        n = len(s)
        visit = [False] * n

        def back_track(track):
            # 满足结束条件
            if n == len(track):
                val = ''.join(track)
                result.add(val)
                return
            for idx in range(n):
                # 剪枝
                if visit[idx]:
                    continue
                # 做选择
                track.append(s[idx])
                visit[idx] = True
                # 进入下一层
                back_track(track)
                # 撤销选择
                track.pop()
                visit[idx] = False

        back_track(track)
        return list(result)
```

# Go

```go
func permutation(s string) []string {
   track := make([]byte, 0, len(s))
   result := map[string]bool{}
   visit := make([]bool, len(s), len(s))
   for i := 0; i < len(s); i++ {
      visit[i] = false
   }
   var backTrack func()
   backTrack = func() {
      if len(track) == len(s){
         result[string(track)] = true
         return
      }
      for idx, _ := range s{
         if visit[idx] == true{
            continue
         }
         track = append(track, s[idx])
         visit[idx] = true
         backTrack()
         track = track[:len(track)-1]
         visit[idx] = false

      }
   }
   backTrack()
   res := make([]string, 0, len(result))
   for k := range result{
      res = append(res, k)
   }
   return res
}
```
