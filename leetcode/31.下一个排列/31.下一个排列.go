package main

func nextPermutation(nums []int) {
	n := len(nums)
	// 从后向前，跳过最后一个，找到第一个 小数
	i := n - 2
	for i >= 0 && nums[i] >= nums[i+1] {
		i -= 1
	}
	// 再从后向前，找到 比小数大的数
	j := n - 1
	if i >= 0 {
		for j > i && nums[i] >= nums[j] {
			j -= 1
		}
		// 进行交换
		swap(nums, i, j)
	}
	// 对交换后的位置到尾部进行反正，减少增加的值(因为原来的逆序变升序，值变小了)
	reverse(nums, i+1, n-1)
}

func swap(nums []int, i int, j int) {
	tmp := nums[i]
	nums[i] = nums[j]
	nums[j] = tmp
}

func reverse(nums []int, i int, j int) {
	for i < j {
		swap(nums, i, j)
		i += 1
		j -= 1
	}
}
