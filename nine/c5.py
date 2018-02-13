# 类方法 & 静态方法

class Student():

    # 特征
    sum = 0 

    # 构造函数
    # 实例方法
    def __init__(self,name,age):
        # 初始化对象属性
        # 实例变量
        self.name = name
        self.age = age
        
    # 行为
    def homework(self):
        print('homework')

    # 类方法
    @classmethod
    def class_sum(cls):
        cls.sum += 1
        print('This is a ClassMethod:' + str(cls.sum))

        # 类方法 调用 类变量
        print(Student.sum)
        # 类方法 调用 实例变量 -> 无法调用
        # print(cls.name)

    # 静态方法 (不提倡使用 这个方法 因为方法本身 与面向对象 关联性并不是太大)
    @staticmethod
    def static_sum(a,b):
        print('This is a StaticMethod:' + str(a+b))

        # 静态方法 调用 类变量
        print(Student.sum)
        # 静态方法 调用 实例变量 -> 无法调用
        # print(self.name) 

# 实例化对象
student1 = Student('lee',18)

student1.class_sum()
Student.class_sum()

student1.static_sum(1,2)
Student.static_sum(1,2)
