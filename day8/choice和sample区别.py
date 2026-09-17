import random

colors = ['red', 'blue', 'green', 'yellow', 'purple']

# 1. sample 返回包含 1 个元素的列表
res1 = random.sample(colors, 1)
print(res1)        # ['green']
print(type(res1))  # <class 'list'>

# 2. choice 直接返回该元素本身
res2 = random.choice(colors)
print(res2)        # 'green'
print(type(res2))  # <class 'str'>