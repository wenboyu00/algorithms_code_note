package main

func search(nums []int, target int) int {
	n := len(nums)
	if n == 0 {
		return -1
	}
	left := 0
	right := n - 1
	for left <= right {
		mid := left + (right-left)/2
		if nums[mid] == target {
			return mid
		}
		if nums[left] <= nums[mid] {
			if nums[left] <= target && target < nums[mid] {
				right = mid - 1
			} else {
				left = mid + 1
			}
		} else {
			if nums[mid] < target && target <= nums[right] {
				left = mid + 1
			} else {
				right = mid - 1
			}
		}
	}
	return -1
}
func main() {
	nums := []int{4, 5, 6, 7, 0, 1, 2}
	target := 0
	println(search(nums, target))
}
