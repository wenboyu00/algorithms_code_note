package main

import "fmt"

func minEatingSpeed(piles []int, h int) int {
	maxVal := 0
	for _, pile := range piles {
		if maxVal < pile {
			maxVal = pile
		}
	}
	left := 1
	right := maxVal
	for left <= right {
		mid := left + (right-left)/2
		midHour := findHour(piles, mid)
		// 耗时太多，速度太慢，加速
		if midHour > h {
			left = mid + 1
			// 耗时太少，速度太慢，减速
		} else {
			right = mid - 1
		}
	}
	return left
}

func findHour(piles []int, speed int) int {
	hour := 0
	for _, pile := range piles {
		hour += pile / speed
		fmt.Println(hour)
		if pile%speed > 0 {
			hour += 1
		}
	}
	return hour
}

func main() {
	piles := []int{3, 6, 7, 11}
	H := 8
	result := minEatingSpeed(piles, H)
	fmt.Println(result)
}
