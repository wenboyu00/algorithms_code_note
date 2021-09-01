package main

type FreqStack struct {
	maxFreq  int
	FreqVals map[int][]int
	valFreq  map[int]int
}

func Constructor() FreqStack {
	return FreqStack{maxFreq: 0,
		FreqVals: make(map[int][]int),
		valFreq:  make(map[int]int),
	}
}

func (this *FreqStack) Push(val int) {
	// 	更新val的freq值，并更新valFreqMap
	freq := this.valFreq[val] + 1
	this.valFreq[val] = freq
	//  更新val在freqVals列表中的位置
	if _, ok := this.FreqVals[freq]; !ok {
		this.FreqVals[freq] = []int{}
	}
	this.FreqVals[freq] = append(this.FreqVals[freq], val)
	// 	更新maxFreq
	if this.maxFreq < freq {
		this.maxFreq = freq
	}
}

func (this *FreqStack) Pop() int {
	// 找出最大freq最后一个值，并更新列表
	vals := this.FreqVals[this.maxFreq]
	valsLen := len(vals)
	val := vals[valsLen-1]
	vals = vals[:valsLen-1]
	// 更新freq对应vals
	this.FreqVals[this.maxFreq] = vals
	// 更新值的valFreq
	freq := this.valFreq[val] - 1
	this.valFreq[val] = freq
	// 更新maxFreq，如果列表为空
	if len(vals) == 0 {
		this.maxFreq -= 1
	}
	return val
}
