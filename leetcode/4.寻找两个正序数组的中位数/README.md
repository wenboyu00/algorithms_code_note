# 题目
<p>给定两个大小分别为 <code>m</code> 和 <code>n</code> 的正序（从小到大）数组&nbsp;<code>nums1</code> 和&nbsp;<code>nums2</code>。请你找出并返回这两个正序数组的 <strong>中位数</strong> 。</p>

<p>算法的时间复杂度应该为 <code>O(log (m+n))</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [1,3], nums2 = [2]
<strong>输出：</strong>2.00000
<strong>解释：</strong>合并数组 = [1,2,3] ，中位数 2
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [1,2], nums2 = [3,4]
<strong>输出：</strong>2.50000
<strong>解释：</strong>合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [0,0], nums2 = [0,0]
<strong>输出：</strong>0.00000
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [], nums2 = [1]
<strong>输出：</strong>1.00000
</pre>

<p><strong>示例 5：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [2], nums2 = []
<strong>输出：</strong>2.00000
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>nums1.length == m</code></li>
	<li><code>nums2.length == n</code></li>
	<li><code>0 &lt;= m &lt;= 1000</code></li>
	<li><code>0 &lt;= n &lt;= 1000</code></li>
	<li><code>1 &lt;= m + n &lt;= 2000</code></li>
	<li><code>-10<sup>6</sup> &lt;= nums1[i], nums2[i] &lt;= 10<sup>6</sup></code></li>
</ul>
<div><div>Related Topics</div><div><li>数组</li><li>二分查找</li><li>分治</li></div></div><br>

# Python

```python
def findMedianSortedArraysLogm(self, nums1: List[int], nums2: List[int]) -> float:
    """
    划分数组法
    合并后的数组中值左半边由nums1和nums2左半边贡献元素，找到num1分割的位置cut1，也就找到cut2，就可以确定中值的位置
    分割线的条件是：分割线左边<=右边
        - L1 <= R2
        - L2 <= R1
        - 因为是数组有序的，所以分割线左右的4个数字也是有序的。
    cut1是num1分割线位置，通过二分法求出
    cut2是num2分割线位置，等于(总元素个数+1的中值) - cut1
        - 总元素个数+1/2 是因为这样可以方便求助总元素个数为奇数时的中值
    比较l1和r2关系l2和r1关系来更新cut1位置
    满足条件时
        - 如果总元素为奇数，中值= l1和l2最大值
        - 如果总元素为偶数，中值= 左半边最大值+右半边最小值的二分之一
    """
    len_1, len_2 = len(nums1), len(nums2)
    if len_1 > len_2:
        return self.findMedianSortedArraysLogm(nums2, nums1)
    if len_1 == 0:
        return (nums2[(len_2 - 1) // 2] + nums2[len_2 // 2]) / 2
    len_all = len_1 + len_2
    # 只对nums1进行二叉查找
    left1, right1 = 0, len_1
    while left1 <= right1:
        # nums1分割线左边的个数(中值)，nums1中点位置
        cut1 = (left1 + right1) // 2
        # nums2分割线左边的个数(中值)，(总长度+1)/2中点位置 - cut1个数
        # len_all+1，如果总元素个数为奇数，直接返回分割线左边元素。所以左半边要比右半边多出一个
        cut2 = (len_all + 1) // 2 - cut1
        # 边界值判断，如果左半边超过边界值就等于 最小值
        l1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
        l2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
        # 如果右半边超过边界就等于 最大值
        r1 = float('inf') if cut1 == len_1 else nums1[cut1]
        r2 = float('inf') if cut2 == len_2 else nums2[cut2]
        # 二分法
        # l1>r2说明l1过大，需要缩小，新的右边界等于 cut1(中值) -1
        if l1 > r2:
            right1 = cut1 - 1
        # l2>r1说明r1过小，需要增大，新的左边界等于 cut1+1
        elif l2 > r1:
            left1 = cut1 + 1
        # 满足条件 l1<=r2 and l2<=r1，找到nums1切割线
        else:
            # 偶数情况 = 左半边的较大者和右半边的较小值相加/2
            if len_all % 2 == 0:
                return (max(l1, l2) + min(r1, r2)) / 2
            # 奇数情况 = 左半边的较大者
            else:
                return max(l1, l2)
    return -1
```



# Go

```go
func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
   /*
      分割数组法
      合并后数组的中位数左半边总数=nums1左半边个数+nums2左半边个数
      通过nums1左半边个数，来确定nums2左半边个数
          nums1的个数通过二分查找和nums2的关系来确定
      当满足条件，nums1分割线左右元素相对nums2分割线左右元素有序:
          - nums1分割线左数l1小于nums2分割线右数r2 and nums2分割线左数l2小于nums1分割线右数r1
          说明找到合并后中位数(分割线)位置
      不满足条件时：通过二分法快速找到分割线

      合并数组为偶数时 max(l1,l2) + min(r1,r2) 的二分之一
          奇数时 max(l1,l2)
   */
   len1 := len(nums1)
   len2 := len(nums2)
   lenAll := len1 + len2
   if len1 > len2 {
      return findMedianSortedArrays(nums2, nums1)
   }
   if len1 == 0 {
      return float64(nums2[(len2-1)/2.0]+nums2[len2/2.0]) / 2.0
   }
   left1 := 0
   right1 := len1
   for left1 <= right1 {
      // nums1和nums2的中位数
      cut1 := (left1 + right1) / 2
      cut2 := (lenAll+1)/2 - cut1
      // 得去分割线左右的值，以更新nums1分割线位置来，求助合并后中值的位置
      l1 := math.MinInt32
      if cut1 != 0 {
         l1 = nums1[cut1-1]
      }
      l2 := math.MinInt32
      if cut2 != 0 {
         l2 = nums2[cut2-1]
      }
      r1 := math.MaxInt32
      if cut1 != len1 {
         r1 = nums1[cut1]

      }
      r2 := math.MaxInt32
      if cut2 != len2 {
         r2 = nums2[cut2]
      }
      // cut1过大，缩小右边界
      if l1 > r2 {
         right1 = cut1 - 1
         // cut1过小，增大左边界
      } else if l2 > r1 {
         left1 = cut1 + 1
         // 满足条件
      } else {
         if lenAll%2 == 0 {
            // 先转换为float64然后再除以2才是float 否则是int
            return float64(max(l1, l2) + min(r1, r2)) / 2
         } else {
            return float64(max(l1, l2))
         }
      }
   }
   return -1
}
```