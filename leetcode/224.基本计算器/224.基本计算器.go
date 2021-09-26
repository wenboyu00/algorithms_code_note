package main

func calculate(s string) int {
	res, s := do(s)
	return res
}

func do(s string) (int,string) {
	stk := []int{}
	num := 0
	sign := '+'
	for len(s) > 0 {
		ch := s[0]
		s = s[1:]
		isDigit := '0' <= ch && ch <= '9'
		if isDigit {
			num = 10*num + int(ch-'0')
		}
		if ch == '(' {
			num, s = do(s)
		}
		if (!isDigit && ch != ' ') || len(s) == 0 {
			if sign == '+' {
				stk = append(stk, num)
			} else if sign == '-' {
				stk = append(stk, -num)
			} else if sign == '*' {
				stk[len(stk)-1] *= num
			} else if sign == '/' {
				stk[len(stk)-1] /= num
			}
			num = 0
			sign = rune(ch)
		}
		if ch == ')' {
			return sum(stk),s
		}

	}
	return sum(stk),s
}
func sum(list []int) (count int) {
	for _, value := range list {
		count += value
	}
	return count
}

func main() {
	println(calculate("3+2*2"))
	println(calculate("1 + 1"))
	println(calculate(" 2-1 + 2 "))
	println(calculate("(1+(4+5+2)-3)+(6+8)"))
}
