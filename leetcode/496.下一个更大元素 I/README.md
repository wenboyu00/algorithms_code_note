# 题目

<p>给你两个<strong> 没有重复元素</strong> 的数组 <code>nums1</code> 和 <code>nums2</code> ，其中<code>nums1</code> 是 <code>nums2</code> 的子集。</p>

<p>请你找出 <code>nums1</code> 中每个元素在 <code>nums2</code> 中的下一个比其大的值。</p>

<p><code>nums1</code> 中数字 <code>x</code> 的下一个更大元素是指 <code>x</code> 在 <code>nums2</code> 中对应位置的右边的第一个比 <code>x</code><strong> </strong>大的元素。如果不存在，对应位置输出 <code>-1</code> 。</p>

<p> </p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> nums1 = [4,1,2], nums2 = [1,3,4,2].
<strong>输出:</strong> [-1,3,-1]
<strong>解释:</strong>
    对于 num1 中的数字 4 ，你无法在第二个数组中找到下一个更大的数字，因此输出 -1 。
    对于 num1 中的数字 1 ，第二个数组中数字1右边的下一个较大数字是 3 。
    对于 num1 中的数字 2 ，第二个数组中没有下一个更大的数字，因此输出 -1 。</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> nums1 = [2,4], nums2 = [1,2,3,4].
<strong>输出:</strong> [3,-1]
<strong>解释:</strong>
    对于 num1 中的数字 2 ，第二个数组中的下一个较大数字是 3 。
    对于 num1 中的数字 4 ，第二个数组中没有下一个更大的数字，因此输出 -1 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums1.length <= nums2.length <= 1000</code></li>
	<li><code>0 <= nums1[i], nums2[i] <= 10<sup>4</sup></code></li>
	<li><code>nums1</code>和<code>nums2</code>中所有整数 <strong>互不相同</strong></li>
	<li><code>nums1</code> 中的所有整数同样出现在 <code>nums2</code> 中</li>
</ul>

<p> </p>

<p><strong>进阶：</strong>你可以设计一个时间复杂度为 <code>O(nums1.length + nums2.length)</code> 的解决方案吗？</p>
<div><div>Related Topics</div><div><li>栈</li><li>数组</li><li>哈希表</li><li>单调栈</li></div></div>

# Python

```python
def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    """
    1. 找到nums2值的下一个最大值
        - map{num: 下一个最大值}关系， stack 单调栈
        - 倒叙循环nums2, 通过栈获得每个值的下个一个最大值，
        - 保存num和下一个最大值的关系
    2. 通过nums1值和map获得值的下一个最大值
    """
    # {num2的值：下一个最大的值}，用于nums1的值和nums2值对应
    res_map = {}
    # 单调栈
    stack = []
    # 最后向前遍历nums2
    for i in range(len(nums2) - 1, -1, -1):
        # 当前num2的值大于 栈顶的值 就弹出栈顶
        while stack and nums2[i] > nums2[stack[-1]]:
            stack.pop()
        # 如果栈为空，说没有下一个最大值
        if stack:
            res_map[nums2[i]] = nums2[stack[-1]]
        else:
            res_map[nums2[i]] = -1
        # 把当前值加入进去
        stack.append(i)
    # 遍历num1获得num的最大值
    res = []
    for num in nums1:
        res.append(res_map.get(num, -1))
    return res
```

# Go

```go
func nextGreaterElement(nums1 []int, nums2 []int) []int {
   numGreaterNumMap := map[int]int{}
   stack := []int{}
   for i := len(nums2) - 1; i >= 0; i-- {
      // 找出当前最大值
      for len(stack) != 0 && nums2[i] > nums2[stack[len(stack)-1]] {
         stack = stack[:len(stack)-1]
      }
      if len(stack) != 0 {
         numGreaterNumMap[nums2[i]] = nums2[stack[len(stack)-1]]
      } else {
         numGreaterNumMap[nums2[i]] = -1
      }
      stack = append(stack, i)

   }
   res := []int{}
   for _, num := range nums1 {
      res = append(res, numGreaterNumMap[num])
   }
   return res
}
```