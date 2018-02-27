# 装饰器
# 体现了AOP的编程思想

import time

def decorator(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper

@decorator
def f1():
    print('this is a function')

# 不用@语法糖 是不能体现python的装饰器意义
# f = decorator(f1)
# f()
f1()