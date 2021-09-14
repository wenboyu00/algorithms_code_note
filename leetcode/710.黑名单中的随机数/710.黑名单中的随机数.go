package main

import "math/rand"

type Solution struct {
	mapping map[int]int
	n       int
}

func Constructor(n int, blacklist []int) Solution {
	mapping := map[int]int{}

	whiteLen := n - len(blacklist)
	// 在whiteLen中的黑名单数字
	inWhiteBlack := make([]int, 0)
	blacklistSet := make(map[int]int8, len(blacklist))
	for _, i := range blacklist {
		if i < whiteLen {
			inWhiteBlack = append(inWhiteBlack, i)
		}
		blacklistSet[i] = -1
	}
	// 在whiteLen之后的白名单数字
	NotInWhite := make([]int, 0)
	for i := whiteLen; i < n; i++ {
		if _, ok := blacklistSet[i]; !ok {
			NotInWhite = append(NotInWhite, i)
		}
	}
	// 把inWhiteBlack和NotInWhite映射上，数量是一致的
	iwbN := len(inWhiteBlack)
	for i := 0; i < iwbN; i++ {
		mapping[inWhiteBlack[i]] = NotInWhite[i]
	}
	return Solution{mapping, whiteLen}
}

func (this *Solution) Pick() int {
	index := rand.Int() % this.n - 1
	if _, ok := this.mapping[index]; ok {
		return this.mapping[index]
	}
	return index
}

func main() {
	N := 7
	blacklist := []int{2, 3, 5}
	//     # #      #
	// 0,1,2,3, | 4,5,6

	obj := Constructor(N, blacklist)
	println(obj.Pick())

}
