# 题目

<p> </p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入: </strong>nums = [1,1,1,2,2,3], k = 2
<strong>输出: </strong>[1,2]
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入: </strong>nums = [1], k = 1
<strong>输出: </strong>[1]</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 10<sup>5</sup></code></li>
	<li><code>k</code> 的取值范围是 <code>[1, 数组中不相同的元素的个数]</code></li>
	<li>题目数据保证答案唯一，换句话说，数组中前 <code>k</code> 个高频元素的集合是唯一的</li>
</ul>

<p> </p>

<p><strong>进阶：</strong>你所设计算法的时间复杂度 <strong>必须</strong> 优于 <code>O(n log n)</code> ，其中 <code>n</code><em> </em>是数组大小。</p>
<div><div>Related Topics</div><div><li>数组</li><li>哈希表</li><li>分治</li><li>桶排序</li><li>计数</li><li>快速选择</li><li>排序</li><li>堆（优先队列）</li></div></div>

# Python

```python
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # 统计每个元素出现的次数，num为key，count为value
    mapping = {}
    for num in nums:
        mapping[num] = mapping.get(num, 0) + 1

    # 桶排序
    # 以频率作为数组下标
    freq_list = [[] for _ in range(len(nums)+1)]
    for num, count in mapping.items():
        freq_list[count].append(num)
    #  倒序遍历数组，添加数组的值到结果集中。遍历到k是返回
    ans = []
    for i in range(len(nums), 0, -1):
        ans.extend(freq_list[i])
        if len(ans) == k:
            return ans
    return ans
```

# Go

```go
func topKFrequent(nums []int, k int) []int {
   mapping := map[int]int{}
   for _, num := range nums {
      mapping[num] += 1
   }
   freqList := make([][]int, len(nums)+1)
   for num, count := range mapping {
      freqList[count] = append(freqList[count], num)
   }
   ans := []int{}
   for i := len(nums); i > 0; i-- {
      ans = append(ans, freqList[i]...)
      if i == k {
         return ans
      }
   }
   return ans
}
```