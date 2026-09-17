# text = input("请输入字符串：")# 例如输入 gbgkkdehh
# text = 'gbgkkdehh'
# n = 1 # 目标出现次数，可修改
# m = 2  # 目标第几个，从 1 开始
# if m < 1 or n < 1:
#     print("m 和 n 都必须是正整数")
# else:
#     # result = [char for char in dict.fromkeys(text) if text.count(char) == n]
#     result = []
#     for char in dict.fromkeys(text):
#         if text.count(char) == n:
#             result.append(char)
#     if m <= len(result):
#         print(f"第 {m} 个只出现过 {n} 次的字符是：{result[m - 1]}")
#     else:
#         print(f"不存在第 {m} 个出现过 {n} 次的字符")
#
# print(input("apple"))
# import secrets
#
# # 生成 [1, 10] 范围内的安全随机整数
# secure_num = secrets.randbelow(10) + 1
# print(secure_num)
# text = [1,2,3]
# a = text
# text= text.append(4)
# print(a)
while True:  # 判断年份是否合法，不合法可以一直输入
    year = int(input("请输入年份: "))
    if year <= 0:
        print("年份输入有误！请重新输入")
    else:
        break

while True:  # 判断月份是否合法，不合法可以一直输入
    month = int(input("请输入月份: "))
    if month < 1 or month > 12:
        print("月份输入有误！请重新输入")
    else:
        break

# 按平年设置每个月的天数
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 判断是否为闰年：能被400整除，或能被4整除但不能被100整除
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    days[1] = 29

while True:  # 判断日期是否合法，不合法可以一直输入
    day = int(input("请输入日期: "))
    if day < 1 or day > days[month - 1]:
        print("日期输入错误！请重新输入")
    else:
        break

total = sum(days[:month - 1]) + day  # 计算这一天是这一年的第几天
print(f"{year}年{month}月{day}日是这一年的第{total}天")