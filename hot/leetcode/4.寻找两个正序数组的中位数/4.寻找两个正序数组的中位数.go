package main

import "math"

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	/*
	   分割数组法
	   合并后数组的中位数左半边总数=nums1左半边个数+nums2左半边个数
	   通过nums1左半边个数，来确定nums2左半边个数
	       nums1的个数通过二分查找和nums2的关系来确定
	   当满足条件，nums1分割线左右元素相对nums2分割线左右元素有序:
	   	- nums1分割线左数l1小于nums2分割线右数r2 and nums2分割线左数l2小于nums1分割线右数r1
	       说明找到合并后中位数(分割线)位置
	   不满足条件时：通过二分法快速找到分割线

	   合并数组为偶数时 max(l1,l2) + min(r1,r2) 的二分之一
	       奇数时 max(l1,l2)
	*/
	len1 := len(nums1)
	len2 := len(nums2)
	lenAll := len1 + len2
	if len1 > len2 {
		return findMedianSortedArrays(nums2, nums1)
	}
	if len1 == 0 {
		return float64(nums2[(len2-1)/2.0]+nums2[len2/2.0]) / 2.0
	}
	left1 := 0
	right1 := len1
	for left1 <= right1 {
		// nums1和nums2的中位数
		cut1 := (left1 + right1) / 2
		cut2 := (lenAll+1)/2 - cut1
		// 得去分割线左右的值，以更新nums1分割线位置来，求助合并后中值的位置
		l1 := math.MinInt32
		if cut1 != 0 {
			l1 = nums1[cut1-1]
		}
		l2 := math.MinInt32
		if cut2 != 0 {
			l2 = nums2[cut2-1]
		}
		r1 := math.MaxInt32
		if cut1 != len1 {
			r1 = nums1[cut1]

		}
		r2 := math.MaxInt32
		if cut2 != len2 {
			r2 = nums2[cut2]
		}
		// cut1过大，缩小右边界
		if l1 > r2 {
			right1 = cut1 - 1
			// cut1过小，增大左边界
		} else if l2 > r1 {
			left1 = cut1 + 1
			// 满足条件
		} else {
			if lenAll%2 == 0 {
				// 先转换为float64然后再除以2才是float 否则是int
				return float64(max(l1, l2) + min(r1, r2)) / 2
			} else {
				return float64(max(l1, l2))
			}
		}
	}
	return -1
}
func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func main() {
	nums1 := []int{1, 2}
	nums2 := []int{3, 4}
	println(findMedianSortedArrays(nums1, nums2))

}
