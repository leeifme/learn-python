from random import randint

# 字典数据过滤 dict
# 筛选出字典里的值大于90的元素

d = {x: randint(60, 100) for x in range(1, 21)}
print(d)

# 采用字典解析
d = {k: v for k, v in d.items() if v > 90}
print(d)
