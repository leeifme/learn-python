# 装饰器

import time

def f1():
    print('This is a function')

def f2():
    print('This is two function')

def time_display(func):
    print(time.time())
    func()

# time_display(f1)
# print()
# time_display(f2)

# 上面是等同于下面代码：
print(time.time())
f1()
print(time.time())
f2()