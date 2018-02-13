class Student():
    
    # 类变量
    # 特征
    # 有意义
    sum1 = 0 

    # 无意义 (与Student类 在实际面向对象设计中 不能特定)
    # name = 'leeifme'
    # age = 0

    # 构造函数
    
    def __init__(self,name,age):
        # 初始化对象属性
        # 实例变量
        self.name = name
        self.age = age
        
        ################
        # 实例方法调用实例变量
        print(self.name)
        ##################

         ################
        # 实例方法调用类变量
        # 第一种 使用 self
        print(self.sum1)

        # 第二种 使用 __class__
        print(self.__class__.sum1)
        #################

    # 行为
    def homework(self):
        print('homework')

# 实例化对象
student1 = Student('lee',18)
# student2 = Student('ifme',17)

# print(student1.name)
# print(student2.name)
# print(Student.name)

