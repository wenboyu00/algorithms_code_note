package main

import "fmt"

type mQueue struct {
	q []int
}

func (mq *mQueue) push(num int) {
	for len(mq.q) != 0 && mq.q[len(mq.q)-1] < num {
		mq.q = mq.q[:len(mq.q)-1]
	}
	mq.q = append(mq.q, num)
}
func (mq *mQueue) max() int {
	return mq.q[0]
}
func (mq *mQueue) pop(num int) {
	if len(mq.q) != 0 && mq.q[0] == num {
		mq.q = mq.q[1:]
	}
}

func maxSlidingWindow(nums []int, k int) []int {
	n := len(nums)
	res := []int{}
	mQueue := mQueue{}
	for i := 0; i < n; i++ {
		// 初始化窗口,把k-1之前的输入入列.[0~k-1]
		if i < k-1 {
			mQueue.push(nums[i])
		} else {
			// 推进窗口，添加数值进来
			mQueue.push(nums[i])
			res = append(res, mQueue.max())
			// 推进窗口，删除旧数据
			mQueue.pop(nums[i+1-k])
		}
	}
	return res
}

func main() {
	nums := []int{1, 3, -1, -3, 5, 3, 6, 7}
	k := 3
	result := maxSlidingWindow(nums, k)
	fmt.Println(result)
}
