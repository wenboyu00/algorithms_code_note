# 题目
<p>给定一个<strong>非空</strong>字符串 <em>s</em> 和一个包含<strong>非空</strong>单词的列表 <em>wordDict</em>，判定&nbsp;<em>s</em> 是否可以被空格拆分为一个或多个在字典中出现的单词。</p>

<p><strong>说明：</strong></p>

<ul>
	<li>拆分时可以重复使用字典中的单词。</li>
	<li>你可以假设字典中没有重复的单词。</li>
</ul>

<p><strong>示例 1：</strong></p>

<pre><strong>输入:</strong> s = &quot;leetcode&quot;, wordDict = [&quot;leet&quot;, &quot;code&quot;]
<strong>输出:</strong> true
<strong>解释:</strong> 返回 true 因为 &quot;leetcode&quot; 可以被拆分成 &quot;leet code&quot;。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入:</strong> s = &quot;applepenapple&quot;, wordDict = [&quot;apple&quot;, &quot;pen&quot;]
<strong>输出:</strong> true
<strong>解释:</strong> 返回 true 因为 <code>&quot;</code>applepenapple<code>&quot;</code> 可以被拆分成 <code>&quot;</code>apple pen apple<code>&quot;</code>。
&nbsp;    注意你可以重复使用字典中的单词。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入:</strong> s = &quot;catsandog&quot;, wordDict = [&quot;cats&quot;, &quot;dog&quot;, &quot;sand&quot;, &quot;and&quot;, &quot;cat&quot;]
<strong>输出:</strong> false
</pre>
<div><div>Related Topics</div><div><li>字典树</li><li>记忆化搜索</li><li>哈希表</li><li>字符串</li><li>动态规划</li></div></div>

# Python

```python
def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    """
    判断s是否可以被连续被wordDict拆分
        找到s[i]是否被拆分，首先要判断s[i-1]可以被拆分

    动态规划
    dp数组: 0 ~ n+1 是否可以被拆分相应单词（index向前移一位）
    base case: dp[0] = True,空字符，可以被拆分，作为开始
            dp[1~n]= False，默认不可拆分
    遍历s，
    判断s[low:high]等于word时，dp[high]=True
        - high = low + 单个单词长度
    遍历s，判断以low为起点+查找单词长度为终点，判断是否查找到
    返回：dp[n]
    """
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for low in range(n):
        if not dp[low]:
            continue
        for word in wordDict:
            high = low + len(word)
            if high < n + 1 and s[low:high] == word:
                dp[high] = True
    return dp[n]
```

# Go

```go
func wordBreak(s string, wordDict []string) bool {
   n := len(s)
   dp := make([]bool, n+1)
   dp[0] = true
   for low := 0; low < n; low++ {
      if !dp[low] {
         continue
      }
      for _, word := range wordDict {
         high := low + len(word)
         if high < n+1 && s[low:high] == word{
            dp[high] = true
         }
      }

   }
   return dp[n]
}
```