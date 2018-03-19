from random import randint

# 使用内置函数Sorted 对列表进行排序
x = [randint(0, 10) for _ in range(10)]
print(x)
print(sorted(x))
print()
# 如果现在要对 一个字典dict的值进行排序
# 生成一个学生成绩表

student = {x: randint(60, 100) for x in 'azcgdyx'}
print(student)
# 对student直接进行排序 会发现 他只是对 key进行排序
print(sorted(student))
# sorted 传入的是一个可迭代对象 iter
# 我们看下dict 的可迭代对象
print(list(iter(student)))
print()

# 所以想根据dict的值进行排序 可以使用 元组 (97,'x')>(63,'y')
# 1.采用zip()函数
# 2.使用dict的items()方法
print(student.values())
print(student.keys())
z = zip(student.values(), student.keys())
print(sorted(list(z)))
print('使用items()')
i = student.items()
print(sorted(i, key=lambda x: x[1]))
