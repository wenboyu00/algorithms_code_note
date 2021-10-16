# 题目
<p>给定一个未排序的整数数组 <code>nums</code> ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。</p>

<p>请你设计并实现时间复杂度为 <code>O(n)</code><em> </em>的算法解决此问题。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [100,4,200,1,3,2]
<strong>输出：</strong>4
<strong>解释：</strong>最长数字连续序列是 <code>[1, 2, 3, 4]。它的长度为 4。</code></pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,3,7,2,5,8,4,6,0,1]
<strong>输出：</strong>9
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 <= nums.length <= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code></li>
</ul>
<div><div>Related Topics</div><div><li>并查集</li><li>数组</li><li>哈希表</li></div></div>

# Python

```python
def longestConsecutive(self, nums: List[int]) -> int:
    """
    找到最长子序列，num为起点，用num递增值在nums查询是否存在，并更新长度。
    用hashSet进行优化查询过程
    在set中查询num-1是否存在，不存在就作为起点，
        查询num递增值在set中存在时，更新长度
        结束时更新答案
    """
    nums_set = set(nums)
    ans = 0
    for num in nums:
        # num-1来确定起点
        if num - 1 not in nums_set:
            size = 0
            # num递增值存在就更新长度
            while num in nums_set:
                size += 1
                num += 1
            # 结束后，更新答案
            ans = max(ans, size)
    return ans
```

# Go

```go
func longestConsecutive(nums []int) int {
   numsSet := map[int]bool{}
   ans := 0
   for _, num := range nums {
      numsSet[num] = true
   }
   for _, num := range nums {
      if !numsSet[num-1] {
         size := 0
         curNum := num
         for numsSet[curNum] {
            curNum += 1
            size += 1
         }
         if ans < size {
            ans = size
         }
      }
   }
   return ans
}
```