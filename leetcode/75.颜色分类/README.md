# 题目
<p>给定一个包含红色、白色和蓝色，一共 <code>n</code><em> </em>个元素的数组，<strong><a href="https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95" target="_blank">原地</a></strong>对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。</p>

<p>此题中，我们使用整数 <code>0</code>、 <code>1</code> 和 <code>2</code> 分别表示红色、白色和蓝色。</p>

<ul>
</ul>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,0,2,1,1,0]
<strong>输出：</strong>[0,0,1,1,2,2]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,0,1]
<strong>输出：</strong>[0,1,2]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [0]
<strong>输出：</strong>[0]
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>nums = [1]
<strong>输出：</strong>[1]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 <= n <= 300</code></li>
	<li><code>nums[i]</code> 为 <code>0</code>、<code>1</code> 或 <code>2</code></li>
</ul>

<p> </p>

<p><strong>进阶：</strong></p>

<ul>
	<li>你可以不使用代码库中的排序函数来解决这道题吗？</li>
	<li>你能想出一个仅使用常数空间的一趟扫描算法吗？</li>
</ul>
<div><div>Related Topics</div><div><li>数组</li><li>双指针</li><li>排序</li></div></div>

# Python

```python
def sortColors(self, nums: List[int]) -> None:
    """
    通过双指针把数组分为3部分[0,1,2]
    遍历数组，把所有0交换到数组左边，1保持不动放在中间，2交换到右边
    遍历数组，i从左到右，p2从右到左，i超过p2时结束
    i <= p2:
        - nums[i]==0,和nums[p0]交换，p0和i前进
        - nums[i]==1,保持不动，i前进
        - nums[i]==2,和nums[p2]交换, p2前进
            - i 保持不动，因为和nums[p2]交换后，nums[i]可能还是2，所以i要进入下一轮循环
    """
    n = len(nums)
    p0, p2 = 0, n - 1
    i = 0
    while i <= p2:
        if nums[i] == 0:
            nums[i], nums[p0] = nums[p0], nums[i]
            p0 += 1
            i += 1
        elif nums[i] == 1:
            i += 1
        elif nums[i] == 2:
            nums[i], nums[p2] = nums[p2], nums[i]
            p2 -= 1
```

# Go

```go
func sortColors(nums []int) {
   n := len(nums)
   p0, p2 := 0, n-1
   i := 0
   for i <= p2 {
      if nums[i] == 0 {
         nums[i], nums[p0] = nums[p0], nums[i]
         p0 += 1
         i += 1
      } else if nums[i] == 1 {
         i += 1
      // nums[i] == 2
      } else {
         // 因为交换后nums[i]可能还是2，所以要进入下一轮循环，i保持不动
         nums[i], nums[p2] = nums[p2], nums[i]
         p2 -= 1
      }
   }

}
```