package main

/*
range遍历是rune格式，unicode
*/
func replaceSpace(s string) string {
	result := ""
	for _, c := range s {
		if c == ' ' {
			result += "%20"
		} else {
			result += string(c)
		}
	}
	return result
}

func main() {
	s := "We are happy."
	println(replaceSpace(s))
}
