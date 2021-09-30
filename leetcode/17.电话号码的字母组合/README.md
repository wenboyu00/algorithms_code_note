# 题目
<p>给定一个仅包含数字 <code>2-9</code> 的字符串，返回所有它能表示的字母组合。答案可以按 <strong>任意顺序</strong> 返回。</p>

<p>给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。</p>

<p><img src="https://assets.leetcode-cn.com/aliyun-lc-upload/original_images/17_telephone_keypad.png" style="width: 200px;" /></p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>digits = "23"
<strong>输出：</strong>["ad","ae","af","bd","be","bf","cd","ce","cf"]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>digits = ""
<strong>输出：</strong>[]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>digits = "2"
<strong>输出：</strong>["a","b","c"]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 <= digits.length <= 4</code></li>
	<li><code>digits[i]</code> 是范围 <code>['2', '9']</code> 的一个数字。</li>
</ul>
<div><div>Related Topics</div><div><li>哈希表</li><li>字符串</li><li>回溯</li></div></div>

# Python

```python
def letterCombinations(self, digits: str) -> List[str]:
    # 组合问题，回溯算法(DFS)
    # 每个数字对应多个字母 进行组合
    # 每组数字的长度 是 每个数字的长度 len(digits)
    # 每次循环拿对应的字母 添加到路径列表中
    phone = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}
    result = []
    path = []
    if not digits:
        return result
    n = len(digits)

    def backtrack(path, index):
        if len(path) == n:
            result.append(''.join(path))
            return
        # 选择列表 数字对应的列表
        # 但是选择的是 数字，所以传入index对数字进行选择
        digit = digits[index]
        for s in phone[digit]:
            path.append(s)
            backtrack(path, index + 1)
            path.pop()

    backtrack(path, 0)
    return result
```

# Go

```go
phone := map[byte][]string{
   '2': {"a", "b", "c"},
   '3': {"d", "e", "f"},
   '4': {"g", "h", "i"},
   '5': {"j", "k", "l"},
   '6': {"m", "n", "o"},
   '7': {"p", "q", "r", "s"},
   '8': {"t", "u", "v"},
   '9': {"w", "x", "y", "z"}}
path := []string{}
result := []string{}
n := len(digits)
if n == 0 {
   return result
}
var backtrack func(path []string, index int)
backtrack = func(path []string, index int) {
   // 满足结束条件
   if len(path) == n {
      result = append(result, strings.Join(path, ""))
      return
   }
   // 循环选择
   digit := digits[index]
   for _, s := range phone[digit] {
      // 做选择
      path = append(path, s)
      backtrack(path, index+1)
      path = path[:len(path)-1]
   }
}
backtrack(path, 0)
return result
```

