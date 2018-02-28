# 正则表达式

import re

# a = 'C|C++|Java|PHP|JavaScript|Python|Golang|R'
a = '1C|C++1|Java2|PHP45|JavaScript6|7Python8|1Golang|R9'

result = re.findall('Python', a)
result1 = re.findall('\d', a)

print(result)
print(result1)

# 字符集
# 概括字符集
# 数量词 (贪婪 与 非贪婪<?>)
## * 匹配0次或者无限多次
## + 匹配1次或者无限多次
## ? 匹配0次或者1次
# 边界匹配 (^ $)