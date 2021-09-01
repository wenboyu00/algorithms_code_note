class FreqStack:
    """
    freq_vals 每个频率对应的元素，用于按照频率存取
    val_freq 每个元素对应的频率，用于调整val在freq对应列表的位置
    max_freq 最大频率值，找到最大频率的vals
    """
    def __init__(self):
        self.freq_vals_map = {}
        self.val_freq_map = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        """
        修改vf表
        更新fvs表
        更新max_freq
        """
        # 频率默认值为0，push一次+1， 更新val-freq
        freq = self.val_freq_map.get(val, 0) + 1
        self.val_freq_map[val] = freq
        # 如果freq对应list不存在就新建一个，存入数据
        if freq not in self.freq_vals_map:
            self.freq_vals_map[freq] = list()
        self.freq_vals_map[freq].append(val)
        # 更新最大频率
        if self.max_freq < freq:
            self.max_freq = freq

    def pop(self) -> int:
        # 在max_freq对应的列表中找到最后一个值，也就是最大频率最后push的值
        vals = self.freq_vals_map[self.max_freq]
        val = vals.pop()
        # 减少频率，并更新val-freq
        freq = self.val_freq_map[val] - 1
        self.val_freq_map[val] = freq
        # 如果列表为空，减少最大频率
        if len(vals) == 0:
            self.max_freq -= 1
            # 删不删 都可以
            del self.freq_vals_map[self.max_freq]
        return val
