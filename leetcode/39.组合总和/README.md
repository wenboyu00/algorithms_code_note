# 题目
<p>给定一个<strong>无重复元素</strong>的正整数数组 <code>candidates</code> 和一个正整数 <code>target</code> ，找出 <code>candidates</code> 中所有可以使数字和为目标数 <code>target</code> 的唯一组合。</p>

<p><code>candidates</code> 中的数字可以无限制重复被选取。如果至少一个所选数字数量不同，则两种组合是唯一的。 </p>

<p>对于给定的输入，保证和为 <code>target</code> 的唯一组合数少于 <code>150</code> 个。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入: </strong>candidates = <code>[2,3,6,7], </code>target = <code>7</code>
<strong>输出: </strong>[[7],[2,2,3]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入: </strong>candidates = [2,3,5]<code>, </code>target = 8
<strong>输出: </strong>[[2,2,2,2],[2,3,3],[3,5]]</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入: </strong>candidates = <code>[2], </code>target = 1
<strong>输出: </strong>[]
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入: </strong>candidates = <code>[1], </code>target = <code>1</code>
<strong>输出: </strong>[[1]]
</pre>

<p><strong>示例 5：</strong></p>

<pre>
<strong>输入: </strong>candidates = <code>[1], </code>target = <code>2</code>
<strong>输出: </strong>[[1,1]]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= candidates.length <= 30</code></li>
	<li><code>1 <= candidates[i] <= 200</code></li>
	<li><code>candidate</code> 中的每个元素都是独一无二的。</li>
	<li><code>1 <= target <= 500</code></li>
</ul>
<div><div>Related Topics</div><div><li>数组</li><li>回溯</li></div></div>

# Python

```python
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    """
    组合-回溯
        - 可重复组合+多数求和
    可重复组合->用回溯算法
        - 避免重复->设置当前递归起始位置
    求和，逐次减值方式，=0时 就满足条件，<0 就超过条件
    剪枝，在进入递归之前发现 减去当前值<0 直接返回
    """
    result = []
    path = []

    def backtrack(target, start):
        # 满足条件
        if target == 0:
            result.append(list(path))
            return
        for i in range(start, len(candidates)):
            num = candidates[i]
            # 剪枝，<0 不满足需要
            if target - num < 0:
                return
            # 加入选择
            path.append(num)
            # 递归，减去当前值为目标值和从当前起点向后搜索
            backtrack(target - num, i)
            # 撤销选择
            path.pop()

    candidates = sorted(candidates)
    backtrack(target, 0)
    return result
```

# Go

```go
func combinationSum(candidates []int, target int) [][]int {
   // 回溯算法-组合，用startIndex来控制重复选择
   result := [][]int{}
   path := []int{}
   n := len(candidates)
   var backtrack func(target int, start int)
   backtrack = func(target int, start int) {
      // 满足条件
      if target == 0 {
         result = append(result, append([]int{}, path...))
         return
      }
      // 遍历选择
      for i := start; i < n; i++ {
         num := candidates[i]
         // 剪枝，超出范围
         if target-num < 0 {
            return
         }
         // 添加选择
         path = append(path, num)
         // 回溯（减去当前值=目标值，起始位置为当前位置->去掉重复)
         backtrack(target-num, i)
         // 撤销选择
         path = path[:len(path)-1]
      }
   }
   // 排序
   sort.Ints(candidates)
   backtrack(target, 0)
   return result
}
```