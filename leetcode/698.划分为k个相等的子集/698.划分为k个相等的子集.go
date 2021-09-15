package main

func canPartitionKSubsets(nums []int, k int) bool {
	// 桶数超过数组长度
	n := len(nums)
	if k > n {
		return false
	}
	// 数组和 平均分 桶
	sum := 0
	for _, num := range nums {
		sum += num
	}
	if sum%k != 0 {
		return false
	}
	// 平均分桶后每桶的 总和
	target := sum / k

	// 值是否被使用
	used := make([]bool, n)
	for i := 0; i < n; i++ {
		used[i] = false
	}
	var backTrack func(bucketNum int, bucketSum int, start int) bool
	backTrack = func(bucketNum int, bucketSum int, start int) bool {
		// base case 回溯结束，所有桶都满了
		if bucketNum == 0 {
			return true
		}
		// 当前桶 已满，从头开始找下个桶
		if bucketSum == target {
			return backTrack(bucketNum-1, 0, 0)
		}
		// 遍历选择
		for i := start; i < n; i++ {
			// 是否已经被使用
			if used[i] {
				continue
			}
			// 是否装不下
			if nums[i]+bucketSum > target {
				continue
			}
			// 做选择
			used[i] = true
			bucketSum += nums[i]
			// 递归下一级, 前进一步
			res := backTrack(bucketNum, bucketSum, i+1)
			if res == true {
				return true
			}
			// 撤销选择
			used[i] = false
			bucketSum -= nums[i]
		}
		// 没有合适就返回false
		return false
	}

	return backTrack(k, 0, 0)
}

func main() {
	nums := []int{4, 3, 2, 3, 5, 2, 1}
	k := 4
	result := canPartitionKSubsets(nums, k)
	println(result)
}
