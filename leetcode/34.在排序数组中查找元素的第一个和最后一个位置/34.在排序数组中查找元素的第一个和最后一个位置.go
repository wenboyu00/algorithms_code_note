package main

import "fmt"

func searchRange(nums []int, target int) []int {
	leftIndex := leftBound(nums, target)
	rightIndex := rightBound(nums, target)
	return []int{leftIndex, rightIndex}
}
func leftBound(nums []int, target int) int {
	left := 0
	right := len(nums)
	for left <= right {
		mid := left + (right-left)/2
		if nums[mid] < target {
			left = mid + 1
		} else if nums[mid] > target {
			right = mid - 1
		} else if nums[mid] == target {
			right = mid - 1
		}
	}
	if left >= len(nums) || nums[left] != target {
		return -1
	}
	return left
}

func rightBound(nums []int, target int) int {
	left := 0
	right := len(nums)
	for left <= right {
		mid := left + (right-left)/2
		if nums[mid] > target {
			right = mid - 1
		} else if nums[mid] < target {
			left = mid + 1
		} else if nums[mid] == target {
			left = mid + 1
		}
	}
	if right < 0 || nums[right] != target {
		return -1
	}
	return right
}

func main() {
	nums := []int{5, 7, 7, 8, 8, 10}
	target := 8
	result := searchRange(nums, target)
	fmt.Println(result)
}
