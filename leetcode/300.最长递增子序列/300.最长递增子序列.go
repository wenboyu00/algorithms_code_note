package main

import "fmt"

func lengthOfLIS(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	dp := make([]int, len(nums))
	for i := range nums {
		dp[i] = 1
	}
	for i := 0; i < len(nums); i++ {
		for j := 0; j < i; j++ {
			if nums[j] < nums[i] {
				if dp[j]+1 > dp[i] {
					dp[i] = dp[j] + 1
				}
			}
		}

	}
	res := 0
	for i := 0; i < len(dp); i++ {
		if res < dp[i] {
			res = dp[i]
		}
	}
	return res
}
func main() {
	nums := []int{10, 9, 2, 5, 3, 7, 101, 18}
	result := lengthOfLIS(nums)
	fmt.Println(result)
}
