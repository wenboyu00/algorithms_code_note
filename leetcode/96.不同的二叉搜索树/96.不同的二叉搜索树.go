package main

func numTrees(n int) int {
	memo := [][]int{}
	for i := 0; i < n+1; i++ {
		memo = append(memo, make([]int, n+1))
	}
	var count func(low int, high int) int
	count = func(low int, high int) int {
		if low > high {
			return 1
		}
		if memo[low][high] != 0 {
			return memo[low][high]
		}
		res := 0
		for i := low; i <= high; i++ {
			left := count(low, i-1)
			right := count(i+1, high)
			res += left * right
		}
		memo[low][high] = res
		return res
	}
	return count(1, n)
}

func main() {
	result := numTrees(3)
	println(result)
}
