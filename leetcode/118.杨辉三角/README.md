# 题目

<p>给定一个非负整数&nbsp;<em>numRows，</em>生成杨辉三角的前&nbsp;<em>numRows&nbsp;</em>行。</p>

<p><img alt="" src="https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif"></p>

<p><small>在杨辉三角中，每个数是它左上方和右上方的数的和。</small></p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> 5
<strong>输出:</strong>
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]</pre>
# Python

```python
"""
杨辉三角对齐后
除了开头结尾是1的
其他都是上一层的当前位置值+当前位置-1
num = result[i-1][j]+result[i-1][j-1]

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            res = []
            for j in range(i + 1):
                # 在开头和结尾都是1
                if j == 0 or j == i:
                    res.append(1)
                else:
                    # 其他位置都是上一层，当前位置1和当前位置-1
                    pre = result[i - 1]     # 上一层
                    res.append(pre[j] + pre[j - 1])
            result.append(res)
        return result
```
