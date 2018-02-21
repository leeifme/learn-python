## 枚举

from enum import Enum

class VIP(Enum):
    Yellow = 1
    Green = 2
    Black = 3
    White = 4

print(VIP.Black)