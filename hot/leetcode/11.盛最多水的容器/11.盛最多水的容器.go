package main

func maxArea(height []int) int {
	left := 0
	right := len(height) - 1
	result := 0
	for left < right {
		var area int
		if height[left] < height[right] {
			area = height[left] * (right - left)
			left += 1
		} else {
			area = height[right] * (right - left)
			right -= 1
		}
		if result < area {
			result = area
		}
	}
	return result
}
