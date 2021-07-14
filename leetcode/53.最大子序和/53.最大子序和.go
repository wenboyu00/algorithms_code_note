package main

func maxSubArray(nums []int) int {
	ans := nums[0]
	count := ans
	for i := 1; i < len(nums); i++ {
		if count > 0 {
			count = count + nums[i]
		} else {
			count = nums[i]
		}
		if count > ans {
			ans = count
		}
	}
	return ans
}
