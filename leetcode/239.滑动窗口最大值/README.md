# 题目
<p>给你一个整数数组 <code>nums</code>，有一个大小为 <code>k</code><em> </em>的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 <code>k</code> 个数字。滑动窗口每次只向右移动一位。</p>

<p>返回滑动窗口中的最大值。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [1,3,-1,-3,5,3,6,7], k = 3
<b>输出：</b>[3,3,5,5,6,7]
<b>解释：</b>
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       <strong>3</strong>
 1 [3  -1  -3] 5  3  6  7       <strong>3</strong>
 1  3 [-1  -3  5] 3  6  7      <strong> 5</strong>
 1  3  -1 [-3  5  3] 6  7       <strong>5</strong>
 1  3  -1  -3 [5  3  6] 7       <strong>6</strong>
 1  3  -1  -3  5 [3  6  7]      <strong>7</strong>
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [1], k = 1
<b>输出：</b>[1]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [1,-1], k = 1
<b>输出：</b>[1,-1]
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<b>输入：</b>nums = [9,11], k = 2
<b>输出：</b>[11]
</pre>

<p><strong>示例 5：</strong></p>

<pre>
<b>输入：</b>nums = [4,-2], k = 2
<b>输出：</b>[4]</pre>

<p> </p>

<p><b>提示：</b></p>

<ul>
	<li><code>1 <= nums.length <= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code></li>
	<li><code>1 <= k <= nums.length</code></li>
</ul>
<div><div>Related Topics</div><div><li>队列</li><li>数组</li><li>滑动窗口</li><li>单调队列</li><li>堆（优先队列）</li></div></div>

# Python

```python
class MQuque:
    def __init__(self):
        self.queue = deque()

    def push(self, num):
        while self.queue and self.queue[-1] < num:
            self.queue.pop()
        self.queue.append(num)

    def max(self):
        return self.queue[0]

    def pop(self, num):
        if num == self.queue[0]:
            self.queue.popleft()


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = MQuque()
        res = []

        for i in range(len(nums)):
            # 先填窗口的前 k -1
            if i < (k - 1):
                window.push(nums[i])
            else:
                # 窗口向前滑动，加入新数字
                window.push(nums[i])
                res.append(window.max())
                # 窗口向前滑动，移除旧数字
                # i是0~n， k是1~k, i+1 才能对上k的index
                window.pop(nums[i + 1 - k])
        return res
```

# Go

```Go
type mQueue struct {
   q []int
}

func (mq *mQueue) push(num int) {
   for len(mq.q) != 0 && mq.q[len(mq.q)-1] < num {
      mq.q = mq.q[:len(mq.q)-1]
   }
   mq.q = append(mq.q, num)
}
func (mq *mQueue) max() int {
   return mq.q[0]
}
func (mq *mQueue) pop(num int) {
   if len(mq.q) != 0 && mq.q[0] == num {
      mq.q = mq.q[1:]
   }
}

func maxSlidingWindow(nums []int, k int) []int {
   n := len(nums)
   res := []int{}
   mQueue := mQueue{}
   for i := 0; i < n; i++ {
      // 初始化窗口,把k-1之前的输入入列.[0~k-1]
      if i < k-1 {
         mQueue.push(nums[i])
      } else {
         // 推进窗口，添加数值进来
         mQueue.push(nums[i])
         res = append(res, mQueue.max())
         // 推进窗口，删除旧数据
         mQueue.pop(nums[i+1-k])
      }
   }
   return res
}
```

