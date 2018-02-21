## 函数式编程
## 闭包
# 闭包的要点:  闭包 = 函数 + 环境变量

# a = 25 # 全局变量

def curve_pre():

    a = 25 #环境变量

    def curve(x): #函数
        # print('This is a functuon')
        return a*x*x
    return curve

# a = 10
f = curve_pre()

# 参看所包含的参数
# print(f.__closure__)
# print(f.__closure__[0].cell_contents)

print(f(2))