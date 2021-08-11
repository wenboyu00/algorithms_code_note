package main

func rob(nums []int) int {
	n := len(nums)
	if n == 1 {
		return nums[0]
	}
	return max(robRange(nums, 0, n-1), robRange(nums, 1, n))
}

func robRange(nums []int, start int, end int) int {
	n := len(nums)
	dp := make([]int, n+2)
	for i := end - 1; i > start-1; i-- {
		dp[i] = max(dp[i+1], nums[i]+dp[i+2])

	}
	return dp[start]
}
func max(int1 int, int2 int) int {
	if int1 < int2 {
		return int2
	} else {
		return int1
	}
}

func main() {
	nums := []int{2, 3, 2}
	result := rob(nums)
	println(result)
}
