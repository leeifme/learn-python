## 闭包注意事项: 

def f1():
    a = 10
    def f2():
        # a = 20 ##此时的a 只会被当做是一个局部变量
        return a
        # print(a)
    # print(a)
    return f2
    # print(a)
 
f = f1()
print(f)
print(f.__closure__)

