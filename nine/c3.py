
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
    def __init__(self,name,age):
        # 初始化对象属性
        # 实例变量

        self.name = name
        self.age = age

    # 行为
    def homework(self):
        print('homework')

# 实例化对象
student1 = Student('lee',18)
student2 = Student('ifme',17)

print(student1.name)
print(student2.name)
print(Student.name)

