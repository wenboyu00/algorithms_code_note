package main

type Trie struct {
	children [26]*Trie
	isEnd    bool
}

func Constructor() Trie {
	return Trie{}
}

func (this *Trie) Insert(word string) {
	node := this
	for _, ch := range word {
		ch -= 'a'
		if node.children[ch] == nil {
			node.children[ch] = &Trie{}
		}
		node = node.children[ch]
	}
	node.isEnd = true
}

func (this *Trie) Search(word string) bool {
	node := this.find(word)
	return node != nil && node.isEnd
}

func (this *Trie) StartsWith(prefix string) bool {
	return this.find(prefix) != nil
}

func (this *Trie) find(word string) *Trie {
	node := this
	for _, ch := range word {
		ch -= 'a'
		if node.children[ch] == nil{
			return nil
		}
		node = node.children[ch]
	}
	return node
}
