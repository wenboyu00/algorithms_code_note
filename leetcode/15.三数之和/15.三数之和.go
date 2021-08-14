package main

import (
	"fmt"
	"sort"
)

func threeSum(nums []int) [][]int {
	sort.Ints(nums)
	n := len(nums)
	ans := [][]int{}
	for i := 0; i < n; i++ {
		val := nums[i]
		if val > 0 {
			continue
		}
		if i > 0 && val == nums[i-1] {
			continue
		}
		l := i + 1
		r := n - 1
		for l < r {
			sum := val + nums[l] + nums[r]
			if sum == 0 {
				ans = append(ans, []int{val, nums[l], nums[r]})
				for l < r && nums[l] == nums[l+1] {
					l += 1
				}
				for l < r && nums[r] == nums[r-1] {
					r -= 1
				}
				l += 1
				r -= 1
			} else if sum > 0 {
				r -= 1
			} else if sum < 0 {
				l += 1

			}
		}
	}
	return ans
}
func main() {
	nums := []int{-1, 0, 1, 2, -1, -4}
	result := threeSum(nums)
	fmt.Println(result)
}
