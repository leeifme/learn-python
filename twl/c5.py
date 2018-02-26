
# reduce

from functools import reduce
list_x = [1,2,3]
list_y = [1,2,3,4,5,6,7,8]
list_xy = [(0,0),(1,2),(2,2),(-1,-2)]


# def func(x):
#     return x * x

r = reduce(lambda x,y:x*y,list_x) # 集合列表与参数要相同
# print(r)
print(r)

# 扩展 
# 大数据
# map/reduce 模型 函数式编程 映射 归约 并行计算