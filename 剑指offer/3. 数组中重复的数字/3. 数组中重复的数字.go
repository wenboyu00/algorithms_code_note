package main

func findRepeatNumber(nums []int) int {
	result := -1
	if len(nums) == 0{
		return 0
	}
	mapping := make(map[int]int, len(nums))
	for _, num := range nums{
		if _, ok := mapping[num]; ok{
			result = num
		}
		mapping[num] = num
	}
	return result
}

func main() {
		nums := []int{2, 3, 1, 0, 2, 5, 3}
		println(findRepeatNumber(nums))
}