package hot

func singleNumber(nums []int) int {
	ans := 0
	for i := 0; i < 32; i++ {
		bit := 0
		for _, num := range nums{
			bit += num>>i & 1
		}
		ans += bit%3 << i
	}
	return ans
}