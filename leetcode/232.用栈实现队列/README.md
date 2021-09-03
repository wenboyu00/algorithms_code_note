# 题目

<p>请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（<code>push</code>、<code>pop</code>、<code>peek</code>、<code>empty</code>）：</p>

<p>实现 <code>MyQueue</code> 类：</p>

<ul>
	<li><code>void push(int x)</code> 将元素 x 推到队列的末尾</li>
	<li><code>int pop()</code> 从队列的开头移除并返回元素</li>
	<li><code>int peek()</code> 返回队列开头的元素</li>
	<li><code>boolean empty()</code> 如果队列为空，返回 <code>true</code> ；否则，返回 <code>false</code></li>
</ul>

<p> </p>

<p><strong>说明：</strong></p>

<ul>
	<li>你只能使用标准的栈操作 —— 也就是只有 <code>push to top</code>, <code>peek/pop from top</code>, <code>size</code>, 和 <code>is empty</code> 操作是合法的。</li>
	<li>你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。</li>
</ul>

<p> </p>

<p><strong>进阶：</strong></p>

<ul>
	<li>你能否实现每个操作均摊时间复杂度为 <code>O(1)</code> 的队列？换句话说，执行 <code>n</code> 个操作的总时间复杂度为 <code>O(n)</code> ，即使其中一个操作可能花费较长时间。</li>
</ul>

<p> </p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
<strong>输出：</strong>
[null, null, null, 1, 1, false]

<strong>解释：</strong>
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
</pre>

<ul>
</ul>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= x <= 9</code></li>
	<li>最多调用 <code>100</code> 次 <code>push</code>、<code>pop</code>、<code>peek</code> 和 <code>empty</code></li>
	<li>假设所有操作都是有效的 （例如，一个空的队列不会调用 <code>pop</code> 或者 <code>peek</code> 操作）</li>
</ul>
<div><div>Related Topics</div><div><li>栈</li><li>设计</li><li>队列</li></div></div>

# Python

```python
class MyQueue:
    """
    用两个栈实现一个队列
    栈1，压入1，2，3，弹出是3，2，1
    栈2，压入3，2，1，弹出是1，2，3
    这样完成队列的先进先出
    """
    def __init__(self):
        self.s1 = []
        self.s2 = []

    # 添加到队尾
    def push(self, x: int) -> None:
        self.s1.append(x)

    # 删除队头并返回
    def pop(self) -> int:
        self.peek()
        return self.s2.pop()

    def peek(self) -> int:
        """
        返回头元素
        如果s2为空，就从s1中压入数据
        返回s2最后一个元素
        """
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        """
        判断队列是否为空
        如果两个栈都为空时，为空
        """
        return not self.s1 and not self.s2
```

# Go

```go
type MyQueue struct {
   s1, s2 []int
}

/** 初始化数据结构，2个栈来实现队列. */
func Constructor() MyQueue {
   return MyQueue{s1: []int{}, s2: []int{}}
}

func (this *MyQueue) Push(x int) {
   this.s1 = append(this.s1, x)
}

func (this *MyQueue) Pop() int {
   this.Peek()
   n := len(this.s2)
   s2Last := this.s2[n-1]
   this.s2 = this.s2[:n-1]
   return s2Last
}

func (this *MyQueue) Peek() int {
   if len(this.s2) == 0 {
      for len(this.s1) != 0 {
         n := len(this.s1)
         s1Last := this.s1[n-1]
         this.s1 = this.s1[:n-1]
         this.s2 = append(this.s2, s1Last)
      }
   }
   return this.s2[len(this.s2)-1]
}

func (this *MyQueue) Empty() bool {
   return len(this.s1) == 0 && len(this.s2) == 0
}
```