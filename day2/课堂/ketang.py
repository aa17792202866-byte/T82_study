# 1。根据用户输入的年龄信息，程序输出结果“Your age is : XXX”
# age = input("请输入年龄")
#
# print(f'Your age is : {age}，数据类型是{type(age)}')
#
#
#
# age = int(input("请输入年龄"))
#
# print(f'Your age is : {age}，数据类型是{type(age)}')

from decimal import Decimal

result = Decimal('9.9') / Decimal('3.3')
print(result)  # 3


print(Decimal('9.9') / Decimal('3.3'))
