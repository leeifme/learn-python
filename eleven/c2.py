from enum import Enum

class VIP(Enum):
    Green = 2
    Black = 3
    White = 4
    Yellow = 1

print(VIP.Green)
print(VIP.Green.name)
print(VIP['Green'])
print()

# <enum 'VIP'>
# <class 'str'>
# <enum 'VIP'>
# 枚举类型  枚举类型的key  枚举类型的value
print(type(VIP.Green))
print(type(VIP.Green.name))
print(type(VIP['Green']))
print()

# 遍历
for v in VIP:
    print(v)