package main

import "fmt"

func nextGreaterElement(nums1 []int, nums2 []int) []int {
	numGreaterNumMap := map[int]int{}
	stack := []int{}
	for i := len(nums2) - 1; i >= 0; i-- {
		// 找出当前最大值
		for len(stack) != 0 && nums2[i] > nums2[stack[len(stack)-1]] {
			stack = stack[:len(stack)-1]
		}
		if len(stack) != 0 {
			numGreaterNumMap[nums2[i]] = nums2[stack[len(stack)-1]]
		} else {
			numGreaterNumMap[nums2[i]] = -1
		}
		stack = append(stack, i)

	}
	res := []int{}
	for _, num := range nums1 {
		res = append(res, numGreaterNumMap[num])
	}
	return res
}
func main() {
	nums1 := []int{4, 1, 2}
	nums2 := []int{1, 3, 4, 2}
	result := nextGreaterElement(nums1, nums2)
	fmt.Println(result)
}
