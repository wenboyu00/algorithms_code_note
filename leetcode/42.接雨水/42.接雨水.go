package main

func trap(height []int) int {
	n := len(height)
	if n == 0 {
		return 0
	}
	// 初始化备忘录
	// 备忘录为 索引i的左、右最大高度
	lMax := make([]int, n)
	rMax := make([]int, n)
	// 初始化备忘录 base case
	lMax[0] = height[0]
	rMax[n-1] = height[n-1]
	// 从左到右，得到索引i的左最大高度
	for i := 1; i < n; i++ {
		lMax[i] = max(height[i], lMax[i-1])
	}
	// 从右到左，得到索引i的右最大高度
	for i := n - 2; i > -1; i-- {
		rMax[i] = max(height[i], rMax[i+1])
	}
	// 计算结果
	// 水的高度 = 左右高度最小值。水量 = 水高度 - 当前高度i
	// 最高累加 = 总水量
	res := 0
	for i, h := range height {
		res += min(lMax[i], rMax[i]) - h
	}
	return res
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	height := []int{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}
	println(trap(height))
}
