# 题目

<p>珂珂喜欢吃香蕉。这里有&nbsp;<code>N</code>&nbsp;堆香蕉，第 <code>i</code> 堆中有&nbsp;<code>piles[i]</code>&nbsp;根香蕉。警卫已经离开了，将在&nbsp;<code>H</code>&nbsp;小时后回来。</p>

<p>珂珂可以决定她吃香蕉的速度&nbsp;<code>K</code>&nbsp;（单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 <code>K</code> 根。如果这堆香蕉少于 <code>K</code> 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。&nbsp;&nbsp;</p>

<p>珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。</p>

<p>返回她可以在 <code>H</code> 小时内吃掉所有香蕉的最小速度 <code>K</code>（<code>K</code> 为整数）。</p>

<p>&nbsp;</p>

<ul>
</ul>

<p><strong>示例 1：</strong></p>

<pre><strong>输入: </strong>piles = [3,6,7,11], H = 8
<strong>输出: </strong>4
</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre><strong>输入: </strong>piles = [30,11,23,4,20], H = 5
<strong>输出: </strong>30
</pre>

<p><strong>示例&nbsp;3：</strong></p>

<pre><strong>输入: </strong>piles = [30,11,23,4,20], H = 6
<strong>输出: </strong>23
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= piles.length &lt;= 10^4</code></li>
	<li><code>piles.length &lt;= H &lt;= 10^9</code></li>
	<li><code>1 &lt;= piles[i] &lt;= 10^9</code></li>
</ul>
<div><div>Related Topics</div><div><li>数组</li><li>二分查找</li></div></div>

# Python

```python
def minEatingSpeed(self, piles: List[int], h: int) -> int:
    # 求速度最小，用二分查找
    # 速度最小，耗时最长
    left = 1
    # 速度最大，耗时最短
    right = 1000000000 + 1
    while left <= right:
        mid = left + (right - left) // 2
        mid_hour = self.find_hour(piles, mid)
        # 耗时太多，说明速度太慢，加快速度，下一轮搜索区间[mid+1，right]
        if mid_hour > h:
            left = mid + 1
        # 耗时小，说明速度太快，减慢速度，下一轮搜索区间[left，mid-1]
        else:
            right = mid - 1
    return left

def find_hour(self, piles: List[int], x: int):
    hour = 0
    for pile in piles:
        # 数量//速度 = 时间（小时）
        hour += pile // x
        # 如果数量//速度有余数，说明还需要一个小时才能吃完。就加上1个小时。
        if pile % x > 0:
            hour += 1
    return hour
```

# Go

```go
func minEatingSpeed(piles []int, h int) int {
   maxVal := 0
   for _, pile := range piles {
      if maxVal < pile {
         maxVal = pile
      }
   }
   left := 1
   right := maxVal
   for left <= right {
      mid := left + (right-left)/2
      midHour := findHour(piles, mid)
      // 耗时太多，速度太慢，加速
      if midHour > h {
         left = mid + 1
         // 耗时太少，速度太慢，减速
      } else {
         right = mid - 1
      }
   }
   return left
}

func findHour(piles []int, speed int) int {
   hour := 0
   for _, pile := range piles {
      hour += pile / speed
      fmt.Println(hour)
      if pile%speed > 0 {
         hour += 1
      }
   }
   return hour
}
```