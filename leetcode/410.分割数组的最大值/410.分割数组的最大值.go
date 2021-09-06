package main

import "fmt"

func splitArray(nums []int, m int) int {
	left, right := getMaxSumNum(nums)
	for left <= right {
		mid := left + (right-left)/2
		// 切分数 > m，数组和太小，增加数组和，下次循环选择右半边
		if getSplitNum(nums, mid) > m {
			left = mid + 1
			// 切分数<m，数组和太大，减小数组和，下次循环选择左半边
			// 切分数==m,继续向左半边收敛，找到最小值
		} else {
			right = mid - 1
		}
	}
	return left
}

func getMaxSumNum(nums []int) (int, int) {
	maxVal := 0
	sumVal := 0
	for _, num := range nums {
		if maxVal < num {
			maxVal = num
		}
		sumVal += num
	}
	return maxVal, sumVal
}

func getSplitNum(nums []int, sumVal int) int {
	// 获得切分数，SumVal是每次数组和
	count := 1
	cur := 0
	for _, num := range nums {
		// 累计+当前 > 数组和，就开启一个新的数组
		if cur+num > sumVal {
			count += 1
			cur = 0
		}
		cur += num
	}
	return count
}

func main() {
	nums := []int{7, 2, 5, 10, 8}
	m := 2
	result := splitArray(nums, m)
	fmt.Println(result)
}
