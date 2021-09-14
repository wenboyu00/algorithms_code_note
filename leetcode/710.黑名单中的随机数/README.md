# 题目
<p>给定一个包含 <code>[0，n)</code> 中不重复整数的黑名单 <code>blacklist</code> ，写一个函数从 <code>[0, n)</code> 中返回一个<strong>不在</strong> <code>blacklist</code> 中的随机整数。</p>

<p>对它进行优化使其尽量少调用系统方法 <code>Math.random()</code> 。</p>

<p><strong>提示:</strong></p>

<ol>
	<li><code>1 <= n <= 1000000000</code></li>
	<li><code>0 <= blacklist.length < min(100000, N)</code></li>
	<li><code>[0, n)</code> 不包含 <code>n</code> ，详细参见 <a href="https://en.wikipedia.org/wiki/Interval_(mathematics)" target="_blank">interval notation</a> 。</li>
</ol>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：
</strong>["Solution","pick","pick","pick"]
[[1,[]],[],[],[]]
<strong>输出：</strong>[null,0,0,0]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：
</strong>["Solution","pick","pick","pick"]
[[2,[]],[],[],[]]
<strong>输出：</strong>[null,1,1,1]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：
</strong>["Solution","pick","pick","pick"]
[[3,[1]],[],[],[]]
<strong>输出：</strong>[null,0,0,2]
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入： 
</strong>["Solution","pick","pick","pick"]
[[4,[2]],[],[],[]]
<strong>输出：</strong>[null,1,3,1]
</pre>

<p><strong>输入语法说明：</strong></p>

<p>输入是两个列表：调用成员函数名和调用的参数。<code>Solution</code>的构造函数有两个参数，<code>n</code> 和黑名单 <code>blacklist</code>。<code>pick</code> 没有参数，输入参数是一个列表，即使参数为空，也会输入一个 <code>[]</code> 空列表。</p>
<div><div>Related Topics</div><div><li>哈希表</li><li>数学</li><li>二分查找</li><li>排序</li><li>随机化</li></div></div>

# Python

```python
class Solution:
    """
    共有N个数字，黑名单个数=len(blacklist), 白名单个数 n - len(blacklist).
    为了可以使用random.randint(0, self.white_len - 1)随机取得white_len个白名单数字中的一个。
    使用 map 将white_len中黑名单的数字和white_len之后白名单的数字映射起来
    pick时，使用random随机选择一个索引，如果这个索引被到黑名单上，就返回对应的白名单的位置
    """

    def __init__(self, n: int, blacklist: List[int]):
        # 黑名单个数: len(blacklist)
        # 白名单个数(white_len): n - len(blacklist)
        self.white_len = n - len(blacklist)
        # black_set，在white_len之前黑名单中的数字
        black_set = set()
        for i in blacklist:
            if i < self.white_len:
                black_set.add(i)

        # white_set：在white_len之后的白名单中的数字
        white_set = set()
        blacklist_set = set(blacklist)
        for i in range(self.white_len, n):
            if i not in blacklist_set:
                white_set.add(i)
        # 使用map将black_set中的元素和white—set映射起来
        self.map = dict(zip(black_set, white_set))

    def pick(self) -> int:
        # 在前white_len个数字中随机选取
        res = random.randint(0, self.white_len - 1)
        # 如res是map的key，说明这个位置是黑名单中的数字，通过映射取出其对应的白名单的数字
        if res in self.map:
            return self.map[res]
        # 如res不是map的key，说明这个位置是白名单中的数字，直接返回
        else:
            return res
```

# Go

```go
import "math/rand"

type Solution struct {
   mapping map[int]int
   n       int
}

func Constructor(n int, blacklist []int) Solution {
   mapping := map[int]int{}

   whiteLen := n - len(blacklist)
   // 在whiteLen中的黑名单数字
   inWhiteBlack := make([]int, 0)
   blacklistSet := make(map[int]int8, len(blacklist))
   for _, i := range blacklist {
      if i < whiteLen {
         inWhiteBlack = append(inWhiteBlack, i)
      }
      blacklistSet[i] = -1
   }
   // 在whiteLen之后的白名单数字
   NotInWhite := make([]int, 0)
   for i := whiteLen; i < n; i++ {
      if _, ok := blacklistSet[i]; !ok {
         NotInWhite = append(NotInWhite, i)
      }
   }
   // 把inWhiteBlack和NotInWhite映射上，数量是一致的
   iwbN := len(inWhiteBlack)
   for i := 0; i < iwbN; i++ {
      mapping[inWhiteBlack[i]] = NotInWhite[i]
   }
   return Solution{mapping, whiteLen}
}

func (this *Solution) Pick() int {
   index := rand.Int() % this.n - 1
   if _, ok := this.mapping[index]; ok {
      return this.mapping[index]
   }
   return index
}
```