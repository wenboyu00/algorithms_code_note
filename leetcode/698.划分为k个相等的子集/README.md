# 题目
<p>给定一个整数数组&nbsp;&nbsp;<code>nums</code> 和一个正整数 <code>k</code>，找出是否有可能把这个数组分成 <code>k</code> 个非空子集，其总和都相等。</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong> nums = [4, 3, 2, 3, 5, 2, 1], k = 4
<strong>输出：</strong> True
<strong>说明：</strong> 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= len(nums) &lt;= 16</code></li>
	<li><code>0 &lt; nums[i] &lt; 10000</code></li>
</ul>
<div><div>Related Topics</div><div><li>位运算</li><li>记忆化搜索</li><li>数组</li><li>动态规划</li><li>回溯</li><li>状态压缩</li></div></div>

# Python

```python
def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
    n = len(nums)
    if k > n:
        return False
    nums_sum = sum(nums)
    # 总值%桶数 == 0 ，可以被整除才能进行元素和查找
    if nums_sum % k != 0:
        return False
    # 每个桶的和
    target = nums_sum / k
    # 标记元素使用状态，避免重复
    used = [False for i in range(n)]

    def back_track(bucket_num, bucket_sum, start):
        # base case 桶数为0, 所有桶都装满了
        if bucket_num == 0:
            return True
        # 装满了当前桶，递归穷举下一个桶的选择 让下一个桶从 nums[0] 开始选数字
        if bucket_sum == target:
            return back_track(bucket_num - 1, 0, 0)

        # 从start开始向后查询是否有有效的nums[1]
        for i in range(start, len(nums)):
            # nums[i]已经被使用
            if used[i]:
                continue
            # 装不下
            if nums[i] + bucket_sum > target:
                continue
            # 做选择，将nums[i]装入
            used[i] = True
            bucket_sum += nums[i]
            # 递归到下一层
            res = back_track(bucket_num, bucket_sum, i + 1)
            if res:
                return True
            # 撤销选择
            used[i] = False
            bucket_sum -= nums[i]

        # 穷举了所有数字，都无法达到目标
        return False

    return back_track(k, 0, 0)
```

# Go

```go
func canPartitionKSubsets(nums []int, k int) bool {
   // 桶数超过数组长度
   n := len(nums)
   if k > n {
      return false
   }
   // 数组和 平均分 桶
   sum := 0
   for _, num := range nums {
      sum += num
   }
   if sum%k != 0 {
      return false
   }
   // 平均分桶后每桶的 总和
   target := sum / k

   // 值是否被使用
   used := make([]bool, n)
   for i := 0; i < n; i++ {
      used[i] = false
   }
   var backTrack func(bucketNum int, bucketSum int, start int) bool
   backTrack = func(bucketNum int, bucketSum int, start int) bool {
      // base case 回溯结束，所有桶都满了
      if bucketNum == 0 {
         return true
      }
      // 当前桶 已满，从头开始找下个桶
      if bucketSum == target {
         return backTrack(bucketNum-1, 0, 0)
      }
      // 遍历选择
      for i := start; i < n; i++ {
         // 是否已经被使用
         if used[i] {
            continue
         }
         // 是否装不下
         if nums[i]+bucketSum > target {
            continue
         }
         // 做选择
         used[i] = true
         bucketSum += nums[i]
         // 递归下一级, 前进一步
         res := backTrack(bucketNum, bucketSum, i+1)
         if res == true {
            return true
         }
         // 撤销选择
         used[i] = false
         bucketSum -= nums[i]
      }
      // 没有合适就返回false
      return false
   }

   return backTrack(k, 0, 0)
```