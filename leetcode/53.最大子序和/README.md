# 题目

<p>给定一个整数数组 <code>nums</code> ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [-2,1,-3,4,-1,2,1,-5,4]
<strong>输出：</strong>6
<strong>解释：</strong>连续子数组 [4,-1,2,1] 的和最大，为 6 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1]
<strong>输出：</strong>1
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [0]
<strong>输出：</strong>0
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>nums = [-1]
<strong>输出：</strong>-1
</pre>

<p><strong>示例 5：</strong></p>

<pre>
<strong>输入：</strong>nums = [-100000]
<strong>输出：</strong>-100000
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 3 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>5</sup> <= nums[i] <= 10<sup>5</sup></code></li>
</ul>

<p> </p>

<p><strong>进阶：</strong>如果你已经实现复杂度为 <code>O(n)</code> 的解法，尝试使用更为精妙的 <strong>分治法</strong> 求解。</p>



# Python

```python
def maxSubArray(self, nums: List[int]) -> int:
    if not nums:
        return nums
    # 存储最大值
    ans = nums[0]
    # dp[i-1]
    count = nums[0]
    for i in range(1, len(nums)):
        # count > 0，则count对结果有正贡献，count保留并加上当前遍历数字
        if count > 0:
            count += nums[i]
        # count <= 0，则sum对结果负贡献，抛弃当前count，更新当前数字为count
        else:
            count = nums[i]
        # 比较count和ans的大小，将最大值置为ans
        if count > ans:
            ans = count
    return ans
```

# Go

```go
func maxSubArray(nums []int) int {
   ans := nums[0]
   count := ans
   for i:=1;i<len(nums);i++{
      if count > 0{
         count = count + nums[i]
      }else{
         count = nums[i]
      }
      if count > ans{
         ans = count
      }
   }
   return ans
}
```