package main

import "fmt"

func checkInclusion(s1 string, s2 string) bool {
	need := map[int32]int{}
	window := map[int32]int{}
	for _, s := range s1 {
		need[s] += 1
		window[s] = 0
	}
	left := 0
	right := 0
	valid := 0
	for right < len(s2){
		c := int32(s2[right])
		right += 1
		if _, ok := need[c]; ok{
			window[c] +=1
			if window[c] == need[c]{
				valid += 1
			}
		}
		for right-left >= len(s1){
			if valid == len(need){
				return true
			}
			d := int32(s2[left])
			left += 1
			if _,ok := need[d];ok{
				if window[d] == need[d]{
					valid -= 1
				}
				window[d] -= 1
			}
		}
	}
	return false
}
func main() {
	s1 := "ab"
	s2 := "eidbaooo"
	result := checkInclusion(s1, s2)
	fmt.Println(result)
}
