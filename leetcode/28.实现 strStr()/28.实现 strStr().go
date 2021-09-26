package main

func strStr(haystack string, needle string) int {
	n := len(needle)
	h := len(haystack)
	if n == 0 {
		return n
	}
	for i := 0; i < h; i++ {
		if haystack[i] == needle[0] {
			if i+n > h {
				return -1
			}
			if haystack[i:i+n] == needle {
				return i
			}
		}
	}
	return -1
}
func main() {
	s1 := "hello"
	s2 := "ll"
	println(strStr(s1, s2))
}
