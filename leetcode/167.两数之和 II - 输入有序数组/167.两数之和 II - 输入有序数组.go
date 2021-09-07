package main

func twoSum(numbers []int, target int) []int {
	left := 0
	right := len(numbers) - 1

	for left < right {
		num := numbers[left] + numbers[right]
		if num == target {
			return []int{left + 1, right + 1}
		} else if num < target {
			left += 1
		} else {
			right -= 1
		}
	}
	return []int{-1, -1}
}
