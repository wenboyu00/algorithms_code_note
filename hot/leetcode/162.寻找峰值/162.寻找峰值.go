package hot

// 对比nums[mid]和nums[mid+1]关系
// 大于,峰值在[l,mid] 因为mid更大所以保留
// 小于,峰值在[mid+1,r]
func findPeakElement(nums []int) int {
	left := 0
	right := len(nums) - 1
	for left < right {
		mid := left + (right-left)/2
		if nums[mid] > nums[mid+1] {
			right = mid
		} else {
			left = mid + 1
		}
	}
	return left
}
