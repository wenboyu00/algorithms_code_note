package main

func maxProduct(nums []int) int {
	// 动态规划
	// 乘法正负特性，要维护dp最大值和dp最小值
	n := len(nums)
	maxVal := nums[0]
	maxDp := nums[0]
	minDp := nums[0]
	for i := 1; i < n; i++ {
		maxTemp := maxDp
		maxDp = max(max(maxDp*nums[i], nums[i]), minDp*nums[i])
		minDp = min(min(maxTemp*nums[i], nums[i]), minDp*nums[i])
		maxVal = max(maxVal, maxDp)
	}
	return maxVal
}
func max(int1 int, int2 int) int {
	if int1 < int2 {
		return int2
	} else {
		return int1
	}
}

func min(int1 int, int2 int) int {
	if int1 > int2 {
		return int2
	} else {
		return int1
	}
}

func main() {
	nums := []int{2, 3, -2, 4}
	println(maxProduct(nums))
}
