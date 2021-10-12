package main

func sortColors(nums []int) {
	n := len(nums)
	p0, p2 := 0, n-1
	i := 0
	for i <= p2 {
		if nums[i] == 0 {
			nums[i], nums[p0] = nums[p0], nums[i]
			p0 += 1
			i += 1
		} else if nums[i] == 1 {
			i += 1
		//	nums[i] == 2
		} else {
			// 因为交换后nums[i]可能还是2，所以要进入下一轮循环，i保持不动
			nums[i], nums[p2] = nums[p2], nums[i]
			p2 -= 1
		}
	}

}
