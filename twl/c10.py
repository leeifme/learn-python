
# 装饰器 可变参数 函数参数中含有关键字
#  应用场景 

import time

def decorator(func):
    def wrapper(*args,**kw):
        print(time.time())
        func(*args,**kw)
    return wrapper

@decorator
def f1(func_name):
    print('this is a function:' + func_name)

@decorator
def f2(func_name1, func_name2):
    print('this is a function:' + func_name1)
    print('this is a function:' + func_name2)

@decorator
def f3(func_name1,func_name2,**kw):
    print('this is a function:' + func_name1)
    print('this is a function:' + func_name2)
    print(kw)

# 不用@语法糖 是不能体现python的装饰器意义
# f = decorator(f1)
# f()
f1('func')
f2('func1', 'func2')
f3('func1', 'func2',a=1,b=2,c='1,2,3')