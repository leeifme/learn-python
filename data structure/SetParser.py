from random import randint

# 集合解析
# 筛选出能被3整除的子集

s = {randint(-10, 10) for _ in range(1, 10)}
print(s)

print({x for x in s if x % 3 == 0})
