package main

func rob(nums []int) int {
	n := len(nums)
	// base case 默认0
	dp := make([]int, n+2)
	for i := n - 1; i > -1; i-- {
		dp[i] = max(dp[i+1], nums[i]+dp[i+2])

	}
	return dp[0]
}

func max(int1 int, int2 int) int {
	if int1 < int2 {
		return int2
	} else {
		return int1
	}
}

func main() {
	nums := []int{1, 2, 3, 1}
	result := rob(nums)
	println(result)
}
