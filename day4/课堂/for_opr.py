'''
for循环：
for循环主要用于实现定次循环，while循环主要用于实现不定次循环

1. 结构一：
语法格式：
for 临时变量 in range():
    重复执行的功能代码

range(start,end,step)：  左闭右开
作用： 用来产生指定范围内一系列连续的整数
3个参数说明：
 start：    开始值      可以不写，默认为0；如果写了则以实际为准
 end:       结束值      必须要写；取到end的前一个
 step:      步长/步距   可以不写，默认为1；如果写了则以实际为准

 2. 结构二：  主要用于遍历字符串/列表/元组/字典
 语法格式：
 for 临时变量 in 字符串/列表/元组/字典：
    print(临时变量)


3.结构三： for-else
说明： 当for循环是因为break结束的，则不执行else里面的功能代码
       当for循环是跑完规定次数结束的，则执行else里面的功能代码


break和continue的区别：
break和continue只能用在循环语句中，不能单独使用
break：     循环碰到break，则终止(停止)整个循环
continue：  循环碰到continue，则结束(跳过)本次循环，紧接着继续下一次循环
'''
# str1 = 'abcde你我他'
# for i in str1:     #i:['a','b','c','d','e','你','我','他']
#     print(i,end=' ')
#
# list1 = [1,'2',3,4]
# for i in list1:    #i:[1,'2',3,4]
#     print(i,type(i),end=' ')

# 1. 玩100以内逢7过的游戏；规则：但凡是含7或7的倍数，则不打印
'''
# 实现方式一: 使用continue实现
#遍历1-100
for i in range(1,101):   #i:[1,2,3,100]
    #重复执行的代码：判断当前遍历的i是7的倍数或含7，则不打印；否则打印
    if i % 7 == 0 or i // 10 == 7 or i % 10 == 7:
        continue
    else:
        print(i,end=' ')

# 实现方式二:  不使用continue实现
#遍历1-100
for i in range(1,101):   #i:[1,2,3,100]
    #重复执行的代码：判断当前遍历的i是7的倍数或含7，则不打印；否则打印
    if not(i % 7 == 0 or i // 10 == 7 or i % 10 == 7):
        print(i,end=' ')
'''

# 题目：人与计算机玩100以内猜数字的游戏，玩5次
#       其中：人猜的不在范围内不算次数

#导入random随机数模块
import random
# 循环跑5次for循环：
for i in range(5):    #i:[0,1,2,3,4]
    #电脑出，人猜，判断人猜的在范围内，则根据大小关系打印结果；否则提示用户
    com = random.randint(1, 100)
    while True:
        user = int(input('请猜一个100以内的正整数：'))
        if 1 <= user <= 100 :
            if user == com:
                print(f'电脑出的是{com}，你猜的是{user}，你猜对了')
            elif user > com:
                print(f'电脑出的是{com}，你猜的是{user}，你猜大了')
            else:
                print(f'电脑出的是{com}，你猜的是{user}，你猜小了')
            break
        else:
            print('只能猜100以内的整数')





