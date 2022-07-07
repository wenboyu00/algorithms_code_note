# 题目

<p>在一个数组 <code>nums</code> 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [3,4,3,3]
<strong>输出：</strong>4
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [9,1,7,9,7,9,7]
<strong>输出：</strong>1</pre>

<p>&nbsp;</p>

<p><strong>限制：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10000</code></li>
	<li><code>1 &lt;= nums[i] &lt; 2^31</code></li>
</ul>

<p>&nbsp;</p>

# Python

```python
"""
异或 ^ ：   相同为0，不同为1
或   & :   同为1时为1，不同时为0
左移1位 <<=

题目:找到数组中出现1次2个数

位运算
找到出现1次的数，用异或
出现2个数，可以对数组进行分组(奇偶分组)。重复的数，数值是一样的，可以被分到同一组中。
如何分组：
    - 得到mask分组值
        对nums遍历进行异或，得到2个数的异或值，因为2个不同的数，至少二进制有一个位是不同的。
        用2数异或值某为1的二进制位，做mask即可对nums进行奇偶分组，因为为1二进制表示这是不同的地方。
    - 遍历nums，num&mask进行奇偶分组再异或，最后得到2组中不同的只出现一次的数。
"""


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        # 得到2数的异或值
        xor = 0
        for num in nums:
            xor ^= num
        mask = 1
        # 得到xor最低位的1，让mask从0001开始，每次都不满足都左移一位
        while (mask & xor) == 0:
            mask <<= 1
        # 用mask对num分组，异或后得出答案
        x, y = 0, 0
        for num in nums:
            if num & mask:
                x ^= num
            else:
                y ^= num
        return [x, y]
```

# Go

```go
func singleNumber(nums []int) int {
   ans := 0
   for i := 0; i < 32; i++ {
      bit := 0
      for _, num := range nums{
         bit += num>>i & 1
      }
      ans += bit%3 << i
   }
   return ans
}
```