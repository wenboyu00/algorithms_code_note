package main

func longestConsecutive(nums []int) int {
	numsSet := map[int]bool{}
	ans := 0
	for _, num := range nums {
		numsSet[num] = true
	}
	for _, num := range nums {
		if !numsSet[num-1] {
			size := 0
			curNum := num
			for numsSet[curNum] {
				curNum += 1
				size += 1
			}
			if ans < size {
				ans = size
			}
		}
	}
	return ans
}

func main() {
	nums := []int{0, 3, 7, 2, 5, 8, 4, 6, 0, 1}
	println(longestConsecutive(nums))
}