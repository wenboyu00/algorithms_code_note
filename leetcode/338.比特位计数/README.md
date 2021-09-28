# 题目
<p>给你一个整数 <code>n</code> ，对于&nbsp;<code>0 &lt;= i &lt;= n</code> 中的每个 <code>i</code> ，计算其二进制表示中 <strong><code>1</code> 的个数</strong> ，返回一个长度为 <code>n + 1</code> 的数组 <code>ans</code> 作为答案。</p>

<p>&nbsp;</p>

<div class="original__bRMd">
<div>
<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 2
<strong>输出：</strong>[0,1,1]
<strong>解释：</strong>
0 --&gt; 0
1 --&gt; 1
2 --&gt; 10
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 5
<strong>输出：</strong>[0,1,1,2,1,2]
<strong>解释：</strong>
0 --&gt; 0
1 --&gt; 1
2 --&gt; 10
3 --&gt; 11
4 --&gt; 100
5 --&gt; 101
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 10<sup>5</sup></code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong></p>

<ul>
	<li>很容易就能实现时间复杂度为 <code>O(n log n)</code> 的解决方案，你可以在线性时间复杂度 <code>O(n)</code> 内用一趟扫描解决此问题吗？</li>
	<li>你能不使用任何内置函数解决此问题吗？（如，C++ 中的&nbsp;<code>__builtin_popcount</code> ）</li>
</ul>
</div>
</div>

<div><div>Related Topics</div><div><li>位运算</li><li>动态规划</li></div></div>

# Python

```python
def countBits(self, n: int) -> List[int]:
    # dp数组, 同时也是结果数组
    result = [0] * (n + 1)
    # base case result[0] = 0, 0的1的个数是0
    for i in range(n + 1):

        if i % 2 == 1:
            # 奇数比前面偶数低位上多1
            result[i] = result[i - 1] + 1
        else:
            # 偶数是除2(0右移，消除一个零)之后的值
            result[i] = result[i // 2]
    return result
```

# Go

```go
func countBits(n int) []int {
   // dp数组，结果数组，存放十进制数对应的二进制1的个数
   // base case：result[0] = 1 ，0的二进制1的个数是0
   // 状态转移方程：
   // 当i为奇数时1的个数 = i-1 +1，因为奇数比上一个数（偶数）多1，这个1出现在低位上。
   // 当i为偶数时1的个数 = i/2，因为i/2相当于去掉一个0，偶数低位是0。
   result := make([]int, n+1)
   for i := 1; i < n+1; i++ {
      if i%2 == 1 {
         result[i] = result[i-1] + 1
      } else {
         result[i] = result[i/2]
      }
   }
   return result
}
```