# 题目
<p>给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> [1,2,1]
<strong>输出:</strong> [2,-1,2]
<strong>解释:</strong> 第一个 1 的下一个更大的数是 2；
数字 2 找不到下一个更大的数； 
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
</pre>

<p><strong>注意:</strong> 输入数组的长度不会超过 10000。</p>
<div><div>Related Topics</div><div><li>栈</li><li>数组</li><li>单调栈</li></div></div>

# Python

```python
def nextGreaterElements(self, nums: List[int]) -> List[int]:
    """
    利用循环数组技巧来模拟数组长度2倍的结果
    n~2n-1 就是2倍长度，在这个范围内找到下一个最大的值放到单调栈中
    0~n-1循环时，nums[n-1]就以单调栈中的数据找到下一个最大值
    因为res对应nums的下一个最大值，所以取值nums[i%n]和存储位置res[i%n]都是要%取模，来模拟长度2倍的效果
    """
    n = len(nums)
    res = [-1] * n
    stk = []
    for i in range(n * 2 - 1, -1, -1):
        while stk and nums[i % n] >= stk[-1]:
            stk.pop()
        res[i % n] = stk[-1] if stk else -1
        stk.append(nums[i % n])
    return res
```

# Go

```go
func nextGreaterElements(nums []int) []int {
   n := len(nums)
   res := make([]int, n)
   stk := []int{}
   for i := n*2 - 1; i >= 0; i-- {
      for len(stk) != 0 && nums[i%n] >= stk[len(stk)-1] {
         stk = stk[:len(stk)-1]
      }
      if len(stk) != 0 {
         res[i%n] = stk[len(stk)-1]
      } else {
         res[i%n] = -1
      }
      stk = append(stk, nums[i%n])
   }
   return res
}
```