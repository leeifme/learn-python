# 内部或外部 调用方法或变量

class Student():

    # 特征
    sum = 0 

    # 构造函数
    # 实例方法
    def __init__(self,name,age,score):
        # 初始化对象属性
        # 实例变量
        self.name = name
        self.age = age
        self.sroce = score
        
    # 行为
    def homework(self):
        # print('homework')
        self.do_english_homework()

    # 调用类的内部方法
    def do_english_homework(self):
        print('student do english homework!!!')

    def marking(self,sroce):
        if sroce < 0:
            return '英语成绩录入失败'
        self.sroce = sroce
        return self.name + '的英语分数是: ' + str(self.sroce)

# 实例化对象
student1 = Student('lee',18,90)

# 一般不提倡直接 在外部调用 类中的变量 不安全不稳定
student1.sroce = -1
print(student1.sroce)

print(end='\n')

# 一般调用类中的方法对类中的变量进行修改 并可以添加限制条件 相对安全以及稳定
result = student1.marking(95)
print(result)