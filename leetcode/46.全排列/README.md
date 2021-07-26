# 题目

<p>给定一个不含重复数字的数组 <code>nums</code> ，返回其 <strong>所有可能的全排列</strong> 。你可以 <strong>按任意顺序</strong> 返回答案。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3]
<strong>输出：</strong>[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,1]
<strong>输出：</strong>[[0,1],[1,0]]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1]
<strong>输出：</strong>[[1]]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 6</code></li>
	<li><code>-10 <= nums[i] <= 10</code></li>
	<li><code>nums</code> 中的所有整数 <strong>互不相同</strong></li>
</ul>

# Python

```Python
class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        result = list()

        def back_track(nums, track):
            # 满足结束条件
            # 达到叶子根节点，将路径装入结果列表
            if len(track) == len(nums):
                result.append(tuple(track))
                return None

            for i in nums:
                # 排除不合法选择
                if i in track:
                    continue
                # 做选择
                track.append(i)
                # 进入下一层决策树
                back_track(nums, track)
                # 取消选择
                track.pop(-1)

        back_track(nums, [])
        return result
```

# Go

```Go
func permute(nums []int) [][]int {
   var result [][]int
   // 选择列表
   var track []int
   // 辅助判断是否使用
   used := make([]bool, len(nums))
   backTrack(nums, track, &result, &used)
   return result
}

func backTrack(nums []int, track []int, result *[][]int, used *[]bool) {
   // 满足结束条件,达到叶子根节点，将路径装入结果列表
   if len(nums) == len(track) {
      trackTemp := make([]int, len(track))
      copy(trackTemp, track)
      *result = append(*result, trackTemp)
      return
   }
   for i, v := range nums {
      // 判断是否使用
      if !(*used)[i] {
         // 做选择，路径.append(路径)
         track = append(track, v)
         (*used)[i] = true
         // 进入下一层决策树
         backTrack(nums, track, result, used)
         // 撤销选择，将该选择再次加入列表
         track = track[:len(track)-1]
         (*used)[i] = false
      }
   }
}
```