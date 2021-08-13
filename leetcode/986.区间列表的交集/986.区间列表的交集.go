package main

import "fmt"

func intervalIntersection(a [][]int, b [][]int) [][]int {
	i := 0
	j := 0
	res := [][]int{}
	for i < len(a) && j < len(b) {
		a1 := a[i][0]
		a2 := a[i][1]
		b1 := b[j][0]
		b2 := b[j][1]
		if b2 >= a1 && a2 >= b1 {
			res = append(res, []int{max(a1, b1), min(a2, b2)})
		}
		if b2 < a2 {
			j += 1
		} else {
			i += 1
		}
	}
	return res

}

func max(int1 int, int2 int) int {
	if int1 < int2 {
		return int2
	} else {
		return int1
	}
}

func min(int1 int, int2 int) int {
	if int1 > int2 {
		return int2
	} else {
		return int1
	}
}
func main() {
	firstList := [][]int{{0, 2}, {5, 10}, {13, 23}, {24, 25}}
	secondList := [][]int{{1, 5}, {8, 12}, {15, 24}, {25, 26}}
	result := intervalIntersection(firstList, secondList)
	fmt.Println(result)
}
