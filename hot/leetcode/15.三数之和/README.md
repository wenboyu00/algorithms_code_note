# 题目
<p>给你一个包含 <code>n</code> 个整数的数组 <code>nums</code>，判断 <code>nums</code> 中是否存在三个元素 <em>a，b，c ，</em>使得 <em>a + b + c = </em>0 ？请你找出所有和为 <code>0</code> 且不重复的三元组。</p>

<p><strong>注意：</strong>答案中不可以包含重复的三元组。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [-1,0,1,2,-1,-4]
<strong>输出：</strong>[[-1,-1,2],[-1,0,1]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = []
<strong>输出：</strong>[]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [0]
<strong>输出：</strong>[]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 <= nums.length <= 3000</code></li>
	<li><code>-10<sup>5</sup> <= nums[i] <= 10<sup>5</sup></code></li>
</ul>
<div><div>Related Topics</div><div><li>数组</li><li>双指针</li><li>排序</li></div></div>

# Python

```python
"""
[   -4, -1, -1,  0,  1, 2   ]
    i   l               r
     ->  -->          <--                           
对排序的数组遍历，使用三指针，固定一个值i，对i后面的数组使用左右双指针，通过目标值的对比来移动l和r 已使达到目标
对数组排序，排序固定一个数nums[i]，再使用左右指针只想nums[i]后两端，计算和0的关系，
    - 大于0：减小r 使值变的更小
    - 小于0：增大l 使值变的更大
    - 等于0：添加到结果集，
        - 对l指针进行去重，和前值相等进一
        - 对r指针进行去重，和后值相等减一
        - 去重后 l加一，r减一
    - 对i指针去重， 和前值相等跳过
时间复杂度O(n^2)
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        ans = []
        for i in range(n):
            val = nums[i]
            if val > 0:
                continue
            # i 去重（和前值相等就跳过，实现去重）
            if i > 0 and val == nums[i - 1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                three_sum = val + nums[l] + nums[r]
                if three_sum == 0:
                    ans.append([val, nums[l], nums[r]])
                    # l去重，和前值相等进一
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    # r去重，和后值相等减一
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
        return ans
```

# Go

```go
func threeSum(nums []int) [][]int {
   sort.Ints(nums)
   n := len(nums)
   ans := [][]int{}
   for i := 0; i < n; i++ {
      val := nums[i]
      if val > 0 {
         continue
      }
      if i > 0 && val == nums[i-1] {
         continue
      }
      l := i + 1
      r := n - 1
      for l < r {
         sum := val + nums[l] + nums[r]
         if sum == 0 {
            ans = append(ans, []int{val, nums[l], nums[r]})
            for l < r && nums[l] == nums[l+1] {
               l += 1
            }
            for l < r && nums[r] == nums[r-1] {
               r -= 1
            }
            l += 1
            r -= 1
         } else if sum > 0 {
            r -= 1
         } else if sum < 0 {
            l += 1

         }
      }
   }
   return ans
}
```