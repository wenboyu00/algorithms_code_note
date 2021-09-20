package main

import (
	"fmt"
	"math/rand"
)

type Solution struct {
	ori []int
}

func Constructor(nums []int) Solution {
	return Solution{nums}
}

/** Resets the array to its original configuration and return it. */
func (this *Solution) Reset() []int {
	return this.ori
}

/** Returns a random shuffling of the array. */
func (this *Solution) Shuffle() []int {
	list := append([]int{}, this.ori...)
	n := len(list)
	for i := 0; i < n; i++ {
		randNum := rand.Intn(n-i) + i
		list[i], list[randNum] = list[randNum], list[i]
	}
	return list
}

func main() {
	nums := []int{1, 2, 3, 4, 5}
	obj := Constructor(nums)
	fmt.Println(obj.Shuffle())
	fmt.Println(obj.Reset())
	fmt.Println(obj.Shuffle())

}
