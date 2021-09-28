# 题目
<p>设计一个支持 <code>push</code> ，<code>pop</code> ，<code>top</code> 操作，并能在常数时间内检索到最小元素的栈。</p>

<ul>
	<li><code>push(x)</code> &mdash;&mdash; 将元素 x 推入栈中。</li>
	<li><code>pop()</code>&nbsp;&mdash;&mdash; 删除栈顶的元素。</li>
	<li><code>top()</code>&nbsp;&mdash;&mdash; 获取栈顶元素。</li>
	<li><code>getMin()</code> &mdash;&mdash; 检索栈中的最小元素。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例:</strong></p>

<pre><strong>输入：</strong>
[&quot;MinStack&quot;,&quot;push&quot;,&quot;push&quot;,&quot;push&quot;,&quot;getMin&quot;,&quot;pop&quot;,&quot;top&quot;,&quot;getMin&quot;]
[[],[-2],[0],[-3],[],[],[],[]]

<strong>输出：</strong>
[null,null,null,null,-3,null,0,-2]

<strong>解释：</strong>
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --&gt; 返回 -3.
minStack.pop();
minStack.top();      --&gt; 返回 0.
minStack.getMin();   --&gt; 返回 -2.
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>pop</code>、<code>top</code> 和 <code>getMin</code> 操作总是在 <strong>非空栈</strong> 上调用。</li>
</ul>
<div><div>Related Topics</div><div><li>栈</li><li>设计</li></div></div>

# Python

```python
class MinStack:

    def __init__(self):
        self.stk = []
        # 最小值为栈顶，保持栈为降序，push和pop值后栈顶保持可以最小值
        self.min_stk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        # 新值 <= 栈顶值(最小值)，保持栈为降序
        if not self.min_stk or val <= self.min_stk[-1]:
            self.min_stk.append(val)

    def pop(self) -> None:
        val = self.stk.pop()
        # 如果值是最小值栈顶，也要pop出来，保持数据同步和降序要求
        if val == self.min_stk[-1]:
            self.min_stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min_stk[-1]
```

# Go

```go
type MinStack struct {
   stk    []int
   minStk []int
}

func Constructor() MinStack {
   return MinStack{stk: []int{},
      minStk: []int{}}
}

func (this *MinStack) Push(val int) {
   this.stk = append(this.stk, val)
   if len(this.minStk) == 0 || val <= this.minStk[len(this.minStk)-1] {
      this.minStk = append(this.minStk, val)
   }
}

func (this *MinStack) Pop() {
   val := this.stk[len(this.stk)-1]
   this.stk = this.stk[:len(this.stk)-1]
   if val == this.minStk[len(this.minStk)-1] {
      this.minStk = this.minStk[:len(this.minStk)-1]
   }
}

func (this *MinStack) Top() int {
   return this.stk[len(this.stk)-1]
}

func (this *MinStack) GetMin() int {
   return this.minStk[len(this.minStk)-1]
}
```