# 题目
<p>给你一个字符串数组，请你将 <strong>字母异位词</strong> 组合在一起。可以按任意顺序返回结果列表。</p>

<p><strong>字母异位词</strong> 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母都恰好只用一次。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> strs = <code>["eat", "tea", "tan", "ate", "nat", "bat"]</code>
<strong>输出: </strong>[["bat"],["nat","tan"],["ate","eat","tea"]]</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> strs = <code>[""]</code>
<strong>输出: </strong>[[""]]
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> strs = <code>["a"]</code>
<strong>输出: </strong>[["a"]]</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= strs[i].length &lt;= 100</code></li>
	<li><code>strs[i]</code>&nbsp;仅包含小写字母</li>
</ul>
<div><div>Related Topics</div><div><li>哈希表</li><li>字符串</li><li>排序</li></div></div>

# Python

```python
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    """
    字母异位词，相同字母，不同位置
    排序后位置也相同，用排序后字母做为map的key，原字母作为val
     - 哈希表：{排序后字符串：[原字符串]}
    再遍历哈希表的values()即可
    """
    sorted_strs = {}
    for s in strs:
        ss = ''.join(sorted(s))
        if ss in sorted_strs:
            sorted_strs[ss].append(s)
        else:
            sorted_strs[ss] = [s]

    result = []
    for val in sorted_strs.values():
        result.append(val)
    return result
```



# Go

```go
func groupAnagrams(strs []string) [][]string {
   mapping := map[string][]string{}
   for _, str := range strs {
      // 转换成字节数组，并进行排序
      s := []byte(str)
      sort.Slice(s, func(i, j int) bool {
         return s[i] < s[j]
      })
      sortedStr := string(s)
      mapping[sortedStr] = append(mapping[sortedStr], str)
   }
   result := make([][]string, 0, len(mapping))
   for _, val := range mapping {
      result = append(result, val)
   }
   return result
}
```