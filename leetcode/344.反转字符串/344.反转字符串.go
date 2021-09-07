package main

func reverseString(s []byte) {
	left := 0
	right := len(s) - 1
	for left < right {
		tmp := s[left]
		s[left] = s[right]
		s[right] = tmp
		left += 1
		right -= 1
	}
}
