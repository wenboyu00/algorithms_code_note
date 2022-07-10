package main
/*
1.找到target-num[i]的值，返回index
2.通过mapping把时间复杂度从O(N)降到O(1)
 */
func twoSum(nums []int, target int) []int {
	// 初始化mapping，用于加快查找target-nums的值
	mapping := map[int]int{}
	for i,num := range nums {
		// 如果找到就返回，找不到就添加
		if p, ok := mapping[target-num]; ok{
			return []int{i,p}
		}else{
			mapping[num] = i
		}
	}
	return nil
}
