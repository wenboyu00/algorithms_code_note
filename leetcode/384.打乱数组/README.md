# 题目

<p>给你一个整数数组 nums ，设计算法来打乱一个没有重复元素的数组。</p>

<p>实现 <code>Solution</code> class:</p>

<ul>
	<li><code>Solution(int[] nums)</code> 使用整数数组 <code>nums</code> 初始化对象</li>
	<li><code>int[] reset()</code> 重设数组到它的初始状态并返回</li>
	<li><code>int[] shuffle()</code> 返回数组随机打乱后的结果</li>
</ul>

<p> </p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入</strong>
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
<strong>输出</strong>
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

<strong>解释</strong>
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。例如，返回 [3, 1, 2]
solution.reset();      // 重设数组到它的初始状态 [1, 2, 3] 。返回 [1, 2, 3]
solution.shuffle();    // 随机返回数组 [1, 2, 3] 打乱后的结果。例如，返回 [1, 3, 2]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 200</code></li>
	<li><code>-10<sup>6</sup> <= nums[i] <= 10<sup>6</sup></code></li>
	<li><code>nums</code> 中的所有元素都是 <strong>唯一的</strong></li>
	<li>最多可以调用 <code>5 * 10<sup>4</sup></code> 次 <code>reset</code> 和 <code>shuffle</code></li>
</ul>
<div><div>Related Topics</div><div><li>数组</li><li>数学</li><li>随机化</li></div></div>

# Python

```python
class Solution:

    def __init__(self, nums: List[int]):
        self.ori = nums

    def reset(self) -> List[int]:
        return self.ori

    def shuffle(self) -> List[int]:
        """
        洗牌算法：随机选取元素进行交换来获取随机性，必须产生n!种可能
        关键：根据i~n长度来实现阶乘效果 rand = random.randrange(i, n)
            第一次：0~n-1, n 种可能
            第二次：1~n-1, n-1 种可能
            第三次：2~n-1, n-2 种可能
            最终完成n!种结果，满足条件实现洗牌算法
        """
        array = list(self.ori)
        n = len(array)
        for i in range(n):
            rand = random.randrange(i, n)
            array[i], array[rand] = array[rand], array[i]
        return array
```

# Go

```go
type Solution struct {
   ori []int
}

func Constructor(nums []int) Solution {
   return Solution{nums}
}

/** Resets the array to its original configuration and return it. */
func (this *Solution) Reset() []int {
   return this.ori
}

/** Returns a random shuffling of the array. */
func (this *Solution) Shuffle() []int {
   list := append([]int{}, this.ori...)
   n := len(list)
   for i := 0; i < n; i++ {
      randNum := rand.Intn(n-i) + i
      list[i], list[randNum] = list[randNum], list[i]
   }
   return list
}
```