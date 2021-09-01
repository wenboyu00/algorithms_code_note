# 题目

<p>实现 <code>FreqStack</code>，模拟类似栈的数据结构的操作的一个类。</p>

<p><code>FreqStack</code>&nbsp;有两个函数：</p>

<ul>
	<li><code>push(int x)</code>，将整数&nbsp;<code>x</code>&nbsp;推入栈中。</li>
	<li><code>pop()</code>，它<strong>移除</strong>并返回栈中出现最频繁的元素。
	<ul>
		<li>如果最频繁的元素不只一个，则移除并返回最接近栈顶的元素。</li>
	</ul>
	</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>
[&quot;FreqStack&quot;,&quot;push&quot;,&quot;push&quot;,&quot;push&quot;,&quot;push&quot;,&quot;push&quot;,&quot;push&quot;,&quot;pop&quot;,&quot;pop&quot;,&quot;pop&quot;,&quot;pop&quot;],
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
<strong>输出：</strong>[null,null,null,null,null,null,null,5,7,5,4]
<strong>解释：</strong>
执行六次 .push 操作后，栈自底向上为 [5,7,5,7,4,5]。然后：

pop() -&gt; 返回 5，因为 5 是出现频率最高的。
栈变成 [5,7,5,7,4]。

pop() -&gt; 返回 7，因为 5 和 7 都是频率最高的，但 7 最接近栈顶。
栈变成 [5,7,5,4]。

pop() -&gt; 返回 5 。
栈变成 [5,7,4]。

pop() -&gt; 返回 4 。
栈变成 [5,7]。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>对&nbsp;<code>FreqStack.push(int x)</code>&nbsp;的调用中&nbsp;<code>0 &lt;= x &lt;= 10^9</code>。</li>
	<li>如果栈的元素数目为零，则保证不会调用&nbsp; <code>FreqStack.pop()</code>。</li>
	<li>单个测试样例中，对&nbsp;<code>FreqStack.push</code>&nbsp;的总调用次数不会超过&nbsp;<code>10000</code>。</li>
	<li>单个测试样例中，对&nbsp;<code>FreqStack.pop</code>&nbsp;的总调用次数不会超过&nbsp;<code>10000</code>。</li>
	<li>所有测试样例中，对&nbsp;<code>FreqStack.push</code>&nbsp;和 <code>FreqStack.pop</code>&nbsp;的总调用次数不会超过&nbsp;<code>150000</code>。</li>
</ul>
<p>&nbsp;</p>
<div><div>Related Topics</div><div><li>栈</li><li>设计</li><li>哈希表</li><li>有序集合</li></div></div>

# Python

```python
class FreqStack:
    """
    freq_vals 每个频率对应的元素，用于按照频率存取
    val_freq 每个元素对应的频率，用于调整val在freq对应列表的位置
    max_freq 最大频率值，找到最大频率的vals
    """
    def __init__(self):
        self.freq_vals_map = {}
        self.val_freq_map = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        """
        修改vf表
        更新fvs表
        更新max_freq
        """
        # 频率默认值为0，push一次+1， 更新val-freq
        freq = self.val_freq_map.get(val, 0) + 1
        self.val_freq_map[val] = freq
        # 如果freq对应list不存在就新建一个，存入数据
        if freq not in self.freq_vals_map:
            self.freq_vals_map[freq] = list()
        self.freq_vals_map[freq].append(val)
        # 更新最大频率
        if self.max_freq < freq:
            self.max_freq = freq

    def pop(self) -> int:
        # 在max_freq对应的列表中找到最后一个值，也就是最大频率最后push的值
        vals = self.freq_vals_map[self.max_freq]
        val = vals.pop()
        # 减少频率，并更新val-freq
        freq = self.val_freq_map[val] - 1
        self.val_freq_map[val] = freq
        # 如果列表为空，减少最大频率
        if len(vals) == 0:
            self.max_freq -= 1
            # 删不删 都可以
            del self.freq_vals_map[self.max_freq]
        return val
```

# Go

```go
package main

type FreqStack struct {
   maxFreq  int
   FreqVals map[int][]int
   valFreq  map[int]int
}

func Constructor() FreqStack {
   return FreqStack{maxFreq: 0,
      FreqVals: make(map[int][]int),
      valFreq:  make(map[int]int),
   }
}

func (this *FreqStack) Push(val int) {
   //     更新val的freq值，并更新valFreqMap
   freq := this.valFreq[val] + 1
   this.valFreq[val] = freq
   //  更新val在freqVals列表中的位置
   if _, ok := this.FreqVals[freq]; !ok {
      this.FreqVals[freq] = []int{}
   }
   this.FreqVals[freq] = append(this.FreqVals[freq], val)
   //     更新maxFreq
   if this.maxFreq < freq {
      this.maxFreq = freq
   }
}

func (this *FreqStack) Pop() int {
   // 找出最大freq最后一个值，并更新列表
   vals := this.FreqVals[this.maxFreq]
   valsLen := len(vals)
   val := vals[valsLen-1]
   vals = vals[:valsLen-1]
   // 更新freq对应vals
   this.FreqVals[this.maxFreq] = vals
   // 更新值的valFreq
   freq := this.valFreq[val] - 1
   this.valFreq[val] = freq
   // 更新maxFreq，如果列表为空
   if len(vals) == 0 {
      this.maxFreq -= 1
   }
   return val
}
```