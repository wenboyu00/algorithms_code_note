package main

func findDuplicate(nums []int) int {
	/*
		快慢指针，通过nums[i]和i的映射把问题转换成判断环形链表入口问题
		因为有重复的数值，必然会出现多对一的情况，形成了环
	*/
	// 找到环
	slow := nums[0]
	fast := nums[nums[0]]
	for slow != fast {
		slow = nums[slow]
		fast = nums[nums[fast]]
	}
	// 找到环入口
	slow = 0
	for slow != fast {
		slow = nums[slow]
		fast = nums[fast]
	}
	return slow
}

func main() {
	println(findDuplicate([]int{1, 3, 4, 2, 2}))
}
