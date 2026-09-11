# 代码题：
# 1. 循环输入7天温度，求平均温度
# tem_sum = 0
# for i in range(1,8):
#
#     tem = float(input(f"请输入第{i}天的温度"))
#     tem_sum += tem
# print(f"七天的平均温度为{tem_sum} / 7 ={tem_sum/7:.1f}")


# 2. 求 100-200以内同时能被7、8整除的数，并统计个数
number2 = 0 #定义能被7、8整除数之和的变量
for i in range(100,201):
    if i % 56 == 0:
        print(f"{i}可以被7整除")
        number2 += 1

print(f"能被7和8整除的数的个数为{number2}")

# 3. 求同时能被2、3、5整除的第一个三位正整数
# number3 = 100
# while 1:
#     if number3 % 2 == 0 and number3 % 3 == 0 and number3 % 5 == 0:
#         print(f"{number3}这个数可以同时被2、3、5整除")
#         break
#     number3 += 1

# 4. 求 0 -1 + 2 - 3 + 4 - 5 + 6 -7.... + 100 的结果
# meici = ''
# sum4 = 0
#
# for i in range (0,101):
#     if i % 2 == 0:
#         sum4 += i
#         meici += str(i)
#     else:
#         i = -i
#         sum4 += i
#         meici += str(i)
# print(f"求和结果为{sum4}")

# 5. 从键盘接收用户输入的自己最喜欢的歌手姓名（一次输入一名歌手信息即可），直到用户不想输入了（输入'q'退出）；
#    统计用户共计输入多少名歌手，并打印所有输入的歌手的姓名
# geshou_sum = 0
# geshou_name = ""
# while 1:
#     name = input("请输入一名歌手的姓名（输q退出）")
#     geshou_name += name + " "
#     if name == "q":
#         print("输入已退出")
#         break
#     geshou_sum += 1
# print(f"你一共输入了{geshou_sum}个歌手，分别是{geshou_name}")


# 6. 小明家有一只乌龟,每天吃一根火腿肠,冰箱中有70根火腿肠,吃光所有的火腿肠需要几周?
#    打印一周后冰箱中还剩多少根火腿肠,二周后?三周后?四周后?...直到最后一周?
#    强制要求：使用不定次循环实现，小明家冰箱的火腿肠根数可以随意给定，不一定非得是70
#                    按周计算、不用按天计算
# week_num = 1
# htc_num = 72
# while 1:
#     htc_num -= 7
#     if htc_num >= 0:
#         print(f"第{week_num}周结束后，火腿肠数量还有{htc_num}个") #保证火腿肠数量>=0
#     elif htc_num<0:
#         print(f"第{week_num}周结束后，火腿肠数量还有0个")
#
#     if htc_num <= 0:
#         print(f"在第{week_num}周后，火腿肠被吃完了")
#         break
#     week_num += 1
#


# 7. Chuckie Lucky赢了100W美元，他把它存入一个每年盈利8%的账户。在每年的最后一天，Chuckie取出10W美元。
#     打印每年他的剩余金额,直至0为止, 打印多少年后Chuckie会清空他的账户。
# money = float(100)
# year = 0
# while money >= 0:
#     money = money * 1.08
#     year += 1
#     if money - 10 >= 0:
#         print(f"第{year}年，原本有{money:.2f}w美元，取走了10w美元，还剩下{money-10:.2f}w美元")
#     else:
#         print(f"第{year}年，原本有{money:.2f}w美元，取走了{money:.2f}w美元，还剩下0美元") #保证被取走后，剩下的钱不能为负数
#     money -= 10
# print(f"在第{year}年取走了所有的钱")

# 8. 依次输入几个数据，直到0作为输入的结束，然后求出输入的这些数据的总和及平均值（0不算次数）
# sum8 = 0
# count = 0
# while 1:
#     number8 = float(input("请依次输入数字，将会计算输入的数字之和和平均值（输入0结束）"))
#     if number8 == 0:
#         break
#     sum8 += number8
#     count += 1
# if count > 0:
#     print(f"一共输入了{count}个数字，数字之和为{sum8:.2f}，数字平均值为{sum8 / count:.2f}")
# else:
#     print("没有有效输入")




# 9. 有一张厚度为0.1毫米的纸，假设它足够大，重复将其对折，问对折多少次之后，其厚度可以抵达（再对折一次就超过）珠穆朗玛峰的高度？
#    # 珠峰高度统一为8844.32米
# 我感觉题目有歧义，到底是对折多少次可以实现再对折一次就超过，还是对折多少次可以抵达，我按照第一种来写
# paper_width = 0.0001
# count = 0
# while 1:
#     if paper_width > 8844.32:
#         break
#     paper_width = paper_width * 2
#     # paper_width = pow(paper_width,2) (引以为戒)
#     count += 1
#     print(f"第{count}次对折为{paper_width}")
# print(f"第{count-1}次对折，实现了再对折一次高度就能超过珠峰高度")


# 10.  有一个10米深的井，井底有只青蛙，青蛙每次向上爬5米后就会下滑3米，设计一个程序计算青蛙需要几次能爬到井外
# height = 0
# count = 0
# while 1:
#     height += 5 #这次爬了多少
#     count += 1 #爬行次数+1
#     print(f"第{count}次爬了{height}m",end="")
#     if height >= 10:
#         print(",已经爬出\n")
#         break
#     height -= 3 #这次下滑了多少
#     print(f"，下滑到了{height}m")
# print(f"需要{count}次，才能爬出")
#
#
#
