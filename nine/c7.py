# public 共有函数或变量  private 私有函数或变量


# 面向对象
# 类与对象
# 模板

class Student():
    
    # 类变量
    # 特征
    # 有意义
    sum = 0

    #无意义
    name = 'leeifme'
    age = 0

    # 构造函数
    def __init__(self,name,age,sorce):
        # 初始化对象属性
        # 实例变量

        self.name = name
        self.age = age
        self.__sroce = sorce

    # 行为
    def __homework(self):
        print('homework')

# 实例化对象
student1 = Student('lee',18,59)
student2 = Student('ifme',17,0)

# student1.__homework() 无法访问私有函数

student1.__sroce = -1  # python是动态语言 在这是动态的添加了 __sroce 这个实例变量 可以使用 __dict__ 查看实现的对象所含的变量
print(student1.__sroce)
print(student1.__dict__) # {'name': 'lee', 'age': 18, '_Student__sroce': 59, '__sroce': -1}

# print(student2.__sroce) # 无法调用私有变量
print(student2.__dict__) # {'name': 'ifme', 'age': 17, '_Student__sroce': 0}