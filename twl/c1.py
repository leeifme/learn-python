# 匿名函数

def add(x,y):
    return x+y

print(add(1,2))

# 变量调用匿名函数 没有意义
f = lambda x,y:x+y
print(f(1,2))

# 将表达式体现出来
# lambda parameter_list: expression

