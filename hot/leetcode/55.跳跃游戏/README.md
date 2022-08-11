# 题目
<p>给定一个非负整数数组 <code>nums</code> ，你最初位于数组的 <strong>第一个下标</strong> 。</p>

<p>数组中的每个元素代表你在该位置可以跳跃的最大长度。</p>

<p>判断你是否能够到达最后一个下标。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,3,1,1,4]
<strong>输出：</strong>true
<strong>解释：</strong>可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,2,1,0,4]
<strong>输出：</strong>false
<strong>解释：</strong>无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 3 * 10<sup>4</sup></code></li>
	<li><code>0 <= nums[i] <= 10<sup>5</sup></code></li>
</ul>
<div><div>Related Topics</div><div><li>贪心</li><li>数组</li><li>动态规划</li></div></div>

# Python

```python
def canJump(self, nums: List[int]) -> bool:
    """
    动态规划-优化
    far(最远距离)代替dp数组：
    base case: far = nums[0]
    选择：far = max(far, nums[i](跳跃长度) + i(当前位置))
    状态:无
    如果 far <= i:
        return False
    return far>= 最后长度
    """
    n = len(nums)
    far = nums[0]
    for i in range(n - 1):
        # 不断计算能跳到的最远距离
        far = max(far, i + nums[i])
        # 最远距离 <= 当前位置距离，就跳不动了
        if far <= i:
            return False
    return far >= n - 1
```

# Go

```go
func canJump(nums []int) bool {
   n := len(nums)
   far := nums[0]
   for i := 0; i < n-1; i++ {
      if far < i+nums[i] {
         far = i + nums[i]
      }
      if far <= i {
         return false
      }
   }
   return far >= n-1
}
```