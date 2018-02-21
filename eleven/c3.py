from enum import Enum

class VIP(Enum):
    YELLOW = 1
    YELLOW_ALTAS =1 
    GREEN = 2
    BLACK = 3
    WHITE = 4

# 别名(是不会打印别名的)
for v in VIP:
    print(v)

print()

# 打印出别名
for v in VIP.__members__.items():
    print(v)