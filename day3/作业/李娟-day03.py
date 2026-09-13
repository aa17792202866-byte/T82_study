# 1. 循环输入7天温度，求平均温度

#定次循环，[1，2，3，4，5，6，7]
#定义变量，保存7天温度的和
# he=0
# for i in range(1,8,1):
#     # 输入每天的温度
#     wd=float(input(f'请输入第{i}天的温度：'))
#     he += wd
# print(f'平均温度为{he/7}')


# 2. 求 100-200以内同时能被7、8整除的数，并统计个数

#定次循环，[100,101,102.....200]
# 定义变量，保存个数
# count=0
# for i in range(100,201,1):
# 设置循环条件
#  if i % 7 ==0 and i % 8 ==0:
#     print(i)
#     count += 1
# print(f'符合条件的数字总个数为{count}')


# 3. 求同时能被2、3、5整除的第一个三位正整数


# for i in range(100,1000,1):
#     if i % 2 == 0 and i % 3 == 0 and i % 5 == 0:
#         print(f'第一个满足条件的正整数为{i}')
#          break


# 4. 求 0 -1 + 2 - 3 + 4 - 5 + 6 -7.... + 100 的结果


#定义变量，保存结果
# res=0
# for i in range(0,101,1):
#     # 偶数都为正，奇数都为负
#      if i % 2 == 0:
#          res += i
#      else:
#          res -= i
# print(res)



# 5. 从键盘接收用户输入的自己最喜欢的歌手姓名（一次输入一名歌手信息即可），直到用户不想输入了（输入'q'退出）；
#    统计用户共计输入多少名歌手，并打印所有输入的歌手的姓名



# 不定次循环
# 定义变量，保存输入的全部的歌手姓名和输入的歌手数量
# all_name=''
# nums=0
# while True:
#     name= input('请输入一个歌手的姓名：')
#     if name == 'q':
#         print('退出')
#         break
#     else:
#         nums += 1
#         all_name += name + ' '
#         print(f'你第{nums}次输入的歌手为：{name}')
# if nums != 0 :
#     print(f'你一共输入了{nums}名歌手，歌手分别为：{all_name}')
#
# else:
#     print('你没有输入任何歌手姓名')



# 6. 小明家有一只乌龟,每天吃一根火腿肠,冰箱中有70根火腿肠,吃光所有的火腿肠需要几周?
#    打印一周后冰箱中还剩多少根火腿肠,二周后?三周后?四周后?...直到最后一周?
#    强制要求：使用不定次循环实现，小明家冰箱的火腿肠根数可以随意给定，不一定非得是70
#                    按周计算、不用按天计算


# 定义变量，保存冰箱里火腿肠的数量和周的总数
# nums = int(input('请输入冰箱中的火腿肠数量: '))
# count = 0
#
# while True:
#     # 每周吃7根火腿肠
#     nums -= 7
#     count += 1
#
#     if nums > 0:
#      print(f'第{count}周,剩余{nums}根火腿肠')
#
#     else:
#         nums = 0
#         print(f'第{count}周,剩余{nums}根火腿肠')
#         break     # 吃完，退出循环
#
# print(f'吃光所有火腿肠需要{count}周')



# 7. Chuckie Lucky赢了100W美元，他把它存入一个每年盈利8%的账户。在每年的最后一天，Chuckie取出10W美元。
#     打印每年他的剩余金额,直至0为止, 打印多少年后Chuckie会清空他的账户。


#定义变量，分别保存金额、利率、年底取出和年数
# dollar = 1000000
# rate = 0.08
# out = 100000
# year = 0
#
# while True:
#     year += 1
#     dollar *= 1 + rate  #8%的利息
#     dollar -= out  #取出金额
#
#     if dollar > 0:
#         print(f'{year}年后,剩余金额为{dollar:.2f}')
#
#     else:
#         dollar = 0
#         break
# print(f'{year}年后,剩余金额为{dollar:.2f}')
# print(f'{year}年后账户被清空')



# 8. 依次输入几个数据，直到0作为输入的结束，然后求出输入的这些数据的总和及平均值（0不算次数）


# 定义变量，保存数据总和、计数
# total = 0
# count = 0
#
# while True:
#     num = int(input('输入数据:'))
#
#     if num == 0:
#         break
#
#     total += num
#     count += 1
#
# print(f'总和:{total}')
#
# if count >= 0 :
#     print(f"平均值：{total / count:.2f}")
# else:
#     print('无有效数字')



# 9. 有一张厚度为0.1毫米的纸，假设它足够大，重复将其对折，问对折多少次之后，其厚度可以抵达（再对折一次就超过）珠穆朗玛峰的高度？
#    # 珠峰高度统一为8844.32米


# 定义变量，保存折叠次数和厚度
# count = 0
# hd = 0.1
#
# while True:
#     if hd >= 8844.32 * 1000:
#         break
#
#     hd *= 2     # 每一次厚度翻倍
#     count += 1
#
# print(f"需要折叠{count}次")



# 10.  有一个10米深的井，井底有只青蛙，青蛙每次向上爬5米后就会下滑3米，设计一个程序计算青蛙需要几次能爬到井外

# 定义变量，保存井的深度、爬的高度、爬的次数
depth = 10
height = 0
count = 0

while True:
    count += 1
    height += 5   #向上爬5m

    if height >= depth:
        break

    height -= 3   #没爬出去才会下滑

print(f'青蛙需要爬{count}次能爬到井外')










