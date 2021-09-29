# 题目
<p>两个整数之间的 <a href="https://baike.baidu.com/item/%E6%B1%89%E6%98%8E%E8%B7%9D%E7%A6%BB">汉明距离</a> 指的是这两个数字对应二进制位不同的位置的数目。</p>

<p>给你两个整数 <code>x</code> 和 <code>y</code>，计算并返回它们之间的汉明距离。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>x = 1, y = 4
<strong>输出：</strong>2
<strong>解释：</strong>
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
上面的箭头指出了对应二进制位不同的位置。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>x = 3, y = 1
<strong>输出：</strong>1
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 <= x, y <= 2<sup>31</sup> - 1</code></li>
</ul>
<div><div>Related Topics</div><div><li>位运算</li></div></div>

# Python

```python
def hammingDistance(self, x: int, y: int) -> int:
    """
    位运算-异或
    异或规则：位上相同为0，不同为1
    两数异或后，1的位置就是不同的位置，1的数量就是1就是答案
    再使用 n&(n-1)去掉二进制最后一个1，并统计数量，即可
    """
    n = x ^ y
    count = 0
    while n != 0:
        n = n & (n - 1)
        count += 1
    return count
```

# Go

```go
func hammingDistance(x int, y int) int {
   // 异或运算，得出两数不同位置上的1，
   n := x ^ y
   count := 0
   for n != 0 {
      // n&(n-1)去掉最后一位的1，对1进行计数
      n = n & (n - 1)
      count += 1
   }
   return count
}
```