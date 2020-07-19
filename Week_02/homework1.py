# 前k个高频元素


def topKFrequent(nums, k):
    dict_c = {}
    # 遍历数组统计每种字符出现次数写入字典
    for n in nums:
        if n not in dict_c.keys():
            dict_c[n] = 0
        dict_c[n]+=1
    
    # 对字典按值排序
    sorted_d = sorted(dict_c.items(), key=lambda x:x[1], reverse=True)  
    outs = []
    
    # 对排序后字典输出前k个键值为结果
    for kk, v in sorted_d:
        outs.append(kk)
    return outs[:k]

if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    print(topKFrequent(nums, k))