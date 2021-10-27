# 题目
<p>给定一个包含 <code>n + 1</code> 个整数的数组 <code>nums</code> ，其数字都在 <code>1</code> 到 <code>n</code><em> </em>之间（包括 <code>1</code> 和 <code>n</code>），可知至少存在一个重复的整数。</p>

<p>假设 <code>nums</code> 只有 <strong>一个重复的整数</strong> ，找出 <strong>这个重复的数</strong> 。</p>

<p>你设计的解决方案必须不修改数组 <code>nums</code> 且只用常量级 <code>O(1)</code> 的额外空间。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,3,4,2,2]
<strong>输出：</strong>2
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,1,3,4,2]
<strong>输出：</strong>3
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1]
<strong>输出：</strong>1
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1,2]
<strong>输出：</strong>1
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= n <= 10<sup>5</sup></code></li>
	<li><code>nums.length == n + 1</code></li>
	<li><code>1 <= nums[i] <= n</code></li>
	<li><code>nums</code> 中 <strong>只有一个整数</strong> 出现 <strong>两次或多次</strong> ，其余整数均只出现 <strong>一次</strong></li>
</ul>

<p> </p>

<p><b>进阶：</b></p>

<ul>
	<li>如何证明 <code>nums</code> 中至少存在一个重复的数字?</li>
	<li>你可以设计一个线性级时间复杂度 <code>O(n)</code> 的解决方案吗？</li>
</ul>
<div><div>Related Topics</div><div><li>位运算</li><li>数组</li><li>双指针</li><li>二分查找</li></div></div>

# Python

```python
def findDuplicate(self, nums: List[int]) -> int:
    """
    快慢指针 类似链表有环
    通过用 nums[i]和下表[i] 做映射形成，链表效果用快慢指针的方法找到存在环，再找到环入口。
     1.数组中有一个重复的整数 <==> 链表中存在环
     2.找到数组中的重复整数 <==> 找到链表的环入口
    slow = slow.next ==> slow = nums[slow]
    fast = fast.next.next ==> fast = nums[nums[fast]]
    """
    # 找到环存在
    slow, fast = nums[0], nums[nums[0]]
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]
    # 找到环入口
    slow = 0
    while slow != fast:
        fast = nums[fast]
        slow = nums[slow]
    return slow
```

# Go

```go
func findDuplicate(nums []int) int {
   /*
      快慢指针，通过nums[i]和i的映射把问题转换成判断环形链表入口问题
      因为有重复的数值，必然会出现多对一的情况，形成了环
   */
   // 找到环
   slow := nums[0]
   fast := nums[nums[0]]
   for slow != fast {
      slow = nums[slow]
      fast = nums[nums[fast]]
   }
   // 找到环入口
   slow = 0
   for slow != fast {
      slow = nums[slow]
      fast = nums[fast]
   }
   return slow
}
```