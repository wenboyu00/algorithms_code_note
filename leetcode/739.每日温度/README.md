# 题目
<p>请根据每日 <code>气温</code> 列表 <code>temperatures</code> ，<span style="font-size:10.5pt"><span style="font-family:Calibri"><span style="font-size:10.5000pt"><span style="font-family:宋体"><font face="宋体">请计算在每一天需要等几天才会有更高的温度</font></span></span></span></span>。如果气温在这之后都不会升高，请在该位置用 <code>0</code> 来代替。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> <code>temperatures</code> = [73,74,75,71,69,72,76,73]
<strong>输出:</strong> [1,1,4,2,1,1,0,0]
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> temperatures = [30,40,50,60]
<strong>输出:</strong> [1,1,1,0]
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> temperatures = [30,60,90]
<strong>输出: </strong>[1,1,0]</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= temperatures.length <= 10<sup>5</sup></code></li>
	<li><code>30 <= temperatures[i] <= 100</code></li>
</ul>
<div><div>Related Topics</div><div><li>栈</li><li>数组</li><li>单调栈</li></div></div>

# Python

```python
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    """
    计算和下一个最大值之间的索引距离
    """
    n = len(temperatures)
    stack = []
    # 存放索引
    res = [0] * n
    # 单调栈，从尾到头
    for i in range(n - 1, -1, -1):
        while stack and temperatures[i] >= temperatures[stack[-1]]:
            stack.pop()
        # 得到索引间隙
        if stack:
            res[i] = stack[-1] - i
        else:
            res[i] = 0
        # 索引入栈
        stack.append(i)
    return res
```

# Go

```go
func dailyTemperatures(temperatures []int) []int {
   n := len(temperatures)
   stack := []int{}
   res := make([]int, len(temperatures))
   for i := n - 1; i >= 0; i-- {
      for len(stack) != 0 && temperatures[i] >= temperatures[stack[len(stack)-1]] {
         stack = stack[:len(stack)-1]
      }
      if len(stack) != 0 {
         res[i] = stack[len(stack)-1] - i
      }
      stack = append(stack, i)
   }
   return res
}
```