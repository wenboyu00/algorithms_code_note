package main

func removeElement(nums []int, val int) int {
	n := len(nums)
	if n == 0 {
		return 0
	}
	slow := 0
	for fast := 0; fast < n; fast++ {
		if nums[fast] != val {
			nums[slow] = nums[fast]
			slow += 1
		}
	}
	return slow
}
func main() {
	nums := []int{0, 1, 2, 2, 3, 0, 4, 2}
	val := 2
	result := removeElement(nums, val)
	println(result)
}
