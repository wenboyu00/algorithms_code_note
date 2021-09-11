package main

import "math/rand"

type RandomizedSet struct {
	l         []int
	valIdxMap map[int]int
}

/** Initialize your data structure here. */
func Constructor() RandomizedSet {
	return RandomizedSet{
		l:         make([]int, 10),
		valIdxMap: make(map[int]int),
	}
}

/** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
func (this *RandomizedSet) Insert(val int) bool {
	if _, ok := this.valIdxMap[val]; ok {
		return false
	}
	this.valIdxMap[val] = len(this.l)
	this.l = append(this.l, val)
	return true
}

/** Removes a value from the set. Returns true if the set contained the specified element. */
func (this *RandomizedSet) Remove(val int) bool {
	if _, ok := this.valIdxMap[val]; !ok {
		return false
	}
	valIdx := this.valIdxMap[val]
	last := this.l[len(this.l)-1]
	this.l[valIdx] = last
	this.valIdxMap[last] = valIdx
	this.l = this.l[:len(this.l)-1]
	delete(this.valIdxMap, val)
	return true
}

/** Get a random element from the set. */
func (this *RandomizedSet) GetRandom() int {
	return this.l[rand.Int()%len(this.l)]
}

func main() {
	l := []int{1,2}
	num :=l[rand.Int()%len(l)]
	println(num)
	num =l[rand.Int()%len(l)]
	println(num)
	num =l[rand.Int()%len(l)]
	println(num)
	num =l[rand.Int()%len(l)]
	println(num)
	num =l[rand.Int()%len(l)]
	println(num)

}