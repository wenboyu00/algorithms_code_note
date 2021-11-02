package main

import (
	"math/rand"
)

// 快排解法
func findKthLargest2(nums []int, k int) int {
	n := len(nums)
	// 要求topk大，排序后是升序。
	// k在n-k位置，让index左边为前n-k个小的数，则index右边为前k个大的数
	findKth(nums, n-k, 0, n-1)
	return nums[n-k]
}
func findKth(nums []int, k int, left int, right int) {
	/*
	对比k和index的关系，递归调用
	*/
	index := partition(nums, left, right)
	if index < k {
		findKth(nums, k, index+1, right)

	} else if index > k {
		findKth(nums, k, left, index-1)
	} else {
		return
	}
}
func partition(nums []int, left int, right int) int {
	/*
	随机一个基准点base，把base的小的数放在base前面，大的放在后面。返回base最终的index
	*/
	// 随机一个base值，交换到头部，防止算法退化
	randomIndex := rand.Int() % (right - left + 1) + left
	nums[left], nums[randomIndex] = nums[randomIndex], nums[left]
	// 比base小在前，比base大在后
	base := nums[left]
	i := left
	j := right
	for i < j {
		//从后向前找，找到比base小的数，交换
		for i < j && nums[j] >= base {
			j--
		}
		nums[i] = nums[j]
		// 从前向后，找到比base大的数，交换
		for i < j && nums[i] <= base {
			i++
		}
		nums[j] = nums[i]
	}
	nums[i] = base
	return i
}

func main() {
	nums := []int{3, 2, 1, 5, 6, 4}
	k := 2
	println(findKthLargest2(nums, k))
}
