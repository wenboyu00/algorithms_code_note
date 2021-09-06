# 题目
<p>给定一个非负整数数组 <code>nums</code> 和一个整数 <code>m</code> ，你需要将这个数组分成 <code>m</code><em> </em>个非空的连续子数组。</p>

<p>设计一个算法使得这 <code>m</code><em> </em>个子数组各自和的最大值最小。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [7,2,5,10,8], m = 2
<strong>输出：</strong>18
<strong>解释：</strong>
一共有四种方法将 nums 分割为 2 个子数组。 其中最好的方式是将其分为 [7,2,5] 和 [10,8] 。
因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,4,5], m = 2
<strong>输出：</strong>9
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,4,4], m = 3
<strong>输出：</strong>4
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 1000</code></li>
	<li><code>0 <= nums[i] <= 10<sup>6</sup></code></li>
	<li><code>1 <= m <= min(50, nums.length)</code></li>
</ul>
<div><div>Related Topics</div><div><li>贪心</li><li>数组</li><li>二分查找</li><li>动态规划</li></div></div>

# Python

```python
def splitArray(self, nums: List[int], m: int) -> int:
    left, right = max(nums), sum(nums)

    while left <= right:
        mid = left + (right - left) // 2
        # mid_m > m, 数组和小了，增加数组和，取右半边
        if self.get_mid_m(nums, mid) > m:
            left = mid + 1
        # mid_m < m, 数组和大了，减少数组和，取左半边。
        # 当mid_m = m，范围内不止一个数，范围继续向左半边收敛，找到最小值。
        else:
            right = mid - 1
    return left

def get_mid_m(self, nums: List[int], sum_val: int):
    # sum_val是数组和，count是数组数量，cur是当前数组和
    count = 1
    cur = 0
    for num in nums:
        # 如果当前数组大于x数组和时，开启一个新的数组
        if cur + num > sum_val:
            count += 1
            cur = 0
        # 每次都叠加
        cur += num
    return count
```

# Go

```go
func splitArray(nums []int, m int) int {
   left, right := getMaxSumNum(nums)
   for left <= right {
      mid := left + (right-left)/2
      // 切分数 > m，数组和太小，增加数组和，下次循环选择右半边
      if getSplitNum(nums, mid) > m {
         left = mid + 1
         // 切分数<m，数组和太大，减小数组和，下次循环选择左半边
         // 切分数==m,继续向左半边收敛，找到最小值
      } else {
         right = mid - 1
      }
   }
   return left
}

func getMaxSumNum(nums []int) (int, int) {
   maxVal := 0
   sumVal := 0
   for _, num := range nums {
      if maxVal < num {
         maxVal = num
      }
      sumVal += num
   }
   return maxVal, sumVal
}

func getSplitNum(nums []int, sumVal int) int {
   // 获得切分数，SumVal是每次数组和
   count := 1
   cur := 0
   for _, num := range nums {
      // 累计+当前 > 数组和，就开启一个新的数组
      if cur+num > sumVal {
         count += 1
         cur = 0
      }
      cur += num
   }
   return count
}
```

