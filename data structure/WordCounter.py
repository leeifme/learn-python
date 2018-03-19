from collections import Counter
import re

# 读取文件 统计出现的高频词汇
text = open('word.txt').read()
# print(text)

c = Counter(re.split('\W+', text))
print(c)
print(c.most_common(3))