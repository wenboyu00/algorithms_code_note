package main

func subarraySum(nums []int, k int) int {
	preSum := map[int]int{}
	preSum[0] = 1
	ans, sumI := 0, 0
	for _, num := range nums {
		sumI += num
		sumJ := sumI - k
		if _, ok := preSum[sumJ]; ok {
			ans += preSum[sumJ]
		}
		preSum[sumI] += 1
	}
	return ans
}

func main() {
	nums := []int{1, 2, 3}
	k := 3
	result := subarraySum(nums, k)
	println(result)
}
