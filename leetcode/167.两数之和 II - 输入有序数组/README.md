# 题目
<p>给定一个已按照<strong><em> </em>非递减顺序排列&nbsp; </strong>的整数数组&nbsp;<code>numbers</code> ，请你从数组中找出两个数满足相加之和等于目标数&nbsp;<code>target</code> 。</p>

<p>函数应该以长度为 <code>2</code> 的整数数组的形式返回这两个数的下标值<em>。</em><code>numbers</code> 的下标 <strong>从 1 开始计数</strong> ，所以答案数组应当满足 <code>1 &lt;= answer[0] &lt; answer[1] &lt;= numbers.length</code> 。</p>

<p>你可以假设每个输入 <strong>只对应唯一的答案</strong> ，而且你 <strong>不可以</strong> 重复使用相同的元素。</p>
&nbsp;

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>numbers = [2,7,11,15], target = 9
<strong>输出：</strong>[1,2]
<strong>解释：</strong>2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>numbers = [2,3,4], target = 6
<strong>输出：</strong>[1,3]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>numbers = [-1,0], target = -1
<strong>输出：</strong>[1,2]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= numbers.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-1000 &lt;= numbers[i] &lt;= 1000</code></li>
	<li><code>numbers</code> 按 <strong>非递减顺序</strong> 排列</li>
	<li><code>-1000 &lt;= target &lt;= 1000</code></li>
	<li><strong>仅存在一个有效答案</strong></li>
</ul>
<div><div>Related Topics</div><div><li>数组</li><li>双指针</li><li>二分查找</li></div></div>

# Python

```python
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    # 数组有序，使用双指针技巧，从数组两边开始，类似于二分查找
    left = 0
    right = len(numbers) - 1
    while left < right:
        num = numbers[left] + numbers[right]
        if num == target:
            # 题目要求的索引是从 1 开始的，所有+1
            return [left + 1, right + 1]
        # 让num大一些
        elif num < target:
            left += 1
        # 让num小一些
        else:
            right -= 1
    return [-1, -1]
```

# Go

```go
func twoSum(numbers []int, target int) []int {
   left := 0
   right := len(numbers) - 1

   for left < right {
      num := numbers[left] + numbers[right]
      if num == target {
         return []int{left + 1, right + 1}
      } else if num < target {
         left += 1
      } else {
         right -= 1
      }
   }
   return []int{-1, -1}
}
```