# 题目
<p>实现<code>RandomizedSet</code> 类：</p>

<div class="original__bRMd">
<div>
<ul>
	<li><code>RandomizedSet()</code> 初始化 <code>RandomizedSet</code> 对象</li>
	<li><code>bool insert(int val)</code> 当元素 <code>val</code> 不存在时，向集合中插入该项，并返回 <code>true</code> ；否则，返回 <code>false</code> 。</li>
	<li><code>bool remove(int val)</code> 当元素 <code>val</code> 存在时，从集合中移除该项，并返回 <code>true</code> ；否则，返回 <code>false</code> 。</li>
	<li><code>int getRandom()</code> 随机返回现有集合中的一项（测试用例保证调用此方法时集合中至少存在一个元素）。每个元素应该有 <strong>相同的概率</strong> 被返回。</li>
</ul>

<p>你必须实现类的所有函数，并满足每个函数的 <strong>平均</strong> 时间复杂度为 <code>O(1)</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入</strong>
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
<strong>输出</strong>
[null, true, false, true, 2, true, false, 2]

<strong>解释</strong>
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // 向集合中插入 1 。返回 true 表示 1 被成功地插入。
randomizedSet.remove(2); // 返回 false ，表示集合中不存在 2 。
randomizedSet.insert(2); // 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
randomizedSet.getRandom(); // getRandom 应随机返回 1 或 2 。
randomizedSet.remove(1); // 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
randomizedSet.insert(2); // 2 已在集合中，所以返回 false 。
randomizedSet.getRandom(); // 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= val &lt;= 2<sup>31</sup> - 1</code></li>
	<li>最多调用 <code>insert</code>、<code>remove</code> 和 <code>getRandom</code> 函数 <code>2 *&nbsp;</code><code>10<sup>5</sup></code> 次</li>
	<li>在调用 <code>getRandom</code> 方法时，数据结构中 <strong>至少存在一个</strong> 元素。</li>
</ul>
</div>
</div>

<div><div>Related Topics</div><div><li>设计</li><li>数组</li><li>哈希表</li><li>数学</li><li>随机化</li></div></div>

# Python

```python
class RandomizedSet:
    """
    等概率在O(1)时间随机取出元素要满足：
    - 底层用数组
    - 数组必须是紧凑的

    数组存储如何满足O(1)插入和删除时间复杂度
    - 对数组尾部进行插入和删除，不涉及到数据搬运，就是O(1)
    - 在 O(1) 的时间删除数组中的某一个元素val，可以先把这个元素交换到数组的尾部，然后再pop掉
    - 交换两个元素必须通过索引进行交换，需要一个哈希表val_index_map来记录每个元素值对应的索引。
    """

    def __init__(self):
        self.l = []
        self.val_idx_map = {}

    def insert(self, val: int) -> bool:
        if val in self.val_idx_map:
            return False
        self.val_idx_map[val] = len(self.l)
        self.l.append(val)

    def remove(self, val: int) -> bool:
        if val in self.val_idx_map:
            val_idx = self.val_idx_map[val]
            last = self.l[-1]
            self.l[val_idx] = last
            self.val_idx_map[last] = val_idx
            self.l.pop()
            self.val_idx_map.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.l)
```

# Go

```go
import "math/rand"

type RandomizedSet struct {
   l         []int
   valIdxMap map[int]int
}

/** Initialize your data structure here. */
func Constructor() RandomizedSet {
   return RandomizedSet{
      l:         make([]int, 10),
      valIdxMap: make(map[int]int),
   }
}

/** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
func (this *RandomizedSet) Insert(val int) bool {
   if _, ok := this.valIdxMap[val]; ok {
      return false
   }
   this.valIdxMap[val] = len(this.l)
   this.l = append(this.l, val)
   return true
}

/** Removes a value from the set. Returns true if the set contained the specified element. */
func (this *RandomizedSet) Remove(val int) bool {
   if _, ok := this.valIdxMap[val]; !ok {
      return false
   }
   valIdx := this.valIdxMap[val]
   last := this.l[len(this.l)-1]
   this.l[valIdx] = last
   this.valIdxMap[last] = valIdx
   this.l = this.l[:len(this.l)-1]
   delete(this.valIdxMap, val)
   return true
}

/** Get a random element from the set. */
func (this *RandomizedSet) GetRandom() int {
   return this.l[rand.Int()%len(this.l)]
}
```