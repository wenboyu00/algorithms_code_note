package hot

func singleNumbers(nums []int) []int {
	var xor int
	for _, num := range nums {
		xor ^= num
	}
	mask := 1
	for mask&xor == 0 {
		mask <<= 1
	}
	x := 0
	y := 0
	for _, num := range nums {
		if num&mask == 0 {
			x ^= num
		} else {
			y ^= num
		}
	}
	return []int{x, y}
}



func main() {
	nums := []int{1,2,10,4,1,4,3,3}
	println(singleNumbers(nums))
}