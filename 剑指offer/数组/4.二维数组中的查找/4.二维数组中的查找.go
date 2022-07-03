
/*
行和列都是单调递增
x,y就相当于2个指针
从右上角开始
    - 如果从左上角开始,无法排除当前所在的行和列
遇到大于的值，就 x-=1
遇到小于的值，就 y+=1
*/

func findNumberIn2DArray(matrix [][]int, target int) bool {
    m := len(matrix)
    if m == 0{
        return false
    }
    n := len(matrix[0])
    if n == 0{
        return false
    }
    x := n - 1
    y := 0
    for y < m && x > -1{
        if matrix[y][x] < target{
            y += 1
        }else if matrix[y][x] > target{
            x -= 1
        }else{
            return true
        }
    }
    return false
}