# 题目
<p>你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： <code>'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'</code> 。每个拨轮可以自由旋转：例如把 <code>'9'</code> 变为 <code>'0'</code>，<code>'0'</code> 变为 <code>'9'</code> 。每次旋转都只能旋转一个拨轮的一位数字。</p>

<p>锁的初始数字为 <code>'0000'</code> ，一个代表四个拨轮的数字的字符串。</p>

<p>列表 <code>deadends</code> 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。</p>

<p>字符串 <code>target</code> 代表可以解锁的数字，你需要给出解锁需要的最小旋转次数，如果无论如何不能解锁，返回 <code>-1</code> 。</p>

<p> </p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入：</strong>deadends = ["0201","0101","0102","1212","2002"], target = "0202"
<strong>输出：</strong>6
<strong>解释：</strong>
可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，
因为当拨动到 "0102" 时这个锁就会被锁定。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> deadends = ["8888"], target = "0009"
<strong>输出：</strong>1
<strong>解释：</strong>
把最后一位反向旋转一次即可 "0000" -> "0009"。
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
<strong>输出：</strong>-1
<strong>解释：
</strong>无法旋转到目标数字且不被锁定。
</pre>

<p><strong>示例 4:</strong></p>

<pre>
<strong>输入:</strong> deadends = ["0000"], target = "8888"
<strong>输出：</strong>-1
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= deadends.length <= 500</code></li>
	<li><code><font face="monospace">deadends[i].length == 4</font></code></li>
	<li><code><font face="monospace">target.length == 4</font></code></li>
	<li><code>target</code> <strong>不在</strong> <code>deadends</code> 之中</li>
	<li><code>target</code> 和 <code>deadends[i]</code> 仅由若干位数字组成</li>
</ul>
# Python

```python
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = ["0000"]
        deadends_set = set(deadends)
        visited = {q[0]}
        step = 0

        while len(q) != 0:
            size = len(q)
            for i in range(size):
                cur = q.pop(0)
                if cur == target:
                    return step
                if cur in deadends_set:
                    continue
                for j in range(4):
                    up = self.plus_one(cur, j)
                    if up not in visited:
                        q.append(up)
                        visited.add(up)
                    down = self.minus_one(cur, j)
                    if down not in visited:
                        q.append(down)
                        visited.add(down)
            step += 1
        return -1

    def plus_one(self, s, j):
        ch = list(s)
        if ch[j] == "9":
            ch[j] = "0"
        else:
            ch[j] = str(int(ch[j]) + 1)
        return ''.join(ch)

    def minus_one(self, s, j):
        ch = list(s)
        if ch[j] == "0":
            ch[j] = "9"
        else:
            ch[j] = str(int(ch[j]) - 1)
        return ''.join(ch)
```

# Go

```Go
func openLock(deadends []string, target string) int {
   //初始化切片作为队列
   q := []string{}
   //初始化已访问集合用于去重
   visited := make(map[string]string)
   q = append(q, "0000")
   visited[q[0]] = q[0]
   // 初始化死亡数字集合用于实现快速查询
   deadendsSet := make(map[string]string)
   for _, v := range deadends {
      deadendsSet[v] = v
   }

   step := 0

   for len(q) != 0 {
      size := len(q)
      // 讲当前队列总的节点向四周扩散
      for i := 0; i < size; i++ {
         cur := q[0]
         q = q[1:]
         // 判断是否到终点
         if cur == target {
            return step
         }
         // 跳过无效数字集合
         if _, ok := deadendsSet[cur]; ok {
            continue
         }
         // 把相邻的节点加入队列
         for j := 0; j < 4; j++ {
            up := plusOne(cur, j)
            if _, ok := visited[up]; !ok {
               q = append(q, up)
               visited[up] = up
            }
            down := minusOne(cur, j)
            if _, ok := visited[down]; !ok {
               q = append(q, down)
               visited[down] = down
            }
         }
      }
      step += 1
   }
   return -1
}

func plusOne(s string, i int) string {
   //分割为字符串数组
   ch := strings.Split(s, "")
   if ch[i] == "9" {
      ch[i] = "0"
   } else {
      // 先转换为数字，然后+1再转回str
      num, _ := strconv.Atoi(ch[i])
      ch[i] = strconv.Itoa(num + 1)
   }
   //拼接回字符串
   return strings.Join(ch, "")
}

func minusOne(s string, i int) string {
   ch := strings.Split(s, "")
   if ch[i] == "0" {
      ch[i] = "9"
   } else {
      num, _ := strconv.Atoi(ch[i])
      ch[i] = strconv.Itoa(num - 1)
   }
   return strings.Join(ch, "")
}
```