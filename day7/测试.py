import random

teachers = ['老师1', '老师2', '老师3', '老师4', '老师5', '老师6', '老师7', '老师8']
offices = []
o_count = 3

# 初始化 3 个空办公室列表
for i in range(o_count):
    offices.append([])

# 打乱教师列表顺序
random.shuffle(teachers)

# 随机分配教师到未满的办公室
for t in teachers:
    while True:
        # 动态抽选办公室索引 [0, o_count - 1]
        i = random.randint(0, o_count - 1)
        if len(offices[i]) < o_count:
            offices[i].append(t)
            break

# 打印最终分配结果
for i in range(len(offices)):
    print(f'办公室{i+1}的人数是{len(offices[i])}个，分别为{offices[i]}')