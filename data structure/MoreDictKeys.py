from random import randint, sample
from functools import reduce

# sample 随机取样
s = sample('abcdefg', randint(3, 6))

d1 = {x: randint(1, 3) for x in s}
d2 = {x: randint(1, 3) for x in sample('abcdefg', randint(3, 6))}
d3 = {x: randint(1, 3) for x in sample('abcdefg', randint(3, 6))}
print(d1)
print(d2)
print(d3)

# 找出d1,d2,d3中 存在的公共 Key
# 常规方法
res = []
for k in d1:
    if k in d2 and k in d3:
        res.append(k)
print(res)

# 第二种方法：使用keys()的到一个dict_keys()的集合对象 并求交集
print(d1.keys())
print(d1.keys() & d2.keys() & d3.keys())

# 思考： 如果有 N 个dict对象
# 使用 map 函数 获取所有 dict_keys 的集合
# 使用 reduce 函数 求所有字典的并集

# m = map(dict.keys, [d1, d2, d3])
# print(list(m))
print(reduce((lambda a, b: a & b), map(dict.keys, [d1, d2, d3])))