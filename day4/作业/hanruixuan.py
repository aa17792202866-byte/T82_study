# 代码题：
# 1.  求 1-100以内所有含6的数，并统计个数
#方法一（有点复杂了）
# sum1 = 0
# for i in range(1,101):
#     i = str(i) #将i从int型转换成str型
#     if i.find("6") == 0:
#         print(i,end=" ") #检测第一个数字是不是6
#         sum1 += 1
#     elif i.find("6") == 1: #检测第二个数字是不是6
#         print(i,end=" ")
#         sum1 += 1
#     # print((i.find("6")))
# print(f"一共{sum1}个含6的数")
#方法二（直接判断是不是不等于-1就行了）
# sum1 = 0
# for i in range(1,100):
#     if str(i).find("6") != -1:
#         print(i,end=" ")
#         sum1 += 1
# print(f"一共{sum1}个含6的数")
#方法三（使用in判断）
# sum1 = 0
# for i in range(1, 101):
#     if "6" in str(i):
#         print(i, end=" ")
#         sum1 += 1
# print("\n总个数:", sum1)

# 2.  计算1到100中除了 30, 60,90之外所有值的和
# sum2 = 0
# for i in range (1,101):
#     if i not in (30,60,90): #判断不在30，60，90中的数字
#         sum2 += i
#     # else:
#     #     print(i)
# print(f"1到100中除了 30, 60,90之外所有值的和为{sum2}")

# 3.  循环生成10个100以内的正整数并判断是奇数还是偶数
# import random
# for i in range(1,11):
#     num3 = random.randint(10,100)
#     if num3 % 2 == 0:
#         print(f"第{i}个数{num3}是偶数")
#     else:
#         print(f"第{i}个数{num3}是奇数")

# 4.  猜100以内数字游戏，程序内先用随机数指定被猜的数值。
#      用户给出的值偏小则给出提示“太小”；
#      用户给出的值偏大，给出提示“太大”，
#      最多只能猜5次。
#      猜中了给出提示“恭喜你!"，结束游戏；
#      如果5次都没猜正确，给出“太笨了！”。
# import random
# jishu = 0
# num4 = random.randint(1,100)
# print(num4)
# for i in range(1,6):
#     while 1:
#         hm_num = int(input("请输入数字"))
#         if 0 < hm_num < 101:
#             if hm_num < num4:
#                 print("太小")
#                 jishu += 1
#             elif hm_num > num4:
#                 print("太大")
#                 jishu += 1
#             else:
#                 print("恭喜你！")
#             break
#         else:
#             print("请输入1-100的数字")
#     if hm_num == num4:
#         break
# if jishu == 5:
#     print("太笨了")

# 5.  猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个 第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
#     以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
#     程序分析：采取逆向思维的方法，从后往前推断。
day1 = 1
for i in range(9,0,-1):
    day1 = (1 + day1) * 2
    print(f"第{i}天, {day1}个桃子")
print(f"第一天摘了{day1}个桃子")

# 6. 一球从100米高度自由落下，每次落地后反跳回原高度的一半，再落下，求它在 第10次落地时，共经过多少米？第10次反弹多高？
# 7. 打印以下图形：
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
#
# 字符串题：
# 1. str1 = 'lilei is a young people,he\'s hometown is beijing'
#    1) 取出人名和地名
#    2) 取出对人物的家乡的介绍
#    3) 判断人物的家乡是不是xian
#    注：人名和地名可以随意给，不一定必须是lilei、beijing；除此以外保留str1原有格式
# 2. str2 = "today is a good day",去掉字符串所有的空格,并使用@进行连接,使其变成这个字符串'today@is@a@good@day'
# 3. 对字符串"Where now? Who now? When now"调用一个方法,返回如下所述列表["Where now","Who now","When now"]
# 4. 对列表["The","fox","jumped","over","the","fence."]进行处理,将其变成一个语法正确的字符串.
# 5. 获取字符串中汉字的个数
#    a = "我的 English 学的不好"
#    注：单个中文字符的unicod码范围为：'\u4e00' <= 单个中文字符的unicode码 <= '\u9fef'
# 6. 分别统计str3中的字母、数字的个数，并将所有的字母、数字打印出来
#    str3 = "toDay is a Good day,112 $$ @!"
