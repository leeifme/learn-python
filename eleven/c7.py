## 闭包解决一个问题

# 非闭包实现
origin = 0

def go(step):
    global origin
    new_pos = origin + step
    origin = new_pos
    return new_pos 

print(go(2))
print(go(3))
print(go(5))