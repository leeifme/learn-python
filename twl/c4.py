
# map类 和 lambda匿名函数


list_x = [1,2,3,4,5,6,7,8]
list_y = [1,2,3,4,5,6,7,8]


# def func(x):
#     return x * x

r = map(lambda x,y:x*x+y,list_x,list_y) # 集合列表与参数要相同
# print(r)
print(list(r))