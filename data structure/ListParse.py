from random import randint

data = [randint(-10, 10) for _ in range(10)]
print('List:', data)

# 案例1---过滤列表中的负数

# 常规过滤函数
res = []
for x in data:
    if x >= 0:
        res.append(x)
print(res)

# filter 函數
print(list(filter(lambda x: x >= 0, data)))

# 列表解析
print([x for x in data if x >= 0])

# 测试后 通常认为列表解析要快点 当让后两种方式都原快于常规迭代

 