## 父类
### 类应该写在不同的模块中 这样代码更具条理性

class Human():
    sum = 0

    def __init__(self,name,age):
        self.name = name 
        self.age = age

    def get_name(self):
        print(self.name)

    def do_homework(self):
        print('This is a parent method')