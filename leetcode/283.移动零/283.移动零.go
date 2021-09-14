package main

func moveZeroes(nums []int) {
	n := len(nums)
	if n == 0 {
		return
	}
	slow := 0
	for fast := 0; fast < n; fast++ {
		if nums[fast] != 0 {
			nums[slow] = nums[fast]
			slow += 1
		}
	}
	for i := slow; i < n; i++ {
		nums[i] = 0
	}
}
