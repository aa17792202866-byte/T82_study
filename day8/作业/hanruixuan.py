# 代码题：
# 以下题目（1-7题）全部用函数实现：
# 1.函数实现：回文数是一个正向和逆向都相同的整数,如123454321,9889,编写一个程序判断一个整数是否是回文数
from day7.shujvku import result


def huiwenshu(num1):
    list1 = list(num1)
    list2 = list1[::-1]
    if list1 == list2 and list1[0] != "0":
        return True
# while 1:
#     num1 = input("请输入一串纯数字，将会判断是否为回文数")
#     for i in list(num1):
#         if i.isdigit() == False:
#             print("请输入纯数字")
#             break
#     else:
#         if huiwenshu(num1):
#             print(f"{num1}是回文数")
#             break
#         else:
#             print(f"{num1}不是回文数")
#             break




# 2.函数实现:  计算你在月球上的体重
#    如果你现在正站在月球上,你的体重将只相当于在地球上的16.5%.你可以通过把你在地球上的体重乘以0.165来计算.
#    如果在接下来的15年里,你每年增长一公斤,那么在直到15年后的你每年里访问月球时的体重都是多少?
#    用for循环来写一个程序,来打印你每年在月球上的体重（定义两个函数：计算每年地球的体重、计算每年月球的体重）.
def earth_height(height):
    for i in range(1,16):
        height += 1
        print(f"第{i}年后，你的体重为{height}")
def moon_height(height):
    for i in range(1,16):
        height += 1
        moon_height = height * 0.165
        print(f"第{i}年后，你的体重为{moon_height:.1f}")
# height2 = int(input("请输入你的体重"))
# moon_height(height2)

# 3. 函数实现:  设计计算器程序，要求用户输入两个整数和一个运算符，程序能够计算出两个数的相应加减乘除结果。（涉及到精确度的，一律保留两位小数）
def calculator(num1,num2,operator):
    if operator == "*":
        return num1 * num2
    elif operator == "/":
        result = round(num1/num2,2)
        return result
    elif operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    else:
        return False
# while 1:
#     num1 = input("请输入第一个整数")
#     num2 = input("请输入第二个整数")
#     operator = input("请输入运算符（只能是*、/、+、-）")
#     if num1.isdigit() and num2.isdigit() and operator in ("*","/","+","-"):
#         num1=int(num1)
#         num2=int(num2)
#         result = calculator(num1,num2,operator)
#         break
#     else:
#         print("请按照要求输入")
# print(f"{num1} {operator} {num2} = {result}")

# 4. 函数实现：有一个10米深的井，井底有只青蛙，青蛙每次向上爬5米后就会下滑3米，设计一个程序计算青蛙需要几次能爬到井外
def qingwa():
    height, cishu = 0, 1
    while 1:
        height += 5
        if height >= 10:
            break
        height -= 3
        cishu += 1
    return cishu
# print(f"青蛙需要{qingwa()}天才能爬出")

# 5. 函数实现：某个公司传输数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：每位数字都加上5,然后再用除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换，设计解密程序，能够根据接收的数据判断出原始数据
def encryption(num5):
    list5 = list(num5)
    for i in range(len(list5)):
        list5[i] = int(list5[i]) + 5
    for i in range(len(list5)):
        list5[i] = int(list5[i]) % 10
    list5[0],list5[3] = list5[3],list5[0]
    list5[1], list5[2] = list5[2], list5[1]
    return int("".join(map(str, list5)))

def decrypt(num5):
    list5 = list(str(num5))
    list5[0], list5[3] = list5[3], list5[0]
    list5[1], list5[2] = list5[2], list5[1]
    for i in range(len(list5)):
        if int(list5[i]) < 5:
            list5[i] = int(list5[i]) + 5
        elif int(list5[i]) > 5:
            list5[i] = (int(list5[i]) + 5) % 10
        else:
            list5[i] = 0
    return int("".join(map(str, list5)))

# a = input("请输入四位整数")
# b=encryption(a)
# print(f"{a}加密后的结果是{b}")
# c = decrypt(str(b))
# print(f"{b}解密后的结果是{c}")
# print(f"{a}加密后的结果是{encryption(a)},解密后的结果是{decrypt(encryption(a))}")

# 6. 函数实现：某系统做限时促销活动
#                     1）要求设计一个程序生成200个邀请码，邀请码由6位字符组成，要求是一个随机字母开头,其它五位为随机数字
#                     2）随机产生3个一等奖，5个二等奖，10个三等奖（要求：每个邀请码只能有一次抽奖的机会）

# import random
# def choujiang():
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z']
#     def create_code(): # 生成一个邀请码
#         letter = random.choice(letters)     # 随机取一个字母
#         nums = ""      # 生成后面5位数字
#         for i in range(5):
#             nums += str(random.randint(0, 9))
#         return letter + nums
#     codes = [] # 生成200个不重复的邀请码
#     while len(codes) < 200:
#         code = create_code()
#         if code not in codes:
#             codes.append(code)
#     winners = random.sample(codes, 18) # 抽奖
#     return winners[0:3],winners[3:8],winners[8:18]
# a,b,c = choujiang() #返回了三个值，所以要解包
# print(f"一等奖：{a}\n二等奖：{b}\n三等奖：{c}")


"""
import random
import string
# 生成一个邀请码
def create_code():
    # 随机生成一个大小写字母
    letter = random.choice(string.ascii_letters)
    # 后面5位随机数字
    nums = ""
    for i in range(5):
        nums += str(random.randint(0, 9))
    return letter + nums
# 生成200个不重复的邀请码
codes = []
while len(codes) < 200:
    code = create_code()
    if code not in codes:
        codes.append(code)
print("邀请码：")
print(codes)
# 随机抽取18个不重复的邀请码
winners = random.sample(codes, 18)
first_prize = winners[0:3]
second_prize = winners[3:8]
third_prize = winners[8:18]
print("一等奖：", first_prize)
print("二等奖：", second_prize)
print("三等奖：", third_prize)
"""

# 7.函数实现:日期计算：输入某年某月某日，判断这一天是这一年的第几天？
#     1).程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第 几天， 特殊情况，闰年且输入月份大于3时需考虑多加一天。
#     2).如果输入的月份大于12时提示错误，重新输入
#     3).如果月份为小月，天数大于30时提示错误，重新输入
#     4).如果月份为大月，天数大于31时提示错误，重新输入
#     5).如果年份为平年，2月天数大于28时提示错误，重新输入
#     6).如果年份为闰年，2月天数大于29时提示错误，重新输入
#
def is_leap_year(year):
    # 判断是否为闰年
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False
def get_day_of_year(year, month, day):
    # 每个月的天数
    month_days = [31, 28, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]
    # 如果是闰年，2月改成29天
    if is_leap_year(year):
        month_days[1] = 29
    # 计算前面月份的总天数
    total = 0
    for i in range(month - 1):
        total += month_days[i]
    # 再加上当前月份的天数
    total += day
    return total
# while True:
#     year = int(input("请输入年份："))
#     month = int(input("请输入月份："))
#     day = int(input("请输入日期："))
#     # 判断月份是否合法
#     if month < 1 or month > 12:
#         print("月份错误，请重新输入")
#         continue
#     # 根据月份得到这个月最多有多少天
#     month_days = [31, 28, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]
#     if is_leap_year(year):
#         month_days[1] = 29
#     # 判断日期是否合法
#     if day < 1 or day > month_days[month - 1]:
#         print("日期错误，请重新输入")
#         continue
#     # 输入合法，计算第几天
#     result = get_day_of_year(year, month, day)
#     print(f"{year}年{month}月{day}日是这一年的第{result}天")
#     break
# 注：第8题可以不用函数实现
# 8. 使用sample()实现：将8名老师随机分配到3个办公室，要求：每个办公室不超过3个人
import random
a = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8"]
dict1 = {}
office_num = 3
offices = [1, 2, 3]
if len(a) <= office_num * 3:
    for i in range(len(a)):
        while True:
            # 用 sample 随机抽取一个办公室编号
            office = random.sample(offices, 1)[0]
            # 如果这个办公室还没创建
            if office not in dict1:
                dict1[office] = []
            # 如果办公室人数少于3人，就把老师放进去
            if len(dict1[office]) < 3:
                dict1[office].append(a[i])
                break
    dict1 = dict(sorted(dict1.items()))
    for j in range(len(dict1)):
        print(f"第{j + 1}个办公室，共有{len(dict1[j + 1])}个老师，分别是{dict1[j + 1]}")
else:
    print("办公室数量不足以容纳所有老师")