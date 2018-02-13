# 面向对象的特性 -- 继承

from c9 import Human
class Student(Human):

    # 构造函数
    def __init__(self,school,name,age): # 继承父类的特称 并且有自己的特征
        
        self.school = school

        # 第一种（不提倡）
        # 子类中调用父类中的构造函数
        # 构造函数可以看作是一个实力函数
        # 而用类去调用一个实例函数，在面向对象设计中是毫无意义的（应该由对象来调用），但这也体现了python 动态语言的灵活性 
        # Human.__init__(self,name,age) 

        # 第二种（主流的使用方法 使用 super）
        super(Student,self).__init__(name,age)

    # 当父类与子类的实例方法同名时 优先调用子类的方法
    def do_homework(self):

        # 使用super 在子类的实例方法中调用父类的实例方法
        super(Student,self).do_homework()

        print('english homework')

# 实例化对象
student1 = Student('八中附小','lee',18)
# student2 = Student('ifme',17,0)
print(student1.name)
print(student1.age)
print(student1.sum)
print(Student.sum)
student1.get_name()
student1.do_homework() 

