# 题目
<p>传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。</p>

<p>传送带上的第 <code>i</code> 个包裹的重量为 <code>weights[i]</code>。每一天，我们都会按给出重量的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。</p>

<p>返回能在 <code>D</code> 天内将传送带上的所有包裹送达的船的最低运载能力。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>weights = [1,2,3,4,5,6,7,8,9,10], D = 5
<strong>输出：</strong>15
<strong>解释：</strong>
船舶最低载重 15 就能够在 5 天内送达所有包裹，如下所示：
第 1 天：1, 2, 3, 4, 5
第 2 天：6, 7
第 3 天：8
第 4 天：9
第 5 天：10

请注意，货物必须按照给定的顺序装运，因此使用载重能力为 14 的船舶并将包装分成 (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) 是不允许的。 
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>weights = [3,2,2,4,1,4], D = 3
<strong>输出：</strong>6
<strong>解释：</strong>
船舶最低载重 6 就能够在 3 天内送达所有包裹，如下所示：
第 1 天：3, 2
第 2 天：2, 4
第 3 天：1, 4
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>weights = [1,2,3,1,1], D = 4
<strong>输出：</strong>3
<strong>解释：</strong>
第 1 天：1
第 2 天：2
第 3 天：3
第 4 天：1, 1
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= D <= weights.length <= 5 * 10<sup>4</sup></code></li>
	<li><code>1 <= weights[i] <= 500</code></li>
</ul>
<div><div>Related Topics</div><div><li>贪心</li><li>数组</li><li>二分查找</li></div></div>

# Python

```python
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # left 最小量：数组中最大值，一次至少把最大值装完
        # right 最大量：数组中值的综合，一次把所有都装完
        left, right = max(weights), sum(weights)
        while left <= right:
            mid = left + (right - left) // 2
            if self.get_need_day(weights, mid) > days:
                # 耗时太多，说明容量太小，加大容量，下一轮搜索区间[mid+1，right]
                left = mid + 1
            else:
                # 耗时太少，说明容量太多，加小容量，下一轮搜索区间[left，mid-1]
                right = mid - 1
        return left

    def get_need_day(self, weights, x):
        # 找到x容量，在weight所需要的天数
        need = 1
        cur = 0
        # 遍历重量，记录当前重量，如果超出容量就加上一天
        for w in weights:
            if cur + w > x:
                need += 1
                cur = 0
            cur += w
        return need
```

# Go

```go
func shipWithinDays(weights []int, days int) int {
   left, right := getMinMaxWeights(weights)
   for left <= right {
      mid := left + (right-left)/2
      // 耗时太多，容量太小，增加容量，下一轮[mid+1, right]
      if getNeedDays(weights, mid) > days {
         left = mid + 1
         // 耗时太小，容量太大，减少容量,下一轮[left , mid-1】
      } else {
         right = mid - 1
      }
   }
   return left
}

func getMinMaxWeights(weights []int) (int, int) {
   maxVal := 0
   sumVal := 0
   for _, weight := range weights {
      if maxVal < weight {
         maxVal = weight
      }
      sumVal += weight

   }
   return maxVal, sumVal
}

func getNeedDays(weights []int, x int) int {
   day := 1
   cur := 0
   for _, weight := range weights {
      if cur+weight > x {
         day += 1
         cur = 0
      }
      cur += weight
   }
   return day
}
```