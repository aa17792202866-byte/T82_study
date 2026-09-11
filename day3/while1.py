# 3. 打印1-10之间所有的偶数(正序打)   2,4,6,8,10
# i=2
# while i<=10:
#
#     print(i,end=" ")
#     i += 2

# i=1
# while i<=10:
#     if i % 2 == 0:
#         print(i,end=" ")
#     i+=1

# 4. 打印1-10之间所有的奇数(倒序打)
# i=10
# while i>=1:
#     if i % 2 == 0:
#         i -= 1
#     else:
#         print(i,end=" ") #一会记得试一下seq配合逗号加上空字符串可以不
#         i -= 1
# i=10
# while i>=1:
#     if i % 2 == 0:
#         i -= 1
#     else:
#         print(i,end="\t") #一会记得试一下seq配合逗号加上空字符串可以不
#         i -= 1

# 6. 计算1-10之间所有偶数的和，奇数的积，并求二和最终的和
#
# i = 1
# sum_ji = 1
# sum_ou = 0
# while i <= 10:
#     if i % 2 == 0:
#         sum_ou += i
#     else:
#         sum_ji *= i
#     i+=1
# print(f"奇数之奇为{sum_ji}，偶数之和为{sum_ou},二者最终和为{sum_ou+sum_ji}")


# 7. 人与计算机玩猜数字的游戏：
#    计算机先随机出一个100以内的正整数，由人猜来；根据人猜的大小打印对应提示信息
#     玩5次
# import random
# num_cm = random.randint(1,100)
# print(num_cm)
# i = 1

# while i <= 5:
#     num_human = int(input('请猜一下1-100的数字'))
#     if num_human == num_cm:
#         print("你猜对了")
#     else:
#         print("你猜错了")
#     i+=1

# while i <= 5:
#     num_human =int(input("请猜一下1-100的数字"))
#     if num_human == num_cm:
#         print("你猜对了")
#     elif num_human > num_cm and i<5:
#         print(f"你猜的太大了，你还有{5-i}次机会")
#     elif i<5:
#         print(f"你猜的太小了，你还有{5-i}次机会")
#     i+=1

#人与电脑玩剪刀石头布，直到人赢了为止
import random

while 1:

    cm_shuchu = random.randint(0, 2)
    print(f"计算机输出的是{cm_shuchu}")
    human_shuru = int(input("请输入石头剪刀布（0=石头，1=剪刀,2=布）"))

    if human_shuru in (0,1,2):
        if (cm_shuchu - human_shuru) % 3 == 1:
            print("你赢了")
            break
        else:
            print("你输了")
    else:
        print("请输入0-2之间的整数")

