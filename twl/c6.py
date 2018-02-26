## filter 

list_x = [1,0,1,0,1,0]
list_u = ['a','A','b','C']
r = filter(lambda x: True if x ==1 else False , list_x) 
# 等价于 lambda x: x
print(list(r))