## 枚举

from enum import Enum

class VIP(Enum):
    Green = 2
    Black = 3
    White = 4
    Yellow = 1

print(VIP.Black)