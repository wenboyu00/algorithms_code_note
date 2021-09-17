package main

func hammingWeight(num uint32) int {
	res := 0
	for num != 0 {
		num = num & (num - 1)
		res += 1
	}
	return res
}
func main() {
	n := 00000000000000000000000000001011
	result := hammingWeight(uint32(n))
	println(result)
}
