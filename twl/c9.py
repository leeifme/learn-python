# 装饰器 可变参数
#  应用场景 

import time

def decorator(func):
    def wrapper(*args):
        print(time.time())
        func(*args)
    return wrapper

@decorator
def f1(func_name):
    print('this is a function:' + func_name)

@decorator
def f2(func_name1, func_name2):
    print('this is a function:' + func_name1)
    print('this is a function:' + func_name2)

# 不用@语法糖 是不能体现python的装饰器意义
# f = decorator(f1)
# f()
f1('func')
f2('func1', 'func2')