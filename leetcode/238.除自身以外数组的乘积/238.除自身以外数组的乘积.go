package main

func productExceptSelf(nums []int) []int {
	// 计算乘积时跳过 nums[1]
	// 前缀乘积*后缀乘积
	n := len(nums)
	res := make([]int, n)
	for i := 0; i < n; i++ {
		res[i] = 1
	}
	// 前缀乘积，下三角，跳过nums[0]
	for i := 1; i < n; i++ {
		res[i] = res[i-1] * nums[i-1]
	}
	// 后缀乘积，上三角，跳过nums[-1]
	tmp := 1
	for i := n - 2; i > -1; i-- {
		tmp *= nums[i+1]
		res[i] *= tmp
	}
	return res
}
