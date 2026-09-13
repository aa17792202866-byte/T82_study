# 代码题：
# 1. 循环输入7天温度，求平均温度
'''
# 定义初始温度
wendu=0
for i in range(1,8):
    shuru =float(input(f'请输入第{i}天温度(单位：摄氏度):'))
    wendu+=shuru
print(f'这7天的平均温度为{wendu/7:.2f}')
'''
# 2. 求 100-200以内同时能被7、8整除的数，并统计个数
'''
# 定义两个变量，保存同时能被7、8整除的数和个数
nums=''
geshu=0
for i in range(100,201):
    if i % (5*6)==0:
        nums+=str(i)+' '
        geshu+=1
print(f'100-200以内同时能被7、8整除的数分别为{nums},一共有{geshu}个')
'''
# 3. 求同时能被2、3、5整除的第一个三位正整数
'''
for i in range(100,1000):
    if i%(2*3*5)==0:
        print(i)
        break
# 定义计数器，个数
i=100
while i <=999:
    if i%(2*3*5)==0:
        print(i)
        break
    i+=1
'''
# 4. 求 0 -1 + 2 - 3 + 4 - 5 + 6 -7.... + 100 的结果
'''
# 定义变量，保存结果
jieguo = 0
for i in range(0,101):
    if i%2!=0:
        jieguo-=i
    else:
        jieguo+=i
print(jieguo)
'''
# 5. 从键盘接收用户输入的自己最喜欢的歌手姓名（一次输入一名歌手信息即可），直到用户不想输入了（输入'q'退出）；
#    统计用户共计输入多少名歌手，并打印所有输入的歌手的姓名
'''
# 定义变量，保存输入的歌手信息和输入的次数
names=''
nums=0
while True:
    shuru=input('请输入你喜欢的歌手姓名：')
    if shuru=='q':
        print()
        break
    else:
        names+=shuru+' '
        nums+=1
print(f'你共计输入了{nums}位歌手姓名，分别是{names}')
'''
# 6. 小明家有一只乌龟,每天吃一根火腿肠,冰箱中有70根火腿肠,吃光所有的火腿肠需要几周?
#    打印一周后冰箱中还剩多少根火腿肠,二周后?三周后?四周后?...直到最后一周?
#    强制要求：使用不定次循环实现，小明家冰箱的火腿肠根数可以随意给定，不一定非得是70
#                    按周计算、不用按天计算
'''
# 定义变量，保存周数和初始火腿肠数
week=0
nums=70
while True:
    if nums<1:
        break
    if nums%7==0:
        week+=1
        nums-=7
    print(f'{week}周后，还剩{nums}根火腿肠')
'''
# 7. Chuckie Lucky赢了100W美元，他把它存入一个每年盈利8%的账户。在每年的最后一天，Chuckie取出10W美元。
#     打印每年他的剩余金额,直至0为止, 打印多少年后Chuckie会清空他的账户。
'''
# 定义两个变量，保存初始金额和年
money=100
year=0
# 使用定次循环
while money>0:
    year+=1
    money=(money+money*0.08)-10
    print(f'第{year}年Chuckie账户余额还剩{money*10000:.2f}美元')
print(f'{year}年后Chuckie会清空他的账户')
'''
# 8. 依次输入几个数据，直到0作为输入的结束，然后求出输入的这些数据的总和及平均值（0不算次数）
'''
# 定义变量，保存次数、和
cishu=0
he=0
while True:
    shuru = float(input('请输入数据：'))
    if shuru==0:
        break
    else:
        cishu+=1
        he+=shuru
print(f'共计输入了{cishu}次，平均值为{he/cishu}')
'''
# 9. 有一张厚度为0.1毫米的纸，假设它足够大，重复将其对折，问对折多少次之后，其厚度可以抵达（再对折一次就超过）珠穆朗玛峰的高度？
#    # 珠峰高度统一为8844.32米
'''
# 定义变量，保存纸张的初始厚度(毫米换算成米)和次数
cishu=0
houdu=0.1/1000
while houdu<8844.32:
    houdu*=2
    cishu+=1
print(f'对折{cishu}后，其厚度可以抵达（再对折一次就超过）珠穆朗玛峰的高度')
'''
# 10.  有一个10米深的井，井底有只青蛙，青蛙每次向上爬5米后就会下滑3米，设计一个程序计算青蛙需要几次能爬到井外
'''
# 定义变量，保存青蛙爬的次数和爬了多少米
cishu=0
mi=0
# 设置循环条件
while mi<10:
    cishu+=1
    mi+=5-3
print(f'青蛙需要爬{cishu-1}次能爬到井外')
'''