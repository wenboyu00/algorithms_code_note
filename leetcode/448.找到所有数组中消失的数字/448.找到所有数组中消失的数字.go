package main

import "fmt"

func findDisappearedNumbers(nums []int) []int {
	n := len(nums)
	res := make([]int, 0, n)
	numsMap := make(map[int]int8, n)
	for _, num := range nums {
		numsMap[num] = 0
	}
	for i := 1; i < n+1; i++ {
		if _, ok := numsMap[i]; !ok {
			res = append(res, i)
		}
	}
	return res
}

func main() {
	nums := []int{4, 3, 2, 7, 8, 2, 3, 1}
	result := findDisappearedNumbers(nums)
	fmt.Println(result)
}
