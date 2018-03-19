from collections import namedtuple

# 为元组每个元素命名 使用标准库中的collections.namedtuple
# 元组优势： 存储空间小，访问速度快

student = namedtuple('student', ['name', 'age', 'sex', 'email'])

s = student('Jim', '16', 'male', 'lee@leeid.me')

print(s)
print(s.name)