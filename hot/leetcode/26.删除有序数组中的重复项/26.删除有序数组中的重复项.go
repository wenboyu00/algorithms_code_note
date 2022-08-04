package main

import "fmt"

func removeDuplicates(nums []int) int {
	/*
	快慢指针
	nums[slow] == nums[fast]表示重复元素(跳过)，fast前进
	不相等时，slow前进一步，并赋值元素为fast元素
	这样 0 ~ slow 就为不重复元素
	返回元素数量为 slow + 1
	*/
	n := len(nums)
	if n == 0 {
		return 0
	}
	slow := 0
	for fast := 0; fast < n; fast++ {
		if nums[slow] != nums[fast] {
			slow += 1
			nums[slow] = nums[fast]
		}
	}
	// 返回数量，slow + 1
	return slow + 1
}

func main() {
	nums := []int{0, 0, 1, 1, 1, 2, 2, 3, 3, 4}
	result := removeDuplicates(nums)
	fmt.Println(result)
}
