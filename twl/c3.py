# 常见用法 map 类

list_x = [1,2,3,4,5,6,7,8]

def func(x):
    return x * x

# for x in list_x:
#     func(x)

r = map(func,list_x)
print(r)
print(list(r))