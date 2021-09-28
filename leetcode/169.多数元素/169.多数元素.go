package main

func majorityElement(nums []int) int {
	halfLen := int(len(nums) / 2)
	numCount := make(map[int]int, halfLen+1)
	for _, num := range nums {
		numCount[num] += 1
		count := numCount[num]
		if count > halfLen {
			return num
		}
	}
	return -1
}
