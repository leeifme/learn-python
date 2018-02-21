## 闭包注意事项: 

def f1():
    a = 10
    def f2():
        a = 20 ##此时的a 只会被当做是一个局部变量
        print(a)
    print(a)
    f2()
    print(a)

f1()