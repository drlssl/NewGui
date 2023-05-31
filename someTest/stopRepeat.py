# target :return the first repeat index

raw_array = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3]


def stopRepeat(raw_array):
    index = 0
    index_list = [0]
    for i in range(len(raw_array)):
        comparision = raw_array[index]
        if raw_array[i] == comparision:
            i += 1
        else:
            index = i
            index_list.append(index)
            i += 1
    return index_list

def find_unique_index(sequence):
    unique_values = set(sequence)  # 获取序列中的唯一值
    index_list = {}  # 存储不同值的索引字典

    for value in unique_values:
        index_list[value] = [i for i, x in enumerate(sequence) if x == value]

    return index_list

# 测试示例序列
sequence = [1, 2, 3, 1, 2, 4, 2, 2, 3, 4, 4, 2, 5]
unique_index_dir = find_unique_index(sequence)

# 打印结果
for value, index in unique_index_dir.items():
    print(f"值 {value} 的索引: {index[0]}")
