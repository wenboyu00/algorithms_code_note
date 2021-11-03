package main

import "fmt"

func topKFrequent(nums []int, k int) []int {
	mapping := map[int]int{}
	for _, num := range nums {
		mapping[num] += 1
	}
	freqList := make([][]int, len(nums)+1)
	for num, count := range mapping {
		freqList[count] = append(freqList[count], num)
	}
	ans := []int{}
	for i := len(nums); i > 0; i-- {
		ans = append(ans, freqList[i]...)
		if i == k {
			return ans
		}
	}
	return ans
}

func main() {
	nums := []int{1, 1, 1, 2, 2, 3}
	k := 2
	fmt.Println(topKFrequent(nums, k))
}
