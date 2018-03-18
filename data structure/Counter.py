from random import randint
from collections import Counter

# 创建一个随机序列List
# 并找出其中重复元素出现的次数

data = [randint(0, 20) for _ in range(30)]
print(data)

# 用字典的形式表示 元组元素，以及出现的次数

c = dict.fromkeys(data, 0)
print(c)

# 对data中的元素进行迭代
for x in data:
    c[x] += 1
print(c)

# 上面的操作其实可以使用标准库中 collections.Counter 实现
c2 = Counter(data)
print(c2)

# 找出出现频度 出现最高的三个元素 使用Counter.most_common()
print(c2.most_common(3))