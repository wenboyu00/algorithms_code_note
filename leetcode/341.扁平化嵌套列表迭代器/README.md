# 题目
<p>给你一个嵌套的整数列表 <code>nestedList</code> 。每个元素要么是一个整数，要么是一个列表；该列表的元素也可能是整数或者是其他列表。请你实现一个迭代器将其扁平化，使之能够遍历这个列表中的所有整数。</p>

<p>实现扁平迭代器类 <code>NestedIterator</code> ：</p>

<ul>
	<li><code>NestedIterator(List&lt;NestedInteger&gt; nestedList)</code> 用嵌套列表 <code>nestedList</code> 初始化迭代器。</li>
	<li><code>int next()</code> 返回嵌套列表的下一个整数。</li>
	<li><code>boolean hasNext()</code> 如果仍然存在待迭代的整数，返回 <code>true</code> ；否则，返回 <code>false</code> 。</li>
</ul>

<p>你的代码将会用下述伪代码检测：</p>

<pre>
initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res</pre>

<p>如果 <code>res</code> 与预期的扁平化列表匹配，那么你的代码将会被判为正确。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nestedList = [[1,1],2,[1,1]]
<strong>输出：</strong>[1,1,2,1,1]
<strong>解释：</strong>通过重复调用&nbsp;<em>next </em>直到&nbsp;<em>hasNex</em>t 返回 false，<em>next&nbsp;</em>返回的元素的顺序应该是: <code>[1,1,2,1,1]</code>。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nestedList = [1,[4,[6]]]
<strong>输出：</strong>[1,4,6]
<strong>解释：</strong>通过重复调用&nbsp;<em>next&nbsp;</em>直到&nbsp;<em>hasNex</em>t 返回 false，<em>next&nbsp;</em>返回的元素的顺序应该是: <code>[1,4,6]</code>。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nestedList.length &lt;= 500</code></li>
	<li>嵌套列表中的整数值在范围 <code>[-10<sup>6</sup>, 10<sup>6</sup>]</code> 内</li>
</ul>
<div><div>Related Topics</div><div><li>栈</li><li>树</li><li>深度优先搜索</li><li>设计</li><li>队列</li><li>迭代器</li></div></div>

# Python

```python
"""
__init__ : 用栈进行储存
hasNext : 完成列表节点的展开
    - 如果是integer直接返回true
    - 如果是列表，就写入栈
    - 为空时返回False
next : 返回栈顶数据

"""


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        # 从尾到头遍历
        for i in range(len(nestedList) - 1, -1, -1):
            self.stack.append(nestedList[i])

    def next(self) -> int:
        cur = self.stack.pop()
        return cur.getInteger()

    def hasNext(self) -> bool:
        while self.stack:
            cur = self.stack[-1]
            if cur.isInteger():
                return True
            self.stack.pop()
            for i in range(len(cur.getList()) - 1, -1, -1):
                self.stack.append(cur.getList[i])
        return False
```

# Go

```go
package main

type NestedIterator struct {
   Stack []*NestedInteger
}

func Constructor(nestedList []*NestedInteger) *NestedIterator {
   stack := []*NestedInteger{}
   for i := len(nestedList) - 1; i >= 0; i-- {
      stack = append(stack, nestedList[i])
   }
   return &NestedIterator{Stack: stack}
}

func (this *NestedIterator) Next() int {
   cur := this.Stack[len(this.Stack)-1]
   this.Stack = this.Stack[:len(this.Stack)-1]
   return cur.GetInteger()
}

func (this *NestedIterator) HasNext() bool {
   for len(this.Stack) > 0 {
      cur := this.Stack[len(this.Stack)-1]
      if cur.IsInteger() {
         return true
      }
      this.Stack = this.Stack[:len(this.Stack)-1]
      list := cur.GetList()
      for i := len(list) - 1; i >= 0; i-- {
         this.Stack = append(this.Stack, list[i])

      }
   }
   return false
}
```

