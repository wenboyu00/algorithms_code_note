\# 题目


<p>给你 <code>k</code> 枚相同的鸡蛋，并可以使用一栋从第 <code>1</code> 层到第 <code>n</code> 层共有 <code>n</code> 层楼的建筑。</p>



<p>已知存在楼层 <code>f</code> ，满足 <code>0 <= f <= n</code> ，任何从<strong> 高于</strong> <code>f</code> 的楼层落下的鸡蛋都会碎，从 <code>f</code> 楼层或比它低的楼层落下的鸡蛋都不会破。</p>



<p>每次操作，你可以取一枚没有碎的鸡蛋并把它从任一楼层 <code>x</code> 扔下（满足 <code>1 <= x <= n</code>）。如果鸡蛋碎了，你就不能再次使用它。如果某枚鸡蛋扔下后没有摔碎，则可以在之后的操作中 <strong>重复使用</strong> 这枚鸡蛋。</p>



<p>请你计算并返回要确定 <code>f</code> <strong>确切的值</strong> 的 <strong>最小操作次数</strong> 是多少？</p>




<p><strong>示例 1：</strong></p>



<pre>
<strong>输入：</strong>k = 1, n = 2
<strong>输出：</strong>2
<strong>解释：</strong>
鸡蛋从 1 楼掉落。如果它碎了，肯定能得出 f = 0 。 
否则，鸡蛋从 2 楼掉落。如果它碎了，肯定能得出 f = 1 。 
如果它没碎，那么肯定能得出 f = 2 。 
因此，在最坏的情况下我们需要移动 2 次以确定 f 是多少。 
</pre>



<p><strong>示例 2：</strong></p>



<pre>
<strong>输入：</strong>k = 2, n = 6
<strong>输出：</strong>3
</pre>



<p><strong>示例 3：</strong></p>



<pre>
<strong>输入：</strong>k = 3, n = 14
<strong>输出：</strong>4
</pre>
# Python

```python
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        memo = list()
        for i in range(k + 1):
            memo.append([None] * (n + 1))

        def dp(k, n):
            # base case
            # 一个鸡蛋，只能线性扫描楼层
            if k == 1:
                return n
            # 0层楼，不需要扔鸡蛋
            if n == 0:
                return 0
            # dp数组（备忘录）
            if memo[k][n] is not None:
                return memo[k][n]
            # float('INF')正无穷
            res = float('INF')
            # 二分查找方式低=1，高=n
            low, high = 1, n
            while low <= high:
                # mid = 低+高 整除 2
                mid = (low + high) // 2
                # 碎了：k-1，搜索楼层从1...N变成了1...mid-1共mid-1层
                # 没碎：k, 搜索楼层从1...N变成了mid+1...n共n-mid层
                broken = dp(k - 1, mid - 1)  # 碎
                not_broken = dp(k, n - mid)  # 没碎
                # 最坏情况下的最少次数min(max(broken, notBroken)
                # 疑问点：high = mid-1和low= mid+1
                if broken > not_broken:
                    high = mid - 1
                    res = min(res, broken + 1)
                else:
                    low = mid + 1
                    res = min(res, not_broken + 1)
            memo[k][n] = res
            return res

        return dp(k, n)
```

# GO

```go
package main

import (
   "fmt"
   "math"
)

func superEggDrop(k int, n int) int {
   memo := make([][]int, k+1)
   for i := range memo {
      rows := make([]int, n+1)
      for j := 0; j < len(rows); j++ {
         rows[j] = math.MaxInt32
      }
      memo[i] = rows

   }
   return dp(k, n, memo)
}

func dp(k int, n int, memo [][]int) int {
   if k == 1 {
      return n
   }
   if n == 0 {
      return 0
   }
   if memo[k][n] != math.MaxInt32{
      return memo[k][n]
   }

   result := math.MaxInt16
   low, high := 1, n
   for low <= high {
      mid := (low + high) / 2
      broken := dp(k-1, mid-1, memo)
      notBroken := dp(k, n-mid, memo)
      if broken > notBroken {
         high = mid - 1
         if result > broken+1 {
            result = broken + 1
         }
      } else {
         low = mid + 1
         if result > notBroken+1 {
            result = notBroken + 1
         }
      }
   }
   memo[k][n] = result
   return result
}

func main() {
   result := superEggDrop(7, 10000)
   fmt.Println(result)

}
```