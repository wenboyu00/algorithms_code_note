# 题目
<p>给你一个整数数组 <code>nums</code> ，数组中的元素 <strong>互不相同</strong> 。返回该数组所有可能的子集（幂集）。</p>

<p>解集 <strong>不能</strong> 包含重复的子集。你可以按 <strong>任意顺序</strong> 返回解集。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3]
<strong>输出：</strong>[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0]
<strong>输出：</strong>[[],[0]]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 10</code></li>
	<li><code>-10 <= nums[i] <= 10</code></li>
	<li><code>nums</code> 中的所有元素 <strong>互不相同</strong></li>
</ul>
<div><div>Related Topics</div><div><li>位运算</li><li>数组</li><li>回溯</li></div></div>

# Python

```python
def subsets(self, nums: List[int]) -> List[List[int]]:
    # 路径
    track = []
    res = []
    n = len(nums)

    def back_track(start):
        # 满足结束条件
        res.append(list(track))
        # 遍历 选择
        for i in range(start, n):
            # 做选择
            track.append(nums[i])
            # 递归
            back_track(i + 1)
            # 撤销选择
            track.pop()

    back_track(0)
    return res
```

# Go

```go
func subsets(nums []int) [][]int {
   n := len(nums)
   // 路径列表
   track := make([]int, 0, n)
   res := [][]int{}

   var backTrack func(start int)
   backTrack = func(start int) {
      // 把路径添加到结果集，生成新的数组的方式
      res = append(res, append(make([]int, 0, n), track...))
      // 遍历选择
      for i := start; i < n; i++ {
         // 做选择
         track = append(track, nums[i])
         // 递归
         backTrack(i + 1)
         // 取消选择
         track = track[:len(track)-1]
      }
   }
   backTrack(0)
   return res
}
```

