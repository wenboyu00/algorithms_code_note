package main

func canJump(nums []int) bool {
	n := len(nums)
	far := nums[0]
	for i := 0; i < n-1; i++ {
		if far < i+nums[i] {
			far = i + nums[i]
		}
		if far <= i {
			return false
		}
	}
	return far >= n-1
}
