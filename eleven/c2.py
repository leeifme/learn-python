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

print(type(VIP.Green))
print(type(VIP.Green.name))
print(type(VIP['Green']))
print()

for v in VIP:
    print(v)