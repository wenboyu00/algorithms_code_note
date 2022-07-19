package main

func longestPalindrome(s string) string {
	n := len(s)
	res := ""
	for i := 0; i < n; i++ {
		s1 := palindrome(s, i, i)
		s2 := palindrome(s, i, i+1)
		res = maxLenStr(res, s1)
		res = maxLenStr(res, s2)
	}
	return res
}
func palindrome(s string, left int, right int) string {
	for left >= 0 && right < len(s) && s[left] == s[right] {
		left -= 1
		right += 1
	}
	return s[left+1 : right]
}
func maxLenStr(s1 string, s2 string) string {
	if len(s1) > len(s2) {
		return s1
	} else {
		return s2
	}
}

func main() {
	s := "babad"
	println(longestPalindrome(s))
}
